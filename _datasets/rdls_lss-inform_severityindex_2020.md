---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-severity-index-september-2020
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-severity-index-september-2020
dataset_id: rdls_lss-inform_severityindex_2020
description: 'The INFORM Severity Index summarises a wide range of already existing,
  quantitative information about crisis severity and presents it in a format that
  can be used more easily in decision-making.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/inform-severity-index-september-2020]'
details: More recent updates can be found via API at https://api.acaps.org/
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The INFORM Severity Index is a composite indicator that synthesizes
    existing quantitative data on humanitarian crisis severity across multiple dimensions
    (geographical scope, human impact, physical effects, and population conditions)
    into a standardized severity scale for decision-making support.
  sources:
  - id: source_1
    license: null
    name: INFORM
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-severity-index-september-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Humanitarian crisis severity assessment across multiple hazard types
      and impact dimensions
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Severity Index
  download_url: https://data.humdata.org/dataset/5e7603ad-07bf-4c52-ae4b-a7d0c0cc1187/resource/3d3e134d-1b74-47e4-ac4e-56f1743fe4cf/download/202404_inform_severity_-_april_2024.xlsx
  format: null
  id: resource_3d3e134d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 202404_INFORM_Severity
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Severity Index - Results by crisis
  download_url: https://data.humdata.org/dataset/5e7603ad-07bf-4c52-ae4b-a7d0c0cc1187/resource/9a92c25e-4f86-4ba8-bddc-4399cf837bb2/download/inform-severity-index-april-2024-all-crisis.pdf
  format: null
  id: resource_9a92c25e
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM Severity Index April 2024 - All Crisis
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Severity Index - Results by country
  download_url: https://data.humdata.org/dataset/5e7603ad-07bf-4c52-ae4b-a7d0c0cc1187/resource/07490f42-8bec-4679-a744-8e02956c9a89/download/inform-severity-index-april-2024-all-countries.pdf
  format: null
  id: resource_07490f42
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM Severity Index April 2024 - All Countries
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Severity Index User Guide
  download_url: https://data.humdata.org/dataset/5e7603ad-07bf-4c52-ae4b-a7d0c0cc1187/resource/4f7c980a-f43d-462d-9e93-04e121662add/download/inform-severity-index-user-guide-v01-october-2020.pdf
  format: null
  id: resource_4f7c980a
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM Severity Index User Guide v01 October 2020.pdf
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-inform_severityindex_2020
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
  end: '2024-04-30'
  start: '2020-09-30'
temporal_resolution: null
title: INFORM Severity Index
version: null
vulnerability: null
---
