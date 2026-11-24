// Runs the query function on the database built by python/import.py. Skipped
// when there is none.
import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..", "..");
process.env.RDL_DATA_DIR ??= root;
const skip = !existsSync(join(process.env.RDL_DATA_DIR, "sqlite.db"));

async function query(body) {
  const { default: handler } = await import("../functions/query/index.mjs");
  const response = await handler(
    new Request("http://localhost/", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  );
  assert.equal(response.status, 200);
  return response.json();
}

const ids = async (q) =>
  (await query({ action: "search", q, pageSize: 50 })).rows.map((row) => row.id);

test("the order of the words does not change the results", { skip }, async () => {
  const results = await ids("flood kenya");
  assert.ok(results.length > 0);
  assert.deepEqual(await ids("kenya flood"), results);
});

test("datasets about the country come first", { skip }, async () => {
  const { rows } = await query({ action: "search", q: "flood kenya" });
  for (const row of rows) {
    assert.ok(row.countries.some((c) => c.slug === "ken"), row.id);
  }
});

test("datasets are found by author", { skip }, async () => {
  assert.ok((await ids("Nirandjan")).includes("rdls_exp-ivm_spatiallyexplicitharmoniz"));
});

test("socio-economic indices are part of the dataset", { skip }, async () => {
  const { dataset } = await query({
    action: "dataset",
    id: "rdls_ev-climate_conflic_climateconflictvulnerabil_2015",
  });
  assert.equal(dataset.vulnerability.socio_economic.length, 1);
});

test("related datasets: lineage comes first", { skip }, async () => {
  const { related } = await query({
    action: "related",
    id: "rdls_he-fra_nismod_sdkicra__corsica",
  });
  assert.equal(related[0].id, "rdls_exp-nismod_powerplantdb");
  assert.equal(related[0].relation, "source");
  assert.ok(related.length <= 6);
});

test("related datasets: an unknown id has none", { skip }, async () => {
  assert.deepEqual(await query({ action: "related", id: "nope" }), { related: [] });
});
