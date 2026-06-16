---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNDAC A&A Cell Mozambique
    url: https://data.humdata.org/dataset/moz-rapid-assessment-april2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/moz-rapid-assessment-april2019
creator:
  affiliation: null
  email: null
  name: REACH Initiative
  url: https://data.humdata.org/dataset/moz-rapid-assessment-april2019
dataset_id: rdls_el-moz_reach_rapidassessmentapril2019_201904
description: 'Data from the Cyclone Idai UNDAC A&A Cell Mozambique Rapid Assessment
  covering Sofala and Manica provinces in April 2019.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/moz-rapid-assessment-april2019]'
details: null
exposure:
- asset_type:
    description: Building stock assessed in Sofala and Manica provinces affected by
      Cyclone Idai
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Residential population in affected areas of Sofala and Manica provinces
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: Rapid assessment data collected by UNDAC A&A Cell in Sofala and Manica
    provinces during April 2019 following Cyclone Idai, compiled and processed by
    REACH Initiative using sample survey methodology to document post-event exposure
    and impact on buildings and population.
  sources:
  - id: source_1
    license: null
    name: UNDAC A&A Cell Mozambique
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: REACH Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/moz-rapid-assessment-april2019
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Cyclone Idai strong winds and associated
      impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Population affected by Cyclone Idai in rapid assessment survey
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique rapid assessment April 2019 (Excel)
  download_url: https://data.humdata.org/dataset/c2c461a3-acb6-42b9-ae22-a37ab2156f53/resource/7dd2f6ec-b1e6-44a3-8586-820ab6803b8e/download/moz_mra_dataset_april2019.xlsx
  format: null
  id: resource_7dd2f6ec
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_MRA_Dataset_April2019.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-moz_reach_rapidassessmentapril2019_201904
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-04-17'
  start: '2019-04-01'
temporal_resolution: null
title: Mozambique rapid assessment April 2019
version: null
vulnerability: null
---
