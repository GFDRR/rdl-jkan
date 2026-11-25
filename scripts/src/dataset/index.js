import { queryApi } from "../shared/api";
import { drawMap } from "./components.js";
import { buildPage } from "./sections.js";

const RELATION_LABELS = {
  source: "Source of this dataset",
  derived: "Derived from this dataset",
  project: "Same project",
  similar: "Similar dataset",
};

// The main facts come first: only this many countries are listed at once.
const COUNTRIES_SHOWN = 6;

const datasetStore = {
  dataset: null,
  // What the page shows of the dataset, see sections.js.
  page: null,
  related: [],
  isLoading: true,
  isLoaded: false,
  loadError: false,
  allCountries: false,
};

// defineProperties to preserve getters, keeping `this` bound to the store
Object.defineProperties(
  datasetStore,
  Object.getOwnPropertyDescriptors({
    async loadDataset(id) {
      this.isLoading = true;
      try {
        const data = await queryApi({ action: "dataset", id });
        const dataset = data.dataset ?? null;
        this.page = dataset && buildPage(dataset);
        this.dataset = dataset;
        this.isLoading = false;
        this.isLoaded = true;
      } catch (error) {
        this.handleLoadError(error);
        return;
      }
      this.loadRelated(id);
    },

    async loadRelated(id) {
      try {
        const data = await queryApi({ action: "related", id });
        this.related = data.related ?? [];
      } catch (error) {
        // The page is complete without its related datasets.
        console.error("Error loading related datasets:", error);
      }
    },

    // The sections of the page, with the related datasets once they are loaded.
    get sections() {
      const sections = this.page?.sections ?? [];
      if (!this.related.length) return sections;
      return [
        ...sections,
        {
          id: "related",
          title: "Related datasets",
          kind: "neutral",
          count: this.related.length,
          summary: "",
        },
      ];
    },

    get countries() {
      const countries = this.page?.countries ?? [];
      const shown = this.allCountries
        ? countries
        : countries.slice(0, COUNTRIES_SHOWN);
      return shown.join(", ");
    },

    get moreCountries() {
      if (this.allCountries) return 0;
      return Math.max(0, (this.page?.countries.length ?? 0) - COUNTRIES_SHOWN);
    },

    relationLabel(relation) {
      return RELATION_LABELS[relation] ?? "";
    },

    drawMap(element, baseUrl) {
      drawMap(element, this.dataset.spatial, baseUrl);
    },

    handleLoadError(err) {
      console.error("Error loading dataset:", err);
      this.isLoading = false;
      this.loadError = true;
    },
  }),
);

export default datasetStore;
