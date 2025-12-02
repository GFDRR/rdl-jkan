#!/usr/bin/python3

import argparse
import json
import os
import re
import sys
import requests
import json
import logging
from pathlib import Path

import yaml

import config
import utils
import mappers
from validator import validate_with_custom_logic


def extract_yaml_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    pattern = r"^---\n(.*?)\n---\n"
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    if match:
        payload = match.group(1)  # Return the captured YAML content
        payload = yaml.safe_load(payload)
        return payload
    return None


def clean_up_old_versions(json_dataset):
    for filename in os.listdir(config.datasets_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(config.datasets_dir, filename)
            frontmatter = extract_yaml_frontmatter(filepath)
            json_dataset_id = json_dataset.get("dataset_id")
            markdown_dataset_id = frontmatter.get("dataset_id")
            if frontmatter and markdown_dataset_id == json_dataset_id:
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
            f"Failed to retrieve schema from {hardcoded_schema_url}, status code: {response.status_code}"
        )


def validate_json_with_schema(dataset_from_json, schema_url):
    if schema_url == config.schema_url_v3:
        schema_path = f"{config.schema_path}/rdl-03.json"
        is_cached = os.path.isfile(schema_path)
        if not is_cached:
            # TODO: delete & replace hardcoded_schema_url with schema_url when v0.3 finalized
            hardcoded_schema_url = "https://raw.githubusercontent.com/GFDRR/CCDR-tools/refs/heads/main/_static/rdls_schema_v0.3.json"            fetch_schema(hardcoded_schema_url, schema_path)
    else:
        schema_path = f"{config.schema_path}/rdl-02.json"
        is_cached = os.path.isfile(schema_path)
        if not is_cached:
            fetch_schema(schema_url, schema_path)

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
        # Delete old file if it exists, in case of filename changes
        clean_up_old_versions(dataset_frontmatter)
        # Write output
        utils.write_frontmatter(dataset_frontmatter, config.datasets_dir)
        return 0
    except Exception as e:
        logging.error(
            f"While writing {dataset.get('title', 'a dataset with a missing title')} "
            f"(dataset_id: {dataset.get('id', 'missing')})",
            exc_info=e,
        )
        return 1


def write_datasets_to_markdown(json_filepaths):
    exit_code = 0
    for json_file in json_filepaths:
        json_filepath = os.path.join(config.root_dir, json_file)
        encoding = utils.detect_encoding(json_filepath)
        with open(json_filepath, encoding=encoding) as input_file:
            datasets_json = json.load(input_file)
            for dataset in datasets_json["datasets"]:
                first_link, *_ = dataset.get("links")
                schema_url = first_link.get("href")
                result = write_dataset_to_markdown(dataset, schema_url)
                if result != 0:
                    exit_code = result
    return exit_code


if __name__ == "__main__":
    # Parse args
    parser = argparse.ArgumentParser(
        description="Convert RDL JSON datasets into JKAN frontmatter"
    )
    parser.add_argument(
        "--input_folder",
        help="Path to the folder containing RDL datasets in JSON format",
        default=".",
        action="store",
    )
    parser.add_argument(
        "--type",
        choices=["ci", "batch"],
        help="Whether the datasets are being generated from new/modified files from the last commit or from a batch directory",
        default="batch",
        action="store",
    )
    args = parser.parse_args()
    # Create output paths if they don't already exist
    if not Path(config.root_dir).is_dir():
        os.makedirs(config.root_dir)
    if not Path(config.datasets_dir).is_dir():
        os.makedirs(config.datasets_dir)
    if not Path(config.json_dir).is_dir():
        os.makedirs(config.json_dir)

    exit_code = 0
    if args.type == "ci":
        result = write_datasets_to_markdown(utils.get_recently_changed_json_files())
        if result != 0:
            exit_code = result
    elif args.type == "batch":
        input_path = Path(args.input_folder)
        result = write_datasets_to_markdown(
            input_path.glob(f"{config.json_dir}/*.json")
        )
        if result != 0:
            exit_code = result
    else:
        raise ValueError(f"Unknown type {args.type}")

    if exit_code == 0:
        print(
            "\nAll done! Please enjoy your datasets :)\n",
            "More info is available at `import/README.md`\n",
            sep=os.linesep,
        )
    else:
        print(f"\nUh oh! Exit code: {exit_code}")
    sys.exit(exit_code)
