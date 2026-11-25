// Runs the query function on the database built by python/import.py. Skipped
// when there is none.
import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..", "..");
process.env.RDL_DATA_DIR ??= root;
const skip = !existsSync(join(process.env.RDL_DATA_DIR, "search.db"));

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

async function get(body, method = "GET") {
  const { default: handler } = await import("../functions/query/index.mjs");
  const payload = encodeURIComponent(JSON.stringify(body));
  return handler(new Request(`http://localhost/?payload=${payload}`, { method }));
}

test("GET answers like POST, and only good answers are cached", { skip }, async () => {
  const body = { action: "datasets", filters: { hazard_type: ["flood"] }, page: 2 };
  const response = await get(body);
  assert.equal(response.status, 200);
  assert.match(response.headers.get("cache-control"), /public/);
  assert.deepEqual(await response.json(), await query(body));

  const unknown = await get({ action: "nope" });
  assert.equal(unknown.status, 400);
  assert.equal(unknown.headers.get("cache-control"), "no-store");
  assert.equal(unknown.headers.get("netlify-cdn-cache-control"), null);

  const { default: handler } = await import("../functions/query/index.mjs");
  assert.equal((await handler(new Request("http://localhost/"))).status, 400);
});

test("the list only has what the cards show", { skip }, async () => {
  const { rows } = await query({ action: "datasets", filters: {} });
  for (const row of rows) {
    assert.ok(row.title && row.slug && row.risk_data_type.length, row.id);
    assert.equal(row.frontmatter, undefined);
    assert.equal(row.resources, undefined);
  }
});

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

test("licenses only given as a URL are grouped under Custom", { skip }, async () => {
  const { options } = await query({ action: "options", filters: {} });
  const titles = options.license.map((item) => item.title);
  assert.deepEqual(titles.filter((title) => /^https?:/.test(title)), []);
  assert.equal(titles.filter((title) => title === "Custom").length, 1);

  const custom = options.license.find((item) => item.slug === "custom");
  const { rows, total } = await query({
    action: "datasets",
    filters: { license: ["custom"] },
    pageSize: 50,
  });
  assert.equal(total, custom.count);
  for (const row of rows) {
    assert.match(row.license_title, /^(Custom$|https?:)/, row.id);
  }

  const counts = options.license.filter((item) =>
    ["custom", "cc0-10"].includes(item.slug),
  );
  assert.equal(counts.length, 2);
  const both = await query({
    action: "datasets",
    filters: { license: counts.map((item) => item.slug) },
  });
  assert.equal(both.total, counts.reduce((sum, item) => sum + item.count, 0));
});
