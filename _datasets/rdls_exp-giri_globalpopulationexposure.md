---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNEP-GRID
    url: https://unepgrid.ch/en
  id: '1'
  role: publisher
- entity:
    affiliation: null
    email: null
    name: UNEP-GRID
    url: https://unepgrid.ch/en
  id: '2'
  role: creator
- entity:
    affiliation: null
    email: mamadio@worldbank.org
    name: Mattia Amadio
    url: null
  id: '3'
  role: contact_point
- entity:
    affiliation: null
    email: null
    name: CDRI
    url: https://cdri.world/
  id: '4'
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: null
  name: UNEP-GRID
  url: https://unepgrid.ch/en
creator:
  affiliation: null
  email: null
  name: UNEP-GRID
  url: https://unepgrid.ch/en
dataset_id: rdls_exp-giri_globalpopulationexposure
description: Datasets containing population distribution at high resolution for exposure
  analysis, including HRSL 2018 and GHSL 2020 datasets at the global scale.
details: Population exposure datasets include HRSL (High Resolution Settlement Layer)
  2018 from Facebook/Meta and GHSL (Global Human Settlement Layer) 2020 from European
  Commission JRC. These datasets provide detailed spatial distribution of population
  for assessing exposure to natural hazards.
exposure:
- asset_type:
    description: null
    id: sei-pop
    scheme: GED4ALL
    title: null
    uri: null
  category: population
  id: rdls_exp-giri_globalpopulationexposure_exp
  metrics:
  - dimension: population
    id: rdls_exp-giri_globalpopulationexposure_m1
    measurement:
      quantity_kind: count
      unit: null
hazard: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Global Infrastructure Risk Model and Resilience Index (GIRI)
  url: https://giri.unepgrid.ch/
publisher:
  affiliation: null
  email: null
  name: UNEP-GRID
  url: https://unepgrid.ch/en
purpose: null
referenced_by: []
resources:
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: High resolution population distribution from Facebook/Meta for 2018
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: HRSL_2018
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal:
    central_year: null
    duration: null
    end: '2018'
    start: '2018'
  temporal_resolution: null
  title: High Resolution Settlement Layer (HRSL) 2018
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: High resolution population distribution from European Commission JRC
    for 2020
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: GHSL_2020
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal:
    central_year: null
    duration: null
    end: '2020'
    start: '2020'
  temporal_resolution: null
  title: Global Human Settlement Layer (GHSL) 2020
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-giri_globalpopulationexposure
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Global population exposure
version: '1'
vulnerability: null
---
