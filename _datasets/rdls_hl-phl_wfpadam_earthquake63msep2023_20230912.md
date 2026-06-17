---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000kv90
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000kv90
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000kv90
dataset_id: rdls_hl-phl_wfpadam_earthquake63msep2023_20230912
description: 'ADAM ID: eq_us7000kv90 Magnitude 6.3 earthquake at 41.281 depth occurred
  on Sep 12 2023 in 29km W of Calayan. It impacted 11275 people. The epicentre was
  at latitude 19.2687 longitude 121.2178.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000kv90]'
details: null
exposure: []
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
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: 'ADAM system processed the 6.3 magnitude earthquake event (USGS ID:
    us7000kv90) occurring 29 km west of Calayan on 12 September 2023, deriving population
    exposure to ground motion intensity zones (MMI 3-6) by administrative division
    using shakemap outputs and gridded population data.'
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
- href: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000kv90
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking across MMI intensity
      zones
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
  description: 'Philippines: Earthquake - 6.3M - Sep 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/90b74ae0-4809-42d2-a84a-65c7319d56d6/resource/3e8b195b-d923-41df-8029-7a10062f98d4/download/sm-us7000kv90-sm-us7000kv90-pop-estimation.csv
  format: null
  id: resource_3e8b195b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000kv90-sm-us7000kv90-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_wfpadam_earthquake63msep2023_20230912
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-12'
temporal_resolution: null
title: 'Philippines: Earthquake - 6.3M - Sep 2023'
version: null
vulnerability: null
---
