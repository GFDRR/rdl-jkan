import "core-js/actual";
import "bootstrap/js/dist/collapse";
import Alpine from "alpinejs";
import persist from "@alpinejs/persist";

import datasetStore from "./dataset";
import datasetsStore from "./datasets";

const urlSearchParams = new URLSearchParams(window.location.search);
const params = {};
urlSearchParams.forEach((value, key) => {
  params[key] = value;
});

window.Alpine = Alpine;
Alpine.plugin(persist);

Alpine.store("dataset", datasetStore);
Alpine.store("datasets", datasetsStore);

Alpine.start();
