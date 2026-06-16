---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000kv0k
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000kv0k
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000kv0k
dataset_id: rdls_hl-idn_wfpadam_earthquake60msep2023_20230911
description: 'ADAM ID: eq_us7000kv0k Magnitude 6.0 earthquake at 162.544 depth occurred
  on Sep 11 2023 in 0km SE of Akelamo. It impacted 506970 people. The epicentre was
  at latitude 1.1251 longitude 127.4792.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000kv0k]'
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
  description: ADAM system processed observed earthquake parameters (magnitude 6.0,
    epicenter location, depth) and integrated with gridded population data to estimate
    affected population counts by administrative division, stratified by Modified
    Mercalli Intensity (MMI) levels.
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
- href: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000kv0k
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking across administrative
      divisions
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
  description: 'Indonesia: Earthquake - 6.0M - Sep 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/5e15969e-0e4a-4285-bf44-ba78bcc54013/resource/03965dbc-f7dd-413a-9732-2d70341ac67f/download/sm-us7000kv0k-sm-us7000kv0k-pop-estimation.csv
  format: null
  id: resource_03965dbc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000kv0k-sm-us7000kv0k-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-idn_wfpadam_earthquake60msep2023_20230911
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
  start: '2023-09-11'
temporal_resolution: null
title: 'Indonesia: Earthquake - 6.0M - Sep 2023'
version: null
vulnerability: null
---
