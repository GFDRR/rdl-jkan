---
attributions:
- entity:
    affiliation: null
    email: null
    name: Kenya National Bureau of Statistics (KNBS)
    url: https://data.humdata.org/dataset/kenya-population-2016
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Satellite imagery
    url: https://data.humdata.org/dataset/kenya-population-2016
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: American Red Cross (inactive)
  url: https://data.humdata.org/dataset/kenya-population-2016
creator:
  affiliation: null
  email: null
  name: American Red Cross (inactive)
  url: https://data.humdata.org/dataset/kenya-population-2016
dataset_id: rdls_exp-ken_amredcross_population2016_20161231
description: '2016 Kenya population density (per square km). [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/kenya-population-2016]'
details: null
exposure:
- asset_type:
    description: Gridded population density derived from KNBS census surveys and satellite
      imagery for Kenya in 2016
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
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: Gridded population density dataset created by integrating Kenya National
    Bureau of Statistics census survey data with satellite imagery through spatial
    modeling techniques to produce a 2016 baseline population distribution at raster
    resolution across Kenya.
  sources:
  - id: source_1
    license: null
    name: Kenya National Bureau of Statistics (KNBS)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Satellite imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kenya-population-2016
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
  description: Kenya Population 2016 (2016 kenya population per square km)
  download_url: https://data.humdata.org/dataset/a6518379-54f0-47eb-a463-6a1c3fbfca2d/resource/bbb48739-9772-4fa4-bdb9-fe5294025c8b/download/ke_pop16.tif
  format: null
  id: resource_bbb48739
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ke_pop16.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ken_amredcross_population2016_20161231
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-12-31'
temporal_resolution: null
title: Kenya Population 2016
version: null
vulnerability: null
---
