---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pacific Community Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-papua-ne
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-papua-ne
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-papua-ne
dataset_id: rdls_exp-png_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-papua-ne]'
details: null
exposure:
- asset_type:
    description: Population counts within coastal buffer zones (1km, 5km, 10km) in
      Papua New Guinea Local Level Government areas
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Census population data from Papua New Guinea was spatially intersected
    with coastal buffer zones at 1km, 5km, and 10km distances from the coastline to
    quantify populations in coastal proximity. Administrative boundaries (LLG) and
    derived buffer geometries were used to aggregate population counts by coastal
    distance bands for risk assessment purposes.
  sources:
  - id: source_1
    license: null
    name: Pacific Community Statistics for Development Division (SDD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-papua-ne
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Papua New Guinea (PNG LLG boundaries)
  download_url: https://pacificdata.org/data/dataset/b560e439-ceb5-4365-986d-2ce73e3b2ea1/resource/eb4967dc-981c-49ab-82a3-c0e60f42938a/download/llg_4326.geojson
  format: null
  id: resource_c7f673d7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PNG LLG boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Papua New Guinea (PNG 1km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/b560e439-ceb5-4365-986d-2ce73e3b2ea1/resource/4694d309-f335-4da1-b12b-3713bb86fa2b/download/buf1km_dis_4326.geojson
  format: null
  id: resource_6d839b64
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PNG 1km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Papua New Guinea (PNG 5km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/b560e439-ceb5-4365-986d-2ce73e3b2ea1/resource/ae35d416-2558-446f-a707-aa2e3bbba660/download/buf5km_dis_4326.geojson
  format: null
  id: resource_cfc8d54e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PNG 5km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Papua New Guinea (PNG 10km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/b560e439-ceb5-4365-986d-2ce73e3b2ea1/resource/871cb004-b2be-45a0-bfb2-ff3416b9296c/download/buf10km_dis_4326.geojson
  format: null
  id: resource_5fbe9095
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PNG 10km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Papua New Guinea (PNG README)
  download_url: https://pacificdata.org/data/dataset/b560e439-ceb5-4365-986d-2ce73e3b2ea1/resource/8395be7b-68dc-4462-ba84-2276b9aee6c2/download/readme.txt
  format: null
  id: resource_5724909d
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PNG README
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-png_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - PNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-09-30'
temporal_resolution: null
title: Coastal proximity of populations in 22 Pacific Island Countries and Territories
  - Dataset - Papua New Guinea
version: null
vulnerability: null
---
