---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP ADAM (Advanced Disaster Analysis & Mapping)
    url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000kx7j
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000kx7j
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000kx7j
dataset_id: rdls_hel-vut_wfpadam_earthquake61msep2023_20230921
description: "ADAM ID: eq_us7000kx7j Magnitude 6.1 earthquake at 188.419 depth occurred\
  \ on Sep 21 2023 in 31km W of V\xC3\xA9tuboso. It impacted 4814 people. The epicentre\
  \ was at latitude -14.0039 longitude 167.1898.. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000kx7j]"
details: null
exposure:
- asset_type:
    description: Population counts per administrative unit exposed to different MMI
      shaking intensity levels
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
license: CC-BY-SA-4.0
lineage:
  description: USGS shakemap data for the M6.1 earthquake (event ID us7000kx7j) was
    ingested by WFP ADAM, which overlaid MMI intensity zones with gridded population
    data to estimate the number of people exposed at each shaking level per administrative
    unit. The resulting CSV provides population-by-MMI estimates at ADM2 level for
    Vanuatu.
  sources:
  - id: source_1
    license: null
    name: WFP ADAM (Advanced Disaster Analysis & Mapping)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000kx7j
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated number of people affected by the M6.1 earthquake in Vanuatu,
      September 2023
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
        type: total
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
  description: 'Vanuatu: Earthquake - 6.1M - Sep 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/037c2008-a9bd-49ee-8c9f-48794025aebe/resource/4308f9d3-990e-4a1c-a551-8033d2fda158/download/sm-us7000kx7j-sm-us7000kx7j-pop-estimation.csv
  format: null
  id: resource_4308f9d3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000kx7j-sm-us7000kx7j-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vut_wfpadam_earthquake61msep2023_20230921
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-21'
temporal_resolution: null
title: 'Vanuatu: Earthquake - 6.1M - Sep 2023'
version: null
vulnerability: null
---
