#!/usr/bin/env node
// Check that the deployed query function (netlify/functions/query) answers the
// requests the site makes.
//
// Usage:
//   node scripts/check-query-function.mjs [base URL]

const base = (process.argv[2] ?? "https://rdl-jkan.netlify.app").replace(/\/+$/, "");
const ATTEMPTS = 5;
const DELAY_MS = 10_000;

async function query(payload) {
  const params = encodeURIComponent(JSON.stringify(payload));
  const response = await fetch(`${base}/.netlify/functions/query?payload=${params}`, {
    signal: AbortSignal.timeout(60_000),
  });
  const text = await response.text();
  if (!response.ok) {
    throw new Error(`${payload.action}: ${response.status} ${text.slice(0, 200)}`);
  }
  return JSON.parse(text);
}

async function check() {
  const { total, rows } = await query({ action: "datasets", filters: {} });
  if (!(total > 0 && rows?.length)) throw new Error("datasets: no datasets");

  const id = rows[0].slug;
  const { dataset } = await query({ action: "dataset", id });
  if (!dataset) throw new Error(`dataset: ${id} not found`);

  const { related } = await query({ action: "related", id });
  if (!Array.isArray(related)) throw new Error("related: no list");

  const { options } = await query({ action: "options", filters: {} });
  if (!options) throw new Error("options: no options");

  const search = await query({ action: "search", q: "flood", filters: {} });
  if (!(search.total > 0)) throw new Error("search: nothing found for flood");

  console.log(`The query function at ${base} works (${total} datasets).`);
}

for (let attempt = 1; ; attempt++) {
  try {
    await check();
    break;
  } catch (error) {
    console.error(`Attempt ${attempt} of ${ATTEMPTS}: ${error.message}`);
    if (attempt === ATTEMPTS) process.exit(1);
    await new Promise((resolve) => setTimeout(resolve, DELAY_MS));
  }
}
