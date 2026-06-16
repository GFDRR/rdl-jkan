---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus Sentinel-2
    url: https://data.humdata.org/dataset/google-open-buildings-temporal
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Google Research
  url: https://data.humdata.org/dataset/google-open-buildings-temporal
creator:
  affiliation: null
  email: null
  name: Google Research
  url: https://data.humdata.org/dataset/google-open-buildings-temporal
dataset_id: rdls_exp-googleres_openbuildings25dtemporal_2016
description: 'Source: https://sites.research.google/gr/open-buildings/temporal/ The
  Open Buildings 2.5D Temporal Dataset contains annual data spanning eight years (2016-2023)
  with building presence, fractional building counts, and building heights covering
  approximately 58 million square kilometers. This dataset requires some knowledge
  with using scripts. The ZIP contains .txt files for over 130 countries and territories.
  The primary purpose of the data is to support comparison of building footprints
  across multiple years.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/google-open-buildings-temporal]'
details: null
exposure:
- asset_type:
    description: Building footprints with fractional counts and heights derived from
      Sentinel-2 imagery across 130+ countries, 2016-2023
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
  description: A deep learning model was trained on Sentinel-2 multispectral imagery
    to detect building presence, fractional counts, and heights. The model was applied
    to annual stacks of 32 Sentinel-2 images centered on June 30th for each year from
    2016-2023 across the Global South, producing annual building exposure data for
    130+ countries and territories.
  sources:
  - id: source_1
    license: null
    name: Copernicus Sentinel-2
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Google Research
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/google-open-buildings-temporal
  rel: source
loss: null
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
  url: https://sentiwiki.copernicus.eu/web/s2-processing
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://arxiv.org/abs/2310.11622
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Contains Python script to download GeoTIFFs by country from Google
    Cloud Storage.
  download_url: https://data.humdata.org/dataset/acab847f-5c1a-462e-9c0e-ddd508525dcb/resource/1a7e9ba0-3fca-4c95-9f5a-a0a1f3bd393d/download/google-open-buildings-temporal.zip
  format: null
  id: resource_1a7e9ba0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: google-open-buildings-temporal.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-googleres_openbuildings25dtemporal_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Google Open Buildings 2.5D Temporal
version: null
vulnerability: null
---
