---
attributions:
- entity:
    affiliation: null
    email: null
    name: EM-DAT (Emergency Events Database)
    url: https://data.humdata.org/dataset/emdat-country-profiles-lao
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-lao
creator:
  affiliation: null
  email: null
  name: Centre for Research on the Epidemiology of Disasters
  url: https://data.humdata.org/dataset/emdat-country-profiles-lao
dataset_id: rdls_lss-lao_cred_emdatcountryprofileslaope_2000
description: 'Aggregated figures for natural hazard related events in EM-DAT: Lao
  People''s Democratic Republic Documentation on the Country Profiles available here
  How to cite the EM-DAT Project here Main dataset on HDX: EM-DAT - Country Profiles
  More on the EM-DAT database : website / data portal Each line corresponds to a given
  combination of year, country, disaster subtype and reports figures for : number
  of disasters total number of people affected total number of deaths economic losses
  (original value and adjusted). [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/emdat-country-profiles-lao]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: EM-DAT aggregates post-event disaster impact data from multiple international
    sources (governments, UN agencies, NGOs, media) into a standardized registry.
    This country profile presents historical disaster event records for Lao PDR with
    aggregated figures by disaster type, including total affected populations, deaths,
    and economic damages in both original and inflation-adjusted USD values.
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
- href: https://data.humdata.org/dataset/emdat-country-profiles-lao
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by flood events
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
    description: Deaths from flood events
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
    description: Economic damage from flood events in USD
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
    description: Total population affected by convective storm events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
    description: Deaths from convective storm events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
    description: Economic damage from convective storm events in USD
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
    description: Total population affected by landslide events
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
    description: Deaths from landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
    description: Economic damage from landslide events in USD
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  description: 'EM-DAT - Country Profiles, Lao People''s Democratic Republic (Version:
    2026-01-30)'
  download_url: https://data.humdata.org/dataset/c9292cc1-6d6c-4525-add4-84628769e546/resource/0e3d0cfe-a676-473b-bddd-3d7874d20cce/download/emdat-country-profiles_lao_2026_01_30.xlsx
  format: null
  id: resource_0e3d0cfe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EMDAT-country-profiles_LAO_2026_01_30.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lao_cred_emdatcountryprofileslaope_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: EM-DAT - Country Profiles, Lao People's Democratic Republic
version: null
vulnerability: null
---
