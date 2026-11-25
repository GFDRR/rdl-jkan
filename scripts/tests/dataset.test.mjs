import assert from "node:assert/strict";
import { test } from "node:test";

import {
  eventFrequency,
  hazardWithType,
  intensityLabel,
  label,
  nameFromId,
  period,
  unitLabel,
  webUrl,
} from "../src/dataset/labels.js";
import { buildPage } from "../src/dataset/sections.js";
import { buildTable, filterEntries } from "../src/dataset/table.js";

const BARE = {
  id: "bare",
  title: "Bare",
  risk_data_type: ["hazard", "loss"],
  resources: [],
};

test("codes read as words", () => {
  assert.equal(label("ground_up"), "Ground up");
  assert.equal(label(null), "");
  assert.equal(intensityLabel("wd:m"), "Flow depth above ground (m)");
  assert.equal(intensityLabel("XYZ:kPa"), "XYZ (kPa)");
  assert.equal(unitLabel({ quantity_kind: "area", unit: "square_metre" }), "m²");
  assert.equal(unitLabel({ quantity_kind: "count", unit: "count" }), "");
  assert.equal(
    hazardWithType({ type: "earthquake", process: "ground_motion" }),
    "Ground motion (earthquake)",
  );
  assert.equal(
    hazardWithType({ type: "flood", process: "coastal_flood" }),
    "Coastal flood",
  );
});

test("ids are only names when they say something", () => {
  assert.equal(nameFromId("metric_road_length"), "Road length");
  assert.equal(nameFromId("event_set_flood_100rp"), "Flood 100rp");
  for (const id of ["metric_1", "metric_VsifqcGY", "FFL_U", "rdls_exp-x_m1", null]) {
    assert.equal(nameFromId(id), "", id);
  }
});

test("only web addresses are links", () => {
  assert.equal(webUrl("https://example.org"), "https://example.org");
  assert.equal(webUrl("javascript:alert(1)"), null);
  assert.equal(webUrl("example.org"), null);
  assert.equal(webUrl(null), null);
});

test("periods and frequencies", () => {
  assert.equal(
    period({ start: "2000-01-01", end: "2020-12-31" }),
    "2000 to 2020",
  );
  assert.equal(period({ start: "2020-01-01", end: "2020-12-31" }), "2020");
  assert.equal(period({ central_year: 2050 }), "2050");
  assert.equal(period(null), "");
  const frequency = (probabilistic) =>
    eventFrequency({ occurrence: { probabilistic } });
  assert.equal(
    frequency({ probability: { value: 0.1, span: 50 } }),
    "10% in 50 years",
  );
  assert.equal(frequency({ return_period: 10 }), "");
  assert.equal(eventFrequency({}), "");
});

const COLUMNS = [
  { id: "name", label: "Name", main: true, value: (row) => row.name },
  { id: "kind", label: "Kind", facet: "chips", value: (row) => row.kind },
  { id: "same", label: "Same", value: () => "always" },
  { id: "none", label: "None", value: () => null },
  {
    id: "years",
    label: "Years",
    value: (row) => `${row.years} years`,
    order: (row) => row.years,
  },
  {
    id: "secret",
    label: "Secret",
    hidden: true,
    value: (row) => row.kind + row.years,
  },
];
const ROWS = Array.from({ length: 12 }, (_, i) => ({
  name: `Scenario RCP${i % 2 ? "8.5" : "4.5"} ${i}`,
  kind: i % 3 ? "a" : "b",
  years: [100, 2, 50][i % 3] + i,
}));

const columnIds = (table) => table.columns.map(({ id }) => id);

test("a table says once what all entries share and drops empty columns", () => {
  const table = buildTable(ROWS, COLUMNS);
  assert.deepEqual(columnIds(table), ["name", "kind", "years"]);
  assert.deepEqual(table.same, [{ label: "Same", value: "always" }]);
  assert.deepEqual(buildTable(ROWS, COLUMNS, { known: ["always"] }).same, []);
  // A single entry keeps its columns.
  assert.deepEqual(columnIds(buildTable(ROWS.slice(0, 1), COLUMNS)), [
    "name",
    "kind",
    "same",
    "years",
  ]);
});

test("only long tables have filters", () => {
  const { facets, filterable } = buildTable(ROWS, COLUMNS);
  assert.ok(filterable);
  assert.equal(facets.length, 1);
  assert.equal(facets[0].id, "kind");
  assert.ok(facets[0].chips);
  assert.deepEqual(
    facets[0].options.map(({ value, count }) => [value, count]),
    [
      ["a", 8],
      ["b", 4],
    ],
  );
  const short = buildTable(ROWS.slice(0, 8), COLUMNS);
  assert.ok(!short.filterable);
  assert.deepEqual(short.facets, []);
});

