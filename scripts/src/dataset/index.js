import { queryApi } from "../shared/api";

const datasetStore = {
  dataset: null,
  isLoading: true,
  isLoaded: false,
  loadError: false,
};

// defineProperties to preserve getters, keeping `this` bound to the store
Object.defineProperties(
  datasetStore,
  Object.getOwnPropertyDescriptors({
    async loadDataset(id) {
      this.isLoading = true;
      try {
        const data = await queryApi({ action: "dataset", id });
        this.dataset = data.dataset ?? null;
        this.isLoading = false;
        this.isLoaded = true;
      } catch (error) {
        this.handleLoadError(error);
      }
    },
    handleLoadError(err) {
      console.error("Error loading dataset:", err);
      this.isLoading = false;
      this.loadError = true;
    },
  }),
);

export default datasetStore;