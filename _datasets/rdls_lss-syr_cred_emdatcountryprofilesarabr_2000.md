---
attributions:
- entity:
    affiliation: null
    email: null
    name: EM-DAT (Emergency Events Database)
    url: https://data.humdata.org/dataset/emdat-country-profiles-syr
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-syr
creator:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-syr
dataset_id: rdls_lss-syr_cred_emdatcountryprofilesarabr_2000
description: 'Aggregated figures for natural hazard related events in EM-DAT: Syrian
  Arab Republic Documentation on the Country Profiles available here How to cite the
  EM-DAT Project here Main dataset on HDX: EM-DAT - Country Profiles More on the EM-DAT
  database : website / data portal Each line corresponds to a given combination of
  year, country, disaster subtype and reports figures for : number of disasters total
  number of people affected total number of deaths economic losses (original value
  and adjusted). [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/emdat-country-profiles-syr]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: EM-DAT aggregates post-event impact data from multiple sources (governments,
    UN agencies, NGOs, media) into a standardized registry of natural disasters. This
    country profile for Syria presents historical disaster event records with total
    affected populations, deaths, and economic damages by disaster type and year.
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
- href: https://data.humdata.org/dataset/emdat-country-profiles-syr
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
  description: 'EM-DAT - Country Profiles, Syrian Arab Republic (Version: 2026-01-30)'
  download_url: https://data.humdata.org/dataset/42abe33a-26a2-4b70-be84-eb3b6b69d1c7/resource/b487a3dd-30d7-41ea-b403-f4750cb54098/download/emdat-country-profiles_syr_2026_01_30.xlsx
  format: null
  id: resource_b487a3dd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EMDAT-country-profiles_SYR_2026_01_30.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_cred_emdatcountryprofilesarabr_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: EM-DAT - Country Profiles, Syrian Arab Republic
version: null
vulnerability: null
---
