export default {
  db: null,
  transformDatasetRow(row) {
    return {
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
      version: row[12],
    };
  },
  loadDatasets(db) {
    this.db = db;
    const results = this.queryDB("SELECT * FROM datasets")
    const datasets = results[0].values.map(this.transformDatasetRow)
    this.all = datasets;
    this.display = datasets;
  },

  getDatasetById(id) {
    if (this.dataset && this.dataset.id === id) {
      return this.dataset;
    }
    this.dataset = this.all.find((dataset) => dataset.id === id);
    return this.dataset;
  },

  get datasetsByFilterAndSearch() {
    if (!this.db) return [];
    // search: `SELECT * FROM datasets_fts(${this.query});`

    const sql = `SELECT * FROM datasets ${this.getWhereSqlForFilters()};`
    const results = this.queryDB(sql)
    const datasets = results.length ? results[0].values.map(this.transformDatasetRow): []
    this.display = datasets;
    return datasets;
  },

  queryDB(sqlString) {
    if (!this.db) {
      console.warn("Database not initialized");
    }
    try {
      const result = this.db.exec(sqlString);
      return result;

    } catch (e) {
      console.error("Error executing SQL:", sqlString,e);
    }

  },
  // one to many, requiring one table
  // "SELECT label FROM licenses;
  // many to many, requiring table and join table
  // "SELECT label FROM risk_data_types;
};
