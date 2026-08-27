export default {
  query: "",
  filteredKeywordResults: [],
  filteredNonKeywordResults: [],

  get results() {
    if (!this.query.trim()) {
      return this.applyFilters();
    }
    const filteredIds = new Set(this.applyFilters().map((d) => d.dataset_id));
    return this.filteredKeywordResults.filter((r) =>
      filteredIds.has(r.dataset_id),
    );
  },
};