test("entries are searched, filtered and sorted", () => {
  const { entries } = buildTable(ROWS, COLUMNS);
  const count = (state) => filterEntries(entries, state).length;
  assert.equal(count({ query: "rcp85" }), 6);
  assert.equal(count({ query: "RCP8.5 scenario" }), 6);
  assert.equal(count({ filters: { kind: "b" } }), 4);
  assert.equal(count({ filters: { kind: "" } }), 12);
  assert.equal(count({ filters: { secret: "b100" } }), 1);
  const years = (state) =>
    filterEntries(entries, { sort: "years", ...state }).map(
      ({ cells }) => cells.years.text,
    );
  assert.deepEqual(years({}).slice(0, 2), ["3 years", "6 years"]);
  assert.equal(years({ descending: true })[0], "109 years");
  // The entries themselves stay in the order of the metadata.
  assert.equal(entries[0].key, 0);
});

test("a dataset without details still has a page", () => {
  const { sections } = buildPage(BARE);
  assert.deepEqual(
    sections.map(({ id, count }) => [id, count]),
    [
      ["hazard", 0],
      ["loss", 0],
      ["files", 0],
      ["about", 0],
    ],
  );
});

test("the key facts keep the version as given", () => {
  const { facts } = buildPage({
    ...BARE,
    version: 1,
    frontmatter: { version: "1.0" },
  });
  assert.deepEqual(facts, [{ name: "Version", value: "1.0" }]);
});

const makeLoss = (process, asset, metric, quantity_kind, unit) => ({
  id: `${process}_${asset}_${metric}`,
  hazard: { type: "flood", process },
  asset_category: asset,
  impact_and_losses: {
    impact: { metric, measurement: { quantity_kind, unit } },
  },
});

test("the losses say what is measured for each hazard and asset", () => {
  const losses = ["coastal_flood", "fluvial_flood"].flatMap((process) => [
    makeLoss(process, "agriculture", "loss", "area", "hectare"),
    makeLoss(process, "population", "casualty_count", "count"),
    makeLoss(process, "population", "displaced", "count"),
    makeLoss(process, "buildings", "loss", "currency", "USD"),
  ]);
  losses.push(makeLoss("coastal_flood", "infrastructure", "loss", "count"));
  const { matrix, table } = buildPage({ ...BARE, loss: { losses } }).loss;
  assert.deepEqual(matrix.assets, [
    "Agriculture",
    "Buildings",
    "Infrastructure",
    "Population",
  ]);
  assert.equal(matrix.rows[1].hazard, "Fluvial flood");
  assert.deepEqual(
    matrix.rows[1].cells.map(({ measures }) =>
      measures.map(({ measure }) => measure),
    ),
    [
      ["Loss (ha)"],
      ["Loss (USD)"],
      [],
      ["Casualty count", "Displaced (count)"],
    ],
  );
  const found = filterEntries(table.entries, {
    filters: {
      hazard: "Fluvial flood",
      asset: "Population",
      measure: "Displaced (count)",
    },
  });
  assert.equal(found.length, 1);
  // Short lists only have the table.
  const few = buildPage({ ...BARE, loss: { losses: losses.slice(0, 4) } });
  assert.equal(few.loss.matrix, null);
});

test("event sets on the same hazard have different titles", () => {
  const makeSet = (id, process) => ({
    id,
    hazards: [{ type: "flood", process }],
    events: [],
  });
  const { hazard } = buildPage({
    ...BARE,
    hazard: {
      event_sets: [
        makeSet("event_set_present", "fluvial_flood"),
        makeSet("FFL_U", "fluvial_flood"),
        makeSet("3", "pluvial_flood"),
      ],
    },
  });
  assert.deepEqual(
    hazard.map(({ title }) => title),
    ["Fluvial flood: Present", "Fluvial flood: FFL_U", "Pluvial flood"],
  );
});

test("many metrics are grouped by dimension", () => {
  const groups = (length) => {
    const metrics = Array.from({ length }, (_, i) => ({
      id: `metric_${i}`,
      dimension: i % 2 ? "structure" : "content",
      measurement: { quantity_kind: "count" },
    }));
    const { exposure } = buildPage({
      ...BARE,
      exposure: [{ id: "exposure_1", category: "buildings", metrics }],
    });
    return exposure[0].groups.map((group) => [group.name, group.metrics.length]);
  };
  assert.deepEqual(groups(3), [["", 3]]);
  assert.deepEqual(groups(8), [
    ["Content", 4],
    ["Structure", 4],
  ]);
});

test("files which share their descriptions are grouped by them", () => {
  const makeFile = (i, description) => ({
    id: String(i),
    title: `file ${i}`,
    description,
    download_url: "https://example.org/file",
    format_label: "CSV",
  });
  const shared = buildPage({
    ...BARE,
    resources: [
      makeFile(1, "x"),
      makeFile(2, "x"),
      makeFile(3, "y"),
      makeFile(4, "y"),
    ],
  }).files;
  assert.deepEqual(columnIds(shared), ["file", "description"]);
  const { entries } = buildPage({
    ...BARE,
    resources: [makeFile(1, "x"), makeFile(2, "file 2")],
  }).files;
  // A description which repeats the title is left out.
  assert.deepEqual(
    entries.map(({ cells }) => cells.file.detail),
    ["x", ""],
  );
  assert.equal(entries[0].cells.file.href, "https://example.org/file");
});
