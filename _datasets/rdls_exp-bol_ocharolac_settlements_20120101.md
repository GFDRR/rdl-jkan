---
attributions:
- entity:
    affiliation: null
    email: null
    name: Geo Bolivia
    url: https://data.humdata.org/dataset/bolivia-settlements
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/bolivia-settlements
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/bolivia-settlements
dataset_id: rdls_exp-bol_ocharolac_settlements_20120101
description: 'Populated places. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/bolivia-settlements]'
details: '**Languages:** ES The data is updated each 10 to 12 years The source is
  a government open data site Geo Node Bolivia https://geo.gob.bo'
exposure:
- asset_type:
    description: Populated settlements with census-based population counts and household
      numbers
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
    description: Residential dwelling units enumerated by settlement from census data
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
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Census data from Geo Bolivia was spatially referenced and compiled
    into a settlement-level geodataset with population and dwelling unit counts, classified
    by settlement type and administrative divisions as of 2012.
  sources:
  - id: source_1
    license: null
    name: Geo Bolivia
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bolivia-settlements
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
  description: Bolivia - Settlements (Bolivia Lugares poblados-2012.zip)
  download_url: https://data.humdata.org/dataset/9fbe6437-8da6-4024-9d59-ea7fc19612a1/resource/dcda7c81-e53b-4318-89a5-d0b749fe0c3b/download/bolivia-lugares-poblados-2012.zip
  format: null
  id: resource_dcda7c81
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Bolivia Lugares poblados-2012.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bol_ocharolac_settlements_20120101
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2012-01-01'
temporal_resolution: null
title: Bolivia - Settlements
version: null
vulnerability: null
---
