#!/usr/bin/python3
import argparse
import json
import os
from pathlib import Path
import re
import requests
from sentence_transformers import SentenceTransformer
import sys
import yaml
import logging


import config
import mappers
import utils
import pr_comment
from validator import validate_with_custom_logic, save_validation_results
from test import run_search_tests


def delete_stale_markdown(json_to_delete_md_for):
    ids_to_delete = []
    for path in json_to_delete_md_for:
        ids_to_delete.extend(utils.get_deleted_json_ids(path))
    for filename in os.listdir(config.datasets_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(config.datasets_dir, filename)
            frontmatter = utils.extract_yaml_frontmatter(filepath)
            markdown_dataset_id = frontmatter.get("dataset_id")
            if frontmatter and markdown_dataset_id in ids_to_delete:
                print(f"Deleting {filepath} with id of {markdown_dataset_id}")
                os.remove(filepath)


def fetch_schema(schema_url, schema_path):
    response = requests.get(schema_url)

    if response.status_code == 200:
        with open(schema_path, mode="w") as file:
            response_dict = response.json()
            json.dump(response_dict, file)
    else:
        raise Exception(
            f"Failed to retrieve schema from {schema_url}, status code: {response.status_code}"
        )


def validate_json_with_schema(dataset_from_json, schema_url, validation_errors):
    """Validate dataset and collect errors for PR comment."""
    if schema_url == config.schema_url_v3:
        schema_path = f"{config.python_path}/rdl-03.json"
        is_cached = os.path.isfile(schema_path)
        if not is_cached:
            # TODO: delete & replace hardcoded_schema_url with schema_url when v0.3 finalized
            hardcoded_schema_url = "https://raw.githubusercontent.com/GFDRR/CCDR-tools/refs/heads/main/_static/rdls_schema_v0.3.json"
            fetch_schema(hardcoded_schema_url, schema_path)
    else:
        schema_path = f"{config.python_path}/rdl-02.json"
        is_cached = os.path.isfile(schema_path)
        if not is_cached:
            fetch_schema(schema_url, schema_path)

    # TODO: drop this condition; temporarily skips v0.2 validations
    if schema_url == config.schema_url_v3:
        with open(schema_path, "r") as file:
            schema = json.load(file)
            exit_code, error_details = validate_with_custom_logic(dataset_from_json, schema)
            if error_details:
                validation_errors.append(error_details)
            return exit_code
    return 0

def write_dataset_to_markdown(dataset_from_json, schema_url, validation_errors):
    dataset_id = dataset_from_json.get('id', 'unknown')
    dataset_title = dataset_from_json.get('title', 'a dataset with a missing title')
    
    try:
        # Generate frontmatter
        dataset_frontmatter = None
        exit_code = validate_json_with_schema(dataset_from_json, schema_url, validation_errors)
        if exit_code != 0:
            return exit_code
        match schema_url:
            case config.schema_url_v3:
                dataset_frontmatter = mappers.make_dataset_frontmatter_v03(
                    dataset_from_json
                )
            case config.schema_url_v2:
                dataset_frontmatter = mappers.make_dataset_frontmatter_v02(
                    dataset_from_json
                )
            case _:
                logging.error(
                    f"Unknown schema: {dataset_from_json.get('schema', "None")}. Using v0.2"
                )
                dataset_frontmatter = mappers.make_dataset_frontmatter_v02(
                    dataset_from_json
                )
        # Write output
        utils.write_frontmatter(dataset_frontmatter, config.datasets_dir)
        return 0
    except Exception as e:
        error_message = str(e)
        logging.error(
            f"While writing {dataset_title} "
            f"(dataset_id: {dataset_id})",
            exc_info=e,
        )
        # Add the error to validation_errors so it shows up in validation_results.json
        validation_errors.append({
            'dataset_id': dataset_id,
            'message': error_message,
            'schema_path': 'mapping/validation'
        })
        return 1

def fetch_geojson_for_countries(countries):
    """Fetch simplified GeoJSON for a list of country codes from the GeoBoundaries API."""
    for country_code in countries:
        try:
            geoboundaries_response = requests.get(f"https://www.geoboundaries.org/api/current/gbOpen/{country_code}/ADM0/")
            if geoboundaries_response.status_code == 200:
                geoboundaries_data = geoboundaries_response.json()
                geojson_response = requests.get(geoboundaries_data.get("simplifiedGeometryGeoJSON"))  # Fetch the GeoJSON to cache it for later use
                geojson_data = geojson_response.json()

                with open(f"{config.country_geojson_dir}/{country_code}.geojson", 'w') as f:
                    json.dump(geojson_data, f)
            else:
                logging.warning(f"Failed to fetch GeoJSON for {country_code}: {geoboundaries_response.status_code}")
        except Exception as e:
            logging.error(f"Error fetching GeoJSON for {country_code}: {str(e)}")

def write_datasets_to_markdown(json_to_generate_md_from, json_to_delete_md_for, validation_errors, include_geojson):
    """Write datasets to markdown and track added/modified/deleted dataset IDs."""
    exit_code = 0
    added_datasets = []
    modified_datasets = []
    deleted_datasets = []
    countries = set()
    # First, collect all dataset IDs from json_to_generate_md_from to determine additions vs modifications
    # This must happen BEFORE we delete any markdown files
    datasets_to_process = []  # List of (dataset, schema_url, is_modification) tuples
    
    for json_filepath in json_to_generate_md_from:
        encoding = utils.detect_encoding(json_filepath)
        with open(json_filepath, encoding=encoding) as input_file:
            datasets_json = json.load(input_file)
            for dataset in datasets_json.get("datasets", []):
                dataset_id = dataset.get("id", "unknown")
                # Determine if this is an addition or modification (check BEFORE deleting)
                md_filename = f"{dataset_id.replace('/', '_')}.md"
                md_filepath = Path(config.datasets_dir) / md_filename
                
                is_modification = md_filepath.exists()
                if is_modification:
                    modified_datasets.append(dataset_id)
                else:
                    added_datasets.append(dataset_id)
                
                links = dataset.get("links", [])
                schema_url = next(
                    (
                        link["href"]
                        for link in links
                        if link.get("rel") == "describedby"
                    ),
                    config.schema_url_v2,
                )
                if include_geojson:
                    countries.update(dataset.get("spatial", {}).get("countries", []))
                datasets_to_process.append((dataset, schema_url, is_modification))
    fetch_geojson_for_countries(countries)
    # Handle deletions - only for files that are truly being deleted (not in json_to_generate_md_from)
    # A file is only truly deleted if it's in json_to_delete_md_for but NOT in json_to_generate_md_from
    json_to_generate_paths = set(str(p) for p in json_to_generate_md_from)
    truly_deleted_json_files = [p for p in json_to_delete_md_for if str(p) not in json_to_generate_paths]
    
    for path in truly_deleted_json_files:
        deleted_ids = utils.get_deleted_json_ids(path)
        deleted_datasets.extend(deleted_ids)
    
    delete_stale_markdown(truly_deleted_json_files)
    
    # Handle additions/modifications - generate markdown
    for dataset, schema_url, is_modification in datasets_to_process:
        result = write_dataset_to_markdown(dataset, schema_url, validation_errors)
        if result != 0:
            exit_code = result
    
    return exit_code, added_datasets, modified_datasets, deleted_datasets


def get_datasets_metadata():
    metadata_entries = []
    for filename in os.listdir(config.datasets_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(config.datasets_dir, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                pattern = r"^---\n(.*?)\n---\n"
                match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
                if match:
                    payload = match.group(1)  # Return captured YAML
                    payload = yaml.safe_load(payload)
                    json_payload = json.dumps(payload)
                    metadata_entries.append(json_payload)
    return metadata_entries


def embed_datasets_metadata(datasets_metadata, model):
    results = []
    for dataset_metadata in datasets_metadata:
        tensor = model.encode(
            dataset_metadata, convert_to_tensor=True, normalize_embeddings=True
        )
        vector_embedding = {
            "vector": tensor.cpu().detach().numpy().tolist(),
            "metadata": json.loads(dataset_metadata),
        }
        results.append(vector_embedding)

    return results

def setup_args():
    parser = argparse.ArgumentParser(
        description="Utility for importing RDL metadata into JKAN"
    )
    parser.add_argument(
        "--ci",
        help="Tells the command to only run on commits since the remote target branch defined in config.py",
        action="store_true",
    )
    parser.add_argument(
        "--geojson",
        help="Tells the command to fetch simplified country boundary GeoJSON from GeoBoundaries API",
        action="store_true",
    )
    parser.add_argument(
        "-m",
        "--markdown",
        help="Tells the command to generate markdown from JSON metadata",
        action="store_true",
    )
    parser.add_argument(
        "-v",
        "--vectors",
        help="Tells the command to generate vector embeddings of metadata",
        action="store_true",
    )
    parser.add_argument(
        "--test",
        help="Run tests after other operations. Use 'search' to run semantic search tests",
        choices=["search"],
    )
    args = parser.parse_args()
    if args.vectors is False and args.markdown is False and args.test is None:
        print("No action specified. Use --markdown, --vectors, and/or --test.")
        sys.exit(1)

    return args

def setup_paths():
    if not Path(config.root_dir).is_dir():
        os.makedirs(config.root_dir)
    if not Path(config.datasets_dir).is_dir():
        os.makedirs(config.datasets_dir)
    if not Path(config.json_dir).is_dir():
        os.makedirs(config.json_dir)

def vectors_are_stale(vectors_path: str, datasets_dir: str) -> bool:
    """Return True if the vectors file is missing or older than any dataset markdown."""
    if not os.path.isfile(vectors_path):
        return True
    vectors_mtime = os.path.getmtime(vectors_path)
    for root, _, files in os.walk(datasets_dir):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            if os.path.getmtime(os.path.join(root, fname)) > vectors_mtime:
                return True
    return False


def setup_plan():
    json_to_generate_md_from = json_to_delete_md_for = []
    model = None
    should_generate_vectors = False

    if args.markdown:
        if args.ci:
            json_to_generate_md_from, json_to_delete_md_for = utils.get_recently_changed_files()
        else:
            json_files = list(Path(".").glob(f"{config.json_dir}/*.json"))
            json_to_generate_md_from = json_files
            json_to_delete_md_for = json_files

    if args.vectors:
        markdown_changes = bool(json_to_generate_md_from or json_to_delete_md_for)
        stale = vectors_are_stale(config.vectors_path, config.datasets_dir)
        should_generate_vectors = markdown_changes or stale
        if should_generate_vectors:
            model = SentenceTransformer("all-MiniLM-L6-v2")

    return json_to_generate_md_from, json_to_delete_md_for, model, should_generate_vectors

if __name__ == "__main__":
    exit_code = 0
    args = setup_args()
    setup_paths()
    json_to_generate_md_from, json_to_delete_md_for, model, should_generate_vectors = setup_plan()
    
    # Track operation results for PR comment
    markdown_files = {"added": [], "modified": [], "deleted": []}
    vectors_generated = False
    vector_count = 0
    validation_errors = []

    # Process markdown generation
    if json_to_generate_md_from or json_to_delete_md_for:
        result, added, modified, deleted = write_datasets_to_markdown(
            json_to_generate_md_from, json_to_delete_md_for, validation_errors, args.geojson
        )
        exit_code = exit_code | result
        markdown_files["added"] = added
        markdown_files["modified"] = modified
        markdown_files["deleted"] = deleted
        if exit_code == 0:
            print(f"Markdown generated in {config.datasets_dir}.")
    
    # Save validation results
    if validation_errors or json_to_generate_md_from or json_to_delete_md_for:
        # Count validated datasets
        validated_count = len(markdown_files["added"]) + len(markdown_files["modified"])
        validation_results = {
            "summary": {
                "passed": validated_count - len(validation_errors),
                "failed": len(validation_errors),
                "total": validated_count
            },
            "errors": validation_errors
        }
        save_validation_results(validation_results)
    
    # Process vector generation
    if should_generate_vectors:
        datasets_metadata = get_datasets_metadata()
        vector_embeddings = embed_datasets_metadata(datasets_metadata, model)
        
        result = utils.save_to_json(vector_embeddings, config.vectors_path)
        exit_code = exit_code | result
        # Only check the result of vector save operation, not cumulative exit_code
        if result == 0:
            vectors_generated = True
            vector_count = len(vector_embeddings)
            print(f"Vectors saved to {config.vectors_path}.")
    
    # Run tests
    if args.test == "search":
        exit_code = exit_code | run_search_tests(model)
    
    # Generate PR comment if in CI mode
    if args.ci:
        pr_comment.generate(
            markdown_files=markdown_files,
            vectors_generated=vectors_generated,
            vector_count=vector_count
        )

    sys.exit(exit_code)
