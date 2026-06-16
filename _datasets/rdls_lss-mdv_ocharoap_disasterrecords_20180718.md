---
attributions:
- entity:
    affiliation: null
    email: null
    name: Desinventar database
    url: https://data.humdata.org/dataset/maldives-disaster-records
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/maldives-disaster-records
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/maldives-disaster-records
dataset_id: rdls_lss-mdv_ocharoap_disasterrecords_20180718
description: 'This datasets include Maldives Disaster Record recorded in Desinventar
  database by UNDP. The data were cleaned by the Faculty of Engineering, Science and
  Technology within the Maldives National University.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/maldives-disaster-records]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: Historical disaster records from the Desinventar database were extracted
    for Maldives and cleaned by the Faculty of Engineering, Science and Technology
    at Maldives National University. The dataset contains post-event impact records
    of natural disasters affecting the country, compiled from official disaster documentation.
  sources:
  - id: source_1
    license: null
    name: Desinventar database
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/maldives-disaster-records
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events
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
    description: Population affected by flooding events
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from strong wind events
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by strong wind events
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
  description: This datasets include Maldives Disaster Record recorded in Desinventar
    database by UNDP. The data were cleaned by the Faculty of Engineering, Science
    and Technology within the Maldives National University.
  download_url: https://data.humdata.org/dataset/509cd879-f937-4428-8868-5459938744d3/resource/8521e7dc-e511-45bb-989b-b9538580daea/download/disaster_record_from_desinventar.xlsx
  format: null
  id: resource_8521e7dc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Disaster_record_from_Desinventar.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mdv_ocharoap_disasterrecords_20180718
spatial:
  bbox: null
  centroid: null
  countries:
  - MDV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-07-18'
temporal_resolution: null
title: Maldives - Disaster Records
version: null
vulnerability: null
---
