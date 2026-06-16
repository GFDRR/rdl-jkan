---
attributions:
- entity:
    affiliation: null
    email: null
    name: Inter-Sector Coordination Group Sudan
    url: https://data.humdata.org/dataset/sudan-humanitarianneeds-overview
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-humanitarianneeds-overview
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-humanitarianneeds-overview
dataset_id: rdls_lss-sdn_ochasdn_2019humanitarianneedsover_20190131
description: 'This data set contains people in need figures for Sudan by locality
  (Admin level 2). [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-humanitarianneeds-overview]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Humanitarian needs data compiled by the Inter-Sector Coordination Group
    through direct observational and anecdotal data collection methods, aggregated
    at Admin Level 2 (locality) to support the 2019 Humanitarian Needs Overview planning
    process.
  sources:
  - id: source_1
    license: null
    name: Inter-Sector Coordination Group Sudan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-humanitarianneeds-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need due to food insecurity and malnutrition including
      IPC classifications
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees requiring humanitarian
      assistance
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: 2019 Humanitarian Needs Overview (HNO excel file)'
  download_url: https://data.humdata.org/dataset/01b94c26-4c5a-4aa9-8397-1348c82068d3/resource/226f8c83-1897-4273-b9bf-0dd614b6d130/download/hno-2019-baseline-data-hxl.xlsx
  format: null
  id: resource_226f8c83
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hno-2019-baseline-data-hxl.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_2019humanitarianneedsover_20190131
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-01-31'
temporal_resolution: null
title: 'Sudan: 2019 Humanitarian Needs Overview'
version: null
vulnerability: null
---
