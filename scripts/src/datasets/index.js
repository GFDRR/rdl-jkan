import { queryDB, transformShape } from "../shared/utils";
import filtering from "./filtering";
import pagination from "./pagination";
import search from "./search";

const datasetsStore = {
  db: null,
  all: [],
  display: [],
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
    get datasetsByFilterAndSearch() {
      if (!this.db) return [];
      // search: `SELECT * FROM datasets_fts(${this.query});`

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
      const results = queryDB(this.db, sql);
      const datasets = transformShape(results) ?? [];
      this.display = datasets;
      return datasets;
    },
    get paginatedDatasets() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.datasetsByFilterAndSearch.slice(
        start,
        start + this.itemsPerPage,
      );
    },
    loadDatasets(db) {
      this.db = db;
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
      this.display = datasets;
    },
  }),
);

export default datasetsStore;
