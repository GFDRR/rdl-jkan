---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9ku
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9ku
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9ku
dataset_id: rdls_hel-idn_wfpadam_earthquake67mnov2023_20231108
description: 'ADAM ID: eq_us7000l9ku Magnitude 6.7 earthquake at 10.0 depth occurred
  on Nov 08 2023 in Banda Sea. It impacted 0 people. The epicentre was at latitude
  -6.1455 longitude 129.9137.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9ku]'
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
  - analysis_type: empirical
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
  description: WFP ADAM processed the magnitude 6.7 earthquake event (USGS ID us7000l9ku)
    occurring in Banda Sea on 8 November 2023 to generate empirical ground motion
    intensity estimates (MMI levels 3-6) and spatially distributed population exposure
    by administrative division, producing a post-event impact assessment dashboard.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9ku
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking stratified by MMI
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Indonesia: Earthquake - 6.7M - Nov 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/4103eef8-78d2-4e74-8da2-841abe0daadf/resource/1bcb25e3-94bc-4b33-b463-1660ee9027aa/download/sm-us7000l9ku-sm-us7000l9ku-pop-estimation.csv
  format: null
  id: resource_1bcb25e3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000l9ku-sm-us7000l9ku-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_wfpadam_earthquake67mnov2023_20231108
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-08'
temporal_resolution: null
title: 'Indonesia: Earthquake - 6.7M - Nov 2023'
version: null
vulnerability: null
---
