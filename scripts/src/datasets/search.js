import { env, pipeline } from "@huggingface/transformers";
import { queryDB } from "../shared/utils.js";

export const KEYWORD_SCORE_MIN = 0.75;
export const KEYWORD_SCORE_MAX = 1.0;
export const SEMANTIC_MAX_RESULTS = 50;
export const SEMANTIC_MIN_SCORE = 0.25;

const VECTORS_URL = "/python/vectors.json";
// Must match the model used to generate vectors.json (see python/generate_vectors.py).
const EMBEDDING_MODEL = "Xenova/all-MiniLM-L6-v2";
const SEARCH_DEBOUNCE_MS = 200;
const EMBEDDING_DEBOUNCE_MS = 350;

env.allowLocalModels = false;

function escapeQuery(query) {
  const phrase = `"${query.replace(/"/g, '""')}"`;
  return `'${phrase.replace(/'/g, "''")}'`;
}

function cosineSimilarity(a, b) {
  if (!a || !b || a.length !== b.length) return 0;
  let dot = 0;
  let magA = 0;
  let magB = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    magA += a[i] * a[i];
    magB += b[i] * b[i];
  }
  if (magA === 0 || magB === 0) return 0;
  return dot / (Math.sqrt(magA) * Math.sqrt(magB));
}

export default {
  _query: "",
  get query() {
    return this._query;
  },
  set query(value) {
    this._query = value ?? "";
    this.isSearching = Boolean(this._query.trim());
    this.queryVector = null;
    this.filteredKeywordResults = [];
    this.filteredNonKeywordResults = [];
    this.refreshDisplay();
    this.scheduleSearch();
    this.scheduleQueryVector();
  },
  filteredKeywordResults: [],
  filteredNonKeywordResults: [],
  vectors: [],
  vectorsLoaded: false,
  queryVector: null,
  embedderPromise: null,
  _searchTimer: null,
  _searchToken: 0,
  _embedTimer: null,
  _embedToken: 0,

  loadVectors() {
    if (this.vectorsPromise) return this.vectorsPromise;
    this.vectorsPromise = fetch(VECTORS_URL)
      .then((response) => (response.ok ? response.json() : []))
      .then((data) => {
        this.vectors = (Array.isArray(data) ? data : [])
          .map((item) => ({
            dataset_id: item?.metadata?.dataset_id,
            vector: item?.vector,
            metadata: item?.metadata,
          }))
          .filter((item) => item.dataset_id && Array.isArray(item.vector));
        this.vectorsLoaded = true;
        return this.vectors;
      })
      .catch(() => {
        this.vectors = [];
        this.vectorsLoaded = false;
        return this.vectors;
      });
    return this.vectorsPromise;
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

  scheduleSearch() {
    clearTimeout(this._searchTimer);
    const trimmed = this.query.trim();
    const token = ++this._searchToken;
    if (!trimmed) return;

    this._searchTimer = setTimeout(() => {
      if (token !== this._searchToken) return;
      this.refreshSearchResults();
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
          this.runSemanticSearch();
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

  runKeywordSearch() {
    const trimmed = this.query.trim();
    if (!this.db || !trimmed) {
      this.filteredKeywordResults = [];
      return this.filteredKeywordResults;
    }

    const results = queryDB(
      this.db,
      `
        SELECT datasets.id AS dataset_id
        FROM datasets_fts
          JOIN datasets ON datasets.rowid = datasets_fts.rowid
        WHERE datasets_fts MATCH ${escapeQuery(trimmed)}
        ORDER BY bm25(datasets_fts)
      `,
    );

    const ids = (results?.[0]?.values ?? []).map(([dataset_id]) => dataset_id);
    const span = KEYWORD_SCORE_MAX - KEYWORD_SCORE_MIN;
    this.filteredKeywordResults = ids.map((dataset_id, index) => ({
      dataset_id,
      score:
        ids.length === 1
          ? KEYWORD_SCORE_MAX
          : KEYWORD_SCORE_MIN + span * (1 - index / (ids.length - 1)),
      match_type: "keyword",
    }));
    return this.filteredKeywordResults;
  },

  runSemanticSearch() {
    if (!this.vectorsLoaded || !this.queryVector) {
      this.filteredNonKeywordResults = [];
      return this.filteredNonKeywordResults;
    }

    const keywordIds = new Set(
      this.filteredKeywordResults.map((r) => r.dataset_id),
    );
    const vectors = window.Alpine.raw(this.vectors);
    const queryVector = window.Alpine.raw(this.queryVector);
    this.filteredNonKeywordResults = vectors
      .filter((item) => !keywordIds.has(item.dataset_id))
      .map((item) => ({
        dataset_id: item.dataset_id,
        score: cosineSimilarity(queryVector, item.vector),
        match_type: "semantic",
      }))
      .filter((r) => r.score >= SEMANTIC_MIN_SCORE)
      .sort((a, b) => b.score - a.score)
      .slice(0, SEMANTIC_MAX_RESULTS);
    return this.filteredNonKeywordResults;
  },

  refreshSearchResults() {
    this.runKeywordSearch();
    this.runSemanticSearch();
    this.refreshDisplay();
  },

  get searchResultIds() {
    return [
      ...this.filteredKeywordResults,
      ...this.filteredNonKeywordResults,
    ].map((r) => r.dataset_id);
  },
};
