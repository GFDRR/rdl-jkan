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
from validator import validate_with_custom_logic


def delete_stale_markdown(json_to_delete_md_for):
    ids_to_delete = [utils.get_deleted_json_id(path) for path in json_to_delete_md_for]
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


def validate_json_with_schema(dataset_from_json, schema_url):
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
            validate_with_custom_logic(dataset_from_json, schema)


def write_dataset_to_markdown(dataset_from_json, schema_url):
    try:
        # Generate frontmatter
        dataset_frontmatter = None
        validate_json_with_schema(dataset_from_json, schema_url)
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
        logging.error(
            f"While writing {dataset_from_json.get('title', 'a dataset with a missing title')} "
            f"(dataset_id: {dataset_from_json.get('id', 'missing')})",
            exc_info=e,
        )
        return 1


def write_datasets_to_markdown(json_to_generate_md_from, json_to_delete_md_for):
    exit_code = 0
    delete_stale_markdown(json_to_delete_md_for)
    for json_filepath in json_to_generate_md_from:
        encoding = utils.detect_encoding(json_filepath)
        with open(json_filepath, encoding=encoding) as input_file:
            datasets_json = json.load(input_file)
            for dataset in datasets_json["datasets"]:
                links = dataset.get("links", [])
                schema_url = next((link["href"] for link in links if link.get("rel") == "describedby"), config.schema_url_v2)
                result = write_dataset_to_markdown(dataset, schema_url)
                if result != 0:
                    exit_code = result
    return exit_code


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


def embed_datasets_metadata(datasets_metadata):
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
    args = parser.parse_args()
    if args.vectors is False and args.markdown is False:
        print("No action specified. Use --markdown and/or --vectors.")
        sys.exit(1)

    return args

def setup_paths():
    if not Path(config.root_dir).is_dir():
        os.makedirs(config.root_dir)
    if not Path(config.datasets_dir).is_dir():
        os.makedirs(config.datasets_dir)
    if not Path(config.json_dir).is_dir():
        os.makedirs(config.json_dir)

def setup_plan():
    if args.markdown:
        if args.ci:
            json_to_generate_md_from, json_to_delete_md_for = utils.get_recently_changed_files()
        else:
            json_to_generate_md_from = json_to_delete_md_for = Path(".").glob(f"{config.json_dir}/*.json")
    should_generate_vectors =  args.vectors and (json_to_delete_md_for or json_to_delete_md_for)

    return json_to_generate_md_from, json_to_delete_md_for, should_generate_vectors

if __name__ == "__main__":
    exit_code = 0
    args = setup_args()
    setup_paths()
    json_to_generate_md_from, json_to_delete_md_for, should_generate_vectors = setup_plan()

    if json_to_generate_md_from or json_to_delete_md_for:
        exit_code = write_datasets_to_markdown(json_to_generate_md_from, json_to_delete_md_for)
        if exit_code == 0:
            print(f"Markdown generated in {config.datasets_dir}.")
    if should_generate_vectors:
        model = SentenceTransformer("all-MiniLM-L6-v2")
        datasets_metadata = get_datasets_metadata()
        vector_embeddings = embed_datasets_metadata(datasets_metadata)

        exit_code = exit_code | utils.save_to_json(
            vector_embeddings, config.vectors_path
        )
        if exit_code == 0:
            print(f"Vectors saved to {config.vectors_path}.")

    sys.exit(exit_code)
