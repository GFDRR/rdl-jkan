## Generate semantic search vector embeddings


### Set up python environment

From `/search`, run:

Linux:

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

If PyYAML gives you trouble, try [these steps](https://github.com/yaml/pyyaml/issues/736#issuecomment-1653209769)

### Generate vectors.json

- Open a shell here, at `/search`
- Generate datasets with `python3 main.py`
