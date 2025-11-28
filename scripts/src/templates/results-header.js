function getText(data) {
  switch (data.type) {
    case "keyword":
      return `${data.count} dataset${data.count === 1 ? '' : 's'} matching query`;
    case "semantic":
      return (data.count === 0) ? '' : `${data.count} additional semantically related dataset${data.count === 1 ? '' : 's'}`;
    default:
      return `${data.count} dataset${data.count === 1 ? '' : 's'}`;
  }
}

export default (data) => (
  `
  <h3>${getText(data)}</h3>
`)