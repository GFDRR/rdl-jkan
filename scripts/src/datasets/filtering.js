import { queryApi } from "../shared/api";

const FILTER_TYPES = [
  "catalog",
  "countries",
  "risk_data_type",
  "geo_scale",
  "hazard_type",
  "license",
  "project",
];

const GEO_ORDER = ["global", "regional", "national", "sub-national"];

// Filter options are fetched from the query function (counts reflect the
// other active filters); this adds the `selected` flag and applies the same
// per-type ordering the old client-side builders used.
function presentOptions(type, store) {
  const raw = store.filterOptions[type] ?? [];
  const withSelected = () =>
    raw.map((item) => ({
      ...item,
      selected: store.isFilterActive(type, item.slug),
    }));

  switch (type) {
    case "catalog": {
      // Selected options disappear from the list (they show in the active
      // filters summary), except the "Unknown" placeholder.
      const values = withSelected();
      const unselected = values.filter((v) => !v.selected);
      const unknown = values.filter((v) => v.selected && v.title === "Unknown");
      return [...unknown, ...unselected];
    }
    case "geo_scale": {
      const values = withSelected();
      const sortByGeo = (arr) =>
        arr.sort((a, b) => {
          const aIdx = GEO_ORDER.indexOf(a.title.toLowerCase());
          const bIdx = GEO_ORDER.indexOf(b.title.toLowerCase());
          if (aIdx === -1 && bIdx === -1) return a.title.localeCompare(b.title);
          if (aIdx === -1) return 1;
          if (bIdx === -1) return -1;
          return aIdx - bIdx;
        });
      return [
        ...sortByGeo(values.filter((v) => v.selected)),
        ...sortByGeo(values.filter((v) => !v.selected)),
      ];
    }
    case "risk_data_type":
      return withSelected();
    default: {
      const values = withSelected();
      const byTitle = (a, b) => a.title.localeCompare(b.title);
      return [
        ...values.filter((v) => v.selected).sort(byTitle),
        ...values.filter((v) => !v.selected).sort(byTitle),
      ];
    }
  }
}

export default {
  filters: Object.fromEntries(FILTER_TYPES.map((type) => [type, []])),
  filterOptions: Object.fromEntries(FILTER_TYPES.map((type) => [type, []])),

  toggleFilter(filterType, value) {
    const idx = this.filters[filterType].indexOf(value);
    idx === -1
      ? this.filters[filterType].push(value)
      : this.filters[filterType].splice(idx, 1);
    this.refreshDisplay();
    this.scheduleOptionsRefresh();
  },

  isFilterActive(filterType, value) {
    return this.filters[filterType].includes(value);
  },

  clearFilters() {
    Object.keys(this.filters).forEach((k) => (this.filters[k] = []));
    this.refreshDisplay();
    this.scheduleOptionsRefresh();
  },

  get activeFilterCount() {
    return Object.values(this.filters).reduce(
      (sum, arr) => sum + arr.length,
      0,
    );
  },

  get hasActiveFilters() {
    return this.activeFilterCount > 0;
  },

  getFilterOptionsCatalog() {
    return presentOptions("catalog", this);
  },
  getFilterOptionsCountries() {
    return presentOptions("countries", this);
  },
  getFilterOptionsGeoScale() {
    return presentOptions("geo_scale", this);
  },
  getFilterOptionsHazardType() {
    return presentOptions("hazard_type", this);
  },
  getFilterOptionsLicense() {
    return presentOptions("license", this);
  },
  getFilterOptionsProject() {
    return presentOptions("project", this);
  },
  getFilterOptionsRiskDataType() {
    return presentOptions("risk_data_type", this);
  },
};