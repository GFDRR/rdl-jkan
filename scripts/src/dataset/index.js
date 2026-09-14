import { queryDB, transformShape } from "../shared/utils";

const datasetStore = {
  dataset: null,
  db: null,
};

// defineProperties to preserve getters, keeping `this` bound to the store
Object.defineProperties(
  datasetStore,
  Object.getOwnPropertyDescriptors({
    loadDataset(db, id) {
      this.db = db
      const results = queryDB(
        db,
        `
          SELECT 
          c.title as catalog_title, c.slug,
          l.title as license_title, l.slug as license_slug, l.url as license_url,
          json_extract(datasets.frontmatter, '$.contact_point') as contact_point,
          json_extract(datasets.frontmatter, '$.creator') as creator,
          json_extract(datasets.frontmatter, '$.details') as details,
          json_extract(datasets.frontmatter, '$.exposure') as exposure,
          json_extract(datasets.frontmatter, '$.loss') as loss,
          json_extract(datasets.frontmatter, '$.publisher') as publisher,
          json_extract(datasets.frontmatter, '$.purpose') as purpose,
          json_extract(datasets.frontmatter, '$.resources') as resources,
          json_extract(datasets.frontmatter, '$.vulnerability') as vulnerability,
          datasets.*
          FROM datasets
          LEFT JOIN catalogs c ON datasets.catalog_slug = c.slug
          LEFT JOIN licenses l ON datasets.license_slug = l.slug
          WHERE id = '${id}'
        `,
      );
      
      this.dataset = transformShape(results)?.[0] ?? null
    },
  }),
);

export default datasetStore;
