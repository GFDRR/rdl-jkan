// How the values of the metadata read on the dataset page.
import INTENSITY_MEASURES from "./intensity-measures.js";

const UNITS = {
  square_metre: "m²",
  square_kilometre: "km²",
  cubic_metre: "m³",
  metre: "m",
  kilometre: "km",
  hectare: "ha",
  kilogram: "kg",
  tonne: "t",
  megawatt: "MW",
  gigawatt_hour: "GWh",
  percent: "%",
};

// What ids start with before the part which says something.
const ID_PREFIX =
  /^(event_set|es|event|exposure|exp|metric|hazard|loss|source|function|func|resource)[ _-]+/i;

// A codelist value as a sentence, e.g. "ground_up" -> "Ground up".
export function label(value) {
  const text = String(value ?? "")
    .replace(/_/g, " ")
    .trim();
  return text.charAt(0).toUpperCase() + text.slice(1);
}

export function plural(count, one, many = `${one}s`) {
  return `${count.toLocaleString("en")} ${count === 1 ? one : many}`;
}

// The name in an id, e.g. "metric_road_length" -> "Road length". Empty when the
// id is only a number, a code or a generated string.
export function nameFromId(id) {
  const text = String(id ?? "").replace(ID_PREFIX, "");
  if (/^rdls[_-]/.test(text)) return "";
  return /^[A-Z]?[a-z]{2,}([ _-][A-Za-z0-9]+)*$/.test(text)
    ? label(text.replace(/-/g, " "))
    : "";
}

export function unitLabel(measurement) {
  const unit = measurement?.unit;
  if (!unit || unit === measurement.quantity_kind) return "";
  return UNITS[unit] ?? label(unit);
}

// The unit of a measurement or, without one, the kind of quantity.
export function measurementLabel(measurement) {
  return (
    unitLabel(measurement) || label(measurement?.quantity_kind).toLowerCase()
  );
}

export function hazardLabel(hazard) {
  return label(hazard?.process ?? hazard?.type);
}

// The process of a hazard, with the type when the process does not name it.
export function hazardWithType(hazard) {
  const process = hazardLabel(hazard);
  const type = label(hazard?.type).toLowerCase();
  return !type || process.toLowerCase().includes(type)
    ? process
    : `${process} (${type})`;
}

// "wd:m" -> "Flow depth above ground (m)".
export function intensityLabel(code) {
  if (!code) return "";
  const [measure, unit] = String(code).split(":");
  return (
    INTENSITY_MEASURES[code] ??
    (unit && unit !== "-" ? `${measure} (${unit})` : measure)
  );
}

// Only web addresses become links: many people write the metadata.
export function webUrl(url) {
  return /^https?:\/\//i.test(url ?? "") ? url : null;
}

export function period(temporal) {
  if (!temporal) return "";
  const year = (date) => String(date ?? "").slice(0, 4);
  const [start, end] = [year(temporal.start), year(temporal.end)];
  if (start && end && start !== end) return `${start} to ${end}`;
  return start || end || year(temporal.central_year);
}

export function returnPeriod(event) {
  const { probabilistic, empirical } = event.occurrence ?? {};
  return probabilistic?.return_period ?? empirical?.return_period ?? null;
}

// How often an event without a return period occurs.
export function eventFrequency(event) {
  if (returnPeriod(event) != null) return "";
  const { probabilistic, deterministic } = event.occurrence ?? {};
  if (probabilistic?.event_rate != null) {
    return `${probabilistic.event_rate} per year`;
  }
  const { value, span } = probabilistic?.probability ?? {};
  if (value != null) {
    const chance =
      value <= 1 ? `${Number((value * 100).toPrecision(3))}%` : String(value);
    return span ? `${chance} in ${span} years` : chance;
  }
  const criteria = deterministic?.index_criteria;
  return typeof criteria === "string" ? criteria : "";
}
