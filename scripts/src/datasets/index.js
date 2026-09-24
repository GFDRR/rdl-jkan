import { queryApi } from "../shared/api";
import filtering from "./filtering";
import pagination from "./pagination";
import search from "./search";

const datasetsStore = {
  display: [],
  totalCount: 0,
  isLoading: true,
  isSearching: false,
  isLoaded: false,
  loadError: false,
  _fetchToken: 0,
  _optionsTimer: null,
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
    // The server returns one page of rows at a time; `display` is that page.
    get paginatedDatasets() {
      return this.display;
    },

    loadDatasets() {
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
      const q = this.query.trim();
      const payload = q
        ? {
            action: "search",
            q,
            vector: this.queryVector,
            filters: this.filters,
            page: this.currentPage,
            pageSize: this.itemsPerPage,
          }
        : {
            action: "datasets",
            filters: this.filters,
            page: this.currentPage,
            pageSize: this.itemsPerPage,
          };
      this.isSearching = Boolean(q);

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
        // Keep the spinner up while the query embedding is still pending.
        if (!q || this.queryVector) this.isSearching = false;
      } catch (error) {
        if (token !== this._fetchToken) return;
        this.handleLoadError(error);
      }
    },

    scheduleOptionsRefresh() {
      clearTimeout(this._optionsTimer);
      this._optionsTimer = setTimeout(() => {
        queryApi({ action: "options", filters: this.filters })
          .then((data) => {
            if (data?.options) this.filterOptions = data.options;
          })
          .catch((error) =>
            console.error("Failed to load filter options:", error),
          );
      }, 150);
    },

    handleLoadError(error) {
      console.error("Error loading datasets:", error);
      this.isLoading = false;
      this.isSearching = false;
      this.loadError = true;
    },
  }),
);

export default datasetsStore;