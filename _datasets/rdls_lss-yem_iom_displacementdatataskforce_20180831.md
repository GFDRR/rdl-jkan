---
attributions:
- entity:
    affiliation: null
    email: null
    name: Task Force on Population Movement (TFPM)
    url: https://data.humdata.org/dataset/yemen-displacement-data-task-force-on-population-movement-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/yemen-displacement-data-task-force-on-population-movement-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/yemen-displacement-data-task-force-on-population-movement-iom-dtm
dataset_id: rdls_lss-yem_iom_displacementdatataskforce_20180831
description: 'The Task Force for Population Movement (TFPM) is a Technical Working
  Group to the Inter-Cluster Coordination Mechanism.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/yemen-displacement-data-task-force-on-population-movement-iom-dtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The dataset aggregates displacement census data collected by IOM's
    Displacement Tracking Matrix (DTM) through the Task Force on Population Movement,
    a technical coordination mechanism. Data were collected via census methodology
    across multiple rounds (Round 16 in October 2017 and Round 17 in August 2018)
    to track internally displaced persons and population movement patterns in Yemen.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Task Force on Population Movement (TFPM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/yemen-displacement-data-task-force-on-population-movement-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement counts from flood and other hazards in Yemen
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Yemen Displacement Data - Task Force on Population Movement (DTM Yemen
    TFPM Data -Aug18- Round 17.xlsx)
  download_url: https://data.humdata.org/dataset/96fea290-f0be-4241-8f10-858ff159e85f/resource/3b0e8f9f-ba6e-4407-be98-aa88877111e8/download/dtm-yemen-tfpm-data-aug18-round-17.xlsx
  format: null
  id: resource_3b0e8f9f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen TFPM Data -Aug18- Round 17.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Yemen Displacement Data - Task Force on Population Movement (DTM Yemen
    TFPM Data -Oct17- Round 16.xlsb)
  download_url: https://data.humdata.org/dataset/96fea290-f0be-4241-8f10-858ff159e85f/resource/6cee9400-d152-45a1-926b-8e770f0f01c8/download/dtm-yemen-tfpm-data-oct17-round-16.xlsb
  format: null
  id: resource_6cee9400
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Yemen TFPM Data -Oct17- Round 16.xlsb
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_iom_displacementdatataskforce_20180831
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-08-31'
temporal_resolution: null
title: Yemen Displacement Data - Task Force on Population Movement
version: null
vulnerability: null
---
