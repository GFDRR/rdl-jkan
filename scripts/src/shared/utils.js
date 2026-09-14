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

export function transformShape(data) {
  if (!data || !Array.isArray(data)) {
    return [];
  }
  
  return data.flatMap(({ columns, values }) => {
    if (!columns || !values || !Array.isArray(values)) {
      return [];
    }
    
    return values.map(row => {
      const obj = {};
      columns.forEach((column, index) => {
        let value = row[index];
        if (typeof value === 'string') {
          try {
            const parsed = JSON.parse(value);
            value = parsed;
          } catch (e) {
            // Not valid JSON, keep original string value
          }
        }
        obj[column] = value;
      });
      return obj;
    });
  });
}
