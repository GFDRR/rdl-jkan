// Tables for the lists of a dataset, which can hold hundreds of entries: what
// is the same for every entry is said once above the table, columns without
// values are left out, and long lists can be searched, filtered and sorted.

// Shorter lists have no search and no filters.
export const FILTER_FROM = 9;
export const PAGE_SIZE = 10;
const MAX_OPTIONS = 40;
const MAX_OPTION_LENGTH = 150;
const MAX_CHIPS = 14;

// "RCP8.5" is also found as "rcp85".
export function normalize(text) {
  return String(text ?? "")
    .toLowerCase()
    .replace(/(\d)[.,](?=\d)/g, "$1");
}

export function compareValues(a, b) {
  if (typeof a === "number" && typeof b === "number") return a - b;
  return String(a ?? "").localeCompare(String(b ?? ""), "en", {
    numeric: true,
  });
}

/**
 * The content of a table.
 *
 * Columns: id, label, value(row) and, optionally, main (the column which names
 * the row), num, tag, hidden (only for filters), facet ("chips" or "select"),
 * order(row) to sort by something else than the value, and href(row),
 * detail(row) and note(row) for what goes with the value.
 *
 * `known` lists values already shown next to the table.
 */
export function buildTable(
  rows,
  columns,
  { noun = ["entry", "entries"], known = [] } = {},
) {
  const entries = rows.map((row, key) => {
    const cells = {};
    for (const column of columns) {
      const value = column.value(row) ?? "";
      cells[column.id] = {
        text: String(value),
        order: column.order ? column.order(row) : value,
        href: column.href?.(row) ?? null,
        detail: column.detail?.(row) ?? "",
        note: column.note?.(row) ?? "",
      };
    }
    const search = normalize(
      Object.values(cells)
        .map(({ text, detail, note }) => `${text} ${detail} ${note}`)
        .join(" "),
    );
    return { key, cells, search };
  });

  const described = columns.map((column) => {
    const options = new Map();
    for (const { cells } of entries) {
      const { text, order } = cells[column.id];
      if (!text) continue;
      const option = options.get(text) ?? { value: text, order, count: 0 };
      option.count += 1;
      options.set(text, option);
    }
    const only = options.size === 1 ? [...options.values()][0] : null;
    return {
      column,
      options: [...options.values()].sort((a, b) =>
        compareValues(a.order, b.order),
      ),
      same: !column.main && rows.length > 1 && only?.count === rows.length,
    };
  });

  const visible = described.filter(({ column }) => !column.hidden);
  const shown = visible.filter(
    ({ column, options, same }) => column.main || (options.length && !same),
  );
  const filterable = rows.length >= FILTER_FROM;
  const facets = filterable
    ? shown.filter(
        ({ column, options }) =>
          column.facet &&
          options.length > 1 &&
          options.length <= MAX_OPTIONS &&
          options.every(({ value }) => value.length <= MAX_OPTION_LENGTH),
      )
    : [];

  return {
    noun,
    entries,
    total: rows.length,
    filterable,
    sortable: rows.length > 3,
    same: visible
      .filter(({ same }) => same)
      .map(({ column, options }) => ({
        label: column.label,
        value: options[0].value,
      }))
      .filter(({ value }) => !known.includes(value)),
    columns: shown.map(({ column: { id, label, main, num, tag } }) => ({
      id,
      label,
      main: Boolean(main),
      num: Boolean(num),
      tag: Boolean(tag),
    })),
    facets: facets.map(({ column, options }) => ({
      id: column.id,
      label: column.label,
      chips: column.facet === "chips" && options.length <= MAX_CHIPS,
      options,
    })),
  };
}

export function filterEntries(
  entries,
  { query = "", filters = {}, sort = null, descending = false },
) {
  const terms = normalize(query).split(/\s+/).filter(Boolean);
  const active = Object.entries(filters).filter(([, value]) => value);
  const found = entries.filter(
    ({ cells, search }) =>
      active.every(([id, value]) => cells[id]?.text === value) &&
      terms.every((term) => search.includes(term)),
  );
  if (!sort) return found;
  const direction = descending ? -1 : 1;
  return found.sort(
    (a, b) =>
      direction * compareValues(a.cells[sort].order, b.cells[sort].order),
  );
}
