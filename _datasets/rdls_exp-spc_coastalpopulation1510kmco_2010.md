---
attributions:
- entity:
    affiliation: null
    email: null
    name: Population and Housing Census
    url: https://data.humdata.org/dataset/pdh-coastal-population-1-5-and-10km-from-coast
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Population projections
    url: https://data.humdata.org/dataset/pdh-coastal-population-1-5-and-10km-from-coast
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-population-1-5-and-10km-from-coast
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-coastal-population-1-5-and-10km-from-coast
dataset_id: rdls_exp-spc_coastalpopulation1510kmco_2010
description: 'Proportion of population living in 1, 5 and 10km buffer zones for Pacific
  Island Countries and Territories, determined using most recent Population and Housing
  Census. Number of people living in 1,5 and 10km buffer zones determined by apportioning
  population projections. Find more Pacific data on PDH.stat . Access this dataset
  from the Pacific Data Hub. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pdh-coastal-population-1-5-and-10km-from-coast]'
details: null
exposure:
- asset_type:
    description: Population living in coastal buffer zones (1, 5, and 10km from coast)
      in Pacific Island Countries and Territories
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
license: CC-BY-4.0
lineage:
  description: Coastal population data derived from most recent Population and Housing
    Census for Pacific Island Countries and Territories, with population projections
    used to apportion census counts into 1, 5, and 10km coastal buffer zones. This
    dataset identifies populations at risk from coastal hazards by quantifying settlement
    patterns in proximity to the coast.
  sources:
  - id: source_1
    license: null
    name: Population and Housing Census
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Population projections
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-coastal-population-1-5-and-10km-from-coast
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
  description: Coastal population (1, 5 and 10km from coast) (Download Coastal population
    (1, 5 and 10km from coast) data)
  download_url: https://stats-sdmx-disseminate.pacificdata.org/rest/data/SPC,DF_POP_COAST,2.0/all/?format=csvfilewithlabels
  format: null
  id: resource_8540ee91
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Coastal population (1, 5 and 10km from coast) data
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-spc_coastalpopulation1510kmco_2010
spatial:
  bbox: null
  centroid: null
  countries:
  - ASM
  - COK
  - FSM
  - MHL
  - NIU
  - NRU
  - PLW
  - TKL
  - TUV
  - WLF
  - WSM
  - KIR
  - PNG
  - SLB
  - TON
  - VUT
  - FJI
  - NCL
  - PYF
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-31'
  start: '2010-01-01'
temporal_resolution: null
title: Coastal population (1, 5 and 10km from coast)
version: null
vulnerability: null
---
