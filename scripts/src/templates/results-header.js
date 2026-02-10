export default (data) => {
  switch (data.type) {
    case "keyword":
      return `<h3>${data.count} dataset${data.count === 1 ? "" : "s"} matching query</h3>`;
    case "semantic":
      return data.count === 0
        ? "<h3></h3>"
        : '<h3 style="border-top: 2px solid #333;border-bottom: 2px solid #333; padding: 0.3em 0;">You may also be interested in...</h3>';
    default:
      return `<h3>${data.count} dataset${data.count === 1 ? "" : "s"}</h3>`;
  }
};
