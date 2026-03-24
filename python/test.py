#!/usr/bin/env python3
"""
Semantic Search Tester
Tests semantic search functionality by comparing query embeddings against dataset vectors.
"""

import json
import sys
import yaml
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple
from sentence_transformers import SentenceTransformer
import logging
import config

# Configuration
SEARCH_TESTS_FILE = Path(__file__).parent / "tests.yml"
VECTORS_PATH = Path(__file__).parent / "vectors.json"
RESULTS_PATH = Path(__file__).parent / "test_results.json"

# Import constants from config (matching front-end hybrid search logic)
KEYWORD_SCORE_MIN = config.KEYWORD_SCORE_MIN
KEYWORD_SCORE_MAX = config.KEYWORD_SCORE_MAX
SCORED_FIELDS = config.SCORED_FIELDS
SEMANTIC_MAX_RESULTS = config.SEMANTIC_MAX_RESULTS
SEMANTIC_MIN_SCORE = config.SEMANTIC_MIN_SCORE


def load_search_tests() -> List[Dict[str, Any]]:
    """Load search test cases from YAML configuration."""
    with open(SEARCH_TESTS_FILE, 'r') as f:
        config = yaml.safe_load(f)
    return config.get('search_tests', [])


def load_vectors() -> List[Dict[str, Any]]:
    """Load pre-generated dataset vectors."""
    with open(VECTORS_PATH, 'r') as f:
        return json.load(f)


def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    a = np.array(vec_a)
    b = np.array(vec_b)
    dot_product = np.dot(a, b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)


def get_nested_value(obj: Dict[str, Any], path: str) -> Any:
    """Get a nested value from a dict using dot notation (e.g., 'creator.name')."""
    keys = path.split('.')
    value = obj
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    return value


