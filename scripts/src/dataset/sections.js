// The sections of the dataset page, as the page shows them.
import {
  eventFrequency,
  hazardLabel,
  hazardWithType,
  intensityLabel,
  label,
  measurementLabel,
  nameFromId,
  period,
  plural,
  returnPeriod,
  unitLabel,
  webUrl,
} from "./labels.js";
import { buildTable, FILTER_FROM } from "./table.js";

const COMPONENTS = ["hazard", "exposure", "vulnerability", "loss"];

const FUNCTION_TYPES = {
  vulnerability: "Vulnerability function",
  fragility: "Fragility function",
  damage_to_loss: "Damage to loss function",
  engineering_demand: "Engineering demand function",
};

// From this many, the metrics of an asset are grouped by dimension.
const GROUP_METRICS_FROM = 7;

const params = (pairs) =>
  pairs
    .filter(([, value]) => value != null && value !== "")
    .map(([name, value]) => ({ name, value: String(value) }));

// --- Hazard

function hazardSetTitles(sets) {
  const titles = sets.map(
    ({ hazards }) =>
      [...new Set((hazards ?? []).map(hazardLabel))].join(" and ") ||
      "Event set",
  );
  // Event sets on the same hazard are told apart by their ids.
  return titles.map((title, i) => {
    if (titles.filter((other) => other === title).length === 1) return title;
    return `${title}: ${nameFromId(sets[i].id) || sets[i].id || i + 1}`;
  });
}

function eventTable(events, known) {
  const dates = (event) => event.occurrence?.empirical?.temporal;
  return buildTable(
    events,
    [
      {
        id: "event",
        label: "Event",
        main: true,
        value: (event) => event.description || event.id,
        note: (event) => (event.description ? event.id : ""),
      },
      {
        id: "return_period",
        label: "Return period",
        num: true,
        facet: "chips",
        value: (event) => {
          const years = returnPeriod(event);
          return years == null ? "" : plural(years, "year");
        },
        order: (event) => returnPeriod(event) ?? 0,
      },
      { id: "frequency", label: "Frequency", value: eventFrequency },
      {
        id: "start",
        label: "Start",
        num: true,
        value: (event) => dates(event)?.start,
      },
      {
        id: "end",
        label: "End",
        num: true,
        value: (event) => dates(event)?.end,
      },
      {
        id: "process",
        label: "Process",
        facet: "select",
        value: (event) => hazardLabel(event.hazard),
      },
      {
        id: "intensity",
        label: "Intensity measure",
        facet: "select",
        value: (event) => intensityLabel(event.hazard?.intensity_measure),
      },
      {
        id: "calculation",
        label: "Calculation",
        facet: "select",
        value: (event) => label(event.calculation_method),
      },
    ],
    { noun: ["event", "events"], known },
  );
}

function hazardTable(hazards) {
  return buildTable(
    hazards,
    [
      { id: "process", label: "Process", main: true, value: hazardLabel },
      { id: "type", label: "Hazard", value: (hazard) => label(hazard.type) },
      {
        id: "intensity",
        label: "Intensity measure",
        value: (hazard) => intensityLabel(hazard.intensity_measure),
      },
      {
        id: "trigger",
        label: "Trigger",
        value: (hazard) => hazardLabel(hazard.trigger),
      },
    ],
    { noun: ["hazard", "hazards"] },
  );
}

