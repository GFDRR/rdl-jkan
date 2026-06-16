---
attributions:
- entity:
    affiliation: null
    email: null
    name: Multiple Sources
    url: https://data.humdata.org/dataset/lake-chad-basin-dashboard
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/lake-chad-basin-dashboard
creator:
  affiliation: null
  email: null
  name: OCHA West and Central Africa (ROWCA)
  url: https://data.humdata.org/dataset/lake-chad-basin-dashboard
dataset_id: rdls_lss-cmrnerngatcd_ocharowca_lakebasindashboard_20190710
description: 'This data is about the displacements, the food insecurity in the Lake
  Chad Basin and also the current funding status.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/lake-chad-basin-dashboard]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Dataset aggregates displacement counts and food insecurity classifications
    from multiple sources across the Lake Chad Basin, compiled by OCHA ROWCA to track
    humanitarian impacts from complex emergency and conflict-driven crises.
  sources:
  - id: source_1
    license: null
    name: Multiple Sources
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/lake-chad-basin-dashboard
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from complex emergency and conflict
      in Lake Chad Basin
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
  - asset_category: population
    asset_dimension: population
    description: Food insecurity affecting population in Lake Chad Basin
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Lake Chad Basin Dashboard (Excel)
  download_url: https://data.humdata.org/dataset/2edb49da-9dd2-4ae1-99f3-485e68256e19/resource/12d37440-7dcc-43fd-86f6-73ce07d22f89/download/lcb_dashboard_data_july2019.xlsx
  format: null
  id: resource_12d37440
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lcb_dashboard_data_July2019.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cmrnerngatcd_ocharowca_lakebasindashboard_20190710
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  - CMR
  - NER
  - NGA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-07-10'
temporal_resolution: null
title: Lake Chad Basin Dashboard
version: null
vulnerability: null
---
