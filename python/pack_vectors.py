#!/usr/bin/env python3
"""Pack vectors.json into the compact binary format used by the query function.

Outputs (next to vectors.json):
- vectors.bin: little-endian float32 matrix, one row per dataset
- vectors.ids.json: dataset_id per row, in the same order
"""

import array
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VECTORS_JSON_PATH = SCRIPT_DIR / "vectors.json"
VECTORS_BIN_PATH = SCRIPT_DIR / "vectors.bin"
VECTORS_IDS_PATH = SCRIPT_DIR / "vectors.ids.json"


def main() -> None:
    with VECTORS_JSON_PATH.open(encoding="utf-8") as json_file:
        vectors = json.load(json_file)

    ids: list[str] = []
    with VECTORS_BIN_PATH.open("wb") as bin_file:
        for item in vectors:
            metadata = item.get("metadata") or {}
            dataset_id = metadata.get("dataset_id")
            vector = item.get("vector")
            if dataset_id is None or not isinstance(vector, list):
                continue
            ids.append(str(dataset_id))
            array.array("f", vector).tofile(bin_file)

    VECTORS_IDS_PATH.write_text(json.dumps(ids), encoding="utf-8")
    print(
        f"Packed {len(ids)} vectors -> {VECTORS_BIN_PATH} "
        f"({VECTORS_BIN_PATH.stat().st_size} bytes), {VECTORS_IDS_PATH}"
    )


if __name__ == "__main__":
    main()