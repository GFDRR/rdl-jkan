import json
import sqlite3
import os
from pathlib import Path

from mappers import make_dataset_frontmatter

DATA_PATH = Path("/Users/lydiascarf/Desktop/web/rdl-jkan/_site/datasets.json")
DB_PATH = Path("/Users/lydiascarf/Desktop/web/rdl-jkan/sqlite.db")


def _serialize(value):
    """Convert values that SQLite cannot store directly (e.g., lists) to JSON strings."""
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return value


def create_tables(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute("DROP TABLE IF EXISTS datasets")
    cur.execute("DROP TABLE IF EXISTS datasets_fts")
    cur.execute("DROP TABLE IF EXISTS catalogs")
    cur.execute("DROP TABLE IF EXISTS licenses")
    cur.execute("""
        CREATE TABLE datasets (
            id TEXT PRIMARY KEY,
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
        CREATE VIRTUAL TABLE datasets_fts 
        USING fts5(
            id, title, description,
            tokenize='trigram'
        )
        """)
    conn.commit()


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
    hazard_type = _serialize((fm.get("hazard") or {}).get('type'))
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

    cur.execute(
        """
        INSERT OR REPLACE INTO datasets_fts (
            id, title, description
        ) VALUES (?, ?, ?)
        """,
        (dataset_id, title, description),
    )

    conn.commit()


def main():
    # Verify data file exists
    if not DATA_PATH.is_file():
        print(f"Data file not found: {DATA_PATH}")
        return 1

    # Load raw JSON
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except Exception as exc:
        print(f"Failed to read JSON: {exc}")
        return 1

    datasets = raw.get("datasets", [])
    if not datasets:
        print("No datasets present in the JSON file.")
        return 0

    # Connect to (or create) the SQLite DB
    conn = sqlite3.connect(DB_PATH)
    try:
        create_tables(conn)
        processed = 0
        for ds in datasets:
            try:
                fm = make_dataset_frontmatter(ds)
                insert_dataset(conn, fm)
                processed += 1
            except Exception as e:
                print(f"Error processing dataset {ds.get('id', 'UNKNOWN')}: {e}")
        print(f"Imported {processed} datasets into {DB_PATH}")
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
