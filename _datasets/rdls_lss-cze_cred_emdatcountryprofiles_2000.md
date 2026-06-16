---
attributions:
- entity:
    affiliation: null
    email: null
    name: EM-DAT (Emergency Events Database)
    url: https://data.humdata.org/dataset/emdat-country-profiles-cze
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-cze
creator:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-cze
dataset_id: rdls_lss-cze_cred_emdatcountryprofiles_2000
description: 'Aggregated figures for natural hazard related events in EM-DAT: Czechia
  Documentation on the Country Profiles available here How to cite the EM-DAT Project
  here Main dataset on HDX: EM-DAT - Country Profiles More on the EM-DAT database
  : website / data portal Each line corresponds to a given combination of year, country,
  disaster subtype and reports figures for : number of disasters total number of people
  affected total number of deaths economic losses (original value and adjusted). [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/emdat-country-profiles-cze]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: EM-DAT aggregates reported natural disaster events from multiple international
    sources and humanitarian organizations. This country profile dataset compiles
    historical impact records (deaths, affected populations, economic damage) for
    Czechia by disaster type, subtype, and year, derived from the main EM-DAT database.
  sources:
  - id: source_1
    license: null
    name: EM-DAT (Emergency Events Database)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/emdat-country-profiles-cze
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by flood events in Czechia
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
    description: Deaths from flood events in Czechia
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Economic damage from flood events in Czechia
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Total population affected by earthquake events in Czechia
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
    description: Deaths from earthquake events in Czechia
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Economic damage from earthquake events in Czechia
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Total population affected by strong wind events in Czechia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Deaths from strong wind events in Czechia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_8
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
  - asset_category: economic_indicator
    asset_dimension: index
    description: Economic damage from strong wind events in Czechia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_9
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'EM-DAT - Country Profiles, Czechia (Version: 2026-01-30)'
  download_url: https://data.humdata.org/dataset/44f51df9-9492-44ba-9c76-b542401bc419/resource/5f02b110-7985-479f-aea3-de8239d49cfe/download/emdat-country-profiles_cze_2026_01_30.xlsx
  format: null
  id: resource_5f02b110
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EMDAT-country-profiles_CZE_2026_01_30.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cze_cred_emdatcountryprofiles_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - CZE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: EM-DAT - Country Profiles, Czechia
version: null
vulnerability: null
---
