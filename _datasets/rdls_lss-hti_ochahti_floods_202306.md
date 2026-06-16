---
attributions:
- entity:
    affiliation: null
    email: null
    name: General Directorate of Civil Protection (DGPC)
    url: https://data.humdata.org/dataset/haiti-floods
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/haiti-floods
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/haiti-floods
creator:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/haiti-floods
dataset_id: rdls_lss-hti_ochahti_floods_202306
description: 'This dataset shows the people affected by floods in Haiti. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/haiti-floods]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Post-event flood impact data collected through direct observation and
    anecdotal reports by the General Directorate of Civil Protection, OCHA Haiti,
    and humanitarian partners. Data aggregated by department covering casualties,
    displacement, building damage, and livestock losses from flood events in Haiti.
  sources:
  - id: source_1
    license: null
    name: General Directorate of Civil Protection (DGPC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OCHA Haiti
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-floods
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Count of houses flooded and destroyed or damaged by floods
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
  - asset_category: population
    asset_dimension: population
    description: Population displaced and evacuated to shelters due to floods
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Deaths and missing persons caused by floods
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Loss of livestock due to floods
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
          quantity_kind: area
          unit: null
        metric: loss
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
  description: "As of 6 June 2023, the DGPC's provisional assessment of the impact\
    \ of the weekend's extreme weather has risen sharply, with 39,458 households affected,\
    \ 3,586 people evacuated or sheltered, 51 deaths, 140 people injured, 18 people\
    \ missing, 31,591 homes flooded and 2,445 homes destroyed or damaged. Numerous\
    \ infrastructures, schools and health centres were damaged in the departments\
    \ of Ouest, Nippes, Sud-Est, Nord-Ouest, Centre and Sud. Ouest, including the\
    \ Port-au-Prince metropolitan area (ZMPAP), was the worst affected department,\
    \ particularly in the communes of L\xE9og\xE2ne (24 deaths reported), Gressier,\
    \ Cit\xE9 Soleil and Tabarre"
  download_url: https://data.humdata.org/dataset/c42d243a-e0a9-4b11-9d07-406c81e6db58/resource/bbd92704-303b-43ef-b873-684afdf328a1/download/floods-haiti-floods-.xlsx
  format: null
  id: resource_bbd92704
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Floods Haiti Floods .xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The torrential rains that fell on at least six departments of the country
    on 2nd and 3rd June, 2023 killed 42 people. At least 11 people are missing. In
    the departments affected, more than 13,500 homes were flooded.
  download_url: https://data.humdata.org/dataset/c42d243a-e0a9-4b11-9d07-406c81e6db58/resource/6ec447fa-47b9-4e6c-a522-0ff20271591a/download/haiti-floods-2023.xlsx
  format: null
  id: resource_6ec447fa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Haiti Floods - 2023.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_ochahti_floods_202306
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-06-03'
  start: '2023-06-02'
temporal_resolution: null
title: Haiti - Floods
version: null
vulnerability: null
---
