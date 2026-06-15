---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ministry of Humanitarian Affairs and Disaster Management, South West State
    url: https://data.humdata.org/dataset/somalia-floods
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/somalia-floods
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-floods
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-floods
dataset_id: rdls_el-som_ochasom_floods_2023
description: 'This dataset is from preliminary reports by the Ministry of Humanitarian
  Affairs and Disaster Management, South West State and humanitarian partners.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/somalia-floods]'
details: null
exposure:
- asset_type:
    description: Residential population in flood-affected areas by administrative
      division
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
- asset_type:
    description: Shelters and schools affected or destroyed by flooding
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Water points, latrines, bridges, and roads affected by flooding
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_3
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Farmland affected by flooding and livestock losses
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_4
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event flood impact data compiled from direct observational reports
    and anecdotal data collected by the Ministry of Humanitarian Affairs and Disaster
    Management in South West State and humanitarian partners. Data aggregated by administrative
    divisions (state, region, district) documenting affected populations, casualties,
    displacement, and damage to shelters, infrastructure, and agricultural assets
    across multiple flood events in 2023-2025.
  sources:
  - id: source_1
    license: null
    name: Ministry of Humanitarian Affairs and Disaster Management, South West State
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
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
- href: https://data.humdata.org/dataset/somalia-floods
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct count of people affected by flooding
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displaced and relocated due to flooding
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
    description: Fatalities directly caused by flooding
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
  - asset_category: buildings
    asset_dimension: structure
    description: Shelters and schools damaged or destroyed by flooding
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Water points, latrines, bridges, and roads damaged by flooding
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Farmland and livestock losses from flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_6
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
  description: 'Somalia : Floods (Flood data consolidated from the Gu season.)'
  download_url: https://data.humdata.org/dataset/5ac53a1a-5dc2-4750-8b96-0b421d140cd3/resource/fa987309-7061-4518-ba5f-8708ebf6e08b/download/gu_floods_impact_respons_template_2025.xlsx
  format: null
  id: resource_fa987309
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Gu_Floods_IMPACT_Respons_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia : Floods (Floods in Somalia from as of May 2024)'
  download_url: https://data.humdata.org/dataset/5ac53a1a-5dc2-4750-8b96-0b421d140cd3/resource/b3cde4cc-eeea-4daf-9e35-6a3f44b780e9/download/floods_mastertable_2024.xlsx
  format: null
  id: resource_b3cde4cc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Floods_Mastertable_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia : Floods (Floods in Somalia from 30 November 2023)'
  download_url: https://data.humdata.org/dataset/5ac53a1a-5dc2-4750-8b96-0b421d140cd3/resource/b5877c1c-f1ac-4009-8548-061478f02ee7/download/floods_mastertable_2023.xlsx-floods_data.csv
  format: null
  id: resource_b5877c1c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Floods_Mastertable_2023.xlsx - Floods_data.csv
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_ochasom_floods_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-06-30'
  start: '2023-10-10'
temporal_resolution: null
title: 'Somalia : Floods'
version: null
vulnerability: null
---
