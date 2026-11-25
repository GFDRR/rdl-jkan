## Importing JSON files

See here on how to convert and prepare you metadata in JSON file https://metadata.riskdatalibrary.org/

### Set up python environment

From `/python`, run:

Linux or Mac:

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Windows:
```
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```


### Check the dataset files

Pull requests run these checks (`.github/workflows/check.yml`). To run them locally:

```
python check_datasets.py --base origin/rdl-1.0   # the files changed on this branch
python check_datasets.py --all                   # every file, takes minutes
python -m unittest discover -s tests
```

Each file must be valid JSON in UTF-8, hold one dataset, and be named after the dataset's id, which no other dataset may use. Changed files must also follow the RDLS schema. An edit must keep the dataset's id, since the id is its URL.

### Build the site's data

```
python import.py
```

This writes, from the files in `_datasets/json`:

- `sqlite.db`: what the dataset pages are built from
- `search.db`: what the query function searches
- `catalog.jsonld`: the catalogue in DCAT (JSON-LD), for harvesting by other catalogues
- `dataset-ids.json`: the ids in use, for editors to check that a new id is free

`generate_vectors.py` and `pack_vectors.py` build the vectors for semantic search. The deploy workflow runs all of them.

The query function has its own tests, which need `search.db`. From the repository root:

```
node --test "netlify/tests/*.test.mjs"
```

### Handling multi-dataset JSON files

Prerequisites:

- install `jq` on your local machine.

Run the following in bash in the `_datasets/json` directory:

```
for f in *.json; do
  echo "Processing file: $f"
  if jq empty "$f" >/dev/null 2>&1; then
    count=$(jq '.datasets | length' "$f")
    echo " - Number of datasets: $count"
    if [ "$count" -gt 1 ]; then
      echo " - Splitting datasets..."
      jq -c '.datasets[] | {id, data: .}' "$f" | while IFS= read -r line; do
        id=$(jq -r '.id' <<<"$line") || { echo " - Error extracting ID"; continue; }
        jq -c '{datasets: [ .data ] }' <<<"$line" > "$id.json"
        echo "   - Created file: $id.json"
      done
      rm "$f"
      echo " - Deleted original file: $f"
    else
      echo " - Only one dataset; no action taken."
    fi
  else
    echo "Invalid JSON in file: $f"
  fi
done
```
