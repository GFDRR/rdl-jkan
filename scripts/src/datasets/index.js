import { queryDB, transformDatasetRow } from "../shared/utils";
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

      const sql = `SELECT * FROM datasets ${this.getWhereSqlForFilters()};`;
      const results = queryDB(this.db, sql);
      const datasets = results.length
        ? results[0].values.map(transformDatasetRow)
        : [];
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
      const results = queryDB(db, "SELECT * FROM datasets");
      const datasets = results[0].values.map(transformDatasetRow);
      this.all = datasets;
      this.display = datasets;
    },
  }),
);

export default datasetsStore;
