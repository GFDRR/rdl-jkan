// Query proxy for the site's search data.
//
// sqlite.db, vectors.bin and vectors.ids.json live in the site's "rdl-data"
// Netlify Blobs store (uploaded by CI — see .github/workflows/deploy.yml).
// This function streams sqlite.db to a temp file and opens it read-only with
// the built-in node:sqlite driver (cached across warm invocations), runs the
// site's SQL/semantic search server-side, and returns small JSON pages. The
// database itself is never sent to the client.
//
// Set RDL_DATA_DIR to read the data files from disk instead of Blobs
// (local development and tests).

import { DatabaseSync } from "node:sqlite";
import { createWriteStream } from "node:fs";
import { mkdir, rename, rm } from "node:fs/promises";
import { Readable } from "node:stream";
import { pipeline } from "node:stream/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";

const BLOB_STORE = "rdl-data";

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

// Column lists mirror the queries the client used to run against sql.js in
// the browser (scripts/src/datasets/index.js and scripts/src/dataset/index.js).
const PAGE_COLUMNS = `
  c.title as catalog_title, c.slug,
  l.title as license_title, l.slug as license_slug, l.url as license_url,
  json_extract(datasets.frontmatter, '$.contact_point') as contact_point,
  json_extract(datasets.frontmatter, '$.creator') as creator,
  json_extract(datasets.frontmatter, '$.details') as details,
  json_extract(datasets.frontmatter, '$.publisher') as publisher,
  json_extract(datasets.frontmatter, '$.resources') as resources,
  json_extract(datasets.spatial, '$.countries') as countries,
  datasets.*
`;

const DETAIL_COLUMNS = `
  c.title as catalog_title, c.slug,
  l.title as license_title, l.slug as license_slug, l.url as license_url,
  json_extract(datasets.frontmatter, '$.contact_point') as contact_point,
  json_extract(datasets.frontmatter, '$.creator') as creator,
  json_extract(datasets.frontmatter, '$.details') as details,
  json_extract(datasets.frontmatter, '$.exposure') as exposure,
  json_extract(datasets.frontmatter, '$.loss') as loss,
  json_extract(datasets.frontmatter, '$.publisher') as publisher,
  json_extract(datasets.frontmatter, '$.purpose') as purpose,
  json_extract(datasets.frontmatter, '$.resources') as resources,
  json_extract(datasets.frontmatter, '$.vulnerability') as vulnerability,
  datasets.*
`;

const DATASET_FROM = `
  FROM datasets
    LEFT JOIN catalogs c ON datasets.catalog_slug = c.slug
    LEFT JOIN licenses l ON datasets.license_slug = l.slug
`;

// Must match scripts/src/datasets/search.js and python/config.py.
const SEMANTIC_MAX_RESULTS = 50;
const SEMANTIC_MIN_SCORE = 0.25;
const MAX_PAGE_SIZE = 50;
const DEFAULT_PAGE_SIZE = 10;
const MAX_FILTER_VALUES = 100;
const ID_CHUNK_SIZE = 500;

let dbPromise = null;
let vectorsPromise = null;

function toArrayBuffer(bytes) {
  if (bytes instanceof ArrayBuffer) return bytes;
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
}

async function loadData(name) {
  const dir = process.env.RDL_DATA_DIR;
  if (dir) {
    const { readFile } = await import("node:fs/promises");
    return readFile(join(dir, name));
  }
  // Imported lazily so local runs (RDL_DATA_DIR set) never need the module.
  const { getStore } = await import("@netlify/blobs");
  const bytes = await getStore({ name: BLOB_STORE }).get(name, {
    type: "arrayBuffer",
  });
  if (!bytes) {
    throw new Error(`"${name}" not found in Netlify Blobs store "${BLOB_STORE}"`);
  }
  return bytes;
}

