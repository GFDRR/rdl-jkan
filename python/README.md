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

- You can configure input and output directories in `config.py`
- Open a shell here, at `/python`
- Generate datasets with `python3 main.py --markdown`
  - To run on only files modified since the most recent commit on the target branch, run `python3 main.py --ci --markdown`
  - To also generate vector embeddings for semantic search, add the `--vectors` flag, e.g. `python3 main.py --ci --markdown --vectors`
