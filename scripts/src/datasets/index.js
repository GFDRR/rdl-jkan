import {
  datasetsPayload,
  isAnswered,
  optionsPayload,
  queryApi,
  searchPayload,
} from "../shared/api.js";
import filtering from "./filtering.js";
import pagination from "./pagination.js";
import search from "./search.js";
import urlState from "./url-state.js";

const datasetsStore = {
  display: [],
  totalCount: 0,
  isLoading: true,
  isSearching: false,
  isLoaded: false,
  loadError: false,
  _fetchToken: 0,
  _optionsTimer: null,
  _optionsToken: 0,
};

// defineProperties to preserve getters, keeping `this` bound to the store
Object.defineProperties(
  datasetsStore,
  Object.getOwnPropertyDescriptors(pagination),
);
Object.defineProperties(
  datasetsStore,
  Object.getOwnPropertyDescriptors(filtering),
);
Object.defineProperties(
  datasetsStore,
  Object.getOwnPropertyDescriptors(search),
);
Object.defineProperties(
  datasetsStore,
  Object.getOwnPropertyDescriptors({
    loadDatasets() {
      urlState.read(this);
      this.fetchPage();
      this.scheduleOptionsRefresh();
    },

    goToPage(page) {
      this.currentPage = Math.min(
        Math.max(1, page),
        Math.max(1, this.totalPages),
      );
      this.refreshDisplay();
    },

    refreshDisplay() {
      return this.fetchPage();
    },

    async fetchPage() {
      const token = ++this._fetchToken;
      urlState.write(this);
      const q = this.query.trim();
      const payload = q
        ? searchPayload(
            q,
            this.queryVector,
            this.filters,
            this.currentPage,
            this.itemsPerPage,
          )
        : datasetsPayload(this.filters, this.currentPage, this.itemsPerPage);
      // The page has other spinners for its first datasets and the related ones.
      this.isSearching =
        Boolean(q) &&
        this.isLoaded &&
        !this.isLookingForRelated &&
        !isAnswered(payload);

      try {
        const data = await queryApi(payload);
        if (token !== this._fetchToken) return;
        this.display = data.rows ?? [];
        this.totalCount = data.total ?? 0;
        if (Number.isInteger(data.page) && data.page !== this.currentPage) {
          this.currentPage = data.page;
        }
        this.isLoading = false;
        this.isLoaded = true;
        this.loadError = false;
        this.isSearching = false;
        if (q && !this.queryVector) this.findRelated(this.totalCount);
      } catch (error) {
        if (token !== this._fetchToken) return;
        this.handleLoadError(error);
      }
    },

    scheduleOptionsRefresh() {
      clearTimeout(this._optionsTimer);
      const token = ++this._optionsToken;
      const payload = optionsPayload(this.filters);
      const refresh = () =>
        queryApi(payload)
          .then((data) => {
            if (token !== this._optionsToken) return;
            if (data?.options) this.filterOptions = data.options;
          })
          .catch((error) =>
            console.error("Failed to load filter options:", error),
          );
      if (isAnswered(payload)) refresh();
      else this._optionsTimer = setTimeout(refresh, 150);
    },

    handleLoadError(error) {
      console.error("Error loading datasets:", error);
      this.isLoading = false;
      this.isSearching = false;
      this.isLookingForRelated = false;
      this.loadError = true;
    },
  }),
);

export default datasetsStore;