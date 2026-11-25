#!/usr/bin/env python3
"""Check that a built site has what search engines and harvesters need."""

import json
import re
import sys
from pathlib import Path


def main():
    site = Path(sys.argv[1])
    ids = json.loads((site / "dataset-ids.json").read_text(encoding="utf-8"))
    errors = []

    catalog = json.loads((site / "catalog.jsonld").read_text(encoding="utf-8"))
    if len(catalog["dcat:dataset"]) != len(ids):
        errors.append(f"catalog.jsonld has {len(catalog['dcat:dataset'])} datasets")

    datasets = json.loads((site / "datasets.json").read_text(encoding="utf-8"))
    if len(datasets["datasets"]) != len(ids):
        errors.append(f"datasets.json has {len(datasets['datasets'])} datasets")

    sitemap = (site / "sitemap.xml").read_text(encoding="utf-8")
    if not sitemap.startswith("<?xml"):
        errors.append("sitemap.xml does not start with an XML declaration")
    # All the datasets and the home page.
    if sitemap.count("<loc>") != len(ids) + 1:
        errors.append(f"sitemap.xml has {sitemap.count('<loc>')} URLs")

    for dataset_id in ids:
        page = site / "datasets" / dataset_id / "index.html"
        if not page.is_file():
            errors.append(f"{dataset_id}: no page")
            continue
        html = page.read_text(encoding="utf-8")
        if "/css/dataset.css" not in html:
            errors.append(f"{dataset_id}: no dataset.css")
        match = re.search(
            r'<script type="application/ld\+json">(.*?)</script>', html, re.S
        )
        try:
            metadata = json.loads(match.group(1)) if match else {}
        except ValueError as exc:
            errors.append(f"{dataset_id}: invalid JSON-LD: {exc}")
            continue
        if not (metadata.get("name") and metadata.get("description")):
            errors.append(f"{dataset_id}: JSON-LD without a name or description")
        # The library of the map.
        if "/leaflet.js" not in html or "/leaflet.css" not in html:
            errors.append(f"{dataset_id}: no Leaflet")

    for error in errors[:50]:
        print(error)
    print(f"{len(ids)} datasets, {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
