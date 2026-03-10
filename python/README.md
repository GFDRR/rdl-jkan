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

If PyYAML gives you trouble, try running this ([source](https://github.com/yaml/pyyaml/issues/736#issuecomment-1653209769)):
```
echo 'Cython < 3.0' > /tmp/constraint.txt
PIP_CONSTRAINT=/tmp/constraint.txt pip install 'PyYAML==5.4.1'

pip install -r requirements.txt
```

### Generate markdown and/or vectors from new JSON metadata

- You can configure input and output directories in `/python/config.py`
- Open a shell here, at `/python`
- Generate datasets with `python3 main.py --markdown`
  - To run on only files modified since the most recent commit on the target branch, run `python3 main.py --ci --markdown`
  - To also generate vector embeddings for semantic search, add the `--vectors` flag, e.g. `python3 main.py --ci --markdown --vectors`
- To test semantic search performance as well, add the following argument: `--test search`
  - To configure these tests, edit `/python/tests.yml`

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
