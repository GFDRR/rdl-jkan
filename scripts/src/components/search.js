  document.addEventListener('alpine:init', async () => {
    Alpine.store('datasets', {
      BASE_URL,
      unfiltered: [],
      isLoading: true,

      async fetchUnfiltered() {
        this.isLoading = true;
        try {
          // Now load sql.js
          const response = await fetch('/sqlite.db');
          const arrayBuffer = await response.arrayBuffer();
          const uint8Array = new Uint8Array(arrayBuffer);

          const SQL = await initSqlJs({
            locateFile: (file) => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.13.0/${file}`
          });
          
          this.db = new SQL.Database(uint8Array);
          const initialDatasets = this.db.exec("SELECT frontmatter FROM Datasets;")[0];
          console.log("✓ Database loaded", initialDatasets);
          this.unfiltered = initialDatasets.values.map(row => JSON.parse(row[0]));
        } catch (error) {
          console.error('Failed to fetch data:', error);
        } finally {
          this.isLoading = false;
        }
      },

      // Debounce utility function
      debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
          const later = () => {
            clearTimeout(timeout);
            func(...args);
          };
          clearTimeout(timeout);
          timeout = setTimeout(later, wait);
        };
      },

      // SQL-based keyword search using FTS5-like functionality
      async keywordSearch() {
        if (!this.db || !this.query.trim()) {
          this.filteredKeywordResults = [];
          this.filteredNonKeywordResults = [...this.unfiltered];
          return;
        }

        try {
          const lowerCaseQuery = this.query.toLowerCase();
          
          // Escape single quotes for SQL
          const escapedQuery = lowerCaseQuery.replace(/'/g, "''");
          
          // Search across multiple fields using SQL LIKE with OR conditions
          const searchFields = ['id', 'title', 'description', 'license', 'catalog', 'risk_data_type', 'slug'];
          const spatialFields = ["spatial->>'$.countries'", "spatial->>'$.scale'"];
          
          let whereConditions = [];
          
          // Add conditions for regular fields
          searchFields.forEach(field => {
            whereConditions.push(`LOWER(${field}) LIKE '%${escapedQuery}%'`);
          });
          
          // Add conditions for spatial fields (JSON extraction)
          spatialFields.forEach(field => {
            whereConditions.push(`${field} LIKE '%${escapedQuery}%'`);
          });
          
          const whereClause = whereConditions.join(' OR ');
          const sql = `SELECT frontmatter FROM Datasets WHERE ${whereClause}`;
          
          const results = this.db.exec(sql);
          
          if (results.length > 0) {
            const matchingFrontmatters = results[0].values.map(row => row[0]);
            this.filteredKeywordResults = matchingFrontmatters.map(frontmatter => JSON.parse(frontmatter));
          } else {
            this.filteredKeywordResults = [];
          }
          
          // Non-matches are everything except matches
          const matchedIds = new Set(this.filteredKeywordResults.map(d => d.dataset_id));
          this.filteredNonKeywordResults = this.unfiltered.filter(dataset => !matchedIds.has(dataset.dataset_id));
          
        } catch (error) {
          console.error('Search error:', error);
          // Fallback to client-side search if SQL fails
          this.fallbackKeywordSearch();
        }
      },

      // Fallback to original client-side search if SQL search fails
      fallbackKeywordSearch() {
        const lowerCaseQuery = this.query.toLowerCase();
        const keywordMatches = [];
        const nonMatches = [];
        
        for (const dataset of this.unfiltered) {
          let matchCount = 0;
          for (const key of this.SCORED_FIELDS) {
            if (dataset[key] && JSON.stringify(dataset[key]).toLowerCase().includes(lowerCaseQuery)) {
              matchCount++;
            }
          }
          
          if (matchCount > 0) {
            keywordMatches.push(dataset);
          } else {
            nonMatches.push(dataset);
          }
        }
        this.filteredKeywordResults = keywordMatches;
        this.filteredNonKeywordResults = nonMatches;
      },

      // Load filters and search from URL params
      loadFromUrlParams() {
        const urlParams = new URLSearchParams(window.location.search);

        // Load search query
        const searchQuery = urlParams.get('q') || '';

        // Load filter values for each filter type
        const filters = {};
        const filterTypes = ['catalog', 'risk_data_type', 'geo_coverage', 'geo_scale', 'hazard_type', 'license_code', 'project'];
        filterTypes.forEach(filterType => {
          const values = urlParams.getAll(filterType + '[]');
          if (values.length > 0) {
            filters[filterType] = values;
          }
        });

        return { searchQuery, filters };
      },

      // Update URL params based on current filters and search
      updateUrlParams(query = '', filters = {}) {
        const urlParams = new URLSearchParams();

        // Add search query if present
        if (query && query.trim()) {
          urlParams.set('q', query.trim());
        }

        // Add filter values
        Object.entries(filters).forEach(([filterType, values]) => {
          values.forEach(value => {
            urlParams.append(filterType + '[]', value);
          });
        });

        // Update URL without reloading page
        const newUrl = window.location.pathname + (urlParams.toString() ? '?' + urlParams.toString() : '');
        window.history.replaceState({}, '', newUrl);
      },
  })
  await Alpine.store('datasets').fetchUnfiltered()
})