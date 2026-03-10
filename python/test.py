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

# Configuration
SEARCH_TESTS_FILE = Path(__file__).parent / "tests.yml"
VECTORS_PATH = Path(__file__).parent / "vectors.json"
RESULTS_PATH = Path(__file__).parent / "test_results.json"


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


def perform_semantic_search(
    query: str,
    model: SentenceTransformer,
    vectors: List[Dict[str, Any]],
    n: int = 10
) -> List[Tuple[str, float]]:
    """
    Perform semantic search by encoding query and comparing to dataset vectors.
    
    Returns list of (dataset_id, similarity_score) tuples, sorted by similarity.
    """
    # Encode the query
    query_embedding = model.encode(query, convert_to_tensor=False, normalize_embeddings=True)
    
    # Calculate similarity with all datasets
    results = []
    for item in vectors:
        dataset_id = item.get('metadata', {}).get('dataset_id')
        vector = item.get('vector', [])
        if dataset_id and vector:
            similarity = cosine_similarity(query_embedding.tolist(), vector)
            results.append((dataset_id, similarity))
    
    # Sort by similarity (descending) and return top N
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:n]


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
        
        # Perform semantic search
        top_n = 20
        results = perform_semantic_search(query, model, vectors, n=top_n)
        result_ids = [r[0] for r in results]
        result_ranks = {dataset_id: idx + 1 for idx, (dataset_id, _) in enumerate(results)}
        result_scores = {dataset_id: score for dataset_id, score in results}

        print(f"  Top {top_n} results (highest similarity first):")
        for idx, (dataset_id, score) in enumerate(results, start=1):
            print(f"    {idx:2d}. {dataset_id} (score {score:.4f})")

        # Check includes & excludes
        missing_includes = [ds_id for ds_id in includes if ds_id not in result_ids]
        unexpected_excludes = [ds_id for ds_id in excludes if ds_id in result_ids]

        print("  Expected includes:")
        expected_includes = []
        for ds_id in includes:
            if ds_id in result_ranks:
                rank = result_ranks[ds_id]
                score = result_scores.get(ds_id, 0.0)
                print(f"    ✓ {ds_id} found at rank {rank} (score {score:.4f})")
                expected_includes.append({
                    "dataset_id": ds_id,
                    "found": True,
                    "rank": rank,
                    "score": round(score, 4)
                })
            else:
                print(f"    ✗ {ds_id} not found in top {top_n}")
                expected_includes.append({
                    "dataset_id": ds_id,
                    "found": False,
                    "rank": None,
                    "score": None
                })

        # Build test result entry
        test_result = {
            "query": query,
            "description": description,
            "passed": not (missing_includes or unexpected_excludes),
            "top_results": [
                {"dataset_id": ds_id, "rank": idx + 1, "score": round(score, 4)}
                for idx, (ds_id, score) in enumerate(results)
            ],
            "expected_includes": expected_includes,
            "missing_includes": missing_includes,
            "unexpected_excludes": unexpected_excludes
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
