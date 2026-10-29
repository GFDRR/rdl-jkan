import { env, pipeline } from "@huggingface/transformers";

// Must match the model used to generate the embeddings
// (see python/generate_vectors.py).
const EMBEDDING_MODEL = "Xenova/all-MiniLM-L6-v2";
const SEARCH_DEBOUNCE_MS = 200;
const EMBEDDING_DEBOUNCE_MS = 350;

env.allowLocalModels = false;

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
    this.queryVector = null;
    this.scheduleSearch();
    this.scheduleQueryVector();
  },
  queryVector: null,
  embedderPromise: null,
  _searchTimer: null,
  _searchToken: 0,
  _embedTimer: null,
  _embedToken: 0,

  scheduleSearch() {
    clearTimeout(this._searchTimer);
    const trimmed = this.query.trim();
    const token = ++this._searchToken;
    if (!trimmed) {
      // Query cleared — refetch the unfiltered page right away.
      this.refreshDisplay();
      return;
    }

    this._searchTimer = setTimeout(() => {
      if (token !== this._searchToken) return;
      this.refreshDisplay();
    }, SEARCH_DEBOUNCE_MS);
  },

  scheduleQueryVector() {
    clearTimeout(this._embedTimer);
    const trimmed = this.query.trim();
    const token = ++this._embedToken;
    if (!trimmed) return;

    this._embedTimer = setTimeout(() => {
      this.embedQuery(trimmed)
        .then((vector) => {
          if (token !== this._embedToken) return;
          this.queryVector = vector;
          this.refreshDisplay();
          this.isSearching = false;
        })
        .catch((error) => {
          if (token !== this._embedToken) return;
          console.error("Failed to embed search query:", error);
          this.isSearching = false;
        });
    }, EMBEDDING_DEBOUNCE_MS);
  },

  loadEmbedder() {
    if (this.embedderPromise) return this.embedderPromise;
    this.embedderPromise = pipeline("feature-extraction", EMBEDDING_MODEL).catch(
      (error) => {
        console.error("Failed to load semantic search model:", error);
        this.embedderPromise = null;
        return null;
      },
    );
    return this.embedderPromise;
  },

  async embedQuery(text) {
    const embedder = await this.loadEmbedder();
    if (!embedder) return null;
    const output = await embedder(text, { pooling: "mean", normalize: true });
    return Array.from(output.data);
  },
};