export function hazardSection(dataset) {
  const sets = dataset.hazard?.event_sets ?? [];
  const titles = hazardSetTitles(sets);
  return sets.map((set, key) => {
    const hazards = set.hazards ?? [];
    const events = set.events ?? [];
    const only = hazards.length === 1 ? hazards[0] : null;
    const hazardParams = only
      ? [
          ["Hazard", label(only.type)],
          ["Process", hazardLabel(only)],
          ["Intensity measure", intensityLabel(only.intensity_measure)],
          ["Trigger", hazardLabel(only.trigger)],
        ]
      : [];
    const setParams = [
      ["Analysis", label(set.analysis_type)],
      ["Calculation", label(set.calculation_method)],
      ["Occurrence", set.occurrence_range],
      ["Distribution", label(set.frequency_distribution)],
      ["Seasonality", label(set.seasonality)],
      [
        "Events in the set",
        set.event_count === events.length ? null : set.event_count,
      ],
    ];
    const shown = params([...hazardParams, ...setParams]);
    return {
      key,
      title: titles[key],
      count: events.length,
      params: shown,
      hazards: hazards.length > 1 ? hazardTable(hazards) : null,
      events: events.length
        ? eventTable(
            events,
            shown.map(({ value }) => value),
          )
        : null,
    };
  });
}

// --- Exposure

function metricView(metric, grouped) {
  const dimension = label(metric.dimension);
  const name = nameFromId(metric.id);
  return {
    quantity: metric.measurement?.quantity_kind ?? "",
    quantityLabel: label(metric.measurement?.quantity_kind),
    name: name || dimension,
    details: [
      name && !grouped ? dimension.toLowerCase() : "",
      unitLabel(metric.measurement),
    ]
      .filter(Boolean)
      .join(", "),
  };
}

function metricGroups(metrics) {
  if (metrics.length < GROUP_METRICS_FROM) {
    return [
      { name: "", metrics: metrics.map((metric) => metricView(metric, false)) },
    ];
  }
  const groups = new Map();
  for (const metric of metrics) {
    const name = label(metric.dimension);
    if (!groups.has(name)) groups.set(name, []);
    groups.get(name).push(metricView(metric, true));
  }
  return [...groups]
    .map(([name, views]) => ({
      name,
      metrics: views.sort((a, b) => a.name.localeCompare(b.name)),
    }))
    .sort((a, b) => a.name.localeCompare(b.name));
}

export function exposureSection(dataset) {
  return (dataset.exposure ?? []).map((exposure, key) => {
    const metrics = exposure.metrics ?? [];
    const category = label(exposure.category);
    const title = nameFromId(exposure.id) || category;
    const asset = exposure.asset_type;
    return {
      key,
      title,
      category: title === category ? "" : category,
      description: asset?.description ?? "",
      assetType:
        asset?.id && asset.scheme ? `${asset.id} in ${asset.scheme}` : "",
      count: metrics.length,
      grouped: metrics.length >= GROUP_METRICS_FROM,
      groups: metricGroups(metrics),
    };
  });
}

// --- Vulnerability

function functionView(fn, key, total) {
  const { impact } = fn;
  return {
    key,
    id: fn.id,
    title: label(impact?.metric) || fn.type,
    type: impact?.metric ? fn.type.toLowerCase() : "",
    category: label(fn.category),
    hazard: hazardLabel(fn.hazard_primary),
    details: fn.analysis_details ?? "",
    open: total < 3 || key === 0,
    params: params([
      [
        "Intensity measure",
        intensityLabel(fn.hazard_primary?.intensity_measure),
      ],
      ["Secondary hazard", hazardLabel(fn.hazard_secondary)],
      ["Approach", label(fn.approach)],
      ["Relationship", label(fn.relationship)],
      ["Analysis", label(fn.hazard_analysis_type)],
      [
        "Impact",
        [label(impact?.type), label(impact?.modelling)]
          .filter(Boolean)
          .join(", "),
      ],
      ["Measured as", label(measurementLabel(impact?.measurement))],
      ["Taxonomy", fn.taxonomy],
      ["Damage scale", fn.damage_scale_name],
      ["Damage states", (fn.damage_states_names ?? []).join(", ")],
    ]),
  };
}

