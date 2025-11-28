/**
 * Usage:
 * <div data-component="rdl-datasets-list">
 *   <h3 class="datasets-count" data-hook="datasets-count"></h3>
 *   <input type="text" data-hook="search-query" placeholder="Search..." class="form-control">
 *   <div data-hook="datasets-items"></div>
 * </div>
 *
 * Optionally, add filters to the component element such as
 *   data-organization="sample-department"
 *   data-category="education"
 */

// Comment for rdl-dataset.json:
// need to loop over each dataset entry and only include fields if it exists in the .md file...
// the contents then get displayed by rdl-datasets-items

import { pick, defaults, filter } from "lodash";
import { pipeline } from "@xenova/transformers";

import TmplDatasetItem from "../templates/rdl-datasets-item";
import { queryByHook, setContent, createDatasetFilters } from "../util";

export default class {
  constructor(opts) {
    this.vectors = {}; // Store pre-generated vectors
    this.model = null; // Store transformer model

    const elements = {
      datasetsItems: queryByHook("rdl-datasets-items", opts.el),
      datasetsCount: queryByHook("rdl-datasets-count", opts.el),
      searchQuery: queryByHook("search-query", opts.el),
    };

    // Load the semantic model and vectors
    Promise.all([this.loadModel(), this.loadVectors()])
      .then(() => {
        this.initializeDatasets(opts, elements);
      })
      .catch((err) => console.error("Error loading model/vectors:", err));

    // Attach search listener
    elements.searchQuery.on("keyup", (e) => {
      const query = e.currentTarget.value;
      this.handleSearch(query, opts.datasets, elements);
    });
  }

  async loadModel() {
    try {
      this.model = await pipeline(
        "feature-extraction",
        "Xenova/all-MiniLM-L6-v2"
      );
    } catch (error) {
      console.error("Failed to load model:", error);
      throw error;
    }
  }

  async loadVectors() {
    try {
      const response = await fetch("../../../vectors.json");
      const vectorsArray = await response.json();
      this.vectors = vectorsArray.reduce((acc, item) => {
        if (item.metadata && item.metadata.dataset_id) {
          acc[item.metadata.dataset_id] = item.vector;
        }
        return acc;
      }, {});
      console.log("Vectors loaded:", Object.keys(this.vectors).length);
    } catch (error) {
      console.error("Failed to load vector:", error);
      throw error;
    }
  }

  initializeDatasets(opts, elements) {
    const paramFilters = pick(opts.params, [
      "category",
      "geo_coverage",
      "geo_scale",
      "license_display",
      "project",
      "hazard_type",
    ]);
    const attributeFilters = pick(opts.el.data(), [
      "category",
      "geo_coverage",
      "geo_scale",
      "license_display",
      "project",
      "hazard_type",
    ]);
    const filters = createDatasetFilters(
      defaults(paramFilters, attributeFilters)
    );

    this.filteredDatasets = filter(opts.datasets, filters);
    this.renderDatasets(this.filteredDatasets, elements);

    const datasetSuffix = this.filteredDatasets.length > 1 ? "s" : "";
    const datasetsCountMarkup =
      this.filteredDatasets.length + " dataset" + datasetSuffix;
    setContent(elements.datasetsCount, datasetsCountMarkup);
  }

  async handleSearch(query, datasets, elements) {
    // First check for semantic search using model embedding
    const semanticResults = await this.semanticSearch(query, datasets);
    console.log("Semantic Results:", semanticResults);
    if (semanticResults.length > 0) {
      this.renderDatasets(semanticResults, elements);
      const resultsCountMarkup = semanticResults.length + " datasets";
      setContent(elements.datasetsCount, resultsCountMarkup);
    } else {
      // Fallback to keyword search if no semantic results
      const results = this._createSearchFunction(datasets)(query);
      this.renderDatasets(results, elements);
      const resultsCountMarkup = results.length + " datasets";
      setContent(elements.datasetsCount, resultsCountMarkup);
    }
  }

  async semanticSearch(query, datasets) {
    const queryVector = await this.vectorizeQuery(query);
    const results = [];

    for (const dataset of datasets) {
      // Look up vector using dataset_id
      const datasetVector = this.vectors[dataset.dataset_id];

      if (!datasetVector) {
        console.warn(`No vector found for dataset ${dataset.dataset_id}`);
        continue;
      }

      const similarity = this.cosineSimilarity(queryVector, datasetVector);
      results.push({ dataset, similarity });
    }

    // Sort by similarity in descending order
    results.sort((a, b) => b.similarity - a.similarity);
    console.log("Semantic Results:", results);
    // Return just the datasets
    return results.map((result) => result.dataset);
  }

  async vectorizeQuery(query) {
    // Get embeddings for the query using the model
    const result = await this.model([query.trim()], {
      pooling: "mean",
      normalize: true,
    });
    return Array.from(result.data);
  }

  cosineSimilarity(vecA, vecB) {
    const dotProduct = vecA.reduce((sum, val, i) => sum + val * vecB[i], 0);
    const magnitudeA = Math.sqrt(vecA.reduce((sum, val) => sum + val * val, 0));
    const magnitudeB = Math.sqrt(vecB.reduce((sum, val) => sum + val * val, 0));
    return dotProduct / (magnitudeA * magnitudeB);
  }

  renderDatasets(datasets, elements) {
    const datasetsMarkup = datasets.map(TmplDatasetItem);
    setContent(elements.datasetsItems, datasetsMarkup);
  }

  // Returns a function that can be used to search an array of datasets
  // The function returns the filtered array of datasets
  _createSearchFunction(datasets) {
    const keys = ["title", "notes", "description", "license"];
    return function (query) {
      const lowerCaseQuery = query.toLowerCase();
      return filter(datasets, function (dataset) {
        return keys.reduce(function (previousValue, key) {
          return (
            previousValue ||
            (dataset[key] &&
              dataset[key].toLowerCase().indexOf(lowerCaseQuery) !== -1)
          );
        }, false);
      });
    };
  }
}
