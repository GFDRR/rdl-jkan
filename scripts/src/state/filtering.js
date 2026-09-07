import { slugify } from "../util";

export default {
  filters: {
    catalog: [],
    countries: [],
    risk_data_type: [],
    geo_scale: [],
    hazard_type: [],
    license: [],
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
      case "country":
        return dataset.spatial?.countries || [];
      case "geo_scale":
        return dataset.spatial?.scale ? dataset.spatial?.scale.split(",") : [];
      case "hazard_type":
        if (!dataset.hazard) return [];
        return String(dataset.hazard.type || "")
          .split(",")
          .map((h) => h.trim())
          .filter((h) => h);
      case "license":
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
    // this.updateUrlParams();
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
    this.display = this.applyFiltersExcluding(null, datasets);
    return this.display;
  },

  applyFiltersExcluding(excludeFilterType = null, datasets = null) {
    const toFilter = datasets || this.all;
    const filterTypes = [
      "catalog",
      "risk_data_type",
      "countries",
      "geo_scale",
      "hazard_type",
      "license",
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
      ["country", "geo_scale", "license", "project"].includes(
        filterType,
      )
    ) {
      const combinedSlug = slugify(datasetValues.join(","));
      return values.some((v) => combinedSlug.includes(v));
    }
    return datasetValues.some((v) => v && values.includes(slugify(v)));
  },

  getFilterOptions(filterType, retries = 5, delay = 1000) {
    return [];
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

      const values = result[0].values.map(([title, slug, count]) => {
        return {
          title,
          slug,
          count,
          selected: this.isFilterActive("catalog", slug),
        };
      });
      return values;
    } else {
      if (retries > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
        return this.getFilterOptionsCatalog(retries - 1, delay * 2);
      } else {
        throw new Error("All retries failed");
      }
    }
  },
  async getFilterOptionsCountries(retries = 5, delay = 1000) {
    if (this.db) {
      const result = this.queryDB(
        `
          SELECT spatial, COUNT(*) as count
          FROM datasets
          GROUP BY spatial
          ORDER BY spatial ASC;
        `,
      );
      const values = Object.values(result[0].values.reduce(
        (acc, [spatial_json, count]) => {
          const c_array = JSON.parse(spatial_json).countries;
          c_array.forEach(({ title, emoji, slug}) => {
            if (acc[slug]) acc[slug]['count'] += count;
            else acc[slug] = {
              emoji,
              title,
              slug,
              selected: this.isFilterActive("countries", slug),
              count,
            };
          });

          return acc;
        },
        {}
      ));
      return values;
    } else {
      if (retries > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
        return this.getFilterOptionsCountries(retries - 1, delay * 2);
      } else {
        throw new Error("All retries failed");
      }
    }
  },
    async getFilterOptionsGeoScale(retries = 5, delay = 1000) {
    if (this.db) {
      const result = this.queryDB(
        `
          SELECT spatial, COUNT(*) as count
          FROM datasets
          GROUP BY spatial
          ORDER BY spatial ASC;
        `,
      );
      const values = Object.values(result[0].values.reduce(
        (acc, [spatial_json, count]) => {
          const slug = JSON.parse(spatial_json).scale;
          
          if (acc[slug]) acc[slug]['count'] += count;
          else acc[slug] = {
            title:String(slug).charAt(0).toUpperCase() + String(slug).slice(1),
            slug,
            selected: this.isFilterActive("geo_scale", slug),
            count,
          };

          return acc;
        },
        {}
      ));
      return values;
    } else {
      if (retries > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
        return this.getFilterOptionsGeoScale(retries - 1, delay * 2);
      } else {
        throw new Error("All retries failed");
      }
    }
  },
  async getFilterOptionsHazardType(retries = 5, delay = 1000) {
    if (this.db) {
      const result = this.queryDB(
        `
          SELECT hazard, COUNT(*) as count
          FROM datasets
          WHERE hazard IS NOT NULL
          GROUP BY hazard
          ORDER BY hazard ASC;
          ;
        `,
      );
      const values = Object.values(result[0].values.reduce(
        (acc, [hazard_json, count]) => {
          const ht_array = hazard_json ? JSON.parse(hazard_json).type : [];
          ht_array.forEach((slug) => {
            if (acc[slug]) acc[slug]['count'] += count;
            else acc[slug] = {
              title:String(slug).charAt(0).toUpperCase() + String(slug).slice(1).replace('_', ' '),
              slug,
              selected: this.isFilterActive("hazard_type", slug),
              count,
            };
          });

          return acc;
        },
        {}
      ));
      return values;
    } else {
      if (retries > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
        return this.getFilterOptionsHazardType(retries - 1, delay * 2);
      } else {
        throw new Error("All retries failed");
      }
    }
  },
  async getFilterOptionsLicense(retries = 5, delay = 1000) {
    if (this.db) {
      const result = this.queryDB(`
        SELECT licenses.title, licenses.slug, COUNT(*) as count
        FROM datasets
        LEFT JOIN licenses ON datasets.license_slug = licenses.slug
        GROUP BY licenses.slug
        ORDER BY licenses.title ASC;
      `);
      const values = result[0].values.map(([title, slug, count]) => {
        return {
          title,
          slug,
          count,
          selected: this.isFilterActive("license", slug),
        };
      });
      return values;
    } else {
      if (retries > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
        return this.getFilterOptionsLicense(retries - 1, delay * 2);
      } else {
        throw new Error("All retries failed");
      }
    }
  },
  async getFilterOptionsProject(retries = 5, delay = 1000) {
    if (this.db) {
      const result = this.queryDB(
        `
          SELECT project, COUNT(*) as count
          FROM datasets
          GROUP BY project
          ORDER BY project ASC;
        `,
      );
      const values = result[0].values.map(([value, count]) => {
        const { title, slug } = JSON.parse(value);

        return {
          title,
          slug,
          count,
          selected: this.isFilterActive("project", slug),
        };
      });
      return values;
    } else {
      if (retries > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
        return this.getFilterOptionsProject(retries - 1, delay * 2);
      } else {
        throw new Error("All retries failed");
      }
    }
  },
  async getFilterOptionsRiskDataType(retries = 5, delay = 1000) {
    if (this.db) {
      const result = this.queryDB(
        `
          SELECT risk_data_type, COUNT(*) as count
          FROM datasets
          GROUP BY risk_data_type
          ORDER BY risk_data_type ASC;
        `,
      );
      const values = Object.values(result[0].values.reduce(
        (acc, [rdt_json, count]) => {
          const rdt_array = JSON.parse(rdt_json);
          rdt_array.forEach((slug) => {
            if (acc[slug]) acc[slug]['count'] += count;
            else acc[slug] = {
              title:String(slug).charAt(0).toUpperCase() + String(slug).slice(1),
              slug,
              selected: this.isFilterActive("risk_data_type", slug),
              count,
            };
          });

          return acc;
        },
        {}
      ));
      return values;
    } else {
      if (retries > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
        return this.getFilterOptionsRiskDataType(retries - 1, delay * 2);
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
