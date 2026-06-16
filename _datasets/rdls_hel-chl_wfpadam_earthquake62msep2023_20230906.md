---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/chile-earthquake-eq-us7000ktti
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/chile-earthquake-eq-us7000ktti
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/chile-earthquake-eq-us7000ktti
dataset_id: rdls_hel-chl_wfpadam_earthquake62msep2023_20230906
description: 'A magnitude 6.2 earthquake at 41.368 depth occurred on Sep 06 2023 in
  42km SW of Coquimbo. It impacted 349977 people. The epicentre was at latitude -30.2775
  longitude -71.536.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/chile-earthquake-eq-us7000ktti]'
details: null
exposure:
- asset_type:
    description: Residential population exposed to earthquake ground motion in the
      affected region
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: ADAM collected observed earthquake parameters (magnitude 6.2, depth,
    epicenter coordinates) from seismic monitoring and integrated gridded population
    exposure data to estimate affected population counts in the impact zone near Coquimbo,
    Chile.
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
- href: https://data.humdata.org/dataset/chile-earthquake-eq-us7000ktti
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population impact from earthquake ground motion
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
  description: 'Chile: Earthquake - 6.2M - Sep 2023 (Population Estimation)'
  download_url: https://adam-project-prod.s3-eu-west-1.amazonaws.com/adam_eq/events/2023/09/sm_us7000ktti/sm_us7000ktti_pop_estimation.csv
  format: null
  id: resource_238cecf8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm_us7000ktti_pop_estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-chl_wfpadam_earthquake62msep2023_20230906
spatial:
  bbox: null
  centroid: null
  countries:
  - CHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-06'
temporal_resolution: null
title: 'Chile: Earthquake - 6.2M - Sep 2023'
version: null
vulnerability: null
---
