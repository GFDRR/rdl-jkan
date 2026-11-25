#!/usr/bin/env node
// Answer the requests the home page makes when it opens, so that the page comes
// with its first datasets and filters instead of waiting for the query function.
//
// Reads search.db, written by python/import.py, and writes _data/initial.json,
// which index.html includes. Without that file the page makes the requests.
//
// Usage:
//   node scripts/initial-data.mjs

import { writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

import pagination from "./src/datasets/pagination.js";
import { datasetsPayload, optionsPayload } from "./src/shared/api.js";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
process.env.RDL_DATA_DIR ??= root;
const { default: handler } = await import("../netlify/functions/query/index.mjs");

async function answer(payload) {
  const response = await handler(
    new Request("http://localhost/", {
      method: "POST",
      body: JSON.stringify(payload),
    }),
  );
  if (!response.ok) throw new Error(`${payload.action}: ${await response.text()}`);
  return { payload, answer: await response.json() };
}

const initialData = [
  await answer(datasetsPayload({}, 1, pagination.itemsPerPage)),
  await answer(optionsPayload({})),
];
if (!initialData[0].answer.total) throw new Error("No datasets");

const path = join(root, "_data", "initial.json");
const json = JSON.stringify(initialData);
await writeFile(path, `${json}\n`);
console.log(`Wrote ${path} (${json.length} characters)`);
