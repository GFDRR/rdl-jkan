#!/usr/bin/env node
// Upload/download the search data files to/from the site's "rdl-data"
// Netlify Blobs store, which the query function (netlify/functions/query)
// reads at runtime.
//
// Requires NETLIFY_SITE_ID and NETLIFY_AUTH_TOKEN (a Netlify personal access
// token) in the environment.
//
// Usage:
//   node scripts/netlify-data.mjs upload
//   node scripts/netlify-data.mjs download [file ...]

import { getStore } from "@netlify/blobs";
import { readFile, writeFile } from "node:fs/promises";

const STORE_NAME = "rdl-data";

// Blob key -> path in the repository.
const FILE_PATHS = {
  "sqlite.db": "sqlite.db",
  "vectors.bin": "python/vectors.bin",
  "vectors.ids.json": "python/vectors.ids.json",
  "sql-wasm.wasm": "sql-wasm.wasm",
};

const [command, ...requested] = process.argv.slice(2);
const files = requested.length ? requested : Object.keys(FILE_PATHS);

for (const name of files) {
  if (!FILE_PATHS[name]) {
    console.error(`Unknown file "${name}". Valid files: ${Object.keys(FILE_PATHS).join(", ")}`);
    process.exit(1);
  }
}

const siteID = process.env.NETLIFY_SITE_ID;
const token = process.env.NETLIFY_AUTH_TOKEN;
if (!siteID || !token) {
  console.error("NETLIFY_SITE_ID and NETLIFY_AUTH_TOKEN must be set.");
  process.exit(1);
}

function toArrayBuffer(bytes) {
  if (bytes instanceof ArrayBuffer) return bytes;
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
}

const store = getStore({ name: STORE_NAME, siteID, token });

if (command === "upload") {
  for (const name of files) {
    const bytes = await readFile(FILE_PATHS[name]);
    await store.set(name, toArrayBuffer(bytes));
    console.log(`Uploaded ${name} (${bytes.length} bytes) to store "${STORE_NAME}".`);
  }
} else if (command === "download") {
  for (const name of files) {
    const bytes = await store.get(name, { type: "arrayBuffer" });
    if (!bytes) {
      console.error(`"${name}" not found in store "${STORE_NAME}".`);
      process.exitCode = 1;
      continue;
    }
    await writeFile(FILE_PATHS[name], Buffer.from(bytes));
    console.log(`Downloaded ${name} (${bytes.byteLength} bytes) from store "${STORE_NAME}".`);
  }
} else {
  console.error("Usage: node scripts/netlify-data.mjs upload|download [file ...]");
  process.exit(1);
}