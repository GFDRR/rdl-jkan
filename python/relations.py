"""Links between catalogue datasets, derived from their lineage metadata."""

import re
from collections import defaultdict

# A source URL shared by more datasets than this is a portal or a home page,
# so it says nothing about which dataset was used.
MAX_DATASETS_PER_URL = 3
# Some datasets are the source of hundreds of others.
MAX_RELATED_PER_DATASET = 6


def _normalize_title(value):
    return re.sub(r"\W+", " ", value or "").strip().lower()


def _normalize_url(value):
    """Host and path, or None for a URL that is only a host."""
    url = re.sub(r"^https?://(www\.)?", "", (value or "").strip(), flags=re.I)
    url = url.split("#")[0].rstrip("/")
    return url if "/" in url else None


def make_relations(frontmatters):
    """Return [(dataset_id, related_id, relation, position)].

    A lineage source matches a catalogue dataset when its name is that
    dataset's title or its URL is one of that dataset's URLs. `relation` is
    "source" when the related dataset was used to make this one, and "derived"
    for the opposite direction.
    """
    by_title = defaultdict(list)
    by_url = defaultdict(list)
    for fm in frontmatters:
        dataset_id = fm["dataset_id"]
        by_title[_normalize_title(fm["title"])].append(dataset_id)
        urls = {
            _normalize_url(resource.get(key))
            for resource in fm["resources"]
            for key in ("access_url", "download_url")
        } | {
            _normalize_url(link.get("href"))
            for link in fm["links"]
            if link.get("rel") in ("source", "cite-as")
        }
        for url in urls - {None}:
            by_url[url].append(dataset_id)

    sources = defaultdict(dict)
    derived = defaultdict(dict)
    for fm in frontmatters:
        dataset_id = fm["dataset_id"]
        for source in (fm.get("lineage") or {}).get("sources", []):
            matches = by_title.get(_normalize_title(source.get("name")), [])
            if not matches:
                matches = by_url.get(_normalize_url(source.get("url")), [])
                if len(matches) > MAX_DATASETS_PER_URL:
                    matches = []
            for match in matches:
                if match != dataset_id:
                    sources[dataset_id][match] = None
                    derived[match][dataset_id] = None

    rows = []
    for relation, related in (("source", sources), ("derived", derived)):
        for dataset_id, matches in related.items():
            for position, match in enumerate(list(matches)[:MAX_RELATED_PER_DATASET]):
                rows.append((dataset_id, match, relation, position))
    return rows
