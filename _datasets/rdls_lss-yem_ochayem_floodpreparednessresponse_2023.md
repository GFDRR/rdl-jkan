---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Yemen
  url: https://data.humdata.org/dataset/yemen-flood-preparedness-and-response
creator:
  affiliation: null
  email: null
  name: OCHA Yemen
  url: https://data.humdata.org/dataset/yemen-flood-preparedness-and-response
dataset_id: rdls_lss-yem_ochayem_floodpreparednessresponse_2023
description: 'Governorates coverage, flood impact, flood response, civilian causalities,
  and stocks.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-flood-preparedness-and-response]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event flood impact data collected through humanitarian cluster
    coordination and operational response monitoring by OCHA Yemen. Data aggregates
    casualty figures, affected populations, and humanitarian assistance records from
    multiple partner organizations across governorates and districts, compiled into
    registry format for preparedness and response tracking.
  sources:
  - id: source_1
    license: null
    name: OCHA Yemen
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/yemen-flood-preparedness-and-response
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Number of individuals impacted by flooding events
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
    description: Civilian deaths caused by flooding
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Civilian injuries caused by flooding
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
        metric: ppl_injured
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
  description: Governorates coverage, flood impact, flood response, civilian causalities,
    and stocks in 2025.
  download_url: https://data.humdata.org/dataset/dbe2b285-2665-4b37-99f7-da321e4358d2/resource/d6c2386c-2c4e-4e8c-b858-a22cda9daa4a/download/flood_operational_response_monitoring_20250701_110241_utc_03_00.xlsx
  format: null
  id: resource_d6c2386c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Flood_Operational_Response_Monitoring_20250701_110241_UTC_03_00.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Governorates coverage, flood impact, flood response, civilian causalities,
    and stocks in 2024.
  download_url: https://data.humdata.org/dataset/dbe2b285-2665-4b37-99f7-da321e4358d2/resource/df58f9d5-26fe-4568-a312-a135cb201768/download/preparedness-and-response-to-floods-data.xlsx
  format: null
  id: resource_df58f9d5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Preparedness and Response to Floods Data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Governorates coverage, flood impact, flood response, civilian causalities,
    and stocks in 2023.
  download_url: https://data.humdata.org/dataset/dbe2b285-2665-4b37-99f7-da321e4358d2/resource/de084ef5-7bd8-4945-8214-046ae6ca32b3/download/preparedness_and_response_to_floods-2023.xlsx
  format: null
  id: resource_de084ef5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Operational capacity and flood impacts 2023.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_ochayem_floodpreparednessresponse_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-02'
  start: '2023-07-01'
temporal_resolution: null
title: 'Yemen: Flood Preparedness and Response'
version: null
vulnerability: null
---
