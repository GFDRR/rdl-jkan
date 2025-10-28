#!/usr/bin/python3

import argparse
import json
import os
import re
import sys

import logging
import fnmatch
from pathlib import Path

import yaml

import config
import utils
import mappers
from git import Repo


def extract_yaml_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    pattern = r'^---\n(.*?)\n---\n'
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    if match:
        payload = match.group(1)  # Return the captured YAML content
        payload = yaml.safe_load(payload)
        return payload
    return None


def clean_up_old_versions(json_dataset):
    for filename in os.listdir(config.datasets_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(config.datasets_dir, filename)
            frontmatter = extract_yaml_frontmatter(filepath)
            json_dataset_id = json_dataset.get("dataset_id")
            markdown_dataset_id = frontmatter.get('dataset_id')
            if frontmatter and markdown_dataset_id == json_dataset_id:
                print(f"Deleting {filepath} with id of {markdown_dataset_id}")
                os.remove(filepath)


def write_to_markdown(dataset_from_json):
    try:
        # Generate frontmatter
        dataset_frontmatter = None
        match dataset_from_json.get('schema'):
            case "https://docs.riskdatalibrary.org/en/0__3__0/rdls_schema.json":
                dataset_frontmatter = mappers.make_dataset_frontmatter_v03(dataset_from_json)
            case "https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json":
                dataset_frontmatter = mappers.make_dataset_frontmatter_v02(dataset_from_json)
            case _:
                logging.error(
                    f"Unknown schema: {dataset_from_json.get('schema', "None")}. Using v0.2"
                )
                dataset_frontmatter = mappers.make_dataset_frontmatter_v02(dataset_from_json)
        # Delete old file if it exists, in case of filename changes
        clean_up_old_versions(dataset_frontmatter)
        # Write output
        utils.write_frontmatter(dataset_frontmatter, config.datasets_dir)
        return 0
    except Exception as e:
        logging.error(
            f"While writing {dataset.get('title', 'a dataset with a missing title')} "
            f"(dataset_id: {dataset.get('id', 'missing')})",
            exc_info=e
        )
        return 1


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
        choices=['ci', 'batch'],
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

    if args.type == "ci":
        repo = Repo(config.root_dir)
        repo.remotes.origin.fetch()
        current_commit = repo.head.commit
        diff = current_commit.diff(f"origin/{config.remote_target_branch}")
        files = {item.a_path for item in diff}
        for json_file in fnmatch.filter(files, '_datasets/*.json'):
            with open(os.path.join(config.root_dir, json_file), encoding='utf-8') as input_file:
                datasets_json = json.load(input_file)
                for dataset in datasets_json["datasets"]:
                    exit_code = write_to_markdown(dataset)
                    sys.exit(exit_code)
    elif args.type == "batch":
        input_path = Path(args.input_folder)
        for json_file in input_path.glob(f"{config.json_dir}/*.json"):
            with open(json_file, encoding='utf-8') as input_file:
                datasets_json = json.load(input_file)
                for dataset in datasets_json["datasets"]:
                    exit_code = write_to_markdown(dataset)
                    sys.exit(exit_code)
    else:
        raise ValueError(f"Unknown type {args.type}")

    print("\nAll done! Please enjoy your datasets :)\n",
          "More info is available at `import/README.md`\n",
          sep=os.linesep)
