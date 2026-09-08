import { queryDB } from "../shared/utils.js";

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

  getWhereSqlForFilters(excludeFilterType = null) {
    // Count only non-excluded filters that have values
    const filtersSetCount =
      (this.filters.catalog.length > 0 && excludeFilterType !== "catalog"
        ? 1
        : 0) +
      (this.filters.countries.length > 0 && excludeFilterType !== "countries"
        ? 1
        : 0) +
      (this.filters.geo_scale.length > 0 && excludeFilterType !== "geo_scale"
        ? 1
        : 0) +
      (this.filters.project.length > 0 && excludeFilterType !== "project"
        ? 1
        : 0) +
      (this.filters.risk_data_type.length > 0 &&
      excludeFilterType !== "risk_data_type"
        ? 1
        : 0) +
      (this.filters.hazard_type.length > 0 &&
      excludeFilterType !== "hazard_type"
        ? 1
        : 0) +
      (this.filters.license.length > 0 && excludeFilterType !== "license"
        ? 1
        : 0);

    let whereSql = filtersSetCount > 0 ? "WHERE " : "";
    let filtersAppliedCount = 0;

    if (this.filters.catalog.length && excludeFilterType !== "catalog") {
      if (this.filters.catalog.length > 1) whereSql += "(";
      filtersAppliedCount++;
      this.filters.catalog.forEach((c, index) => {
        whereSql += `catalog_slug = '${c}' ${index < this.filters.catalog.length - 1 ? "OR" : ""} `;
      });
      if (this.filters.catalog.length > 1) whereSql += ")";
      if (filtersAppliedCount < filtersSetCount) whereSql += " AND ";
    }
    if (this.filters.countries.length && excludeFilterType !== "countries") {
      if (this.filters.countries.length > 1) whereSql += "(";
      filtersAppliedCount++;
      this.filters.countries.forEach((c, index) => {
        whereSql += `json_extract(spatial, '$.countries') LIKE '%${c}%' ${index < this.filters.countries.length - 1 ? "OR" : ""} `;
      });
      if (this.filters.countries.length > 1) whereSql += ")";
      if (filtersAppliedCount < filtersSetCount) whereSql += " AND ";
    }
    if (this.filters.geo_scale.length && excludeFilterType !== "geo_scale") {
      if (this.filters.geo_scale.length > 1) whereSql += "(";
      filtersAppliedCount++;
      this.filters.geo_scale.forEach((s, index) => {
        whereSql += `json_extract(spatial, '$.scale') LIKE '%${s}%' ${index < this.filters.geo_scale.length - 1 ? "OR" : ""} `;
      });
      if (this.filters.geo_scale.length > 1) whereSql += ")";
      if (filtersAppliedCount < filtersSetCount) whereSql += " AND ";
    }
    if (this.filters.project.length && excludeFilterType !== "project") {
      if (this.filters.project.length > 1) whereSql += "(";
      filtersAppliedCount++;
      this.filters.project.forEach((p, index) => {
        whereSql += `json_extract(project, '$') LIKE '%${p}%' ${index < this.filters.project.length - 1 ? "OR" : ""} `;
      });
      if (this.filters.project.length > 1) whereSql += ")";
      if (filtersAppliedCount < filtersSetCount) whereSql += " AND ";
    }
    if (
      this.filters.risk_data_type.length &&
      excludeFilterType !== "risk_data_type"
    ) {
      if (this.filters.risk_data_type.length > 1) whereSql += "(";
      filtersAppliedCount++;
      this.filters.risk_data_type.forEach((rdt, index) => {
        whereSql += `json_extract(risk_data_type, '$') LIKE '%${rdt}%' ${index < this.filters.risk_data_type.length - 1 ? "OR" : ""} `;
      });
      if (this.filters.risk_data_type.length > 1) whereSql += ")";
      if (filtersAppliedCount < filtersSetCount) whereSql += " AND ";
    }
    if (
      this.filters.hazard_type.length > 0 &&
      excludeFilterType !== "hazard_type"
    ) {
      whereSql += "(";
      if (this.filters.hazard_type.length > 1) whereSql += "(";
      filtersAppliedCount++;
      this.filters.hazard_type.forEach((ht, index) => {
        whereSql += `json_extract(hazard, '$.type') LIKE '%${ht}%' ${index < this.filters.hazard_type.length - 1 ? "OR" : ""} `;
      });
      whereSql += "AND hazard IS NOT NULL)";
      if (this.filters.hazard_type.length > 1) whereSql += ")";
      if (filtersAppliedCount < filtersSetCount) whereSql += " AND ";
    }
    if (this.filters.license.length && excludeFilterType !== "license") {
      if (this.filters.license.length > 1) whereSql += "(";
      filtersAppliedCount++;
      this.filters.license.forEach((l, index) => {
        whereSql += `license_slug = '${l}' ${index < this.filters.license.length - 1 ? "OR" : ""} `;
      });
      if (this.filters.license.length > 1) whereSql += ")";
      if (filtersAppliedCount < filtersSetCount) whereSql += " AND ";
    }
    return whereSql;
  },

  async getFilterOptionsCatalog(retries = 5, delay = 1000) {
    if (this.db) {
      const result = queryDB(
        this.db,
        `
        SELECT catalogs.title, catalogs.slug, COUNT(*) as count
        FROM datasets
        LEFT JOIN catalogs ON datasets.catalog_slug = catalogs.slug
        ${this.getWhereSqlForFilters("catalog")}
        GROUP BY catalogs.slug
        ORDER BY count DESC;
      `,
      );

      const values = result[0].values.map(([title, slug, count]) => {
        return {
          title,
          slug,
          count,
          selected: this.isFilterActive("catalog", slug),
        };
      });

      const filtered = values.filter((v) => !v.selected);
      const others = values.filter((v) => v.selected && v.title === "Unknown");
      return [...others, ...filtered];
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
      const result = queryDB(
        this.db,
        `
          SELECT spatial, COUNT(*) as count
          FROM datasets
          ${this.getWhereSqlForFilters("countries")}
          GROUP BY spatial
          ORDER BY count DESC;
        `,
      );
      const values = Object.values(
        result[0].values.reduce((acc, [spatial_json, count]) => {
          const c_array = JSON.parse(spatial_json).countries;
          c_array.forEach(({ title, emoji, slug }) => {
            if (acc[slug]) acc[slug]["count"] += count;
            else
              acc[slug] = {
                emoji,
                title,
                slug,
                selected: this.isFilterActive("countries", slug),
                count,
              };
          });

          return acc;
        }, {}),
      );

      const selected = values.filter((v) => v.selected);
      const unselected = values.filter((v) => !v.selected);
      return [
        ...selected.sort((a, b) => a.title.localeCompare(b.title)),
        ...unselected.sort((a, b) => a.title.localeCompare(b.title)),
      ];
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
      const result = queryDB(
        this.db,
        `
          SELECT spatial, COUNT(*) as count
          FROM datasets
          ${this.getWhereSqlForFilters("geo_scale")}
          GROUP BY spatial
          ORDER BY count DESC;
        `,
      );
      const values = Object.values(
        result[0].values.reduce((acc, [spatial_json, count]) => {
          const slug = JSON.parse(spatial_json).scale;

          if (acc[slug]) acc[slug]["count"] += count;
          else
            acc[slug] = {
              title:
                String(slug).charAt(0).toUpperCase() + String(slug).slice(1),
              slug,
              selected: this.isFilterActive("geo_scale", slug),
              count,
            };

          return acc;
        }, {}),
      );

      const geoOrder = ["global", "regional", "national", "sub-national"];
      const selected = values.filter((v) => v.selected);
      const unselected = values.filter((v) => !v.selected);
      const sortByGeo = (arr) =>
        arr.sort((a, b) => {
          const aIdx = geoOrder.indexOf(a.title.toLowerCase());
          const bIdx = geoOrder.indexOf(b.title.toLowerCase());
          if (aIdx === -1 && bIdx === -1) return a.title.localeCompare(b.title);
          if (aIdx === -1) return 1;
          if (bIdx === -1) return -1;
          return aIdx - bIdx;
        });
      return [...sortByGeo(selected), ...sortByGeo(unselected)];
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
      const whereSql = this.getWhereSqlForFilters("hazard_type");
      const result = queryDB(
        this.db,
        `
          SELECT hazard, COUNT(*) as count
          FROM datasets
          ${whereSql.length > 6 ? whereSql : " "}
          GROUP BY hazard
          ORDER BY count DESC;
        `,
      );
      const values = Object.values(
        result[0].values.reduce((acc, [hazard_json, count]) => {
          const ht_array = hazard_json ? JSON.parse(hazard_json).type : [];
          ht_array.forEach((slug) => {
            if (acc[slug]) acc[slug]["count"] += count;
            else
              acc[slug] = {
                title:
                  String(slug).charAt(0).toUpperCase() +
                  String(slug).slice(1).replace("_", " "),
                slug,
                selected: this.isFilterActive("hazard_type", slug),
                count,
              };
          });

          return acc;
        }, {}),
      );

      const selected = values.filter((v) => v.selected);
      const unselected = values.filter((v) => !v.selected);
      return [
        ...selected.sort((a, b) => a.title.localeCompare(b.title)),
        ...unselected.sort((a, b) => a.title.localeCompare(b.title)),
      ];
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
      const result = queryDB(
        this.db,
        `
        SELECT licenses.title, licenses.slug, COUNT(*) as count
        FROM datasets
        LEFT JOIN licenses ON datasets.license_slug = licenses.slug
        ${this.getWhereSqlForFilters("license")}
        GROUP BY licenses.slug
        ORDER BY count DESC;
      `,
      );
      const values = result[0].values.map(([title, slug, count]) => {
        return {
          title,
          slug,
          count,
          selected: this.isFilterActive("license", slug),
        };
      });

      const selected = values.filter((v) => v.selected);
      const unselected = values.filter((v) => !v.selected);
      return [
        ...selected.sort((a, b) => a.title.localeCompare(b.title)),
        ...unselected.sort((a, b) => a.title.localeCompare(b.title)),
      ];
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
      const result = queryDB(
        this.db,
        `
          SELECT project, COUNT(*) as count
          FROM datasets
          ${this.getWhereSqlForFilters("project")}
          GROUP BY project
          ORDER BY count DESC;
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

      const selected = values.filter((v) => v.selected);
      const unselected = values.filter((v) => !v.selected);
      return [
        ...selected.sort((a, b) => a.title.localeCompare(b.title)),
        ...unselected.sort((a, b) => a.title.localeCompare(b.title)),
      ];
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
      const whereSql = this.getWhereSqlForFilters("risk_data_type");
      const result = queryDB(
        this.db,
        `
          SELECT risk_data_type, COUNT(*) as count
          FROM datasets
          ${whereSql.length > 6 ? whereSql : " "}
          GROUP BY risk_data_type
          ORDER BY count DESC;
        `,
      );
      const values = Object.values(
        result[0].values.reduce((acc, [rdt_json, count]) => {
          const rdt_array = JSON.parse(rdt_json);
          rdt_array.forEach((slug) => {
            if (acc[slug]) acc[slug]["count"] += count;
            else
              acc[slug] = {
                title:
                  String(slug).charAt(0).toUpperCase() + String(slug).slice(1),
                slug,
                selected: this.isFilterActive("risk_data_type", slug),
                count,
              };
          });

          return acc;
        }, {}),
      );
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