async function getDbPath() {
  const dir = process.env.RDL_DATA_DIR;
  if (dir) return join(dir, "sqlite.db");

  const dataDir = join(tmpdir(), "rdl-data");
  const dbPath = join(dataDir, "sqlite.db");
  const partialPath = `${dbPath}.${process.pid}.part`;
  const { getStore } = await import("@netlify/blobs");
  const stream = await getStore({ name: BLOB_STORE }).get("sqlite.db", {
    type: "stream",
  });
  if (!stream) {
    throw new Error(`"sqlite.db" not found in Netlify Blobs store "${BLOB_STORE}"`);
  }

  await mkdir(dataDir, { recursive: true });
  try {
    await pipeline(Readable.fromWeb(stream), createWriteStream(partialPath));
    await rename(partialPath, dbPath);
  } catch (error) {
    await rm(partialPath, { force: true });
    throw error;
  }
  return dbPath;
}

function getDb() {
  dbPromise ??= (async () => {
    const dbPath = await getDbPath();
    return new DatabaseSync(dbPath, { readOnly: true });
  })().catch((error) => {
    // Don't cache a failed load — let a later invocation retry.
    dbPromise = null;
    throw error;
  });
  return dbPromise;
}

// vectors.bin is a little-endian float32 matrix (one row per dataset, in the
// order of vectors.ids.json). Vectors are L2-normalized, so the dot product
// is the cosine similarity.
function getVectors() {
  vectorsPromise ??= (async () => {
    const [bin, ids] = await Promise.all([
      loadData("vectors.bin"),
      loadData("vectors.ids.json"),
    ]);
    const idList = JSON.parse(new TextDecoder().decode(ids));
    const floats = new Float32Array(toArrayBuffer(bin));
    const dims = idList.length ? Math.floor(floats.length / idList.length) : 0;
    return { ids: idList, floats, dims };
  })();
  return vectorsPromise;
}

function exec(db, sql, params = []) {
  const rows = db.prepare(sql).all(...params);
  // node:sqlite returns rows as objects; derive the column list from the first
  // row. Duplicate column names collapse to the last value, which matches how
  // rowsToObjects() built objects from the old sql.js {columns, values} shape.
  const columns = rows.length ? Object.keys(rows[0]) : [];
  const values = rows.map((row) => columns.map((name) => row[name]));
  return [{ columns, values }];
}

// Mirrors transformShape in the old client code: JSON-parse any string value
// that is valid JSON (frontmatter, spatial, json_extract results, ...).
function rowsToObjects(result) {
  if (!result || !Array.isArray(result)) return [];
  return result.flatMap(({ columns, values }) => {
    if (!columns || !values || !Array.isArray(values)) return [];
    return values.map((row) => {
      const obj = {};
      columns.forEach((column, index) => {
        let value = row[index];
        if (typeof value === "string") {
          try {
            value = JSON.parse(value);
          } catch {
            // Not valid JSON, keep the original string value.
          }
        }
        obj[column] = value;
      });
      return obj;
    });
  });
}

// Server-side port of getWhereSqlForFilters() from the old client code. All
// values are bound as parameters — nothing from the request is ever
// interpolated into SQL.
function buildFilterClauses(filters, excludeType = null) {
  const clauses = [];
  const params = [];

  const values = (type) => {
    const list = filters?.[type];
    if (!Array.isArray(list)) return [];
    return list
      .filter((value) => typeof value === "string" && value.length > 0)
      .slice(0, MAX_FILTER_VALUES);
  };

  const addEquals = (type, column) => {
    const list = values(type);
    if (!list.length) return;
    clauses.push(`(${list.map(() => `${column} = ?`).join(" OR ")})`);
    params.push(...list);
  };
  const addLike = (type, expression) => {
    const list = values(type);
    if (!list.length) return;
    clauses.push(`(${list.map(() => `${expression} LIKE '%' || ? || '%'`).join(" OR ")})`);
    params.push(...list);
  };

  if (excludeType !== "catalog") addEquals("catalog", "datasets.catalog_slug");
  if (excludeType !== "countries") {
    addLike("countries", "json_extract(datasets.spatial, '$.countries')");
  }
  if (excludeType !== "geo_scale") {
    addLike("geo_scale", "json_extract(datasets.spatial, '$.scale')");
  }
  if (excludeType !== "project") {
    addLike("project", "json_extract(datasets.project, '$')");
  }
  if (excludeType !== "risk_data_type") {
    addLike("risk_data_type", "json_extract(datasets.risk_data_type, '$')");
  }
  // No "IS NOT NULL" guard needed: NULL LIKE anything is NULL, so NULL rows
  // never match anyway.
  if (excludeType !== "hazard_type") addLike("hazard_type", "datasets.hazard_type");
  if (excludeType !== "license") addEquals("license", "datasets.license_slug");

  return { clauses, params };
}

