---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/peru-earthquake-eq-us7000lkb1
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/peru-earthquake-eq-us7000lkb1
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/peru-earthquake-eq-us7000lkb1
dataset_id: rdls_hl-per_wfpadam_earthquake62mdec2023_20231220
description: 'ADAM ID: eq_us7000lkb1 Magnitude 6.2 earthquake at 93.43 depth occurred
  on Dec 20 2023 in 12km S of Iray. It impacted 32748 people. The epicentre was at
  latitude -15.9595 longitude -72.6028.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/peru-earthquake-eq-us7000lkb1]'
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
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: ADAM system collected earthquake parameters (magnitude 6.2, epicenter
    coordinates, depth) from seismic networks and overlaid observed ground motion
    intensity (MMI) with gridded population data to estimate affected population counts
    by administrative division.
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
- href: https://data.humdata.org/dataset/peru-earthquake-eq-us7000lkb1
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by ground shaking from the 6.2 magnitude earthquake
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
  description: 'Peru: Earthquake - 6.2M - Dec 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/35fe5d11-6a05-4ea8-8fa7-ff63cdc6fe07/resource/8ecd4b8d-6701-4fae-bb37-63803ee940df/download/sm-us7000lkb1-sm-us7000lkb1-pop-estimation.csv
  format: null
  id: resource_8ecd4b8d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000lkb1-sm-us7000lkb1-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-per_wfpadam_earthquake62mdec2023_20231220
spatial:
  bbox: null
  centroid: null
  countries:
  - PER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-12-20'
temporal_resolution: null
title: 'Peru: Earthquake - 6.2M - Dec 2023'
version: null
vulnerability: null
---
