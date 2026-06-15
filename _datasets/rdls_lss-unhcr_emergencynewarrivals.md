---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/new-arrivals-from-sudan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Government
    url: https://data.humdata.org/dataset/new-arrivals-from-sudan
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/new-arrivals-from-sudan
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/new-arrivals-from-sudan
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/new-arrivals-from-sudan
dataset_id: rdls_lss-unhcr_emergencynewarrivals
description: 'Following the outbreak of armed conflict in Sudan on 15 April 2023,
  large numbers of civilians have been forced to flee, including people who were already
  internally displaced because of previous conflicts in Sudan and refugees from other
  countries who had sought safety in Sudan. In addition to new internal displacement,
  hundreds of thousands of people, including Sudanese refugees and refugees of other
  nationalities hosted by Sudan have fled Sudan to neighbouring countries or returned
  home in adverse circumstances - notably to Chad, South Sudan, the Central African
  Republic, Egypt and Ethiopia. UNHCR Operational Data Portal for the Sudan Situation:
  https://data.unhcr.org/en/situations/sudansituation. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/new-arrivals-from-sudan]'
details: 'UNHCR Operational Data Portal for the Sudan Situation: https://data.unhcr.org/en/situations/sudansituation'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Registry-based data compiled from UNHCR, government, and IOM sources
    tracking new arrivals and displacement flows from Sudan following the April 2023
    armed conflict outbreak. Data aggregates cross-border population movements into
    neighbouring countries (Chad, South Sudan, Central African Republic, Egypt, Ethiopia)
    and includes both Sudanese refugees and third-country nationals previously hosted
    in Sudan.
  sources:
  - id: source_1
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Government
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/new-arrivals-from-sudan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement and forced migration due to armed conflict
      in Sudan
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
    description: New arrivals and returnees from Sudan to neighbouring countries
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: New arrivals from Sudan to Chad, Egypt and Ethiopia, South Sudan, the
    Central African Republic since 16 April, 2023.
  download_url: https://docs.google.com/spreadsheets/d/1G5FSrIZ5qvyrMSps4xE3vZf6kIQ9311Wm-mSx7HcPog/edit?usp=drive_web
  format: null
  id: resource_a9950d94
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNHCR - New Arrivals from Sudan
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Daily new arrivals from Sudan to Chad, Egypt and Ethiopia, South Sudan,
    the Central African Republic since 16 April, 2023.
  download_url: https://docs.google.com/spreadsheets/d/1MEDlbvR09E4xcKtjJDnF6mQtb11NhuI_BEDPxkIuSfY/edit?usp=drive_web
  format: null
  id: resource_51677222
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNHCR - New Arrivals from Sudan per day
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-unhcr_emergencynewarrivals
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  - TCD
  - SSD
  - CAF
  - EGY
  - ETH
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: 'Sudan Emergency: New arrivals from Sudan'
version: null
vulnerability: null
---
