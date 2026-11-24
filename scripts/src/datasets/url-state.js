import { FILTER_TYPES } from "./filtering";

// Keeps the search, filters and page in the address bar, so that a result list
// can be linked to: /?q=flood+kenya&catalog[]=zenodo&page=2
export default {
  read(store) {
    const params = new URLSearchParams(window.location.search);
    // Set behind the setter, which would start a search of its own.
    store._query = params.get("q") ?? "";
    for (const type of FILTER_TYPES) {
      store.filters[type] = [
        ...new Set([...params.getAll(`${type}[]`), ...params.getAll(type)]),
      ].filter(Boolean);
    }
    const page = Number.parseInt(params.get("page"), 10);
    store.currentPage = page > 0 ? page : 1;
  },

  write(store) {
    const params = new URLSearchParams();
    const q = store.query.trim();
    if (q) params.set("q", q);
    for (const type of FILTER_TYPES) {
      for (const value of store.filters[type]) params.append(`${type}[]`, value);
    }
    if (store.currentPage > 1) params.set("page", store.currentPage);

    const search = params.toString();
    const url = `${window.location.pathname}${search ? `?${search}` : ""}${window.location.hash}`;
    window.history.replaceState(window.history.state, "", url);
  },
};
