export function queryDB(db, sqlString) {
  if (!db) {
    console.warn("Database not initialized");
  }
  try {
    const result = db.exec(sqlString);
    return result;
  } catch (e) {
    console.error("Error executing SQL:", sqlString, e);
  }

  // one to many, requiring one table
  // "SELECT label FROM licenses;
  // many to many, requiring table and join table
  // "SELECT label FROM risk_data_types;
}

export function transformDatasetRow(row) {
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
}
