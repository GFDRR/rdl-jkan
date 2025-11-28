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

import { pick, defaults, filter, partition } from "lodash";
import { pipeline } from "@xenova/transformers";

import ResultsHeader from "../templates/results-header";
import TmplDatasetItem from "../templates/rdl-datasets-item";
import { queryByHook, setContent, createDatasetFilters } from "../util";

const PATH_TO_VECTORS = "../../../search/vectors.json";

export default class {
  constructor(opts) {
    this.vectors = {}; // Store pre-generated vectors
    this.model = null; // Store transformer model

    const elements = {
      keywordResultsHeader: queryByHook("keyword-results-header", opts.el),
      datasetsItems: queryByHook("rdl-datasets-items", opts.el),
      searchQuery: queryByHook("search-query", opts.el),
      semanticResultsHeader: queryByHook("semantic-results-header", opts.el),
      semanticDatasetsItems: queryByHook("rdl-semantic-datasets-items", opts.el),
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
      const response = await fetch(PATH_TO_VECTORS);
      const vectorsArray = await response.json();
      this.vectors = vectorsArray.reduce((acc, item) => {
        if (item.metadata && item.metadata.dataset_id) {
          acc[item.metadata.dataset_id] = item.vector;
        }
        return acc;
      }, {});
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
    const filteredDatasets = filter(opts.datasets, filters);
    const datasetsMarkup = filteredDatasets.map(TmplDatasetItem);
    setContent(elements.keywordResultsHeader, ResultsHeader({
      count: filteredDatasets.length
    }));
    setContent(elements.datasetsItems, datasetsMarkup);
  }

  async handleSearch(query, datasets, elements) {
    const datasetsNotInKeywordResults = this.keywordSearch(query, datasets, elements);
    await this.semanticSearch(query, datasetsNotInKeywordResults, elements);
  }

  keywordSearch(query, datasets, elements) {
    const { matches, others } = this._createSearchFunction(datasets)(query);
    const datasetsMarkup = matches.map(TmplDatasetItem);
    setContent(elements.datasetsItems, datasetsMarkup);
    setContent(elements.keywordResultsHeader, ResultsHeader({
      type: "keyword",
      count: matches.length
    }));
    return others;
  }

  async semanticSearch(query, datasets, elements, n = 10) {
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

    const topNResults = results.sort((a, b) => b.similarity - a.similarity).slice(0, n);
    const semanticResults = topNResults.map((result) => result.dataset);
    const datasetsMarkup = semanticResults.map(TmplDatasetItem);
    setContent(elements.semanticDatasetsItems, datasetsMarkup);
    setContent(elements.semanticResultsHeader, ResultsHeader({
      type: "semantic",
      count: semanticResults.length
    }));
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

  // Returns a function that can be used to search an array of datasets
  // The function returns the filtered array of datasets
  _createSearchFunction(datasets) {
    const keys = ["title", "notes", "description", "license"];
    return function (query) {
      const lowerCaseQuery = query.toLowerCase();
      const [matches, others] = partition(datasets, function (dataset) {
        return keys.reduce(function (previousValue, key) {
          return (
            previousValue ||
            (dataset[key] &&
              dataset[key].toLowerCase().indexOf(lowerCaseQuery) !== -1)
          );
        }, false);
      });
      return { matches, others };
    };
  }
}
