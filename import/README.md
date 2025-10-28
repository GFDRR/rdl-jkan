## Importing JSON to JKAN-compatible markdown

See here on how to convert and prepare you metadata in JSON file https://metadata.riskdatalibrary.org/

### Set up python environment

From `/import`, run:

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

### Generate datasets

- You can configure input and output directories in `config.py`
- Open a shell here, at `/import`
- Generate datasets with `python3 main.py`

### CI mode

The script can be run on files modified since the most recent commit on the
target branch (`remote_target_branch`), which can be set in `config.py`.

To run in CI mode, simply run `python3 main.py --type ci` in `/import`.
 CI mode was developed to support the import GitHub action.