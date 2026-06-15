---
attributions:
- entity:
    affiliation: null
    email: null
    name: EM-DAT
    url: https://data.humdata.org/dataset/haiti-natural-disaster-incidents
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/haiti-natural-disaster-incidents
creator:
  affiliation: null
  email: null
  name: OCHA Haiti
  url: https://data.humdata.org/dataset/haiti-natural-disaster-incidents
dataset_id: rdls_lss-hti_ochahti_naturaldisasterincidents_1909
description: 'Haiti natural disaster incidents dating from 1909 up to 2022.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/haiti-natural-disaster-incidents]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Natural disaster incident records for Haiti were extracted from the
    EM-DAT database, which compiles historical disaster events from multiple international
    sources. The dataset contains post-event impact data including affected populations
    and hazard types spanning over a century of disaster occurrences in Haiti.
  sources:
  - id: source_1
    license: null
    name: EM-DAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-natural-disaster-incidents
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood events in Haiti from 1909-2022
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
    description: Population affected by convective storm events in Haiti from 1909-2022
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
    description: Population affected by strong wind events in Haiti from 1909-2022
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
    description: Population affected by earthquake events in Haiti from 1909-2022
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
  description: Haiti - Natural Disaster Incidents (HT_Climato-Hydro-Meteo_EMDAT_Data
    20220623)
  download_url: https://data.humdata.org/dataset/5079795b-f11a-4102-85a5-d8c3f709ef64/resource/60d15653-37e7-433c-87a4-20826ef74456/download/ht_climato-hydro-meteo_emdat_data-20220623.xlsx
  format: null
  id: resource_60d15653
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: HT_Climato-Hydro-Meteo_EMDAT_Data 20220623
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_ochahti_naturaldisasterincidents_1909
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-06-23'
  start: '1909-01-01'
temporal_resolution: null
title: Haiti - Natural Disaster Incidents
version: null
vulnerability: null
---
