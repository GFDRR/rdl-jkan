import { slugify } from "../util";
export default {
  db: null,
  loadDB(db) {
    this.db = db;
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
