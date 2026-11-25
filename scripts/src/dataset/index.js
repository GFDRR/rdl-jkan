import { queryApi } from "../shared/api.js";

const FUNCTION_TYPES = {
  vulnerability: "Vulnerability Function",
  fragility: "Fragility Function",
  damage_to_loss: "Damage-to-loss Function",
  engineering_demand: "Engineering Demand Function",
};

const RELATION_LABELS = {
  source: "Source of this dataset",
  derived: "Derived from this dataset",
  project: "Same project",
  similar: "Similar dataset",
};

const datasetStore = {
  dataset: null,
  related: [],
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

    relationLabel(relation) {
      return RELATION_LABELS[relation] ?? "";
    },

    // Readable form of a codelist value, e.g. "ground_up" -> "Ground Up".
    label(value) {
      return String(value ?? "")
        .replace(/_/g, " ")
        .replace(/\b\w/g, (char) => char.toUpperCase());
    },

    measurementLabel(measurement) {
      return this.label(measurement?.unit ?? measurement?.quantity_kind);
    },

    eventFrequency(event) {
      const { probabilistic, empirical } = event.occurrence ?? {};
      const returnPeriod =
        probabilistic?.return_period ?? empirical?.return_period;
      if (returnPeriod != null) return `1 in ${returnPeriod} years`;
      if (probabilistic?.event_rate != null) {
        return `${probabilistic.event_rate} per year`;
      }
      const { value, span } = probabilistic?.probability ?? {};
      return value != null ? `${value} in ${span} years` : "";
    },

    get lossGroups() {
      const groups = new Map();
      for (const loss of this.dataset?.loss?.losses ?? []) {
        const type = loss.hazard?.type ?? "other";
        if (!groups.has(type)) groups.set(type, []);
        groups.get(type).push(loss);
      }
      return [...groups]
        .map(([hazard_type, losses]) => ({ hazard_type, losses }))
        .sort((a, b) => a.hazard_type.localeCompare(b.hazard_type));
    },

    get lossCount() {
      return this.dataset?.loss?.losses?.length ?? 0;
    },

    get vulnerabilityGroups() {
      const functions = this.dataset?.vulnerability?.functions ?? {};
      return Object.entries(FUNCTION_TYPES)
        .map(([type, title]) => ({
          type,
          title,
          functions: functions[type] ?? [],
        }))
        .filter((group) => group.functions.length);
    },

    get socioEconomicIndices() {
      return this.dataset?.vulnerability?.socio_economic ?? [];
    },

    handleLoadError(err) {
      console.error("Error loading dataset:", err);
      this.isLoading = false;
      this.loadError = true;
    },
  }),
);

export default datasetStore;