function whereSql(clauses) {
  return clauses.length ? `WHERE ${clauses.join(" AND ")}` : "";
}

function andSql(clauses) {
  return clauses.length ? ` AND ${clauses.join(" AND ")}` : "";
}

function pageParams(body) {
  const page = Math.max(1, Math.floor(Number(body?.page)) || 1);
  const pageSize = Math.min(
    Math.max(1, Math.floor(Number(body?.pageSize)) || DEFAULT_PAGE_SIZE),
    MAX_PAGE_SIZE,
  );
  return { page, pageSize };
}

function fetchPageRows(db, clauses, params, page, pageSize) {
  const result = exec(
    db,
    `SELECT ${PAGE_COLUMNS} ${DATASET_FROM} ${whereSql(clauses)}
     ORDER BY datasets.rowid LIMIT ? OFFSET ?`,
    [...params, pageSize, (page - 1) * pageSize],
  );
  return rowsToObjects(result);
}

async function handleDatasets(body) {
  const db = await getDb();
  const { clauses, params } = buildFilterClauses(body.filters);
  const { page, pageSize } = pageParams(body);

  const total =
    exec(db, `SELECT COUNT(*) FROM datasets ${whereSql(clauses)}`, params)[0]
      ?.values[0][0] ?? 0;
  const clampedPage = Math.min(page, Math.max(1, Math.ceil(total / pageSize)));
  const rows =
    total === 0
      ? []
      : fetchPageRows(db, clauses, params, clampedPage, pageSize);

  return { rows, total, page: clampedPage };
}

async function handleDataset(body) {
  const db = await getDb();
  const id = typeof body?.id === "string" ? body.id : "";
  if (!id) return { dataset: null };
  const result = exec(
    db,
    `SELECT ${DETAIL_COLUMNS} ${DATASET_FROM} WHERE datasets.id = ?`,
    [id],
  );
  return { dataset: rowsToObjects(result)[0] ?? null };
}

// Ids from a candidate list that also pass the active filters. Chunked to
// stay well under SQLite's bound-parameter limit.
function selectIds(db, ids, clauses, params) {
  const found = new Set();
  for (let start = 0; start < ids.length; start += ID_CHUNK_SIZE) {
    const chunk = ids.slice(start, start + ID_CHUNK_SIZE);
    const placeholders = chunk.map(() => "?").join(", ");
    const result = exec(
      db,
      `SELECT datasets.id FROM datasets
       WHERE datasets.id IN (${placeholders})${andSql(clauses)}`,
      [...chunk, ...params],
    );
    for (const [id] of result[0]?.values ?? []) found.add(id);
  }
  return found;
}

function semanticSearch(vectors, queryVector, { exclude, limit, minScore }) {
  if (!vectors?.dims || queryVector.length !== vectors.dims) return [];
  const { ids, floats, dims } = vectors;
  const scores = [];
  for (let row = 0; row < ids.length; row++) {
    const id = ids[row];
    if (exclude.has(id)) continue;
    let dot = 0;
    const base = row * dims;
    for (let i = 0; i < dims; i++) dot += queryVector[i] * floats[base + i];
    if (dot >= minScore) scores.push([id, dot]);
  }
  scores.sort((a, b) => b[1] - a[1]);
  return scores.slice(0, limit).map(([id]) => id);
}

