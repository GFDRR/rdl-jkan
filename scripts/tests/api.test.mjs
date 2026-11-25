import assert from "node:assert/strict";
import { test } from "node:test";

import {
  datasetsPayload,
  isAnswered,
  optionsPayload,
  queryApi,
  rememberInitialData,
  searchPayload,
} from "../src/shared/api.js";

function mockFetch(t, requests) {
  t.mock.method(globalThis, "fetch", async (url, init) => {
    requests.push({ url, method: init?.method ?? "GET", headers: init?.headers });
    return Response.json({ total: requests.length });
  });
}

test("the same list always has the same payload", () => {
  const filters = { catalog: [], countries: ["phl", "ken"] };
  const same = { countries: ["ken", "phl"], license: [] };
  assert.deepEqual(datasetsPayload(filters, 1, 10), datasetsPayload(same, 1, 10));
  assert.deepEqual(optionsPayload({ catalog: [] }), optionsPayload({}));
});

test("the first page of the site needs no request", async (t) => {
  const requests = [];
  mockFetch(t, requests);
  const payload = datasetsPayload({}, 1, 10);
  // As in _data/initial.json.
  rememberInitialData(JSON.parse(JSON.stringify([{ payload, answer: { total: 9 } }])));
  assert.ok(isAnswered(datasetsPayload({ catalog: [] }, 1, 10)));
  assert.deepEqual(await queryApi(datasetsPayload({}, 1, 10)), { total: 9 });
  assert.equal(requests.length, 0);
});

test("a list is requested once, and a vector is sent without preflight", async (t) => {
  const requests = [];
  mockFetch(t, requests);
  const payload = datasetsPayload({ hazard_type: ["flood"] }, 2, 10);
  await queryApi(payload);
  await queryApi(payload);
  assert.equal(requests.length, 1);
  assert.equal(requests[0].method, "GET");
  const { searchParams } = new URL(requests[0].url, "http://localhost");
  assert.deepEqual(JSON.parse(searchParams.get("payload")), payload);

  const vector = Array.from({ length: 384 }, () => 0.123456789);
  await queryApi(searchPayload("flood", vector, {}, 1, 10));
  assert.equal(requests[1].method, "POST");
  assert.equal(requests[1].headers["Content-Type"], "text/plain");
});

test("a failed request is made again", async (t) => {
  const payload = datasetsPayload({ hazard_type: ["drought"] }, 1, 10);
  t.mock.method(globalThis, "fetch", async () => new Response("no", { status: 500 }));
  await assert.rejects(queryApi(payload), /500/);
  assert.equal(isAnswered(payload), false);
});
