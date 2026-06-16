---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/china-earthquake-eq-us7000ljvg
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-earthquake-eq-us7000ljvg
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-earthquake-eq-us7000ljvg
dataset_id: rdls_hl-chn_wfpadam_earthquake60mdec2023_20231218
description: 'ADAM ID: eq_us7000ljvg Magnitude 6.0 earthquake at 10.0 depth occurred
  on Dec 18 2023 in 5km NW of Jishishan Bonan. It impacted 867547 people. The epicentre
  was at latitude 35.7339 longitude 102.8364.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/china-earthquake-eq-us7000ljvg]'
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
license: CC-BY-SA-4.0
lineage:
  description: 'Post-event earthquake impact assessment derived from USGS ShakeMaps
    (ADAM ID: us7000ljvg) intersected with gridded population data to estimate affected
    population counts by Modified Mercalli Intensity (MMI) zones across administrative
    divisions in the Jishishan region.'
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
- href: https://data.humdata.org/dataset/china-earthquake-eq-us7000ljvg
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking at different MMI
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
  description: 'China: Earthquake - 6.0M - Dec 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/f86746c9-95b0-49c7-b06e-fc9dcbc78d48/resource/fe37ca6b-a574-40d3-9317-e0531c23870b/download/sm-us7000ljvg-sm-us7000ljvg-pop-estimation.csv
  format: null
  id: resource_fe37ca6b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000ljvg-sm-us7000ljvg-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-chn_wfpadam_earthquake60mdec2023_20231218
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
  start: '2023-12-18'
temporal_resolution: null
title: 'China: Earthquake - 6.0M - Dec 2023'
version: null
vulnerability: null
---
