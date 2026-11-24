#!/usr/bin/env python3
"""Check the dataset JSON files before they are merged.

Every file is checked for encoding, JSON syntax and id/filename collisions. The
files changed since --base (or all of them, with --all) are also validated
against the RDLS schema and passed through the mappers that build the site.

Exits with 1 when there are errors. Warnings do not fail the check.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import requests
import yaml
from jsonschema import validators

import config
import mappers
from validator import custom_properties, custom_required

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
DATASETS_JSON_DIR = ROOT_DIR / "_datasets" / "json"
JSON_DIR_IN_REPO = "_datasets/json/"
SCHEMA_PATH = SCRIPT_DIR / "rdls_schema.json"

ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
COMPONENTS = ("hazard", "exposure", "vulnerability", "loss")
BAD_CHARACTERS = {
    " ": "non-breaking space (U+00A0)",
    "​": "zero-width space (U+200B)",
    "﻿": "byte order mark (U+FEFF)",
    "�": "replacement character (U+FFFD), text was decoded wrongly",
}
# UTF-8 text that was read as Windows-1252, e.g. "Ã©" for "é".
MOJIBAKE = re.compile("[ÃÂ][\u0080-¿]|â€")
MAX_SCHEMA_ERRORS_PER_FILE = 10


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, name, message):
        self.errors.append((name, message))

    def warning(self, name, message):
        self.warnings.append((name, message))


def reject_duplicate_keys(pairs):
    keys = [key for key, _ in pairs]
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    if duplicates:
        raise ValueError(f"duplicate key(s): {', '.join(duplicates)}")
    return dict(pairs)


def load_dataset(name, raw, report):
    """The dataset in a file, or None (with an error reported)."""
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        report.error(name, f"not valid UTF-8: {exc}")
        return None
    if text.startswith("﻿"):
        report.error(name, "starts with a byte order mark; save as UTF-8 without BOM")
        return None
    try:
        data = json.loads(text, object_pairs_hook=reject_duplicate_keys)
    except ValueError as exc:
        report.error(name, f"invalid JSON: {exc}")
        return None
    datasets = data.get("datasets") if isinstance(data, dict) else None
    if not isinstance(datasets, list) or len(datasets) != 1:
        report.error(name, 'must be {"datasets": [...]} with exactly one dataset')
        return None
    if not isinstance(datasets[0], dict):
        report.error(name, "the dataset must be an object")
        return None
    return datasets[0]


def check_text(name, dataset, report):
    # Dumped again, so that escaped characters ( ) are found as well.
    text = json.dumps(dataset, ensure_ascii=False)
    for character, label in BAD_CHARACTERS.items():
        if character in text:
            report.error(name, f"contains a {label}")
    match = MOJIBAKE.search(text)
    if match:
        context = text[max(0, match.start() - 20) : match.end() + 20]
        report.error(name, f"text with the wrong encoding: …{context}…")


def check_id(name, dataset, names_by_id, report):
    dataset_id = dataset.get("id")
    if not isinstance(dataset_id, str) or not ID_PATTERN.fullmatch(dataset_id):
        report.error(
            name,
            f"id {dataset_id!r} must have only letters, digits, hyphens and underscores",
        )
        return
    if name != f"{dataset_id}.json":
        report.error(name, f"must be named {dataset_id}.json, after the dataset's id")
    # Ids become URLs and file names, so they must differ by more than case.
    other = names_by_id.setdefault(dataset_id.lower(), name)
    if other != name:
        report.error(name, f"id {dataset_id!r} is already used by {other}")


def check_bbox(name, dataset, report):
    bbox = (dataset.get("spatial") or {}).get("bbox")
    if bbox is not None and not mappers.is_geographic_bbox(bbox):
        report.warning(name, f"spatial.bbox is not in degrees: {bbox}")


def check_components(name, dataset, report):
    declared = dataset.get("risk_data_type") or []
    for component in COMPONENTS:
        if component in declared and not dataset.get(component):
            report.warning(
                name, f"risk_data_type lists {component}, but it is not described"
            )
        if component not in declared and dataset.get(component):
            report.warning(
                name, f"{component} is described, but not listed in risk_data_type"
            )
    for event_set in (dataset.get("hazard") or {}).get("event_sets", []):
        for event in event_set.get("events", []):
            if not event.get("occurrence"):
                report.warning(name, f"event {event.get('id')!r} has no occurrence")


def get_schema():
    if not SCHEMA_PATH.is_file():
        response = requests.get(config.schema_url, timeout=60)
        response.raise_for_status()
        SCHEMA_PATH.write_text(response.text, encoding="utf-8")
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def make_schema_validator(schema):
    base = validators.validator_for(schema)
    checks = dict(base.VALIDATORS)
    checks["properties"] = custom_properties
    checks["required"] = custom_required
    return validators.create(meta_schema=base.META_SCHEMA, validators=checks)(schema)


def check_schema(name, dataset, schema_validator, report):
    errors = sorted(schema_validator.iter_errors(dataset), key=lambda e: e.json_path)
    for error in errors[:MAX_SCHEMA_ERRORS_PER_FILE]:
        message = error.message
        if len(message) > 300:
            message = message[:300] + "…"
        report.error(name, f"{error.json_path}: {message}")
    if len(errors) > MAX_SCHEMA_ERRORS_PER_FILE:
        more = len(errors) - MAX_SCHEMA_ERRORS_PER_FILE
        report.error(name, f"…and {more} more schema error(s)")


def check_mapping(name, dataset, report):
    try:
        mappers.make_dataset_frontmatter(dataset)
    except Exception as exc:
        report.error(name, f"cannot be shown on the site: {exc!r}")


def check_yaml(report):
    for path in git("ls-files", "*.yml", "*.yaml").splitlines():
        try:
            yaml.safe_load((ROOT_DIR / path).read_text(encoding="utf-8"))
        except (yaml.YAMLError, UnicodeDecodeError) as exc:
            report.error(path, f"invalid YAML: {exc}")


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT_DIR, check=True, capture_output=True, encoding="utf-8"
    ).stdout


def get_changes(base):
    """{"A"|"M"|"D": [file name]} since the branch left `base`."""
    # Renames are reported as a deletion and an addition.
    output = git(
        "-c", "core.quotepath=off", "diff", "--name-status", "--no-renames",
        f"{base}...HEAD", "--", JSON_DIR_IN_REPO,
    )  # fmt: skip
    changes = {"A": [], "M": [], "D": []}
    for line in output.splitlines():
        status, path = line.split("\t", 1)
        changes[status if status in changes else "M"].append(Path(path).name)
    return changes


def check_edits(changes, base, datasets, report):
    """An edit must keep the id: changing it would break the dataset's URL."""
    merge_base = git("merge-base", base, "HEAD").strip()
    for name in changes["M"]:
        if name not in datasets:
            continue
        try:
            old = json.loads(git("show", f"{merge_base}:{JSON_DIR_IN_REPO}{name}"))
            old_dataset = old["datasets"][0]
        except (ValueError, KeyError, IndexError):
            continue  # The old version was broken; nothing to compare with.
        new_dataset = datasets[name]
        if old_dataset.get("id") != new_dataset.get("id"):
            report.error(
                name,
                f"edits {old_dataset.get('id')!r} but changes its id to "
                f"{new_dataset.get('id')!r}",
            )
        elif old_dataset.get("title") != new_dataset.get("title"):
            report.warning(
                name,
                "replaces an existing dataset with another title: "
                f"{old_dataset.get('title')!r} -> {new_dataset.get('title')!r}. "
                "If this is a new dataset, give it a new id",
            )


