import Alpine from "alpinejs";
import persist from "@alpinejs/persist";

import datasetStore from "./dataset";
import { datasetTable, sectionIndex } from "./dataset/components.js";
import datasetsStore from "./datasets";
import { rememberInitialData } from "./shared/api.js";

const initialData = document.getElementById("initial-data");
if (initialData) rememberInitialData(JSON.parse(initialData.textContent));

window.Alpine = Alpine;
Alpine.plugin(persist);

Alpine.data("datasetTable", datasetTable);
Alpine.data("sectionIndex", sectionIndex);

Alpine.store("dataset", datasetStore);
Alpine.store("datasets", datasetsStore);

Alpine.start();
