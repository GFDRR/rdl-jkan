---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/eswatini-settlements
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Kontur
    url: https://data.humdata.org/dataset/eswatini-settlements
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Meta
    url: https://data.humdata.org/dataset/eswatini-settlements
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/eswatini-settlements
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Google
    url: https://data.humdata.org/dataset/eswatini-settlements
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Crosscut
  url: https://data.humdata.org/dataset/eswatini-settlements
creator:
  affiliation: null
  email: null
  name: Crosscut
  url: https://data.humdata.org/dataset/eswatini-settlements
dataset_id: rdls_exp-swz_crosscut_settlements_2021
description: 'This dataset shows Eswatini catchment areas with information on total
  population disaggregated by sex and age and number of buildings.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/eswatini-settlements]'
details: null
exposure:
- asset_type:
    description: Residential population disaggregated by sex and age groups in settlement
      catchment areas
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
- asset_type:
    description: Building stock counts from multiple sources (OpenStreetMap, Google)
      with confidence levels and average footprint area
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Settlement catchment areas were delineated by identifying population
    clusters from gridded population data (WorldPop, Kontur, Meta), assigning representative
    points to each cluster, and generating Voronoi-based catchment areas. Population
    counts were disaggregated by sex and age from multiple demographic sources, and
    building inventories were compiled from OpenStreetMap and Google building detection
    datasets with varying confidence levels.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Kontur
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Meta
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_5
    license: null
    name: Google
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/eswatini-settlements
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Eswatini - Settlements (GeoJSON)
  download_url: https://data.humdata.org/dataset/6bb02296-89ad-4a69-8ce0-2aed3b0d8e00/resource/a9d25757-0a60-4222-ad22-9e8fd175a7af/download/eswatini_2024-01-11.geojson
  format: null
  id: resource_a9d25757
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Eswatini_2024-01-11.geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-swz_crosscut_settlements_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - SWZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-11-06'
  start: '2021-04-01'
temporal_resolution: null
title: Eswatini - Settlements
version: null
vulnerability: null
---
