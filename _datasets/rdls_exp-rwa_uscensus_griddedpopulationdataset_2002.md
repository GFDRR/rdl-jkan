---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/rwanda-gridded-population-dataset
creator:
  affiliation: null
  email: null
  name: U.S. Census Bureau
  url: https://data.humdata.org/dataset/rwanda-gridded-population-dataset
dataset_id: rdls_exp-rwa_uscensus_griddedpopulationdataset_2002
description: 'Using the same methods applied to Pakistan (methods described in the
  journal Remote Sensing of Environment), the Census Bureau mapped Rwanda, a country
  with a substantial, dense rural population. Satellite imagery was combined with
  data from the 2002 Census of Rwanda to produce a geospatial distributed population
  layer.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/rwanda-gridded-population-dataset]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution derived from 2002 census data and
      satellite imagery
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
  description: Satellite imagery was integrated with Rwanda's 2002 Census data using
    spatial interpolation methods (as applied to Pakistan and published in Remote
    Sensing of Environment) to produce a gridded population layer representing distributed
    population density across the country.
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
- href: https://data.humdata.org/dataset/rwanda-gridded-population-dataset
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
  description: Rwanda Gridded Population Dataset (100-meter spatial resolution gridded
    population dataset.)
  download_url: https://data.humdata.org/dataset/09806feb-d200-46ae-8306-296a5275999c/resource/36840b26-43f7-453f-8bd8-ab5d22d5fa4a/download/rwanda_gridded_2002.zip
  format: null
  id: resource_36840b26
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwanda_gridded_2002.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-rwa_uscensus_griddedpopulationdataset_2002
spatial:
  bbox: null
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2002-12-31'
  start: '2002-01-01'
temporal_resolution: null
title: Rwanda Gridded Population Dataset
version: null
vulnerability: null
---
