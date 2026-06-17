---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/inform-sub-national-for-eastern-africa
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/inform-sub-national-for-eastern-africa
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/inform-sub-national-for-eastern-africa
dataset_id: rdls_hev-ocharosea_informsubnational_20150101
description: 'INFORM SUB NATIONAL data for Eastern Africa Region. It contains the
  Hazards/Exposures, Vulnerbilities and Lack of Coping Capacity of the Greater Horn
  of Africa Region and the Overal Rick Index. The scale is from 0 - 10. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/inform-sub-national-for-eastern-africa]'
details: null
exposure:
- asset_type:
    description: Population exposure component of INFORM risk index
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
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Sub-national INFORM risk index calculated by aggregating multiple hazard
    exposure indicators, vulnerability measures, and coping capacity assessments for
    administrative units across the Greater Horn of Africa region, normalized to a
    0-10 scale.
  sources:
  - id: source_1
    license: null
    name: INFORM
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-sub-national-for-eastern-africa
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
  description: INFORM SUB NATIONAL for Eastern Africa (INFORM_GHoA 2015_v13_16Feb.xlsx)
  download_url: https://data.humdata.org/dataset/d2ebf607-4d8d-47b5-a1f5-ea7671fe19c9/resource/91313d2e-5f62-4873-9edf-172db9aeeebf/download/inform-ghoa-2015-v13-16feb.xlsx
  format: null
  id: resource_91313d2e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_GHoA 2015_v13_16Feb.xlsx
risk_data_type:
- hazard
- exposure
- vulnerability
schema: rdls-10
slug: rdls_hev-ocharosea_informsubnational_20150101
spatial:
  bbox: null
  centroid: null
  countries:
  - BDI
  - DJI
  - ERI
  - ETH
  - KEN
  - RWA
  - SOM
  - SSD
  - SDN
  - TZA
  - UGA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-01'
temporal_resolution: null
title: INFORM SUB NATIONAL for Eastern Africa
version: null
vulnerability: null
---
