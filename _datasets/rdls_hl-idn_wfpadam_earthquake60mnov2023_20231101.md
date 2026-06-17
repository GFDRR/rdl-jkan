---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l85t
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l85t
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l85t
dataset_id: rdls_hl-idn_wfpadam_earthquake60mnov2023_20231101
description: 'ADAM ID: eq_us7000l85t Magnitude 6.0 earthquake at 27.656 depth occurred
  on Nov 01 2023 in 19km NW of Oelamasi. It impacted 182248 people. The epicentre
  was at latitude -10.0109 longitude 123.7132.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l85t]'
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
  description: 'ADAM system processed the 6.0 magnitude earthquake event (USGS ID:
    us7000l85t) occurring on Nov 1, 2023 near Oelamasi, Indonesia. Ground motion intensity
    (MMI) was estimated across administrative divisions, and affected population counts
    were derived by intersecting MMI zones with gridded population data to generate
    impact estimates by intensity level.'
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
- href: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l85t
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
  description: 'Indonesia: Earthquake - 6.0M - Nov 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/5bd2c040-6f97-48ab-8631-f385f393d86c/resource/a4cd4a27-ad86-4806-bf67-045503a8db22/download/sm-us7000l85t-sm-us7000l85t-pop-estimation.csv
  format: null
  id: resource_a4cd4a27
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000l85t-sm-us7000l85t-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-idn_wfpadam_earthquake60mnov2023_20231101
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
  start: '2023-11-01'
temporal_resolution: null
title: 'Indonesia: Earthquake - 6.0M - Nov 2023'
version: null
vulnerability: null
---
