import "core-js/actual";
import "bootstrap/js/dist/collapse";
import Alpine from "alpinejs";
import persist from "@alpinejs/persist";

import datasetStore from "./dataset";
import { datasetTable, sectionIndex } from "./dataset/components.js";
import datasetsStore from "./datasets";

window.Alpine = Alpine;
Alpine.plugin(persist);

Alpine.data("datasetTable", datasetTable);
Alpine.data("sectionIndex", sectionIndex);

Alpine.store("dataset", datasetStore);
Alpine.store("datasets", datasetsStore);

Alpine.start();
