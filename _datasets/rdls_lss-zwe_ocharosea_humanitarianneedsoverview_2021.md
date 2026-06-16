---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners in Zimbabwe
    url: https://data.humdata.org/dataset/zimbabwe-humanitarian-needs-overview-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/zimbabwe-humanitarian-needs-overview-2021
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/zimbabwe-humanitarian-needs-overview-2021
dataset_id: rdls_lss-zwe_ocharosea_humanitarianneedsoverview_2021
description: 'Humanitarian needs overview document for Zimbabwe 2021. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/zimbabwe-humanitarian-needs-overview-2021]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The Humanitarian Needs Overview aggregates direct observational data
    and anecdotal reports from multiple humanitarian partners operating in Zimbabwe
    to compile estimates of people in need, internally displaced persons, refugees,
    and returnees affected by various crises including displacement and humanitarian
    emergencies.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Partners in Zimbabwe
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/zimbabwe-humanitarian-needs-overview-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need and affected populations from multiple hazards including
      displacement
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and returnees from flood-related displacement
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
  description: 'Zimbabwe : Humanitarian Needs Overview (Humanitarian needs overview
    data for zimbabwe 2021)'
  download_url: https://data.humdata.org/dataset/51bf4bbe-b66d-4a15-8d3e-f276698e6652/resource/618c6f61-bd9c-448a-8913-5c96ba956af1/download/zimbabwe_hno.xlsx
  format: null
  id: resource_618c6f61
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zimbabwe_HNO.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-zwe_ocharosea_humanitarianneedsoverview_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - ZWE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: 'Zimbabwe : Humanitarian Needs Overview'
version: null
vulnerability: null
---
