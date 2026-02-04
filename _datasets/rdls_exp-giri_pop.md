---
contact_point:
  email: mamadio@worldbank.org
  id: '3'
  name: Mattia Amadio
  url: null
creator:
  email: null
  id: '2'
  name: UNEP-GRID
  url: https://unepgrid.ch/en
dataset_id: rdls_exp-GIRI_POP
description: Datasets containing population distribution at high resolution for exposure
  analysis, including HRSL 2018 and GHSL 2020 datasets at the global scale.
details: Population exposure datasets include HRSL (High Resolution Settlement Layer)
  2018 from Facebook/Meta and GHSL (Global Human Settlement Layer) 2020 from European
  Commission JRC. These datasets provide detailed spatial distribution of population
  for assessing exposure to natural hazards.
exposure:
- category: population
  dimension: population
  quantity_kind: count
  taxonomy: null
extra_attributions:
- email: null
  id: '4'
  name: CDRI
  role: resource_provider
  url: https://cdri.world/
hazard: null
license: CC-BY-4.0
loss: null
project:
  name: Global Infrastructure Risk Model and Resilience Index (GIRI)
  url: https://giri.unepgrid.ch/
publisher:
  email: null
  id: '1'
  name: UNEP-GRID
  url: https://unepgrid.ch/en
purpose: null
resources:
- coordinate_system: EPSG:4326
  description: High resolution population distribution from Facebook/Meta for 2018
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: HRSL_2018
  media_type: null
  spatial_resolution: 1000
  temporal:
    duration: null
    end: '2018'
    start: '2018'
    temporal_resolution: null
  title: High Resolution Settlement Layer (HRSL) 2018
- coordinate_system: EPSG:4326
  description: High resolution population distribution from European Commission JRC
    for 2020
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF (tif)
  id: GHSL_2020
  media_type: null
  spatial_resolution: 1000
  temporal:
    duration: null
    end: '2020'
    start: '2020'
    temporal_resolution: null
  title: Global Human Settlement Layer (GHSL) 2020
risk_data_type:
- exposure
schema: rdl-03
slug: rdls_exp-GIRI_POP
spatial:
  countries:
  - GLO
  scale: global
title: Global population exposure
version: '1'
vulnerability: null
---
