---
attributions:
- entity:
    affiliation: null
    email: null
    name: Bing Maps
    url: https://data.humdata.org/dataset/ai-building-footprint-in-southern-guatemala
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Netherlands Red Cross - 510 automated-building-detection
    url: https://data.humdata.org/dataset/ai-building-footprint-in-southern-guatemala
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/ai-building-footprint-in-southern-guatemala
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/ai-building-footprint-in-southern-guatemala
dataset_id: rdls_exp-gtm_nlrc510_aibuildingfootprintsouthe_20201120
description: 'Southern Guatemala: AI predictions of building footprint on Bing Maps
  images (approximately 2016-2019), see https://github.com/rodekruis/automated-building-detection.
  Produced in support to DRRT Guatemala for hurricane Eta and Iota. Coordinate reference
  system: WGS 84 / EPSG:4326. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ai-building-footprint-in-southern-guatemala]'
details: Buildings might be missing, complement if possible.
exposure:
- asset_type:
    description: AI-detected building footprints in southern Guatemala derived from
      satellite imagery
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Building footprints were automatically detected using AI algorithms
    applied to Bing Maps satellite imagery (2016-2019) covering southern Guatemala.
    The methodology leverages machine learning for feature extraction from optical
    satellite data to generate vector building geometries. The dataset was produced
    to support disaster risk assessment for hurricanes Eta and Iota in Guatemala.
  sources:
  - id: source_1
    license: null
    name: Bing Maps
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Netherlands Red Cross - 510 automated-building-detection
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ai-building-footprint-in-southern-guatemala
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://github.com/rodekruis/automated-building-detection
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Southern Guatemala: AI predictions of building footprint on Bing Maps
    images (approximately 2016-2019), see https://github.com/rodekruis/automated-building-detection.
    Produced in support to DRRT Guatemala for hurricane Eta and Iota. Coordinate reference
    system: WGS 84 / EPSG:4326'
  download_url: https://data.humdata.org/dataset/5ff73bdc-09cf-450a-9efd-ea81258f9006/resource/287b4426-299f-4cf5-b492-261e43128d88/download/buidings_guatemala.geojson
  format: null
  id: resource_287b4426
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: buildings_guatemala.geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gtm_nlrc510_aibuildingfootprintsouthe_20201120
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-20'
temporal_resolution: null
title: AI building footprint in southern Guatemala
version: null
vulnerability: null
---
