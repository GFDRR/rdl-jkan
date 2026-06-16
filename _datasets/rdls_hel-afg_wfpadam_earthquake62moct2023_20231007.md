---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000ldpg
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000ldpg
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000ldpg
dataset_id: rdls_hel-afg_wfpadam_earthquake62moct2023_20231007
description: 'ADAM ID: eq_us6000ldpg Magnitude 6.2 earthquake at 10.0 depth occurred
  on Oct 07 2023 in 30km SW of Koshk. It impacted 983360 people. The epicentre was
  at latitude 34.6259 longitude 61.926.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000ldpg]'
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
  description: USGS earthquake parameters (magnitude 6.2, epicenter coordinates, depth)
    were used to generate Modified Mercalli Intensity (MMI) distribution across administrative
    divisions. Population exposure data was intersected with MMI zones to estimate
    affected population counts by intensity level and administrative area.
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
- href: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000ldpg
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total affected population (983,360 people) from 6.2 magnitude earthquake
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
  description: 'Afghanistan: Earthquake - 6.2M - Oct 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/ef6bc5e1-7141-47ec-8450-c2c6a1a5602a/resource/9f019482-676b-4200-b9f3-c60cc083827b/download/sm-us6000ldpg-sm-us6000ldpg-pop-estimation.csv
  format: null
  id: resource_9f019482
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us6000ldpg-sm-us6000ldpg-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-afg_wfpadam_earthquake62moct2023_20231007
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-07'
temporal_resolution: null
title: 'Afghanistan: Earthquake - 6.2M - Oct 2023'
version: null
vulnerability: null
---