function indexTable(indices) {
  return buildTable(
    indices,
    [
      {
        id: "name",
        label: "Index",
        main: true,
        value: (index) => index.indicator_name,
      },
      {
        id: "description",
        label: "Description",
        value: (index) => index.description,
      },
      { id: "scheme", label: "Scheme", value: (index) => index.scheme },
      {
        id: "year",
        label: "Reference year",
        num: true,
        value: (index) => index.reference_year,
      },
    ],
    { noun: ["index", "indices"] },
  );
}

export function vulnerabilitySection(dataset) {
  const functions = dataset.vulnerability?.functions ?? {};
  const indices = dataset.vulnerability?.socio_economic ?? [];
  const all = Object.entries(FUNCTION_TYPES).flatMap(([name, type]) =>
    (functions[name] ?? []).map((fn) => ({ ...fn, type })),
  );
  return {
    functions: all.map((fn, key) => functionView(fn, key, all.length)),
    indices: indices.length ? indexTable(indices) : null,
  };
}

// --- Loss

const impactOf = (loss) => loss.impact_and_losses?.impact ?? {};
const assetOf = (loss) => label(loss.asset_category);
const hazardOf = (loss) => hazardWithType(loss.hazard);

// What a loss measures and its unit, e.g. "Loss (ha)", "Casualty count".
function measureOf(loss) {
  const { metric, measurement } = impactOf(loss);
  const name = label(metric);
  const unit = measurementLabel(measurement);
  return !unit || name.toLowerCase().includes(unit.toLowerCase())
    ? name
    : `${name} (${unit})`;
}

function measuredAs(loss) {
  const { measurement } = impactOf(loss);
  return [label(measurement?.quantity_kind), unitLabel(measurement)]
    .filter(Boolean)
    .join(", ");
}

// What is measured for each hazard and asset, for the datasets with many
// losses on several hazards and assets.
function lossMatrix(losses) {
  const assets = [...new Set(losses.map(assetOf))].sort();
  const hazards = [...new Set(losses.map(hazardOf))].sort();
  if (losses.length < FILTER_FROM || assets.length < 2 || hazards.length < 2) {
    return null;
  }
  const cell = (hazard, asset) => {
    const measures = new Map();
    for (const loss of losses) {
      if (hazardOf(loss) !== hazard || assetOf(loss) !== asset) continue;
      measures.set(
        measureOf(loss),
        impactOf(loss).measurement?.quantity_kind ?? "",
      );
    }
    return {
      asset,
      measures: [...measures]
        .map(([measure, quantity]) => ({ measure, quantity }))
        .sort((a, b) => a.measure.localeCompare(b.measure)),
    };
  };
  return {
    assets,
    rows: hazards.map((hazard) => ({
      hazard,
      cells: assets.map((asset) => cell(hazard, asset)),
    })),
  };
}

function lossTable(losses, hasMatrix) {
  // The matrix already filters by hazard and asset.
  const facet = hasMatrix ? null : "select";
  return buildTable(
    losses,
    [
      {
        id: "loss",
        label: "Loss",
        main: true,
        value: (loss) => loss.description || loss.id,
      },
      { id: "hazard", label: "Hazard", facet, value: hazardOf },
      { id: "asset", label: "Asset", facet, value: assetOf },
      {
        id: "dimension",
        label: "Dimension",
        facet: "select",
        value: (loss) => label(loss.asset_dimension),
      },
      {
        id: "impact",
        label: "Impact",
        facet: "select",
        value: (loss) => label(impactOf(loss).metric),
      },
      { id: "unit", label: "Measured as", value: measuredAs },
      { id: "type", label: "Type", value: (loss) => label(impactOf(loss).type) },
      {
        id: "modelling",
        label: "Modelling",
        value: (loss) => label(impactOf(loss).modelling),
      },
      {
        id: "loss_type",
        label: "Loss type",
        value: (loss) => label(loss.impact_and_losses?.loss_type),
      },
      {
        id: "approach",
        label: "Approach",
        value: (loss) => label(loss.impact_and_losses?.loss_approach),
      },
      {
        id: "frequency",
        label: "Frequency",
        value: (loss) => label(loss.impact_and_losses?.loss_frequency_type),
      },
      { id: "measure", label: "Measure", hidden: true, value: measureOf },
    ],
    { noun: ["loss entry", "loss entries"] },
  );
}

