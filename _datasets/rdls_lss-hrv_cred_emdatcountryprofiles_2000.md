---
attributions:
- entity:
    affiliation: null
    email: null
    name: 'EM-DAT: The Emergency Events Database'
    url: https://data.humdata.org/dataset/emdat-country-profiles-hrv
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-hrv
creator:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-hrv
dataset_id: rdls_lss-hrv_cred_emdatcountryprofiles_2000
description: 'Aggregated figures for natural hazard related events in EM-DAT: Croatia
  Documentation on the Country Profiles available here How to cite the EM-DAT Project
  here Main dataset on HDX: EM-DAT - Country Profiles More on the EM-DAT database
  : website / data portal Each line corresponds to a given combination of year, country,
  disaster subtype and reports figures for : number of disasters total number of people
  affected total number of deaths economic losses (original value and adjusted). [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/emdat-country-profiles-hrv]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: EM-DAT country profiles are derived from the global EM-DAT disaster
    database maintained by CRED, which aggregates disaster impact data from UN agencies,
    governmental and non-governmental sources, insurance companies, research institutes,
    and press agencies. For Croatia, records are filtered and aggregated by year,
    disaster group, type, and subtype to produce annual summary statistics including
    total events, total affected, total deaths, and total economic damage in both
    original and inflation-adjusted USD. The resulting dataset provides a historical
    time-series of multi-hazard disaster impacts at the national level for use in
    disaster risk analysis and policy.
  sources:
  - id: source_1
    license: null
    name: 'EM-DAT: The Emergency Events Database'
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/emdat-country-profiles-hrv
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by flood events in Croatia as recorded
      in EM-DAT
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
    description: Total deaths from flood events in Croatia as recorded in EM-DAT
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
        metric: casualty_count
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Total economic damage (original and adjusted USD) from flood events
      in Croatia as recorded in EM-DAT
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
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Total population affected by earthquake events in Croatia as recorded
      in EM-DAT
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  - asset_category: population
    asset_dimension: population
    description: Total deaths from earthquake events in Croatia as recorded in EM-DAT
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Total economic damage from earthquake events in Croatia as recorded
      in EM-DAT
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_6
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Total population affected by landslide events in Croatia as recorded
      in EM-DAT
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_7
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
    description: Total population affected by wildfire events in Croatia as recorded
      in EM-DAT
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_8
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
  description: 'EM-DAT - Country Profiles, Croatia (Version: 2026-01-30)'
  download_url: https://data.humdata.org/dataset/007beaa0-305d-4006-8b5a-a6ae43668082/resource/09ccaf3c-07df-4531-a4fe-aa36a85741fe/download/emdat-country-profiles_hrv_2026_01_30.xlsx
  format: null
  id: resource_09ccaf3c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EMDAT-country-profiles_HRV_2026_01_30.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hrv_cred_emdatcountryprofiles_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - HRV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: EM-DAT - Country Profiles, Croatia
version: null
vulnerability: null
---