async function handleSearch(body) {
  const q = typeof body?.q === "string" ? body.q.trim() : "";
  if (!q) return handleDatasets(body);

  const db = await getDb();
  const { clauses, params } = buildFilterClauses(body.filters);
  const { page, pageSize } = pageParams(body);

  // Keyword (FTS) results, best first — same query the client used to run.
  let keywordIds = [];
  try {
    const phrase = `"${q.replace(/"/g, '""')}"`;
    const result = exec(
      db,
      `SELECT datasets.id AS dataset_id
       FROM datasets_fts
         JOIN datasets ON datasets.rowid = datasets_fts.rowid
       WHERE datasets_fts MATCH ?
       ORDER BY bm25(datasets_fts)`,
      [phrase],
    );
    keywordIds = (result[0]?.values ?? []).map(([id]) => id);
  } catch (error) {
    // Malformed match expression (e.g. stray FTS operators) — degrade to
    // semantic-only results instead of failing the request.
    console.error("FTS query failed:", error);
  }

  // Semantic results appended after keyword results, mirroring the old
  // client-side merge order.
  let semanticIds = [];
  const vector = Array.isArray(body?.vector)
    ? body.vector.filter(
        (value) => typeof value === "number" && Number.isFinite(value),
      )
    : [];
  if (vector.length) {
    try {
      const vectors = await getVectors();
      semanticIds = semanticSearch(vectors, vector, {
        exclude: new Set(keywordIds),
        limit: SEMANTIC_MAX_RESULTS,
        minScore: SEMANTIC_MIN_SCORE,
      });
    } catch (error) {
      console.error("Semantic search failed:", error);
    }
  }

  const mergedIds = [...keywordIds, ...semanticIds];
  const passingSet = selectIds(db, mergedIds, clauses, params);
  // Preserve the merged (relevance) order, keeping only filter matches.
  const orderedIds = mergedIds.filter((id) => passingSet.has(id));

  const total = orderedIds.length;
  const clampedPage = Math.min(page, Math.max(1, Math.ceil(total / pageSize)));
  const pageIds = orderedIds.slice(
    (clampedPage - 1) * pageSize,
    clampedPage * pageSize,
  );

  let rows = [];
  if (pageIds.length) {
    const placeholders = pageIds.map(() => "?").join(", ");
    const result = exec(
      db,
      `SELECT ${PAGE_COLUMNS} ${DATASET_FROM}
       WHERE datasets.id IN (${placeholders})`,
      pageIds,
    );
    const byId = new Map(rowsToObjects(result).map((row) => [row.id, row]));
    rows = pageIds.map((id) => byId.get(id)).filter(Boolean);
  }

  return { rows, total, page: clampedPage };
}

// One row per option value, in the shape the old client-side option builders
// produced (title/slug/count plus emoji for countries). The client adds the
// `selected` flag and per-type sorting.
function optionRows(db, sql, params, transform) {
  const result = exec(db, sql, params);
  const values = result[0]?.values ?? [];
  return values.map(transform).filter(Boolean);
}

