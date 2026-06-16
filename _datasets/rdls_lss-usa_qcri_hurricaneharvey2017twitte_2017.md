---
attributions:
- entity:
    affiliation: null
    email: null
    name: Twitter API
    url: https://data.humdata.org/dataset/hurricane-harvey-2017-twitter-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: AIDR system
    url: https://data.humdata.org/dataset/hurricane-harvey-2017-twitter-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/hurricane-harvey-2017-twitter-data
creator:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/hurricane-harvey-2017-twitter-data
dataset_id: rdls_lss-usa_qcri_hurricaneharvey2017twitte_2017
description: 'This resource is comprised of Twitter data collected and processed by
  the AIDR system during the 2017 hurricane Harvey. The data contains information
  about number of people affected, injured, dead, reports of damages, missing people
  and so on. The data was automatically classified using state of the art machine
  learning techniques.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hurricane-harvey-2017-twitter-data]'
details: Please contact us if you need full dataset with tweets content.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Real-time Twitter data was collected via the public API during Hurricane
    Harvey 2017 and processed through the AIDR (Artificial Intelligence for Disaster
    Response) machine learning system to automatically classify and extract impact
    metrics including affected populations, injuries, fatalities, and damage reports.
  sources:
  - id: source_1
    license: null
    name: Twitter API
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: AIDR system
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hurricane-harvey-2017-twitter-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Hurricane Harvey reported via social media
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Injuries from Hurricane Harvey reported via social media
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
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Deaths from Hurricane Harvey reported via social media
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Building damage reports from Hurricane Harvey via social media
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: This resource is comprised of Twitter data collected and processed
    by the AIDR system during the 2017 hurricane Harvey. The data contains information
    about number of people affected, injured, dead, reports of damages, missing people
    and so on. Please contact us if you need full dataset with tweets content.
  download_url: https://data.humdata.org/dataset/2dd2e855-9d60-4dd1-86a7-be43e0dde7e8/resource/aea0e67a-b129-4f0a-8d20-e46aa5532fb1/download/hurricane_harvey_twitter_text_data_processed_by_aidr.xlsx
  format: null
  id: resource_aea0e67a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Hurricane_harvey_twitter_text_data_processed_by_AIDR.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-usa_qcri_hurricaneharvey2017twitte_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-09-05'
  start: '2017-08-25'
temporal_resolution: null
title: United States - Hurricane Harvey 2017 Twitter data
version: null
vulnerability: null
---
