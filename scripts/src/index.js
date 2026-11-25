import Alpine from "alpinejs";
import persist from "@alpinejs/persist";

import datasetStore from "./dataset";
import datasetsStore from "./datasets";
import { rememberInitialData } from "./shared/api.js";

const initialData = document.getElementById("initial-data");
if (initialData) rememberInitialData(JSON.parse(initialData.textContent));

window.Alpine = Alpine;
Alpine.plugin(persist);

Alpine.store("dataset", datasetStore);
Alpine.store("datasets", datasetsStore);

Alpine.start();