export function lossSection(dataset) {
  const losses = dataset.loss?.losses ?? [];
  if (!losses.length) return null;
  const matrix = lossMatrix(losses);
  return { matrix, table: lossTable(losses, Boolean(matrix)) };
}

// --- Files

export function fileTable(dataset) {
  const resources = dataset.resources ?? [];
  // Many files can share a few descriptions, which then tell groups of files.
  const descriptions = new Set(resources.map((file) => file.description));
  const grouped =
    resources.length > 2 && descriptions.size <= resources.length / 2;
  const repeated = ({ title, description }) =>
    !description || description.trim() === (title ?? "").trim();
  const link = (file) => webUrl(file.download_url) ?? webUrl(file.access_url);
  return buildTable(
    resources,
    [
      {
        id: "file",
        label: "File",
        main: true,
        value: (file) => file.title || file.id,
        href: link,
        detail: (file) => (grouped || repeated(file) ? "" : file.description),
        // Addresses browsers do not open, e.g. "gs://...".
        note: (file) =>
          link(file) ? "" : file.download_url || file.access_url || "",
      },
      {
        id: "description",
        label: "Description",
        facet: "select",
        value: (file) => (grouped ? file.description : ""),
      },
      {
        id: "format",
        label: "Format",
        tag: true,
        facet: "chips",
        value: (file) => file.format_label,
      },
      {
        id: "resolution",
        label: "Resolution",
        num: true,
        value: ({ spatial_resolution: metres }) =>
          metres ? `${metres.toLocaleString("en")} m` : "",
        order: (file) => file.spatial_resolution ?? 0,
      },
      {
        id: "aggregation",
        label: "Spatial detail",
        value: (file) => file.spatial_aggregation,
      },
      {
        id: "crs",
        label: "Coordinates",
        value: (file) => file.coordinate_system,
      },
      {
        id: "period",
        label: "Period",
        num: true,
        value: (file) => period(file.temporal),
      },
    ],
    { noun: ["file", "files"] },
  );
}

// --- Sources and references

function sourceTable(sources) {
  return buildTable(
    sources,
    [
      {
        id: "name",
        label: "Source",
        main: true,
        value: (source) => source.name || source.id,
        href: (source) => webUrl(source.url),
        detail: (source) => source.description,
      },
      { id: "type", label: "Type", value: (source) => label(source.type) },
      {
        id: "used_in",
        label: "Used in",
        facet: "select",
        value: (source) => label(source.used_in),
      },
      { id: "license", label: "License", value: (source) => source.license },
    ],
    { noun: ["source", "sources"] },
  );
}

function referenceView(reference, key) {
  const authors = (reference.author_names ?? []).join(", ");
  const year = String(reference.date_published ?? "").slice(0, 4);
  const lead = [authors.replace(/\.$/, ""), year && `(${year})`]
    .filter(Boolean)
    .join(" ");
  return {
    key,
    lead: lead && `${lead}. `,
    name: String(
      reference.name || reference.url || reference.doi || reference.id || "",
    ).trim(),
    url: webUrl(reference.url) ?? webUrl(reference.doi),
  };
}

export function sourceSection(dataset) {
  const { lineage, referenced_by: references } = dataset.frontmatter ?? {};
  const sources = lineage?.sources ?? [];
  return {
    description: lineage?.description ?? "",
    sources: sources.length ? sourceTable(sources) : null,
    references: (references ?? []).map(referenceView),
  };
}

// --- About

