import re
import unicodedata

import logging
from pathlib import Path


import config

import yaml


logging.basicConfig(filename=config.log_filename,
                    filemode='a',
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

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
