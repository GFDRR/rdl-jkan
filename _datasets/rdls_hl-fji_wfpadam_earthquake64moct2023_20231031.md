---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/fiji-earthquake-eq-us7000l7qy
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/fiji-earthquake-eq-us7000l7qy
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/fiji-earthquake-eq-us7000l7qy
dataset_id: rdls_hl-fji_wfpadam_earthquake64moct2023_20231031
description: 'ADAM ID: eq_us7000l7qy Magnitude 6.4 earthquake at 547.578 depth occurred
  on Oct 31 2023 in 19km SE of Mago Island. It impacted 1953 people. The epicentre
  was at latitude -17.538 longitude -179.0119.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/fiji-earthquake-eq-us7000l7qy]'
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
  description: WFP ADAM system processed observed earthquake parameters (magnitude
    6.4, epicentre location, depth) and derived MMI ground motion intensity values
    at administrative levels, then intersected with gridded population data to estimate
    affected population counts by administrative division.
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
- href: https://data.humdata.org/dataset/fiji-earthquake-eq-us7000l7qy
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by the 6.4 magnitude earthquake, estimated at
      1953 people
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
  description: 'Fiji: Earthquake - 6.4M - Oct 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/cd2aed89-f350-40cd-bc5d-78fffcb69010/resource/76400a9b-9526-45bd-89f2-6a7853fd0e6d/download/sm-us7000l7qy-sm-us7000l7qy-pop-estimation.csv
  format: null
  id: resource_76400a9b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000l7qy-sm-us7000l7qy-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-fji_wfpadam_earthquake64moct2023_20231031
spatial:
  bbox: null
  centroid: null
  countries:
  - FJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-31'
temporal_resolution: null
title: 'Fiji: Earthquake - 6.4M - Oct 2023'
version: null
vulnerability: null
---