async function handleOptions(body) {
  const db = await getDb();
  const filters = body?.filters ?? {};

  const option = (type, build) => {
    try {
      return build();
    } catch (error) {
      console.error(`Failed to build "${type}" filter options:`, error);
      return [];
    }
  };

  const where = (excludeType) => buildFilterClauses(filters, excludeType);

  return {
    options: {
      catalog: option("catalog", () => {
        const { clauses, params } = where("catalog");
        return optionRows(
          db,
          `SELECT catalogs.title, catalogs.slug, COUNT(*) as count
           FROM datasets
           LEFT JOIN catalogs ON datasets.catalog_slug = catalogs.slug
           ${whereSql(clauses)}
           GROUP BY catalogs.slug
           ORDER BY count DESC`,
          params,
          ([title, slug, count]) => ({ title, slug, count }),
        );
      }),
      countries: option("countries", () => {
        const { clauses, params } = where("countries");
        const rows = optionRows(
          db,
          `SELECT spatial, COUNT(*) as count
           FROM datasets
           ${whereSql(clauses)}
           GROUP BY spatial
           ORDER BY count DESC`,
          params,
          ([spatial, count]) => {
            try {
              const countries =
                spatial == null ? [] : JSON.parse(spatial).countries;
              return { countries, count };
            } catch {
              return null;
            }
          },
        );
        const acc = {};
        for (const { countries, count } of rows) {
          if (!Array.isArray(countries)) continue;
          for (const country of countries) {
            const { title, emoji, slug } = country ?? {};
            if (!slug) continue;
            if (acc[slug]) acc[slug].count += count;
            else acc[slug] = { emoji, title, slug, count };
          }
        }
        return Object.values(acc);
      }),
      geo_scale: option("geo_scale", () => {
        const { clauses, params } = where("geo_scale");
        const acc = {};
        for (const [spatial, count] of
          exec(
            db,
            `SELECT spatial, COUNT(*) as count
             FROM datasets
             ${whereSql(clauses)}
             GROUP BY spatial
             ORDER BY count DESC`,
            params,
          )[0]?.values ?? []) {
          let slug;
          try {
            slug = spatial == null ? null : JSON.parse(spatial).scale;
          } catch {
            continue;
          }
          if (slug == null) continue;
          if (acc[slug]) acc[slug].count += count;
          else {
            acc[slug] = {
              title:
                String(slug).charAt(0).toUpperCase() + String(slug).slice(1),
              slug,
              count,
            };
          }
        }
        return Object.values(acc);
      }),
      hazard_type: option("hazard_type", () => {
        const { clauses, params } = where("hazard_type");
        const acc = {};
        for (const [hazardType, count] of
          exec(
            db,
            `SELECT hazard_type, COUNT(*) as count
             FROM datasets
             ${whereSql(clauses)}
             GROUP BY hazard_type
             ORDER BY count DESC`,
            params,
          )[0]?.values ?? []) {
          let slugs;
          try {
            slugs = hazardType ? JSON.parse(hazardType) : [];
          } catch {
            continue;
          }
          if (!Array.isArray(slugs)) continue;
          for (const slug of slugs) {
            if (acc[slug]) acc[slug].count += count;
            else {
              acc[slug] = {
                title:
                  String(slug).charAt(0).toUpperCase() +
                  String(slug).slice(1).replace("_", " "),
                slug,
                count,
              };
            }
          }
        }
        return Object.values(acc);
      }),
      license: option("license", () => {
        const { clauses, params } = where("license");
        return optionRows(
          db,
          `SELECT licenses.title, licenses.slug, COUNT(*) as count
           FROM datasets
           LEFT JOIN licenses ON datasets.license_slug = licenses.slug
           ${whereSql(clauses)}
           GROUP BY licenses.slug
           ORDER BY count DESC`,
          params,
          ([title, slug, count]) => ({ title, slug, count }),
        );
      }),
      project: option("project", () => {
        const { clauses, params } = where("project");
        return optionRows(
          db,
          `SELECT project, COUNT(*) as count
           FROM datasets
           ${whereSql(clauses)}
           GROUP BY project
           ORDER BY count DESC`,
          params,
          ([value, count]) => {
            try {
              const { title, slug } = JSON.parse(value);
              return { title, slug, count };
            } catch {
              return null;
            }
          },
        );
      }),
      risk_data_type: option("risk_data_type", () => {
        const { clauses, params } = where("risk_data_type");
        const acc = {};
        for (const [riskDataType, count] of
          exec(
            db,
            `SELECT risk_data_type, COUNT(*) as count
             FROM datasets
             ${whereSql(clauses)}
             GROUP BY risk_data_type
             ORDER BY count DESC`,
            params,
          )[0]?.values ?? []) {
          let slugs;
          try {
            slugs = JSON.parse(riskDataType);
          } catch {
            continue;
          }
          if (!Array.isArray(slugs)) continue;
          for (const slug of slugs) {
            if (acc[slug]) acc[slug].count += count;
            else {
              acc[slug] = {
                title:
                  String(slug).charAt(0).toUpperCase() + String(slug).slice(1),
                slug,
                count,
              };
            }
          }
        }
        return Object.values(acc);
      }),
    },
  };
}

function jsonResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { "Content-Type": "application/json", ...CORS_HEADERS },
  });
}

export default async (req) => {
  if (req.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: CORS_HEADERS });
  }
  if (req.method !== "POST") {
    return jsonResponse({ error: "Method not allowed" }, 405);
  }

  let body;
  try {
    body = await req.json();
  } catch {
    return jsonResponse({ error: "Invalid JSON body" }, 400);
  }

  try {
    switch (body?.action) {
      case "datasets":
        return jsonResponse(await handleDatasets(body));
      case "dataset":
        return jsonResponse(await handleDataset(body));
      case "options":
        return jsonResponse(await handleOptions(body));
      case "search":
        return jsonResponse(await handleSearch(body));
      default:
        return jsonResponse({ error: `Unknown action "${body?.action}"` }, 400);
    }
  } catch (error) {
    console.error("Query function failed:", error);
    return jsonResponse(
      { error: "Query failed", detail: String(error?.message ?? error) },
      500,
    );
  }
};