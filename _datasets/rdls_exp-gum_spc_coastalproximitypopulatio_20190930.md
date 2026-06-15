---
attributions:
- entity:
    affiliation: null
    email: null
    name: SPC Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-guam
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-guam
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-guam
dataset_id: rdls_exp-gum_spc_coastalproximitypopulatio_20190930
description: 'Spatial datasets utilized to conduct the spatial analysis and additional
  information from the research article: Coastal proximity of populations in 22 Pacific
  Island Countries and Territories. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0223249
  https://sdd.spc.int/mapping-coastal Access this dataset from the Pacific Data Hub.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-guam]'
details: null
exposure:
- asset_type:
    description: Population counts within 1km coastal buffer zones across administrative
      units in Guam, derived from 2010 census data
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
  description: Administrative boundary and population data from the 2010 census were
    spatially intersected with a 1km coastal buffer derived from coastline geometry
    to estimate the proportion of population and area within coastal proximity. The
    analysis was conducted for 22 Pacific Island Countries and Territories to support
    coastal risk and vulnerability assessments.
  sources:
  - id: source_1
    license: null
    name: SPC Statistics for Development Division (SDD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-coastal-proximity-of-populations-in-22-pacific-island-countries-and-territories-dataset-guam
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
    Territories - Dataset - Guam (GUM admin boundaries)
  download_url: https://pacificdata.org/data/dataset/fa39bb92-f4ba-4555-a0f3-5e353d4fd51f/resource/0e11b564-4349-47d2-b3e0-4f68e8057f3d/download/gum_dist_4326.geojson
  format: null
  id: resource_baf81f0b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GUM admin boundaries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Guam (GUM 1km Coastal Buffer)
  download_url: https://pacificdata.org/data/dataset/fa39bb92-f4ba-4555-a0f3-5e353d4fd51f/resource/eb829cd2-9b2a-450a-b6a5-937ce31193d6/download/gum1kmbuff_4326.geojson
  format: null
  id: resource_f6b59886
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GUM 1km Coastal Buffer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Coastal proximity of populations in 22 Pacific Island Countries and
    Territories - Dataset - Guam (NRU README)
  download_url: https://pacificdata.org/data/dataset/fa39bb92-f4ba-4555-a0f3-5e353d4fd51f/resource/93bf0021-a9e6-47e8-960d-1afa61768382/download/readme.txt
  format: null
  id: resource_e1cdad8e
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NRU README
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gum_spc_coastalproximitypopulatio_20190930
spatial:
  bbox: null
  centroid: null
  countries:
  - GUM
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
  - Dataset - Guam
version: null
vulnerability: null
---
