#!/usr/bin/python3

import argparse
import json
import os
import re
import shutil

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

    frontmatter_match = re.match(r'---(.*?|\n)---', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(0)
        return yaml.safe_load(frontmatter)

    return None


def filter_markdown_files(directory, key, value):
    filtered_files = []

    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            frontmatter = extract_yaml_frontmatter(filepath)

            if frontmatter and frontmatter.get(key) == value:
                filtered_files.append(filepath)

    return filtered_files

def write_to_markdown(dataset):
    try:
        # Generate output
        dataset_frontmatter = mappers.make_dataset_frontmatter(dataset)
        # Delete old file if it exists, in case of filename changes
        filtered_files = filter_markdown_files('../_datasets', 'dataset_id', dataset_frontmatter["id"])
        for file_to_delete in filtered_files:
            shutil.rmtree(file_to_delete)
        # Write output
        utils.write_frontmatter(dataset_frontmatter, config.datasets_output_dir)

    except Exception as e:
        logging.error(
            f"While writing {dataset.get('title', 'a dataset with a missing title')} "
            f"(dataset_id: {dataset.get('id', 'missing')}, file: {json_file})",
            exc_info=e
        )


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
        choices=['diff', 'batch'],
        help="Whether the datasets are being generated from new/modified files or from a batch directory",
        default="batch",
        action="store",
    )
    args = parser.parse_args()
    # Create output paths if they don't already exist
    if not Path(config.generated_dir).is_dir():
        os.makedirs(config.generated_dir)
    if not Path(config.datasets_output_dir).is_dir():
        os.makedirs(config.datasets_output_dir)

    repo = Repo('..')
    files = list(repo.head.commit.stats.files.keys())

    if args.type == "diff":
        for json_file in fnmatch.filter(files, '_datasets/json/*.json'):
            with open("../" + json_file, encoding='utf-8') as input_file:
                datasets_json = json.load(input_file)
                for dataset in datasets_json["datasets"]:
                    write_to_markdown(dataset)
    elif args.type == "batch":
        input_path = Path(args.input_folder)
        for json_file in input_path.glob("../_datasets/json/*.json"):
            with open(json_file, encoding='utf-8') as input_file:
                datasets_json = json.load(input_file)
                for dataset in datasets_json["datasets"]:
                    write_to_markdown(dataset)
    else:
        raise ValueError(f"Unknown type {args.type}")


    print("\nAll done! Please enjoy your datasets :)\n",
          "Datasets have been generated in: `import/generated/_datasets`",
          "To include them in your JKAN site, run the following from `import`",
          "\nmv generated/_datasets/* ../_datasets\n",
          "This may overwrite the existing contents of `_datasets`.\n",
          f"Issues with your input files have been logged to: `import/{config.log_filename}`",
          "More info is available at `import/README.md`\n",
          sep=os.linesep)
