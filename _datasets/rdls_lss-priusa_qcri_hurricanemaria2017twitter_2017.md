---
attributions:
- entity:
    affiliation: null
    email: null
    name: Twitter
    url: https://data.humdata.org/dataset/hurricane-maria-2017-twitter-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: AIDR (Artificial Intelligence for Disaster Response)
    url: https://data.humdata.org/dataset/hurricane-maria-2017-twitter-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/hurricane-maria-2017-twitter-data
creator:
  affiliation: null
  email: null
  name: Qatar Computing Research Institute
  url: https://data.humdata.org/dataset/hurricane-maria-2017-twitter-data
dataset_id: rdls_lss-priusa_qcri_hurricanemaria2017twitter_2017
description: 'This resource is comprised of Twitter data collected and processed by
  the AIDR system during the 2017 hurricane Maria. The data contains information about
  number of people affected, injured, dead, reports of damages, missing people and
  so on. Please contact us if you need full dataset with tweets content.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hurricane-maria-2017-twitter-data]'
details: Please contact us if you need full dataset with tweets content.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Public tweets were collected in real-time via the Twitter API during
    Hurricane Maria 2017 and processed using the AIDR machine learning system to automatically
    extract and classify impact information including affected populations, injuries,
    fatalities, and damage reports. The processed data was aggregated into a summary
    table with structured impact metrics.
  sources:
  - id: source_1
    license: null
    name: Twitter
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: AIDR (Artificial Intelligence for Disaster Response)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hurricane-maria-2017-twitter-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Hurricane Maria 2017
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
    description: Injuries caused by Hurricane Maria 2017
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
    description: Deaths caused by Hurricane Maria 2017
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
    description: Building damage reports from Hurricane Maria 2017
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
    by the AIDR system during the 2017 hurricane Maria. The data contains information
    about number of people affected, injured, dead, reports of damages, missing people
    and so on. The data was automatically classified using state of the art machine
    learning techniques.
  download_url: https://data.humdata.org/dataset/71ac6a0c-88a3-456b-86b5-7120f9005684/resource/d734df32-bd40-47d2-8bf6-8ee3ea8b457c/download/maria_text_image_data_analysis_summarytable.xlsx
  format: null
  id: resource_d734df32
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Maria_Text_Image_Data_Analysis_SummaryTable.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-priusa_qcri_hurricanemaria2017twitter_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  - PRI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-10-03'
  start: '2017-09-20'
temporal_resolution: null
title: United States, Puerto Rico - Hurricane Maria 2017 Twitter Data
version: null
vulnerability: null
---
