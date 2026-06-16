---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/south-sudan-gridded-population-data
creator:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/south-sudan-gridded-population-data
dataset_id: rdls_exp-ssd_uscensus_griddedpopulationdataset_2017
description: 'The Census Bureau mapped South Sudan, a country with a substantial rural
  population. Satellite imagery was combined with 2008 census data and 2017 population
  estimates to produce gridded population layers.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/south-sudan-gridded-population-data]'
details: null
exposure:
- asset_type:
    description: Gridded population estimates derived from 2008 census data and 2017
      population projections
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
  description: Satellite imagery was combined with 2008 census enumeration data and
    2017 population estimates using spatial interpolation methods to produce gridded
    population density layers at sub-national resolution for South Sudan.
  sources:
  - id: source_1
    license: null
    name: U.S. Census Bureau
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-gridded-population-data
  rel: source
loss: null
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
  description: South Sudan Gridded Population Dataset (100-meter spatial resolution
    gridded population dataset.)
  download_url: https://data.humdata.org/dataset/891fc716-2b22-436c-b6d4-937ac9cb26e2/resource/5fd888a6-f733-4d01-8ca6-a5533917ae9f/download/south-sudan-gridded-population-estimates-2017-1.zip
  format: null
  id: resource_5fd888a6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: south-sudan-gridded-population-estimates-2017.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_uscensus_griddedpopulationdataset_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-12-31'
  start: '2017-07-01'
temporal_resolution: null
title: South Sudan Gridded Population Dataset
version: null
vulnerability: null
---
