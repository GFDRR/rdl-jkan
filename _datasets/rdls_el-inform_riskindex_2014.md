---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-risk-index-2021
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-risk-index-2021
dataset_id: rdls_el-inform_riskindex_2014
description: 'The INFORM Risk Index is a global, open-source risk assessment for humanitarian
  crises and disasters. It can support decisions about prevention, preparedness and
  response.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/inform-risk-index-2021]'
details: null
exposure:
- asset_type:
    description: Population exposed to multiple hazards including earthquakes, floods,
      tsunamis, cyclones, coastal floods, and drought
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
hazard: null
license: CC-BY-4.0
lineage:
  description: INFORM Risk Index is a composite indicator methodology that integrates
    multi-hazard exposure data (earthquake, flood, tsunami, cyclone, coastal flood,
    drought) with population vulnerability indicators (demographics, health, poverty,
    development indices) and historical disaster impact records to produce a global
    risk assessment. Source data are compiled from international databases and national
    statistics, processed through imputation and standardization procedures, and combined
    using a weighted composite indicator framework to generate country-level risk
    scores and trend analysis from 2014-2025.
  sources:
  - id: source_1
    license: null
    name: INFORM
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: INFORM
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: INFORM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-risk-index-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by natural disasters including earthquakes
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
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
    description: Population affected by natural disasters including floods
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by natural disasters including drought
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Risk Index (INFORM Risk v 0.7.0)
  download_url: https://data.humdata.org/dataset/f5ec2ee7-8a1b-49b4-864b-70bdb582a022/resource/11a789fc-e9b3-48c6-b1e6-260959799220/download/inform_risk_2025_v070.xlsx
  format: null
  id: resource_11a789fc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_Risk_2025_v070.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Risk Index (INFORM TREND 2015 - 2024)
  download_url: https://data.humdata.org/dataset/f5ec2ee7-8a1b-49b4-864b-70bdb582a022/resource/9640d1d5-83da-4969-aa6a-52ff57386d10/download/inform2024_trend_2015_2024_v70_all.xlsx
  format: null
  id: resource_9640d1d5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM2024_TREND_2015_2024_v70_ALL.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Risk Index (INFORM Risk v 0.6.8)
  download_url: https://data.humdata.org/dataset/f5ec2ee7-8a1b-49b4-864b-70bdb582a022/resource/0edecb32-4ef4-46ea-92fa-0d8bf24c6834/download/inform_risk_mid_2024_v068.xlsx
  format: null
  id: resource_0edecb32
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_Risk_Mid_2024_v068.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Risk Index (INFORM Risk v 0.6.7)
  download_url: https://data.humdata.org/dataset/f5ec2ee7-8a1b-49b4-864b-70bdb582a022/resource/603e40eb-a620-47e2-b8ac-e51961c7d661/download/inform_risk_2024_v067-.xlsx
  format: null
  id: resource_603e40eb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_Risk_2024_v067 .xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Risk Index (INFORM TREND 2014 - 2023)
  download_url: https://data.humdata.org/dataset/f5ec2ee7-8a1b-49b4-864b-70bdb582a022/resource/a04977ed-ff5d-4b78-a0de-1fdac8765418/download/inform2024_trend_2014_2023_v67_all-.xlsx
  format: null
  id: resource_a04977ed
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM2024_TREND_2014_2023_v67_ALL .xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Risk Index (INFORM Concept and Methodology Version 2017 Pdf
    FINAL.pdf)
  download_url: https://data.humdata.org/dataset/f5ec2ee7-8a1b-49b4-864b-70bdb582a022/resource/93dd74fd-7b9a-4e61-b452-62b3d5bed4ff/download/inform-concept-and-methodology-version-2017-pdf-final-4.pdf
  format: null
  id: resource_93dd74fd
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM Concept and Methodology Version 2017 Pdf FINAL.pdf
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-inform_riskindex_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-03-31'
  start: '2014-01-01'
temporal_resolution: null
title: INFORM Risk Index
version: null
vulnerability: null
---
