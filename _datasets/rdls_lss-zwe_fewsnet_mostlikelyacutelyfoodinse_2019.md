---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/zimbabwe_most_likely_fewsnet_fipe
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/zimbabwe_most_likely_fewsnet_fipe
dataset_id: rdls_lss-zwe_fewsnet_mostlikelyacutelyfoodinse_2019
description: 'Zimbabwe Most Likely FEWS NET Acutely Food Insecure Population Estimates
  Data from 2019. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/zimbabwe_most_likely_fewsnet_fipe]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: FEWS NET enumerators conducted regular (typically monthly) surveys
    across Zimbabwe to estimate acutely food insecure populations under different
    scenarios. Population estimates were aggregated to produce most likely food insecurity
    impact figures for 2019.
  sources:
  - id: source_1
    license: null
    name: FEWS NET
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/zimbabwe_most_likely_fewsnet_fipe
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acutely food insecure population estimates from drought-driven food
      insecurity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Acutely Food Insecure Population Estimates in different scenarios collected
  by FEWS NET enumerators on a regular schedule (typically monthly).
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zimbabwe Most Likely FEWS NET Acutely Food Insecure Population Estimates
    Data from 2019
  download_url: https://fdw.fews.net/api/ipcpopulationsize/?preference=best&country=ZW&scenario=ML&format=xlsx
  format: null
  id: resource_5717d751
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zimbabwe Most Likely FEWS NET Acutely Food Insecure Population Estimates
    Data from 2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zimbabwe Most Likely FEWS NET Acutely Food Insecure Population Estimates
    Data from 2019
  download_url: https://fdw.fews.net/api/ipcpopulationsize/?preference=best&country=ZW&scenario=ML&format=csv
  format: null
  id: resource_72e12656
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zimbabwe Most Likely FEWS NET Acutely Food Insecure Population Estimates
    Data from 2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zimbabwe Most Likely FEWS NET Acutely Food Insecure Population Estimates
    Data from 2019
  download_url: https://fdw.fews.net/api/ipcpopulationsize/?preference=best&country=ZW&scenario=ML&format=json
  format: null
  id: resource_8cd379ac
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zimbabwe Most Likely FEWS NET Acutely Food Insecure Population Estimates
    Data from 2019
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-zwe_fewsnet_mostlikelyacutelyfoodinse_2019
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
  end: '2026-05-31'
  start: '2019-07-01'
temporal_resolution: null
title: Zimbabwe Most Likely FEWS NET Acutely Food Insecure Population Estimates Data
version: null
vulnerability: null
---