def keyword_search(query: str, vectors: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Perform keyword search on all datasets, matching front-end logic.
    
    Returns:
        Tuple of (keyword_matches, non_matching_datasets)
        keyword_matches: list of dicts with dataset_id, score, metadata, match_type
        non_matching_datasets: list of vector items that didn't match keywords
    """
    query_lower = query.lower()
    keyword_matches = []
    non_matching = []
    
    for item in vectors:
        metadata = item.get('metadata', {})
        dataset_id = metadata.get('dataset_id')
        if not dataset_id:
            continue
        
        # Count matches across scored fields (same as front-end)
        match_count = 0
        for field in SCORED_FIELDS:
            value = get_nested_value(metadata, field)
            if value is not None:
                # Convert to JSON string for consistent matching
                if query_lower in json.dumps(value).lower():
                    match_count += 1
        
        if match_count > 0:
            # Calculate score: 0.75 + (0.25 * match_ratio)
            score = KEYWORD_SCORE_MIN + (KEYWORD_SCORE_MAX - KEYWORD_SCORE_MIN) * (match_count / len(SCORED_FIELDS))
            keyword_matches.append({
                'dataset_id': dataset_id,
                'score': score,
                'match_type': 'keyword',
                'metadata': metadata
            })
        else:
            non_matching.append(item)
    
    # Sort by score descending
    keyword_matches.sort(key=lambda x: x['score'], reverse=True)
    return keyword_matches, non_matching


def perform_semantic_search(
    query: str,
    model: SentenceTransformer,
    vectors: List[Dict[str, Any]],
    n: int = SEMANTIC_MAX_RESULTS,
    min_score: float = SEMANTIC_MIN_SCORE
) -> List[Dict[str, Any]]:
    """
    Perform semantic search by encoding query and comparing to dataset vectors.
    Only returns results above min_score threshold (matching front-end logic).
    
    Returns list of dicts with dataset_id, score, match_type, metadata.
    """
    if not vectors:
        return []
    
    # Encode the query
    query_embedding = model.encode(query, convert_to_tensor=False, normalize_embeddings=True)
    
    # Calculate similarity with all datasets
    results = []
    for item in vectors:
        dataset_id = item.get('metadata', {}).get('dataset_id')
        vector = item.get('vector', [])
        metadata = item.get('metadata', {})
        if dataset_id and vector:
            similarity = cosine_similarity(query_embedding.tolist(), vector)
            # Only include results above minimum score (same as front-end)
            if similarity >= min_score:
                results.append({
                    'dataset_id': dataset_id,
                    'score': float(similarity),
                    'match_type': 'semantic',
                    'metadata': metadata
                })
    
    # Sort by similarity (descending) and return top N
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:n]


def get_all_semantic_scores(
    query: str,
    model: SentenceTransformer,
    vectors: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Get semantic scores for ALL datasets (even below threshold).
    Used for ranking purposes in test results.
    
    Returns list of dicts with dataset_id, score, match_type, metadata.
    """
    if not vectors:
        return []
    
    # Encode the query
    query_embedding = model.encode(query, convert_to_tensor=False, normalize_embeddings=True)
    
    # Calculate similarity with all datasets
    results = []
    for item in vectors:
        dataset_id = item.get('metadata', {}).get('dataset_id')
        vector = item.get('vector', [])
        metadata = item.get('metadata', {})
        if dataset_id and vector:
            similarity = cosine_similarity(query_embedding.tolist(), vector)
            results.append({
                'dataset_id': dataset_id,
                'score': float(similarity),
                'match_type': 'semantic',
                'metadata': metadata
            })
    
    # Sort by similarity (descending)
    results.sort(key=lambda x: x['score'], reverse=True)
    return results


def hybrid_search(
    query: str,
    model: SentenceTransformer,
    vectors: List[Dict[str, Any]],
    top_n: int = SEMANTIC_MAX_RESULTS,
    return_all: bool = False
) -> List[Dict[str, Any]]:
    """
    Perform hybrid search matching front-end logic:
    1. First do keyword search on all datasets
    2. Then do semantic search only on non-matching datasets
    3. Combine and sort by score
    
    Args:
        query: Search query string
        model: SentenceTransformer model
        vectors: List of dataset vectors
        top_n: Number of top results to return
        return_all: If True, return all results instead of just top_n
    
    Returns list of result dicts with dataset_id, score, match_type, metadata.
    """
    # Step 1: Keyword search on all datasets
    keyword_results, non_matching = keyword_search(query, vectors)
    
    # Step 2: Semantic search only on datasets that didn't match keywords
    semantic_results = perform_semantic_search(query, model, non_matching)
    
    # Step 3: Combine results
    all_results = keyword_results + semantic_results
    
    # Sort by score descending
    all_results.sort(key=lambda x: x['score'], reverse=True)
    
    if return_all:
        return all_results
    return all_results[:top_n]


def run_search_tests(model: SentenceTransformer = None) -> int:
    """
    Run all search tests from the configuration file.
    
    Args:
        model: Optional pre-loaded SentenceTransformer model. If None, will load default.
    
    Returns:
        Exit code: 0 if all tests pass, 1 if any fail
    """
    print("\n" + "="*60)
    print("Running Semantic Search Tests")
    print("="*60)
    
    # Load model if not provided
    if model is None:
        print("Loading SentenceTransformer model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")
    
    # Load test cases and vectors
    print("Loading test configuration...")
    test_cases = load_search_tests()
    
    print(f"Loading vectors from {VECTORS_PATH}...")
    vectors = load_vectors()
    print(f"Loaded {len(vectors)} dataset vectors")
    
    # Track results for JSON output
    test_results = {
        "summary": {"passed": 0, "failed": 0, "total": 0},
        "tests": []
    }
    
    # Track console output
    passed = 0
    failed = 0
    failed_tests = []
    
    # Run each test case
    for test_case in test_cases:
        query = test_case['query']
        description = test_case.get('description', '')
        includes = test_case.get('includes', [])
        excludes = test_case.get('excludes', [])
        
        print(f"\nTesting query: '{query}'")
        if description:
            print(f"  Description: {description}")
        
        # Perform hybrid search (matching front-end logic)
        top_n = SEMANTIC_MAX_RESULTS
        results = hybrid_search(query, model, vectors, top_n=top_n)
        result_ids = [r['dataset_id'] for r in results]
        result_scores = {r['dataset_id']: r['score'] for r in results}
        result_match_types = {r['dataset_id']: r['match_type'] for r in results}
        
        # Get all results to determine ranks for datasets outside top N
        # Use get_all_semantic_scores to include datasets below threshold
        keyword_results, non_matching = keyword_search(query, vectors)
        all_semantic_results = get_all_semantic_scores(query, model, non_matching)
        
        # Combine keyword and all semantic results for full ranking
        all_results = keyword_results + all_semantic_results
        all_results.sort(key=lambda x: x['score'], reverse=True)
        all_result_ranks = {r['dataset_id']: idx + 1 for idx, r in enumerate(all_results)}

        # Show result breakdown
        keyword_count = sum(1 for r in results if r['match_type'] == 'keyword')
        semantic_count = sum(1 for r in results if r['match_type'] == 'semantic')
        print(f"  Results: {len(results)} total ({keyword_count} keyword, {semantic_count} semantic)")
        
        print(f"  Top results (highest score first):")
        for idx, result in enumerate(results[:SEMANTIC_MAX_RESULTS], start=1):
            dataset_id = result['dataset_id']
            score = result['score']
            match_type = result['match_type']
            print(f"    {idx:2d}. {dataset_id} (score {score:.4f}, {match_type})")

        # Check includes & excludes
        missing_includes = [ds_id for ds_id in includes if ds_id not in result_ids]
        unexpected_excludes = [ds_id for ds_id in excludes if ds_id in result_ids]

        print("  Expected includes:")
        expected_includes = []
        for ds_id in includes:
            # Get rank from all results (even if outside top N)
            rank = all_result_ranks.get(ds_id)
            
            if ds_id in result_ids:
                score = result_scores.get(ds_id, 0.0)
                match_type = result_match_types.get(ds_id, 'unknown')
                print(f"    ✓ {ds_id} found at rank {rank} (score {score:.4f}, {match_type})")
                expected_includes.append({
                    "dataset_id": ds_id,
                    "found": True,
                    "rank": rank,
                    "score": round(score, 4),
                    "match_type": match_type
                })
            else:
                # Provide diagnostic info for missing includes and capture score
                print(f"    ✗ {ds_id} not found in top {top_n}")
                missing_score = None
                missing_match_type = None
                
                # Check if it would have matched keywords
                keyword_results, _ = keyword_search(query, vectors)
                keyword_ids = [r['dataset_id'] for r in keyword_results]
                if ds_id in keyword_ids:
                    for r in keyword_results:
                        if r['dataset_id'] == ds_id:
                            missing_score = r['score']
                            missing_match_type = 'keyword'
                            print(f"      ↳ Keyword match (score {missing_score:.4f}) but outside top {top_n}")
                            break
                else:
                    # Check if it would have matched semantically
                    for item in vectors:
                        if item.get('metadata', {}).get('dataset_id') == ds_id:
                            query_embedding = model.encode(query, convert_to_tensor=False, normalize_embeddings=True)
                            similarity = cosine_similarity(query_embedding.tolist(), item.get('vector', []))
                            missing_score = float(similarity)
                            if similarity >= SEMANTIC_MIN_SCORE:
                                missing_match_type = 'semantic'
                                print(f"      ↳ Semantic score {similarity:.4f} but outside top {top_n}")
                            else:
                                missing_match_type = 'semantic (below threshold)'
                                print(f"      ↳ Semantic score {similarity:.4f} below threshold ({SEMANTIC_MIN_SCORE})")
                            break
                    else:
                        print(f"      ↳ Dataset not found in vectors.json")
                
                expected_includes.append({
                    "dataset_id": ds_id,
                    "found": False,
                    "rank": rank,
                    "score": round(missing_score, 4) if missing_score is not None else None,
                    "match_type": missing_match_type
                })

        # Build test result entry
        test_result = {
            "query": query,
            "description": description,
            "passed": not (missing_includes or unexpected_excludes),
            "top_results": [
                {"dataset_id": r['dataset_id'], "rank": idx + 1, "score": round(r['score'], 4), "match_type": r['match_type']}
                for idx, r in enumerate(results)
            ],
            "expected_includes": expected_includes,
            "missing_includes": missing_includes,
            "unexpected_excludes": unexpected_excludes,
            "result_breakdown": {"keyword": keyword_count, "semantic": semantic_count}
        }
        test_results["tests"].append(test_result)

        if missing_includes or unexpected_excludes:
            failed += 1
            failed_tests.append(query)
            print(f"  ❌ FAILED")
            if missing_includes:
                print(f"    Missing expected datasets: {missing_includes}")
            if unexpected_excludes:
                print(f"    Unexpected datasets found: {unexpected_excludes}")
        else:
            passed += 1
            print(f"  ✓ PASSED")
    
    # Update summary
    test_results["summary"] = {
        "passed": passed,
        "failed": failed,
        "total": passed + failed
    }
    
    # Write results to JSON file
    with open(RESULTS_PATH, 'w') as f:
        json.dump(test_results, f, indent=2)
    print(f"\n  Test results written to {RESULTS_PATH}")
    
    # Print summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {passed + failed}")
    
    if failed > 0:
        print(f"\n  Failed queries:")
        for query in failed_tests:
            print(f"    - {query}")
        return 1
    else:
        print("\n  All tests passed! ✓")
        return 0


def main():
    """Main entry point for running search tests."""
    try:
        exit_code = run_search_tests()
        sys.exit(exit_code)
    except Exception as e:
        logging.error(f"Error running search tests: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
