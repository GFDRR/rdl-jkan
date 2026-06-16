---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Aid Commissioner (HAC)
    url: https://data.humdata.org/dataset/sudan-people-affected-by-floods
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-people-affected-by-floods
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-people-affected-by-floods
dataset_id: rdls_lss-sdn_ochasdn_peopleaffectedfloods_2021
description: 'The dataset contains information on flood-affected people and flood
  damage by Locality and State.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-people-affected-by-floods]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event flood impact data collected by the Humanitarian Aid Commissioner
    through direct observation and anecdotal reports at locality and state administrative
    levels in Sudan. Data aggregated annually from 2015-2024 and compiled into multi-year
    analysis files tracking casualties, building damage, and affected populations
    by geographic area.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Aid Commissioner (HAC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-people-affected-by-floods
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding recorded by locality and state
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building destruction from flooding recorded by locality and
      state
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding recorded by locality and state
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from flooding recorded by locality and state
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Injured persons from flooding recorded by locality and state
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: People Affected by Floods (Spreadsheet tracking people and
    households affected by floods in 2024.)'
  download_url: https://docs.google.com/spreadsheets/d/1zt76HwQWo7fwoRQCMfT0o4eaXmeg3cVFBRQHAa8SOfk/edit?gid=0#gid=0
  format: null
  id: resource_5a9102ba
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Floods Data 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file contains the flood affected locations, people affected, houses
    damaged and destroyed.
  download_url: https://data.humdata.org/dataset/2e49de77-72e6-46c3-b0b8-439ee21e6ad5/resource/ba91fb45-04e2-4742-a32f-47748856f6cb/download/sudan-floods-data-2021-to-2023_hxl.xlsx
  format: null
  id: resource_ba91fb45
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Floods Data 2021 to 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file contains flood prone localities and average number of people
    affected over time.
  download_url: https://data.humdata.org/dataset/2e49de77-72e6-46c3-b0b8-439ee21e6ad5/resource/e2a6245b-dc00-42f7-81e1-139e1ff1a8cb/download/floods-data-analysis-2015-to-2023.xlsx
  format: null
  id: resource_e2a6245b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Floods Data Analysis 2015 to 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This file contains the flood affected locations, people killed, houses
    damaged and destroyed. May - Sep 2022.
  download_url: https://data.humdata.org/dataset/2e49de77-72e6-46c3-b0b8-439ee21e6ad5/resource/5fd834bf-cb49-488d-820f-fa77f3cc5f55/download/2022-sdn-flood-disaster-monitoring-matrix-may-to-sep-2022-1.xlsx
  format: null
  id: resource_5fd834bf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2022-sdn-flood-disaster-monitoring-matrix-may-to-sep-2022.xlsx
- access_url: https://data.humdata.org/dataset/sudan-people-affected-by-floods-as-of-6-october-2020
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: People Affected by Floods (Dataset on people affected by floods
    in Sudan in the year 2020.)'
  download_url: null
  format: null
  id: resource_34a83783
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SDN_HAC_Flood data by state and locality_07102020
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_peopleaffectedfloods_2021
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
  end: '2024-12-29'
  start: '2021-01-01'
temporal_resolution: null
title: 'Sudan: People Affected by Floods'
version: null
vulnerability: null
---
