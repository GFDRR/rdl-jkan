---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-national-risk
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-national-risk
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/hdx-hapi-national-risk
dataset_id: rdls_lss-hdxapi_hdxhapicoordinationcontex_2024
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-national-risk]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    sources including INFORM risk assessments. National risk scores are calculated
    by combining hazard exposure, vulnerability, and coping capacity components into
    composite risk indices with global rankings and risk classifications.
  sources:
  - id: source_1
    license: null
    name: INFORM
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-national-risk
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: National risk classification and overall risk score aggregating hazard
      exposure, vulnerability, and coping capacity
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
    description: National risk classification and overall risk score aggregating hazard
      exposure, vulnerability, and coping capacity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: National risk classification and overall risk score aggregating hazard
      exposure, vulnerability, and coping capacity
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
  - asset_category: population
    asset_dimension: population
    description: National risk classification and overall risk score aggregating hazard
      exposure, vulnerability, and coping capacity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_4
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: National Risk data from HDX HAPI, please see the documentation for
    more information
  download_url: https://data.humdata.org/dataset/856c326d-748c-43c2-89e4-8b25098a7340/resource/0af14f51-8db7-4131-87c9-30479054e629/download/hdx_hapi_national_risk_global.csv
  format: null
  id: resource_0af14f51
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Global Coordination & Context: National Risk'
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hdxapi_hdxhapicoordinationcontex_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  - BRN
  - COD
  - CPV
  - CZE
  - FSM
  - GBR
  - IRN
  - IRQ
  - KOR
  - MHL
  - MKD
  - NRU
  - PLW
  - PSE
  - STP
  - SWZ
  - SYR
  - TLS
  - TUV
  - USA
  - VEN
  - VNM
  - WSM
  - YEM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2024-01-01'
temporal_resolution: null
title: 'HDX HAPI - Coordination & Context: National Risk'
version: null
vulnerability: null
---
