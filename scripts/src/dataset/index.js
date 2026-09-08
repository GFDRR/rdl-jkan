import { queryDB, transformDatasetRow } from "../shared/utils";

const datasetStore = {
  dataset: null,
  db: null,
};

function transformShape(data) {
  return data.flatMap(({ columns, values }) => {
    return values.map(row => {
      const obj = {};
      columns.forEach((column, index) => {
        obj[column] = row[index];
      });
      return obj;
    });
  });
}

// defineProperties to preserve getters, keeping `this` bound to the store
Object.defineProperties(
  datasetStore,
  Object.getOwnPropertyDescriptors({
    loadDataset(db, id) {
      this.db = db
      const results = queryDB(
        db,
        `
          SELECT datasets.*, catalogs.title as catalog_title, catalogs.slug
          FROM datasets
          LEFT JOIN catalogs ON datasets.catalog_slug = catalogs.slug
          WHERE id = '${id}'
        `,
      );
      
      this.dataset = transformShape(results)?.[0] ?? null
      console.log(this.dataset);
    },
  }),
);

export default datasetStore;
