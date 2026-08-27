import { slugify } from "../util";

export default {
  showCatalogs: 5,
  showCategories: 5,
  showCountries: 5,
  showHazards: 5,
  showLicenses: 5,
  showProjects: 5,
  showScales: 5,
  filters: {
    catalog: [],
    risk_data_type: [],
    geo_coverage: [],
    geo_scale: [],
    hazard_type: [],
    license_code: [],
    project: [],
  },

  getDatasetValues(dataset, filterType) {
    switch (filterType) {
      case "catalog":
        return (dataset.catalog || "Other")
          .toString()
          .split(",")
          .map((c) => c.trim())
          .filter((c) => c);
      case "risk_data_type":
        return Array.isArray(dataset.risk_data_type)
          ? dataset.risk_data_type
          : [dataset.risk_data_type];
      case "geo_coverage":
        return dataset.spatial?.countries || [];
      case "geo_scale":
        return dataset.spatial?.scale ? dataset.spatial?.scale.split(",") : [];
      case "hazard_type":
        if (!dataset.hazard) return [];
        return String(dataset.hazard.type || "")
          .split(",")
          .map((h) => h.trim())
          .filter((h) => h);
      case "license_code":
        return dataset.license ? dataset.license.split(",") : [];
      case "project":
        return dataset.project ? [dataset.project.name] : [];
    }
    return [];
  },

  toggleFilter(filterType, value) {
    const idx = this.filters[filterType].indexOf(value);
    idx === -1
      ? this.filters[filterType].push(value)
      : this.filters[filterType].splice(idx, 1);
  },

  isFilterActive(filterType, value) {
    return this.filters[filterType].includes(value);
  },

  clearFilters() {
    Object.keys(this.filters).forEach((k) => (this.filters[k] = []));
    this.updateUrlParams();
  },

  get activeFilterCount() {
    return Object.values(this.filters).reduce(
      (sum, arr) => sum + arr.length,
      0,
    );
  },

  get hasActiveFilters() {
    return this.activeFilterCount > 0;
  },

  get filteredResultsBeforeSearch() {
    return this.applyFilters();
  },

  getDatasetsForFilterOptions(excludeFilterType) {
    const searchResultDatasets = this.query.trim() ? this.display : this.all;
    return this.applyFiltersExcluding(excludeFilterType, searchResultDatasets);
  },

  applyFilters(datasets = null) {
    return this.applyFiltersExcluding(null, datasets);
  },

  applyFiltersExcluding(excludeFilterType = null, datasets = null) {
    const toFilter = datasets || this.all;
    const filterTypes = [
      "catalog",
      "risk_data_type",
      "geo_coverage",
      "geo_scale",
      "hazard_type",
      "license_code",
      "project",
    ];
    return toFilter.filter((dataset) =>
      filterTypes.every(
        (type) =>
          type === excludeFilterType ||
          this.datasetMatchesFilter(dataset, type),
      ),
    );
  },

  datasetMatchesFilter(dataset, filterType) {
    const values = this.filters[filterType];
    if (!values.length) return true;
    const datasetValues = this.getDatasetValues(dataset, filterType);
    if (
      ["geo_coverage", "geo_scale", "license_code", "project"].includes(
        filterType,
      )
    ) {
      const combinedSlug = slugify(datasetValues.join(","));
      return values.some((v) => combinedSlug.includes(v));
    }
    return datasetValues.some((v) => v && values.includes(slugify(v)));
  },

  async queryDatasetColumnOptions(queryOptions, retries = 5, delay = 1000) {
    const {
      column,
      filterType,
      joinedTable,
      primaryKeyColumn,
      foreignKeyColumn,
    } = queryOptions;
    if (this.db) {
      const requiresJoin = !!joinedTable;
      const result = requiresJoin
        ? this.queryDB(`
            SELECT ${joinedTable}.${column}, COUNT(*) as count
            FROM datasets
            LEFT JOIN ${joinedTable} ON datasets.${foreignKeyColumn} = ${joinedTable}.${primaryKeyColumn}
            GROUP BY ${joinedTable}.${column}
            ORDER BY ${joinedTable}.${column} ASC;
          `)
        : this.queryDB(
            `
          SELECT ${column}, COUNT(*) as count
          FROM datasets
          GROUP BY ${column}
          ORDER BY ${column} ASC;
        `,
          );
      console.log(result);
      const values = result[0].values.map(([value, count]) => {
        const { title, slug } = JSON.parse(value);

        return {
          title,
          slug,
          count,
          // selected: this.isFilterActive(filterType, slug),
        };
      });
      console.log(column, values);
      return values;
    } else {
      if (retries > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
        return this.queryDatasetColumnOptions(
          queryOptions,
          retries - 1,
          delay * 2,
        );
      } else {
        throw new Error("All retries failed");
      }
    }
  },
  getFilterOptions(filterType) {
    return []
  },

  async getFilterOptionsCatalog(retries = 5, delay = 1000) {
    if (this.db) {
      const result = this.queryDB(`
        SELECT catalogs.title, catalogs.slug, COUNT(*) as count
        FROM datasets
        LEFT JOIN catalogs ON datasets.catalog_slug = catalogs.slug
        GROUP BY catalogs.slug
        ORDER BY catalogs.title ASC;
      `);

      console.log(result);
      const values = result[0].values.map(([title, slug, count]) => {

        return {
          title,
          slug,
          count,
          selected: this.isFilterActive('catalog', slug),
        };
      });
      console.log(values);
      return values;
    } else {
      if (retries > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
        return this.getFilterOptionsCatalog(
          retries - 1,
          delay * 2,
        );
      } else {
        throw new Error("All retries failed");
      }
    }
  },
  // getFilterOptions(filterType, datasets) {
  //   const allValues = new Set();
  //   this.all.forEach((d) => {
  //     this.getDatasetValues(d, filterType).forEach(
  //       (v) => v && v !== "None" && allValues.add(v.trim()),
  //     );
  //   });
  //   const counts = {};
  //   datasets.forEach((d) => {
  //     this.getDatasetValues(d, filterType).forEach((v) => {
  //       if (v && v !== "None") counts[v.trim()] = (counts[v.trim()] || 0) + 1;
  //     });
  //   });
  //   return Array.from(allValues)
  //     .map((title) => ({
  //       title,
  //       slug: slugify(title),
  //       count: counts[title] || 0,
  //       selected: this.isFilterActive(filterType, slugify(title)),
  //     }))
  //     .sort((a, b) => {
  //       if (a.selected !== b.selected) return a.selected ? -1 : 1;
  //       if (
  //         filterType === "catalog" &&
  //         (a.title === "Other") !== (b.title === "Other")
  //       )
  //         return a.title === "Other" ? 1 : -1;
  //       else if (filterType === "geo_scale") {
  //         const order = ["global", "regional", "national", "sub-national"];
  //         return (
  //           order.indexOf(a.title.toLowerCase()) -
  //           order.indexOf(b.title.toLowerCase())
  //         );
  //       }
  //       return b.count - a.count || a.title.localeCompare(b.title);
  //     });
  // },
};
