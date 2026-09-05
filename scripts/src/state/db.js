import { slugify } from "../util";
export default {
  db: null,
  loadDB(db) {
    this.db = db;
    const results = this.queryDB("SELECT * FROM datasets")
    const datasets = results[0].values.map((row) => ({
      id: row[0],
      catalog_slug: row[1],
      description: row[2],
      frontmatter: row[3],
      hazard: row[4],
      license_slug: row[5],
      project: JSON.parse(row[6]),
      risk_data_type: JSON.parse(row[7]),
      slug: row[8],
      spatial: JSON.parse(row[9]),
      temporal: JSON.parse(row[10]),
      title: row[11],
    }))
    this.all = datasets;
    this.display = datasets;
  },

  queryDB(sqlString) {
    if (!this.db) {
      console.warn("Database not initialized");
    }

    const result = this.db.exec(sqlString);
    return result;
  },
  // one to many, requiring one table
  // "SELECT label FROM licenses;
  // many to many, requiring table and join table
  // "SELECT label FROM risk_data_types;
};
