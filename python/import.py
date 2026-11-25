import json
import sqlite3
import os
from pathlib import Path

from mappers import make_dataset_frontmatter
from relations import make_relations
from structured_data import make_dcat_catalog, make_schema_org

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
# Dataset JSON files, merged in the same order as the site's load_data_json
# filter (_plugins/load_data_json.rb) and the root datasets.json page.
DATASETS_JSON_DIR = ROOT_DIR / "_datasets" / "json"
DB_PATH = ROOT_DIR / "sqlite.db"
# Published as they are by Jekyll. The first is the endpoint for harvesters; the
# second lets editors check whether a dataset id is already in use.
DCAT_PATH = ROOT_DIR / "catalog.jsonld"
DATASET_IDS_PATH = ROOT_DIR / "dataset-ids.json"


def _serialize(value):
    """Convert values that SQLite cannot store directly (e.g., lists) to JSON strings."""
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return value


def create_tables(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("DROP TABLE IF EXISTS dataset_jsonld")
    cur.execute("DROP TABLE IF EXISTS dataset_relations")
    cur.execute("DROP TABLE IF EXISTS datasets")
    cur.execute("DROP TABLE IF EXISTS datasets_fts")
    cur.execute("DROP TABLE IF EXISTS catalogs")
    cur.execute("DROP TABLE IF EXISTS licenses")
    cur.execute("""
        CREATE TABLE datasets (
            rowid INTEGER PRIMARY KEY AUTOINCREMENT,
            id TEXT UNIQUE,
            catalog_slug TEXT,
            description TEXT,
            frontmatter TEXT,
            hazard_type TEXT,
            license_slug TEXT,
            project TEXT,
            risk_data_type TEXT,
            slug TEXT,
            spatial TEXT,
            temporal TEXT,
            title TEXT,
            version TEXT,
            FOREIGN KEY(catalog_slug) REFERENCES catalogs(slug) ON DELETE SET NULL,
            FOREIGN KEY(license_slug) REFERENCES licenses(slug) ON DELETE SET NULL
        );
        """)
    cur.execute("""
        CREATE TABLE catalogs (
            slug TEXT PRIMARY KEY,
            title TEXT,
            url TEXT
        );
        """)
    cur.execute("""
        CREATE TABLE licenses (
            slug TEXT PRIMARY KEY,
            title TEXT,
            url TEXT
        );
        """)
    cur.execute("""
        CREATE TABLE dataset_jsonld (
            dataset_id TEXT PRIMARY KEY,
            schema_org TEXT
        );
        """)
    cur.execute("""
        CREATE TABLE dataset_relations (
            dataset_id TEXT,
            related_id TEXT,
            relation TEXT,
            position INTEGER,
            PRIMARY KEY (dataset_id, relation, position)
        );
        """)
    # bm25() in netlify/functions/query weighs these columns by position: keep
    # FTS_COLUMN_WEIGHTS there in the same order.
    cur.execute("""
        CREATE VIRTUAL TABLE datasets_fts USING fts5(
            id,
            title,
            description,
            catalog,
            creator,
            countries,
            license,
            project,
            risk_data_type,
            hazard_type,
            resources,
            details,
            purpose,
            publisher,
            contact_point,
            lineage,
            exposure,
            loss,
            hazard,
            spatial,
            temporal,
            version,
            attributions,
            vulnerability,
            referenced_by,
            content='',
            tokenize=trigram
        );
    """)
    conn.commit()


def _fts_keyword_text(fm: dict) -> dict:
    def _flatten(value):
        if value is None:
            return ""
        if isinstance(value, dict):
            return " ".join(_flatten(v) for v in value.values())
        if isinstance(value, list):
            return " ".join(_flatten(v) for v in value)
        return str(value)

    def _text(*paths):
        parts = []
        for path in paths:
            value = fm
            for key in path.split("."):
                if isinstance(value, dict):
                    value = value.get(key)
                else:
                    value = None
                    break
            parts.append(_flatten(value))
        return " ".join(parts).strip()

    countries = _text("spatial.countries")
    catalog = _text("catalog.title", "catalog.slug")
    creator = _text("creator.name", "creator.affiliation.name")
    publisher = _text("publisher.name", "publisher.affiliation.name")
    contact_point = _text("contact_point.name", "contact_point.affiliation.name")
    license = _text("license.title")
    project = _text("project.title")
    resources = _text("resources")
    # The descriptions of the sources are about other datasets: only shown.
    lineage = _flatten(
        [
            (fm.get("lineage") or {}).get("description"),
            [
                {key: value for key, value in source.items() if key != "description"}
                for source in (fm.get("lineage") or {}).get("sources") or []
            ],
        ]
    ).strip()
    exposure = _text("exposure")
    loss = _text("loss")
    hazard = _text("hazard")
    spatial = _text("spatial.scale", "spatial.gazetteer_entries")
    temporal = _text("temporal")
    attributions = " ".join(
        _flatten([entity.get("name"), (entity.get("affiliation") or {}).get("name")])
        for entity in (a["entity"] for a in fm.get("attributions") or [])
    )
    referenced_by = " ".join(
        _flatten([r.get("name"), r.get("author_names"), r.get("doi")])
        for r in fm.get("referenced_by") or []
    )

    return {
        "id": _text("dataset_id"),
        "title": _text("title"),
        "description": _text("description"),
        "catalog": catalog,
        "creator": creator,
        "countries": countries,
        "license": license,
        "project": project,
        "risk_data_type": _text("risk_data_type"),
        "hazard_type": _text("hazard.type"),
        "resources": resources,
        "details": _text("details"),
        "purpose": _text("purpose"),
        "publisher": publisher,
        "contact_point": contact_point,
        "lineage": lineage,
        "exposure": exposure,
        "loss": loss,
        "hazard": hazard,
        "spatial": spatial,
        "temporal": temporal,
        "version": _text("version"),
        "attributions": attributions,
        "vulnerability": _text("vulnerability"),
        "referenced_by": referenced_by,
    }


def insert_dataset(conn: sqlite3.Connection, fm: dict):
    cur = conn.cursor()
    dataset_id = _serialize(fm.get("dataset_id"))
    title = _serialize(fm.get("title"))
    description = _serialize(fm.get("description"))
    license = fm.get("license")
    catalog = fm.get("catalog")
    project = _serialize(fm.get("project"))
    risk_data_type = _serialize(fm.get("risk_data_type"))
    slug = _serialize(fm.get("slug"))
    hazard_type = _serialize((fm.get("hazard") or {}).get("type"))
    spatial = _serialize(fm.get("spatial"))
    temporal = _serialize(fm.get("temporal"))
    version = _serialize(fm.get("version"))

    catalog_slug = catalog.get("slug")
    cur.execute(
        """
        INSERT OR IGNORE INTO catalogs (title, url, slug)
        VALUES (?, ?, ?)
        """,
        (
            catalog.get("title"),
            catalog.get("url"),
            catalog_slug,
        ),
    )
    license_slug = license.get("slug")
    cur.execute(
        """
        INSERT OR IGNORE INTO licenses (title, url, slug)
        VALUES (?, ?, ?)
        """,
        (
            license.get("title"),
            license.get("url"),
            license_slug,
        ),
    )
    cur.execute(
        """
        INSERT OR REPLACE INTO datasets (
            id, title, description,
            hazard_type, license_slug,
            project, catalog_slug,
            risk_data_type, slug,
            spatial, temporal, version,
            frontmatter
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?)
        """,
        (
            dataset_id,
            title,
            description,
            hazard_type,
            license_slug,
            project,
            catalog_slug,
            risk_data_type,
            slug,
            spatial,
            temporal,
            version,
            json.dumps(fm),
        ),
    )

    # Rebuild the FTS row for this dataset (handles both insert and update).
    # The FTS table is contentless (content=''), which does not support
    # INSERT OR REPLACE, so delete then insert.
    fts = _fts_keyword_text(fm)
    rowid = cur.lastrowid
    cur.execute("DELETE FROM datasets_fts WHERE rowid = ?", (rowid,))
    cur.execute(
        """
        INSERT INTO datasets_fts(
            rowid, id, title, description, catalog, creator, countries,
            license, project, risk_data_type, hazard_type, resources,
            details, purpose, publisher, contact_point, lineage, exposure,
            loss, hazard, spatial, temporal, version, attributions,
            vulnerability, referenced_by
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?
        )
        """,
        (
            rowid,
            fts["id"],
            fts["title"],
            fts["description"],
            fts["catalog"],
            fts["creator"],
            fts["countries"],
            fts["license"],
            fts["project"],
            fts["risk_data_type"],
            fts["hazard_type"],
            fts["resources"],
            fts["details"],
            fts["purpose"],
            fts["publisher"],
            fts["contact_point"],
            fts["lineage"],
            fts["exposure"],
            fts["loss"],
            fts["hazard"],
            fts["spatial"],
            fts["temporal"],
            fts["version"],
            fts["attributions"],
            fts["vulnerability"],
            fts["referenced_by"],
        ),
    )


def insert_jsonld(conn: sqlite3.Connection, fm: dict):
    # Escaped so that no metadata text can close the <script> element the page
    # puts it in.
    schema_org = json.dumps(make_schema_org(fm), ensure_ascii=False)
    conn.execute(
        "INSERT INTO dataset_jsonld (dataset_id, schema_org) VALUES (?, ?)",
        (fm["dataset_id"], schema_org.replace("<", "\\u003c")),
    )


def insert_relations(conn: sqlite3.Connection, frontmatters: list[dict]):
    conn.executemany(
        """
        INSERT INTO dataset_relations (dataset_id, related_id, relation, position)
        VALUES (?, ?, ?, ?)
        """,
        make_relations(frontmatters),
    )


def write_json(path: Path, value):
    path.write_text(
        json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


def main():
    # Verify data directory exists
    if not DATASETS_JSON_DIR.is_dir():
        print(f"Datasets directory not found: {DATASETS_JSON_DIR}")
        return 1

    # Load and merge the raw dataset JSON files
    datasets = []
    try:
        for json_path in sorted(DATASETS_JSON_DIR.glob("*.json")):
            with json_path.open("r", encoding="utf-8") as f:
                datasets.extend(json.load(f).get("datasets", []))
    except Exception as exc:
        print(f"Failed to read dataset JSON: {exc}")
        return 1

    if not datasets:
        print("No datasets present in the JSON files.")
        return 0

    # Connect to (or create) the SQLite DB
    conn = sqlite3.connect(DB_PATH)
    try:
        create_tables(conn)
        frontmatters = []
        failed = 0
        for ds in datasets:
            try:
                fm = make_dataset_frontmatter(ds)
                insert_dataset(conn, fm)
                insert_jsonld(conn, fm)
                frontmatters.append(fm)
            except Exception as e:
                failed += 1
                print(f"Error processing dataset {ds.get('id', 'UNKNOWN')}: {e!r}")
        insert_relations(conn, frontmatters)
        conn.commit()
        print(f"Imported {len(frontmatters)} datasets into {DB_PATH}")
    finally:
        conn.close()

    write_json(DCAT_PATH, make_dcat_catalog(frontmatters))
    write_json(DATASET_IDS_PATH, sorted(fm["dataset_id"] for fm in frontmatters))
    print(f"Wrote {DCAT_PATH} and {DATASET_IDS_PATH}")

    if failed:
        # Fail the build rather than deploy a catalogue with datasets missing.
        print(f"{failed} dataset(s) could not be imported")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
