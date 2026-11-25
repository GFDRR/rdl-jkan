// Alpine components of the dataset page.
import { plural } from "./labels.js";
import { filterEntries, PAGE_SIZE } from "./table.js";

export const datasetTable = (table) => ({
  table,
  query: "",
  filters: {},
  sort: null,
  descending: false,
  all: false,
  pageSize: PAGE_SIZE,

  get found() {
    return filterEntries(this.table.entries, this);
  },

  get visible() {
    return this.all ? this.found : this.found.slice(0, PAGE_SIZE);
  },

  get filtered() {
    return this.found.length < this.table.total;
  },

  get status() {
    const { length } = this.found;
    const shown =
      this.visible.length < length
        ? `Showing ${this.visible.length} of ${length.toLocaleString("en")}`
        : plural(length, ...this.table.noun);
    return this.filtered
      ? `${shown} (${this.table.total.toLocaleString("en")} in total)`
      : shown;
  },

  sortBy(id) {
    this.descending = this.sort === id && !this.descending;
    this.sort = id;
  },

  ariaSort(id) {
    if (this.sort !== id) return "none";
    return this.descending ? "descending" : "ascending";
  },

  // Filters by these values, or no longer when it already does.
  toggle(values) {
    const on = this.isOn(values);
    for (const [id, value] of Object.entries(values)) {
      this.filters[id] = on ? "" : value;
    }
  },

  isOn(values) {
    return Object.entries(values).every(
      ([id, value]) => this.filters[id] === value,
    );
  },

  clear() {
    this.query = "";
    this.filters = {};
  },
});

// Marks the section in view in the index of the page.
export const sectionIndex = () => ({
  current: null,

  init() {
    this.mark();
    // A link to a section: the section was not there when the page opened.
    this.$nextTick(() => {
      const { hash } = window.location;
      if (hash.length > 1) {
        document.getElementById(hash.slice(1))?.scrollIntoView();
      }
    });
  },

  mark() {
    const sections = [...document.querySelectorAll(".ds-section")];
    const passed = sections.filter(
      (section) => section.getBoundingClientRect().top < 140,
    );
    const current = (passed.pop() ?? sections[0])?.id ?? null;
    if (current === this.current) return;
    this.current = current;
    // On narrow pages the index scrolls sideways.
    this.$nextTick(() => {
      const links = this.$root.querySelector(".ds-index-links");
      const link = links?.querySelector('[aria-current="true"]');
      if (link) links.scrollLeft = link.offsetLeft - links.offsetLeft - 16;
    });
  },
});

// The spatial extent: the bounding box or else the countries of the dataset.
export function drawMap(element, spatial, baseUrl = "") {
  const map = window.L.map(element, {
    zoomControl: false,
    dragging: false,
    scrollWheelZoom: false,
    doubleClickZoom: false,
    boxZoom: false,
    keyboard: false,
    tap: false,
    touchZoom: false,
    attributionControl: true,
  });
  window.L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '<a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> and <a href="https://www.geoboundaries.org/">GeoBoundaries</a>',
  }).addTo(map);

  const extent = window.L.featureGroup().addTo(map);
  const fit = () => {
    if (extent.getLayers().length > 0) {
      map.fitBounds(extent.getBounds(), { animate: false });
    } else {
      map.setView([20, 0], 1, { animate: false });
    }
  };
  // The map changes size with the layout of the page.
  new ResizeObserver(() => {
    map.invalidateSize({ animate: false });
    // Leave the room of a small map to what it shows.
    map.attributionControl.setPrefix(
      element.clientWidth < 200
        ? false
        : window.L.Control.Attribution.prototype.options.prefix,
    );
    fit();
  }).observe(element);
  fit();

  if (spatial?.scale?.toLowerCase() === "global") return;
  if (spatial?.bbox) {
    const [minLon, minLat, maxLon, maxLat] = spatial.bbox;
    window.L.rectangle([
      [minLat, minLon],
      [maxLat, maxLon],
    ]).addTo(extent);
    fit();
    return;
  }
  const codes = (spatial?.countries ?? [])
    .map(({ slug }) => slug?.toUpperCase())
    .filter(Boolean);
  Promise.all(
    codes.map((code) =>
      fetch(`${baseUrl}/country_geojson/${code}.geojson`)
        .then((response) => response.json())
        .then((data) => window.L.geoJSON(data).addTo(extent))
        .catch((error) => console.error("Error loading GeoJSON:", error)),
    ),
  ).then(fit);
}
