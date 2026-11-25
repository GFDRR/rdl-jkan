const SEARCH_DEBOUNCE_MS = 200;
// Semantic search adds related datasets to the ones that contain the words of
// the query. Its model is a large download, so it is for searches that find few.
const FEW_RESULTS = 20;

// Keyword search (FTS) and semantic search both run server-side in the query
// function; this module only embeds the query text in the browser and keeps
// the debouncing that decides when to refetch results.
export default {
  _query: "",
  get query() {
    return this._query;
  },
  set query(value) {
    this._query = value ?? "";
    this.isSearching = Boolean(this._query.trim());
    this.isLookingForRelated = false;
    this.queryVector = null;
    this.currentPage = 1;
    this.scheduleSearch();
  },
  queryVector: null,
  // The results are on the page and semantic search may still add some.
  isLookingForRelated: false,
  _searchTimer: null,
  // The query that was last embedded, or is being embedded.
  _embeddedQuery: null,

  scheduleSearch() {
    clearTimeout(this._searchTimer);
    this._embeddedQuery = null;
    // The answer to the previous query must not be shown any more.
    this._fetchToken++;
    if (!this.query.trim()) {
      // Query cleared — show the unfiltered page right away.
      this.refreshDisplay();
      return;
    }
    this._searchTimer = setTimeout(
      () => this.refreshDisplay(),
      SEARCH_DEBOUNCE_MS,
    );
  },

  // Called with the number of datasets found by keyword.
  async findRelated(total) {
    const q = this.query.trim();
    if (total >= FEW_RESULTS || this._embeddedQuery === q) return;
    this._embeddedQuery = q;
    this.isLookingForRelated = true;

    let vector = null;
    try {
      const { embed } = await import(new URL("./embedder.js", import.meta.url));
      if (this._embeddedQuery !== q) return;
      vector = await embed(q);
    } catch (error) {
      console.error("Semantic search is not available:", error);
    }
    if (this._embeddedQuery !== q) return;

    if (vector) {
      this.queryVector = vector;
      await this.refreshDisplay();
      if (this._embeddedQuery !== q) return;
    }
    this.isLookingForRelated = false;
  },
};
