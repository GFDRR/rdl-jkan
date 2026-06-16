---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000knq0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000knq0
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000knq0
dataset_id: rdls_hl-vut_wfpadam_earthquake65maug2023_20230816
description: "ADAM ID: eq_us7000knq0 Magnitude 6.5 earthquake at 192.955 depth occurred\
  \ on Aug 16 2023 in 33km W of V\xC3\xA9tuboso. It impacted 3825 people. The epicentre\
  \ was at latitude -13.8814 longitude 167.1582.. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000knq0]"
details: null
exposure: []
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: ADAM system processed observed earthquake parameters (magnitude 6.5,
    epicenter location, depth) and derived ground motion intensity (MMI) distribution
    across administrative divisions. Population exposure data was intersected with
    MMI intensity zones to estimate affected population counts by intensity level.
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
- href: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000knq0
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking at different MMI
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
  description: 'Vanuatu: Earthquake - 6.5M - Aug 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/389e4855-da34-4498-986b-82298f1aec60/resource/3274351c-c513-48bd-9fb2-83bab24a7013/download/sm-us7000knq0-sm-us7000knq0-pop-estimation.csv
  format: null
  id: resource_3274351c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000knq0-sm-us7000knq0-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vut_wfpadam_earthquake65maug2023_20230816
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-08-16'
temporal_resolution: null
title: 'Vanuatu: Earthquake - 6.5M - Aug 2023'
version: null
vulnerability: null
---
