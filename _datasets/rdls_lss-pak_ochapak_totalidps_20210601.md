---
attributions:
- entity:
    affiliation: null
    email: null
    name: CEW PDMA Khyber Pakhtoonkhwa
    url: https://data.humdata.org/dataset/pakistan-idps-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Pakistan
  url: https://data.humdata.org/dataset/pakistan-idps-data
creator:
  affiliation: null
  email: null
  name: OCHA Pakistan
  url: https://data.humdata.org/dataset/pakistan-idps-data
dataset_id: rdls_lss-pak_ochapak_totalidps_20210601
description: 'Pakistan district wise Total IDPs from areas of origin and by host location.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/pakistan-idps-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDP registry data collected by PDMA Khyber Pakhtoonkhwa through the
    Common Emergency Workspace (CEW) system, aggregated to district level to track
    displacement flows from origin areas to host locations across Pakistan.
  sources:
  - id: source_1
    license: null
    name: CEW PDMA Khyber Pakhtoonkhwa
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pakistan-idps-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flood-affected areas of origin
      and current host locations in Pakistan
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pakistan Total IDPs from areas of origin with PCodes
  download_url: https://data.humdata.org/dataset/3ecf5c88-9b54-43cc-b47c-8523b0e80519/resource/496f4397-99b0-4381-8c44-80584d1f8738/download/pakistan-total-idps-till-date.xlsx
  format: null
  id: resource_496f4397
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Pakistan IDPs by Area of Origin
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pakistan Total IDPs (Pakistan Current IDPs by host location)
  download_url: https://data.humdata.org/dataset/3ecf5c88-9b54-43cc-b47c-8523b0e80519/resource/99e1e07f-d839-4d3e-b884-0a01a7045d64/download/pakistan-current-idps.xlsx
  format: null
  id: resource_99e1e07f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Pakistan Current IDPs
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pak_ochapak_totalidps_20210601
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-06-01'
temporal_resolution: null
title: Pakistan Total IDPs
version: null
vulnerability: null
---
