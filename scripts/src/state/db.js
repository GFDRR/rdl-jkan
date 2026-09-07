import { slugify } from "../util";
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
    const filtersSetCount = !!this.filters.catalog.length + !!this.filters.countries.length + !!this.filters.geo_scale.length + !!this.filters.project.length + !!this.filters.risk_data_type.length + !!this.filters.hazard_type.length + !!this.filters.license.length
    let whereSql = filtersSetCount ? 'WHERE ' : '';
    let filtersAppliedCount = 0;

    if (this.filters.catalog.length) {
      whereSql += '('
      if (this.filters.catalog.length > 1) filtersAppliedCount ++
      this.filters.catalog.forEach((c, index) => {
        whereSql += `catalog_slug = '${c}' ${index < this.filters.catalog.length - 1 ? 'OR':''} `
      })
      if (this.filters.catalog.length > 1) whereSql += ')'
      if (filtersAppliedCount < filtersSetCount) whereSql += ' AND '
    }
    if (this.filters.countries.length) {
      if (this.filters.countries.length > 1) whereSql += '('
      filtersAppliedCount ++
      this.filters.countries.forEach((c, index) => {
        whereSql += `json_extract(spatial, '$.countries') LIKE '%${c}%' ${index < this.filters.countries.length - 1 ? 'OR':''} `
      })
      if (this.filters.countries.length > 1) whereSql += ')'
      if (filtersAppliedCount < filtersSetCount) whereSql += ' AND '
    }
    if (this.filters.geo_scale.length) {
      if (this.filters.geo_scale.length > 1) whereSql += '('
      filtersAppliedCount ++
      this.filters.geo_scale.forEach((s, index) => {
        whereSql += `json_extract(spatial, '$.scale') LIKE '%${s}%' ${index < this.filters.geo_scale.length - 1 ? 'OR':''} `
      }) 
      if (this.filters.geo_scale.length > 1) whereSql += ')'
      if (filtersAppliedCount < filtersSetCount) whereSql += ' AND '
    }
    if (this.filters.project.length) {
      if (this.filters.project.length > 1) whereSql += '('
      filtersAppliedCount ++
      this.filters.project.forEach((p, index) => {
        whereSql += `json_extract(project, '$') LIKE '%${p}%' ${index < this.filters.project.length - 1 ? 'OR':''} `
      })  
      if (this.filters.project.length > 1) whereSql += ')'
      if (filtersAppliedCount < filtersSetCount) whereSql += ' AND '
    }
    if (this.filters.risk_data_type.length) {
      if (this.filters.risk_data_type.length > 1) whereSql += '('
      filtersAppliedCount ++
      this.filters.risk_data_type.forEach((rdt, index) => {
        whereSql += `json_extract(risk_data_type, '$') LIKE '%${rdt}%' ${index < this.filters.risk_data_type.length - 1 ? 'OR':''} `
      })
      if (this.filters.risk_data_type.length > 1) whereSql += ')'
      if (filtersAppliedCount < filtersSetCount) whereSql += ' AND '
    }
    if (this.filters.hazard_type.length) {
      if (this.filters.hazard_type.length > 1) whereSql += '('
      filtersAppliedCount ++
      this.filters.hazard_type.forEach((ht, index) => {
        whereSql += `json_extract(hazard, '$.type') LIKE '%${ht}%' ${index < this.filters.hazard_type.length - 1 ? 'OR':''} `
      })
      if (this.filters.hazard_type.length > 1) whereSql += ')'
      if (filtersAppliedCount < filtersSetCount) whereSql += ' AND '
    }
    if (this.filters.license.length) {
      if (this.filters.license.length > 1) whereSql += '('
      filtersAppliedCount ++
      this.filters.license.forEach((l) => {
        whereSql += `license_slug = '${l}' ${index < this.filters.license.length - 1 ? 'OR':''} `
      })
      if (this.filters.license.length > 1) whereSql += ')'
      if (filtersAppliedCount < filtersSetCount) whereSql += ' AND '
    }
    const sql = `SELECT * FROM datasets ${whereSql};`
    const results = this.queryDB(sql)
    const datasets = results.length ? results[0].values.map(this.transformDatasetRow): []
    this.display = datasets;
    return datasets;
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