export function aboutRows(dataset) {
  const { attributions, catalog } = dataset.frontmatter ?? {};
  const { project } = dataset;
  const value = (text, url = null, note = "") =>
    text ? [{ text: String(text), url: webUrl(url), note }] : [];
  const entity = (item, note) => value(item?.name, item?.url, note);
  return [
    { label: "Dataset ID", code: true, values: value(dataset.id) },
    { label: "Purpose", values: value(dataset.purpose) },
    { label: "Details", values: value(dataset.details) },
    {
      label: "Project",
      values:
        project?.slug === "unknown" ? [] : value(project?.title, project?.url),
    },
    {
      label: "Catalog",
      values: catalog?.slug === "unknown" ? [] : value(dataset.catalog_title),
    },
    { label: "Publisher", values: entity(dataset.publisher) },
    { label: "Creator", values: entity(dataset.creator) },
    { label: "Contact", values: entity(dataset.contact_point) },
    {
      label: "Attributions",
      values: (attributions ?? []).flatMap((item) =>
        entity(item.entity, label(item.role).toLowerCase()),
      ),
    },
    {
      label: "License",
      values: value(dataset.license_title, dataset.license_url),
    },
  ].filter(({ values }) => values.length);
}

// --- The whole page

export function keyFacts(dataset) {
  const { creator, publisher, spatial } = dataset;
  const countries = spatial?.countries ?? [];
  return params([
    ["Creator", creator?.name],
    [
      "Coverage",
      countries.length > 1
        ? plural(countries.length, "country", "countries")
        : (countries[0]?.title ?? label(spatial?.scale)),
    ],
    ["Period", period(dataset.temporal)],
    ["License", dataset.license_title],
    // Versions such as "1.0" are numbers outside of the frontmatter.
    ["Version", dataset.frontmatter?.version ?? dataset.version],
    ["Publisher", publisher?.name === creator?.name ? "" : publisher?.name],
  ]);
}

export function buildPage(dataset) {
  const hazard = hazardSection(dataset);
  const exposure = exposureSection(dataset);
  const vulnerability = vulnerabilitySection(dataset);
  const loss = lossSection(dataset);
  const files = fileTable(dataset);
  const sources = sourceSection(dataset);

  const sum = (items) => items.reduce((total, { count }) => total + count, 0);
  // [number, singular, plural], for what each section holds.
  const contents = {
    hazard: [
      [hazard.length, "event set"],
      [sum(hazard), "event"],
    ],
    exposure: [
      [exposure.length, "asset type"],
      [sum(exposure), "metric"],
    ],
    vulnerability: [
      [vulnerability.functions.length, "function"],
      [vulnerability.indices?.total ?? 0, "index", "indices"],
    ],
    loss: [[loss?.table.total ?? 0, "loss entry", "loss entries"]],
    files: [[files.total, "file"]],
    sources: [
      [sources.sources?.total ?? 0, "source"],
      [sources.references.length, "reference"],
    ],
    about: [],
  };
  const counts = {
    hazard: hazard.length,
    exposure: exposure.length,
    vulnerability:
      vulnerability.functions.length + (vulnerability.indices?.total ?? 0),
    loss: loss?.table.total ?? 0,
    files: files.total,
    sources: (sources.sources?.total ?? 0) + sources.references.length,
    about: 0,
  };
  const section = (id, title = label(id)) => ({
    id,
    title,
    kind: COMPONENTS.includes(id) ? id : "neutral",
    count: counts[id],
    summary: contents[id]
      .filter(([number]) => number)
      .map((content) => plural(...content))
      .join(", "),
  });

  return {
    facts: keyFacts(dataset),
    countries: (dataset.spatial?.countries ?? []).map(({ title }) => title),
    hazard,
    exposure,
    vulnerability,
    loss,
    files,
    sources,
    about: aboutRows(dataset),
    sections: [
      ...COMPONENTS.filter((id) => dataset.risk_data_type?.includes(id)).map(
        (id) => section(id),
      ),
      section("files"),
      ...(counts.sources || sources.description
        ? [section("sources", "Sources and references")]
        : []),
      section("about"),
    ],
  };
}
