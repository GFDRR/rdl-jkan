import "core-js/actual";
import $ from "jquery";
import "bootstrap/js/dist/collapse";
import Alpine from "alpinejs";
import persist from "@alpinejs/persist";

import database from "./state/db";
import filtering from "./state/filtering";
import pagination from "./state/pagination";
import search from "./state/search";
import ui from "./state/ui";
import { queryByComponent } from "./util";

const urlSearchParams = new URLSearchParams(window.location.search);
const params = {};
urlSearchParams.forEach((value, key) => {
  params[key] = value;
});

window.Alpine = Alpine;
Alpine.plugin(persist);

const indexStore = {
  all: [],
  display: [],
};

// defineProperties to preserve getters, keeping `this` bound to the store
Object.defineProperties(
  indexStore,
  Object.getOwnPropertyDescriptors(database),
);
Object.defineProperties(
  indexStore,
  Object.getOwnPropertyDescriptors(pagination),
);
Object.defineProperties(
  indexStore,
  Object.getOwnPropertyDescriptors(filtering),
);
Object.defineProperties(indexStore, Object.getOwnPropertyDescriptors(search));
Object.defineProperties(indexStore, Object.getOwnPropertyDescriptors(ui));

Alpine.store("index", indexStore);

Alpine.start();
