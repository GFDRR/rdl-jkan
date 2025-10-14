#!/usr/bin/python3

import argparse
import json
import os

import logging
from pathlib import Path

import config
import utils
import mappers

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
        default="diff",
        action="store",
    )
    args = parser.parse_args()
    # Create output paths if they don't already exist
    if not Path(config.generated_dir).is_dir():
        os.makedirs(config.generated_dir)
    if not Path(config.datasets_output_dir).is_dir():
        os.makedirs(config.datasets_output_dir)

    # Iterate over all JSON files in the input folder
    input_path = Path(args.input_folder)
    for json_file in input_path.glob("../_datasets/json/*.json"):
        with open(json_file, encoding='utf-8') as input_file:
            datasets_json = json.load(input_file)
            for dataset in datasets_json["datasets"]:
                try:
                    # Generate output
                    dataset_frontmatter = mappers.make_dataset_frontmatter(dataset)
                    # Write output
                    utils.write_frontmatter(dataset_frontmatter, config.datasets_output_dir)
                except Exception as e:
                    logging.error(
                        f"While writing {dataset.get('title', 'a dataset with a missing title')} "
                        f"(dataset_id: {dataset.get('id', 'missing')}) {json_file}",
                        exc_info=e
                    )

    print("\nAll done! Please enjoy your datasets :)\n",
          "Datasets have been generated in: `import/generated/_datasets`",
          "To include them in your JKAN site, run the following from `import`",
          "\nmv generated/_datasets/* ../_datasets\n",
          "This may overwrite the existing contents of `_datasets`.\n",
          f"Issues with your input files have been logged to: `import/{config.log_filename}`",
          "More info is available at `import/README.md`\n",
          sep=os.linesep)
