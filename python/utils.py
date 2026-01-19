import os
import chardet
from git import Repo
import json
import logging
from pathlib import Path
import re
import unicodedata
import yaml

import config


logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
    handlers=[
    logging.FileHandler("python.log"),
    logging.StreamHandler()
    ]
)
logging.getLogger('chardet').setLevel(logging.WARNING)
logging.getLogger('git').setLevel(logging.WARNING)


def detect_encoding(filepath):
    with open(filepath, "rb") as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result["encoding"]


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


def get_recently_changed_files():
    repo = Repo(config.root_dir)
    repo.remotes.origin.fetch()
    current_commit = repo.head.commit
    # get diff between current commit and remote target branch
    current_diff = current_commit.diff(f"origin/{config.remote_target_branch}", paths="_datasets/json/", R=True)
    # get diff from unstaged changes
    unstaged_diff = repo.index.diff(None, paths="_datasets/json/", R=True)
    # combine diffs
    diff = current_diff + unstaged_diff

    json_to_generate_md_from = []
    json_to_delete_md_for = []
    tweak_filepath = lambda path: os.path.join(config.root_dir, path)
    
    for item in diff:
        if item.change_type == "D":
            json_to_delete_md_for.append(tweak_filepath(item.a_path))
        elif item.change_type in {"A", "M", "R", "C"}:
            json_to_generate_md_from.append(tweak_filepath(item.b_path))
    return json_to_generate_md_from, json_to_delete_md_for


def get_deleted_json_id(json_path):
    repo = Repo(config.root_dir)
    repo.remotes.origin.fetch()
    tree = repo.commit("origin/rdl-0.3").tree

    # Specify the path to the JSON file
    blob = tree[os.path.relpath(json_path, config.root_dir)]
    # encoding = detect_encoding(json_path)

    # Read the content of the file
    content = blob.data_stream.read().decode("utf-8")
    data = json.loads(content)

    return data.get("dataset_id")


def save_to_json(data, filename) -> int:
    try:
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=4)
            return 0
    except Exception as e:
        logging.error(f"Failed to save to JSON: {e}")
        return 1


# Copied Django's slugify from https://github.com/django/django/blob/main/django/utils/text.py
# It's somewhat overkill for our case (which is just generating valid filenames), but it's relatively
# short, we're familiar with it, and it should be thoroughly battle-tested at this point.
def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def write_frontmatter(metadata, output_path):
    filename = (
        slugify(metadata.get("dataset_id"), allow_unicode=True) + ".md"
    )

    with open((Path(output_path) / filename), "w") as outfile:
        outfile.write("---\n")
        outfile.write(yaml.dump(metadata))
        outfile.write("---\n")
