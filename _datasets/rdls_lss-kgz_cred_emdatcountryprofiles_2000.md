---
attributions:
- entity:
    affiliation: null
    email: null
    name: 'EM-DAT: Emergency Events Database'
    url: https://data.humdata.org/dataset/emdat-country-profiles-kgz
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-kgz
creator:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-kgz
dataset_id: rdls_lss-kgz_cred_emdatcountryprofiles_2000
description: 'Aggregated figures for natural hazard related events in EM-DAT: Kyrgyzstan
  Documentation on the Country Profiles available here How to cite the EM-DAT Project
  here Main dataset on HDX: EM-DAT - Country Profiles More on the EM-DAT database
  : website / data portal Each line corresponds to a given combination of year, country,
  disaster subtype and reports figures for : number of disasters total number of people
  affected total number of deaths economic losses (original value and adjusted). [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/emdat-country-profiles-kgz]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: EM-DAT aggregates post-event disaster impact data from multiple sources
    including government reports, UN agencies, and media reports. This country profile
    dataset presents compiled statistics for Kyrgyzstan across multiple disaster types
    and subtypes, organized by year with totals for affected populations, deaths,
    and economic damages in both original and inflation-adjusted USD values.
  sources:
  - id: source_1
    license: null
    name: 'EM-DAT: Emergency Events Database'
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/emdat-country-profiles-kgz
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by natural hazard events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
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
    description: Total deaths from natural hazard events
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Total economic damage in USD from natural hazard events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: 'EM-DAT - Country Profiles, Kyrgyzstan (Version: 2026-01-30)'
  download_url: https://data.humdata.org/dataset/cee3e0e5-f623-428f-9cbe-c1c2128d64a9/resource/16987aae-3cc3-4d64-ab21-6a8f8fb487ab/download/emdat-country-profiles_kgz_2026_01_30.xlsx
  format: null
  id: resource_16987aae
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EMDAT-country-profiles_KGZ_2026_01_30.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-kgz_cred_emdatcountryprofiles_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - KGZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: EM-DAT - Country Profiles, Kyrgyzstan
version: null
vulnerability: null
---