def render(report, changes, total):
    lines = ["## Dataset checks", "", f"{total} dataset files."]
    if changes:
        for status, label in (("A", "Added"), ("M", "Edited"), ("D", "Deleted")):
            if changes[status]:
                names = sorted(changes[status])
                shown = ", ".join(f"`{n}`" for n in names[:20])
                more = f" and {len(names) - 20} more" if len(names) > 20 else ""
                lines.append(f"- {label}: {shown}{more}")
    for title, items in (("Errors", report.errors), ("Warnings", report.warnings)):
        if items:
            lines += ["", f"### {title} ({len(items)})", ""]
            lines += [f"- `{name}`: {message}" for name, message in items]
    if not report.errors:
        lines += ["", "No errors found."]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--base", help="Validate only the files changed since this ref")
    group.add_argument(
        "--all", action="store_true", help="Validate every file (takes minutes)"
    )
    args = parser.parse_args()

    report = Report()
    changes = get_changes(args.base) if args.base else None
    datasets = {}
    names_by_id = {}
    for path in sorted(DATASETS_JSON_DIR.glob("*")):
        name = path.name
        if path.suffix != ".json":
            report.error(name, "only .json files belong in _datasets/json")
            continue
        dataset = load_dataset(name, path.read_bytes(), report)
        if dataset is None:
            continue
        datasets[name] = dataset
        check_text(name, dataset, report)
        check_id(name, dataset, names_by_id, report)

    if args.all:
        to_validate = list(datasets)
    elif changes:
        to_validate = [n for n in changes["A"] + changes["M"] if n in datasets]
    else:
        to_validate = []
    if to_validate:
        schema_validator = make_schema_validator(get_schema())
        for name in to_validate:
            check_schema(name, datasets[name], schema_validator, report)
            check_mapping(name, datasets[name], report)
            check_components(name, datasets[name], report)
            check_bbox(name, datasets[name], report)
    if changes:
        check_edits(changes, args.base, datasets, report)
    check_yaml(report)

    text = render(report, changes, len(datasets))
    sys.stdout.reconfigure(encoding="utf-8")
    print(text)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write(text)
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
