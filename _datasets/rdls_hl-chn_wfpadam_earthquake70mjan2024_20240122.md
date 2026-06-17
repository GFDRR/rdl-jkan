---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/china-earthquake-eq-us7000lsze
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-earthquake-eq-us7000lsze
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-earthquake-eq-us7000lsze
dataset_id: rdls_hl-chn_wfpadam_earthquake70mjan2024_20240122
description: 'ADAM ID: eq_us7000lsze Magnitude 7.0 earthquake at 27.366 depth occurred
  on Jan 22 2024 in 70km W of Wushi. It impacted 24706 people. The epicentre was at
  latitude 41.2938 longitude 78.5937.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/china-earthquake-eq-us7000lsze]'
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
  description: 'Post-event earthquake ground motion intensity (MMI) distribution derived
    from the USGS ShakeCast system (ADAM ID: eq_us7000lsze) for the 7.0 magnitude
    Wushi earthquake. Population exposure data was intersected with MMI intensity
    zones to estimate affected populations at different hazard intensity levels across
    administrative divisions.'
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
- href: https://data.humdata.org/dataset/china-earthquake-eq-us7000lsze
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking at different Modified
      Mercalli Intensity levels
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
  description: 'China: Earthquake - 7.0M - Jan 2024 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/5ac85b5f-d232-45c6-9fef-a524aed2a5dc/resource/1e7339f9-7832-4b1c-a889-784afe27f1b3/download/sm-us7000lsze-sm-us7000lsze-pop-estimation.csv
  format: null
  id: resource_1e7339f9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000lsze-sm-us7000lsze-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-chn_wfpadam_earthquake70mjan2024_20240122
spatial:
  bbox: null
  centroid: null
  countries:
  - CHN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-01-22'
temporal_resolution: null
title: 'China: Earthquake - 7.0M - Jan 2024'
version: null
vulnerability: null
---
