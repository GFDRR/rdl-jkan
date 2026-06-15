---
attributions:
- entity:
    affiliation: null
    email: null
    name: Pacific Community Statistics for Development Division (SPC SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-new-cale
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-new-cale
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-new-cale
dataset_id: rdls_exp-ncl_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-new-cale]'
details: null
exposure:
- asset_type:
    description: Population counts by district and coastal proximity buffers (1km,
      5km, 10km from coastline)
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
  description: Census population counts were spatially intersected with district administrative
    boundaries and coastal buffer zones (1km, 5km, 10km) derived from coastline data
    to quantify populations at varying distances from the coast. The dataset supports
    analysis of coastal population exposure in Pacific Island territories.
  sources:
  - id: source_1
    license: null
    name: Pacific Community Statistics for Development Division (SPC SDD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-new-cale
  rel: source
loss:
  losses: []
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
    Territories - Dataset - New Caledonia (NCL district boundaries)
  download_url: https://pacificdata.org/data/dataset/08645cda-22d6-4edb-9afd-fbe519504e58/resource/b7e8a7b9-d818-43a6-82b2-4593cd75f794/download/ncl_dist_4326.geojson
  format: null
  id: resource_c5359f5d
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NCL district boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - New Caledonia (NCL 1km coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/08645cda-22d6-4edb-9afd-fbe519504e58/resource/414a0c57-d3f8-473a-bedd-2863154712b6/download/ncl1kmbuff_4326.geojson
  format: null
  id: resource_4d1c5a57
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NCL 1km coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - New Caledonia (NCL 5km coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/08645cda-22d6-4edb-9afd-fbe519504e58/resource/aa16d0e1-2d06-4944-8aef-1aaf44d1ba29/download/ncl5kmbuff_4326.geojson
  format: null
  id: resource_2eb6edf9
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NCL 5km coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - New Caledonia (NCL 10km coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/08645cda-22d6-4edb-9afd-fbe519504e58/resource/75499dad-e962-4beb-bf51-5d2fcbaeff11/download/ncl10kmbuff_4326.geojson
  format: null
  id: resource_8d43c10d
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NCL 10km coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - New Caledonia (NCL README)
  download_url: https://pacificdata.org/data/dataset/08645cda-22d6-4edb-9afd-fbe519504e58/resource/9621a3d1-00a2-4f98-aaae-973e4ef84be1/download/readme.txt
  format: null
  id: resource_0d7b739e
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NCL README
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ncl_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - NCL
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
  - Dataset - New Caledonia
version: null
vulnerability: null
---
