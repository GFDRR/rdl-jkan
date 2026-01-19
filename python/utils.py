import os
import chardet
import fnmatch
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
)


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


def get_recently_changed_files(pattern):
    repo = Repo(config.root_dir)
    repo.remotes.origin.fetch()
    current_commit = repo.head.commit
    # get diff between current commit and remote target branch
    diff = current_commit.diff(f"origin/{config.remote_target_branch}")
    files = {item.a_path for item in diff}
    # add in unstaged changes
    for item in repo.index.diff(None):
        files.add(item.a_path)
    if pattern:
        return fnmatch.filter(files, pattern)
    return [os.path.join(config.root_dir, file) for file in files]


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
        slugify(metadata.get("name", metadata["title"]), allow_unicode=True) + ".md"
    )

    with open((Path(output_path) / filename), "w") as outfile:
        outfile.write("---\n")
        outfile.write(yaml.dump(metadata))
        outfile.write("---\n")
