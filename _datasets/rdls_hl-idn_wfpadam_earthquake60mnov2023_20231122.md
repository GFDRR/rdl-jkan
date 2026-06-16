---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us6000lpyx
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us6000lpyx
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us6000lpyx
dataset_id: rdls_hl-idn_wfpadam_earthquake60mnov2023_20231122
description: 'ADAM ID: eq_us6000lpyx Magnitude 6.0 earthquake at 115.83 depth occurred
  on Nov 22 2023 in 72km W of Danau. It impacted 8055 people. The epicentre was at
  latitude 1.7425 longitude 127.1526.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indonesia-earthquake-eq-us6000lpyx]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    earthquake:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM system processed observed earthquake parameters (magnitude
    6.0, epicenter coordinates, depth) and generated MMI intensity estimates across
    administrative divisions. Population exposure data was intersected with MMI zones
    to estimate affected population counts by administrative level.
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
- href: https://data.humdata.org/dataset/indonesia-earthquake-eq-us6000lpyx
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking, estimated at 8055
      people
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
  description: 'Indonesia: Earthquake - 6.0M - Nov 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/3e8f76dc-dd01-4e44-84ca-f148a399820f/resource/f7d541f7-f4ed-440b-af88-f46d423733e3/download/sm-us6000lpyx-sm-us6000lpyx-pop-estimation.csv
  format: null
  id: resource_f7d541f7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us6000lpyx-sm-us6000lpyx-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-idn_wfpadam_earthquake60mnov2023_20231122
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
  start: '2023-11-22'
temporal_resolution: null
title: 'Indonesia: Earthquake - 6.0M - Nov 2023'
version: null
vulnerability: null
---
