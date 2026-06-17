---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/russian-federation-earthquake-eq-us7000ksrl
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/russian-federation-earthquake-eq-us7000ksrl
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/russian-federation-earthquake-eq-us7000ksrl
dataset_id: rdls_hel-rus_wfpadam_federationearthquake61mse_20230901
description: 'ADAM ID: eq_us7000ksrl Magnitude 6.1 earthquake at 141.248 depth occurred
  on Sep 01 2023 in 13 km ENE of Severo-Kuril''sk, Russia. It impacted 2019 people.
  The epicentre was at latitude 50.7026 longitude 156.316.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/russian-federation-earthquake-eq-us7000ksrl]'
details: null
exposure:
- asset_type:
    description: Population distribution by administrative division exposed to earthquake
      ground shaking
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
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system processed observed earthquake parameters (magnitude
    6.1, epicenter location, depth) and derived ground motion intensity (MMI) distribution
    across administrative divisions. Population exposure data was intersected with
    MMI intensity zones to estimate affected population counts by administrative level.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/russian-federation-earthquake-eq-us7000ksrl
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking, stratified by MMI
      intensity levels
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: 'Russian Federation: Earthquake - 6.1M - Sep 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/9f749dfe-cbfc-41f3-b056-9e865420b88d/resource/3b84f316-66cc-4aca-8ceb-c3da21650752/download/sm-us7000ksrl-sm-us7000ksrl-pop-estimation.csv
  format: null
  id: resource_3b84f316
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000ksrl-sm-us7000ksrl-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-rus_wfpadam_federationearthquake61mse_20230901
spatial:
  bbox: null
  centroid: null
  countries:
  - RUS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-01'
temporal_resolution: null
title: 'Russian Federation: Earthquake - 6.1M - Sep 2023'
version: null
vulnerability: null
---
