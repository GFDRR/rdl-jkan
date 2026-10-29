#!/usr/bin/env python3
"""Generate dataset embeddings used by the site's semantic search."""

import argparse
import json
from pathlib import Path

from sentence_transformers import SentenceTransformer

import mappers


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_DATASETS_DIR = SCRIPT_DIR.parent / "_datasets" / "json"
DEFAULT_VECTORS_PATH = SCRIPT_DIR / "vectors.json"
MODEL_NAME = "all-MiniLM-L6-v2"


def _hazard_terms(metadata: dict) -> list[str]:
    """Collect hazard type/process/classification values from a dataset."""
    terms: list[str] = []
    details = metadata.get("details")
    details_hazard = details.get("hazard") if isinstance(details, dict) else None

    for source in (metadata.get("hazard"), details_hazard):
        if not isinstance(source, dict):
            continue
        for key in ("type", "process", "classification"):
            value = source.get(key)
            if isinstance(value, str):
                terms.append(value)
            elif isinstance(value, list):
                terms.extend(str(item) for item in value)

    return list(dict.fromkeys(terms))


def dataset_to_text(metadata: dict) -> str:
    """Build the text embedded for a dataset.

    The embedding model truncates input at 256 tokens, so the most
    discriminative fields (title, countries, risk data type, hazard) are placed
    first and the long description last. Embedding the raw metadata JSON
    instead would push the title and countries past the truncation limit.
    """
    parts: list[str] = []

    title = metadata.get("title")
    if title:
        parts.append(str(title))

    spatial = metadata.get("spatial")
    if isinstance(spatial, dict):
        countries = [
            country.get("title")
            for country in spatial.get("countries") or []
            if isinstance(country, dict) and country.get("title")
        ]
        if countries:
            parts.append("Countries: " + ", ".join(countries))
        if spatial.get("scale"):
            parts.append("Scale: " + str(spatial["scale"]))

    risk_data_type = metadata.get("risk_data_type")
    if risk_data_type:
        parts.append("Risk data type: " + ", ".join(map(str, risk_data_type)))

    hazards = _hazard_terms(metadata)
    if hazards:
        parts.append("Hazard: " + ", ".join(hazards))

    description = metadata.get("description")
    if description:
        parts.append(str(description))

    return "\n".join(parts)


def load_dataset_metadata(datasets_dir: Path) -> list[dict]:
    metadata = []
    for json_path in sorted(datasets_dir.glob("*.json")):
        with json_path.open(encoding="utf-8") as json_file:
            payload = json.load(json_file)

        for dataset in payload.get("datasets", []):
            metadata.append(mappers.make_dataset_frontmatter(dataset))

    if not metadata:
        raise ValueError(f"No datasets found in {datasets_dir}")

    return metadata


def generate_vectors(datasets_dir: Path, vectors_path: Path) -> int:
    datasets_metadata = load_dataset_metadata(datasets_dir)
    texts = [dataset_to_text(dataset) for dataset in datasets_metadata]

    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(
        texts,
        batch_size=32,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )

    vectors = [
        {
            "vector": embedding.tolist(),
            "metadata": metadata,
        }
        for metadata, embedding in zip(datasets_metadata, embeddings)
    ]

    vectors_path.parent.mkdir(parents=True, exist_ok=True)
    with vectors_path.open("w", encoding="utf-8") as json_file:
        json.dump(vectors, json_file, ensure_ascii=False, separators=(",", ":"))
        json_file.write("\n")

    return len(vectors)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--datasets-dir",
        type=Path,
        default=DEFAULT_DATASETS_DIR,
        help="Directory containing dataset JSON files (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_VECTORS_PATH,
        help="Output vectors JSON file (default: %(default)s)",
    )
    args = parser.parse_args()

    count = generate_vectors(args.datasets_dir, args.output)
    print(f"Generated {count} vectors at {args.output}.")


if __name__ == "__main__":
    main()
