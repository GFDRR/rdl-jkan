import { queryDB, transformShape } from "../shared/utils";
import filtering from "./filtering";
import pagination from "./pagination";
import search from "./search";

const datasetsStore = {
  db: null,
  all: [],
  display: [],
  filteredDatasets: [],
  filterCacheKey: null,
  isLoading: true,
  isSearching: false,
  isLoaded: false,
  loadError: false,
};

// defineProperties to preserve getters, keeping `this` bound to the store
Object.defineProperties(
  datasetsStore,
  Object.getOwnPropertyDescriptors(pagination),
);
Object.defineProperties(
  datasetsStore,
  Object.getOwnPropertyDescriptors(filtering),
);
Object.defineProperties(
  datasetsStore,
  Object.getOwnPropertyDescriptors(search),
);
Object.defineProperties(
  datasetsStore,
  Object.getOwnPropertyDescriptors({
    getFilteredDatasets() {
      if (!this.db) return [];

      const filterKey = JSON.stringify(this.filters);
      if (filterKey !== this.filterCacheKey) {
        const sql = `
          SELECT
            c.title as catalog_title, c.slug,
            l.title as license_title, l.slug as license_slug, l.url as license_url,
            json_extract(datasets.frontmatter, '$.contact_point') as contact_point,
            json_extract(datasets.frontmatter, '$.creator') as creator,
            json_extract(datasets.frontmatter, '$.details') as details,
            json_extract(datasets.frontmatter, '$.publisher') as publisher,
            json_extract(datasets.frontmatter, '$.resources') as resources,
            json_extract(datasets.spatial, '$.countries') as countries,
            datasets.*
          FROM datasets
            LEFT JOIN catalogs c ON datasets.catalog_slug = c.slug
            LEFT JOIN licenses l ON datasets.license_slug = l.slug
            ${this.getWhereSqlForFilters()};
        `;
        this.filteredDatasets = transformShape(queryDB(this.db, sql)) ?? [];
        this.filterCacheKey = filterKey;
      }
      return this.filteredDatasets;
    },
    refreshDisplay() {
      if (!this.db) return;

      const filtered = this.getFilteredDatasets();
      if (!this.query.trim()) {
        this.display = filtered;
        return;
      }

      const byId = new Map(filtered.map((d) => [d.id, d]));
      this.display = this.searchResultIds
        .map((id) => byId.get(id))
        .filter(Boolean);
    },
    get paginatedDatasets() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.display.slice(start, start + this.itemsPerPage);
    },
    loadDatasets(db) {
      this.db = db;
      this.loadVectors();
      const results = queryDB(db, `
        SELECT
          c.title as catalog_title, c.slug,
          l.title as license_title, l.slug as license_slug, l.url as license_url,
          json_extract(datasets.frontmatter, '$.contact_point') as contact_point,
          json_extract(datasets.frontmatter, '$.creator') as creator,
          json_extract(datasets.frontmatter, '$.details') as details,
          json_extract(datasets.frontmatter, '$.publisher') as publisher,
          json_extract(datasets.frontmatter, '$.resources') as resources,
          json_extract(datasets.spatial, '$.countries') as countries,
          datasets.*
        FROM datasets
          LEFT JOIN catalogs c ON datasets.catalog_slug = c.slug
          LEFT JOIN licenses l ON datasets.license_slug = l.slug
      `);
      const datasets = transformShape(results) ?? [];
      this.all = datasets;
      this.filteredDatasets = datasets;
      this.filterCacheKey = JSON.stringify(this.filters);
      this.display = datasets;
      this.isLoading = false;
      this.isLoaded = true;
      if (this.query.trim()) {
        this.scheduleSearch();
        this.scheduleQueryVector();
      }
    },
    handleLoadError(err) {
      console.error("Error loading database:", err);
      this.isLoading = false;
      this.loadError = true;
    },
  }),
);

export default datasetsStore;
