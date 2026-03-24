#!/usr/bin/env python3
"""
PR Comment Generator
Generates and posts PR comments with test results, validation errors, and dataset changes.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
import logging

# Configuration
TEST_RESULTS_PATH = Path(__file__).parent / "test_results.json"
VALIDATION_RESULTS_PATH = Path(__file__).parent / "validation_results.json"


def is_ci_environment() -> bool:
    """Check if running in GitHub Actions CI environment."""
    return os.environ.get('GITHUB_ACTIONS') == 'true'


def load_json_results(path: Path) -> Optional[Dict[str, Any]]:
    """Load JSON results from file if it exists."""
    if not path.exists():
        return None
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logging.warning(f"Failed to load results from {path}: {e}")
        return None


def generate_dataset_changes_section(added: List[str], modified: List[str], deleted: List[str]) -> str:
    """Generate markdown section for dataset changes."""
    total = len(added) + len(modified) + len(deleted)
    
    sections = ["### 📝 Dataset Changes"]
    
    if total == 0:
        sections.append("- No dataset changes detected")
    else:
        sections.append(f"- ✅ Added: {len(added)} datasets")
        sections.append(f"- 📝 Modified: {len(modified)} datasets")
        sections.append(f"- 🗑️ Deleted: {len(deleted)} datasets")
        
        if added:
            sections.append("\n<details>")
            sections.append(f"<summary>📥 Added Datasets ({len(added)})</summary>")
            sections.append("")
            for ds_id in added:
                sections.append(f"- `{ds_id}`")
            sections.append("</details>")
        
        if modified:
            sections.append("\n<details>")
            sections.append(f"<summary>📝 Modified Datasets ({len(modified)})</summary>")
            sections.append("")
            for ds_id in modified:
                sections.append(f"- `{ds_id}`")
            sections.append("</details>")
        
        if deleted:
            sections.append("\n<details>")
            sections.append(f"<summary>🗑️ Deleted Datasets ({len(deleted)})</summary>")
            sections.append("")
            for ds_id in deleted:
                sections.append(f"- `{ds_id}`")
            sections.append("</details>")
    
    return "\n".join(sections)


def generate_vectors_section(vectors_generated: bool, vector_count: int = 0) -> str:
    """Generate markdown section for vector generation status."""
    if vectors_generated:
        return f"### 🧮 Vectors\n- ✅ Vectors generated/updated ({vector_count} datasets)"
    else:
        return "### 🧮 Vectors\n- ⏭️ No vector updates needed"


def generate_validation_section(validation_results: Optional[Dict[str, Any]]) -> str:
    """Generate markdown section for validation results."""
    if validation_results is None:
        return "### ✅ Validation\n- ⏭️ Validation skipped"
    
    summary = validation_results.get('summary', {})
    passed = summary.get('passed', 0)
    failed = summary.get('failed', 0)
    total = summary.get('total', 0)
    
    if failed == 0:
        return f"### ✅ Validation\n- ✅ {total}/{total} datasets passed validation"
    
    errors = validation_results.get('errors', [])
    lines = [f"### ❌ Validation\n- ❌ {total - failed}/{total} datasets passed validation ({failed} errors)"]
    
    if errors:
        lines.append("\n<details>")
        lines.append(f"<summary>❌ Validation Errors ({len(errors)})</summary>")
        lines.append("")
        lines.append("| Dataset | Error | Schema Path |")
        lines.append("|---------|-------|-------------|")
        for error in errors[:10]:  # Show first 10 errors
            dataset_id = error.get('dataset_id', 'N/A')
            message = error.get('message', 'Unknown error')[:80]
            schema_path = error.get('schema_path', 'N/A')
            lines.append(f"| `{dataset_id}` | {message}... | `{schema_path}` |")
        if len(errors) > 10:
            lines.append(f"| ... | *{len(errors) - 10} more errors* | ... |")
        lines.append("</details>")
    
    return "\n".join(lines)


def generate_test_results_section(test_results: Optional[Dict[str, Any]]) -> str:
    """Generate markdown section for test results."""
    if test_results is None:
        return "### 🧪 Search Tests\n- ⏭️ Tests skipped"
    
    summary = test_results.get('summary', {})
    passed = summary.get('passed', 0)
    failed = summary.get('failed', 0)
    total = summary.get('total', 0)
    
    if total == 0:
        return "### 🧪 Search Tests\n- ⏭️ No tests configured"
    
    lines = [f"### 🧪 Search Tests\n- {'✅' if failed == 0 else '❌'} {passed}/{total} tests passed"]
    
    # Show failed tests
    tests = test_results.get('tests', [])
    failed_tests = [t for t in tests if not t.get('passed', True)]
    
    for test in failed_tests:
        query = test.get('query', 'Unknown query')
        description = test.get('description', '')
        top_results = test.get('top_results', [])[:5]  # Show top 5
        expected_includes = test.get('expected_includes', [])
        missing_includes = test.get('missing_includes', [])
        unexpected_excludes = test.get('unexpected_excludes', [])
        
        lines.append(f"\n<details>")
        lines.append(f"<summary>❌ Failed: \"{query}\"</summary>")
        lines.append("")
        
        if description:
            lines.append(f"**Description:** {description}")
            lines.append("")
        
        # Expected includes table
        if expected_includes:
            lines.append("**Expected includes:**")
            lines.append("")
            lines.append("| Dataset | Expected | Found | Rank | Score |")
            lines.append("|---------|----------|-------|------|-------|")
            for inc in expected_includes:
                ds_id = inc.get('dataset_id', 'N/A')
                found = inc.get('found', False)
                rank = inc.get('rank', '-')
                score = inc.get('score', '-')
                if score != '-' and score is not None:
                    score = f"{score:.4f}"
                lines.append(f"| `{ds_id}` | ✅ | {'✅' if found else '❌'} | {rank} | {score} |")
            lines.append("")
        
        # Missing includes and unexpected excludes
        if missing_includes:
            lines.append(f"**Missing includes:** `{', '.join(missing_includes)}`")
            lines.append("")
        if unexpected_excludes:
            lines.append(f"**Unexpected excludes found:** `{', '.join(unexpected_excludes)}`")
            lines.append("")
        
        # Top actual results
        if top_results:
            lines.append("**Top 5 actual results:**")
            lines.append("")
            lines.append("| Rank | Dataset | Score |")
            lines.append("|------|---------|-------|")
            for result in top_results:
                ds_id = result.get('dataset_id', 'N/A')
                rank = result.get('rank', '-')
                score = result.get('score', 0.0)
                lines.append(f"| {rank} | `{ds_id}` | {score:.4f} |")
            lines.append("")
        
        lines.append("</details>")
    
    return "\n".join(lines)


def generate_pr_comment(
    markdown_files: Dict[str, List[str]],
    vectors_generated: bool,
    vector_count: int = 0,
    test_results: Optional[Dict[str, Any]] = None,
    validation_results: Optional[Dict[str, Any]] = None
) -> str:
    """Generate the full PR comment markdown."""
    sections = [
        "## 📊 PR Sync Results",
        "",
        generate_dataset_changes_section(
            markdown_files.get('added', []),
            markdown_files.get('modified', []),
            markdown_files.get('deleted', [])
        ),
        "",
        generate_vectors_section(vectors_generated, vector_count),
        "",
        generate_validation_section(validation_results),
        "",
        generate_test_results_section(test_results),
    ]
    
    return "\n".join(sections)


def find_existing_comment(pr_number: str, repo: str) -> Optional[str]:
    """Find existing PR comment ID from the bot."""
    try:
        import subprocess
        import json
        
        # List comments using gh API
        cmd = [
            'gh', 'api',
            f'/repos/{repo}/issues/{pr_number}/comments',
            '--jq', '.[] | select(.user.type == "Bot" or .user.login == "github-actions[bot]") | {id: .id, body: .body}'
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            logging.warning(f"Failed to list PR comments: {result.stderr}")
            return None
        
        # Parse each line as JSON and find our comment
        for line in result.stdout.strip().split('\n'):
            if not line:
                continue
            try:
                comment_data = json.loads(line)
                body = comment_data.get('body', '')
                # Look for our comment signature
                if '📊 PR Sync Results' in body:
                    return str(comment_data['id'])
            except json.JSONDecodeError:
                continue
        
        return None
        
    except Exception as e:
        logging.warning(f"Error finding existing comment: {e}")
        return None


def post_pr_comment(comment: str) -> bool:
    """Post or update PR comment using GitHub CLI."""
    try:
        # Get PR number and repository from environment
        pr_number = os.environ.get('GITHUB_PR_NUMBER')
        repo = os.environ.get('GITHUB_REPOSITORY')
        
        if not pr_number or not repo:
            logging.error("GITHUB_PR_NUMBER or GITHUB_REPOSITORY not set")
            return False
        
        import subprocess
        
        # Check for existing comment
        existing_comment_id = find_existing_comment(pr_number, repo)
        
        # Write comment to temporary file
        comment_file = Path('/tmp/pr_comment.md')
        with open(comment_file, 'w') as f:
            f.write(comment)
        
        if existing_comment_id:
            # Update existing comment
            logging.info(f"Updating existing comment {existing_comment_id}")
            cmd = [
                'gh', 'api',
                '--method', 'PATCH',
                f'/repos/{repo}/issues/comments/{existing_comment_id}',
                '-f', f'body={comment}'
            ]
        else:
            # Create new comment
            logging.info("Creating new PR comment")
            cmd = [
                'gh', 'pr', 'comment', pr_number,
                '--repo', repo,
                '--body-file', str(comment_file)
            ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            logging.error(f"Failed to post PR comment: {result.stderr}")
            return False
        
        action = "updated" if existing_comment_id else "posted"
        logging.info(f"PR comment {action} successfully on PR #{pr_number}")
        return True
        
    except Exception as e:
        logging.error(f"Error posting PR comment: {e}", exc_info=True)
        return False


def generate(
    markdown_files: Dict[str, List[str]],
    vectors_generated: bool = False,
    vector_count: int = 0,
    test_results_path: Optional[Path] = None,
    validation_results_path: Optional[Path] = None
) -> bool:
    """
    Generate and post PR comment.
    
    Args:
        markdown_files: Dict with 'added', 'modified', 'deleted' dataset lists
        vectors_generated: Whether vectors were generated/updated
        vector_count: Number of datasets with vectors
        test_results_path: Path to test results JSON file
        validation_results_path: Path to validation results JSON file
    
    Returns:
        True if successful (or if not in CI), False if posting failed
    """
    # Load results
    test_results = load_json_results(test_results_path or TEST_RESULTS_PATH)
    validation_results = load_json_results(validation_results_path or VALIDATION_RESULTS_PATH)
    
    # Generate comment
    comment = generate_pr_comment(
        markdown_files=markdown_files,
        vectors_generated=vectors_generated,
        vector_count=vector_count,
        test_results=test_results,
        validation_results=validation_results
    )
    
    # Check if running in CI
    if not is_ci_environment():
        print("\n" + "="*60)
        print("⚠️  Warning: Not running in GitHub Actions CI environment")
        print("="*60)
        print("\nPR comment would be:\n")
        print(comment)
        print("\n" + "="*60)
        return True
    
    # Post PR comment
    return post_pr_comment(comment)


if __name__ == "__main__":
    # Simple test when run directly
    test_data = {
        "added": ["dataset_1", "dataset_2"],
        "modified": ["dataset_3"],
        "deleted": []
    }
    generate(test_data, vectors_generated=True, vector_count=3)
