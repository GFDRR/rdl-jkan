---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/zimbabwe-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
  url: https://data.humdata.org/dataset/zimbabwe-humanitarian-needs-overview
dataset_id: rdls_lss-zwe_ocharosea_humanitarianneedsmultisec_2021
description: 'Humanitarian needs overview for Zimbabwe. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/zimbabwe-humanitarian-needs-overview]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian Needs Overview (HNO) compiled from multiple observational
    and anecdotal sources by OCHA ROSEA, aggregating sectoral needs assessments to
    estimate total people in need (PiN) and humanitarian response targets across Zimbabwe
    for the 2021 humanitarian response plan.
  sources:
  - id: source_1
    license: null
    name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/zimbabwe-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need from flood-related humanitarian impacts in Zimbabwe
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
    description: People in need from drought-related humanitarian impacts in Zimbabwe
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
    description: People in need from cyclone/strong wind-related humanitarian impacts
      in Zimbabwe
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
        metric: exposure
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
  description: 'Zimbabwe: Humanitarian Needs Multisector Analysis (Zimbabwe humanitarian
    needs overview)'
  download_url: https://data.humdata.org/dataset/c6250510-c5e1-4b21-897e-d2694f94b749/resource/90246cd0-781b-4e03-9cd8-6bad9c614355/download/zwe_hno_hrp2021_joint_analysis_pin_target_21122020.xlsx
  format: null
  id: resource_90246cd0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ZWE_HNO_HRP2021_Joint_Analysis_PiN_Target_21122020.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-zwe_ocharosea_humanitarianneedsmultisec_2021
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
  end: '2021-09-30'
  start: '2021-01-31'
temporal_resolution: null
title: 'Zimbabwe: Humanitarian Needs Multisector Analysis'
version: null
vulnerability: null
---
