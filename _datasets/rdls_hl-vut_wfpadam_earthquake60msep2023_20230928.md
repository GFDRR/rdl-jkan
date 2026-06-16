---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us6000lbdi
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us6000lbdi
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us6000lbdi
dataset_id: rdls_hl-vut_wfpadam_earthquake60msep2023_20230928
description: 'ADAM ID: eq_us6000lbdi Magnitude 6.0 earthquake at 125.735 depth occurred
  on Sep 28 2023 in 19km SW of Loone. It impacted 12399 people. The epicentre was
  at latitude -15.5748 longitude 167.712.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us6000lbdi]'
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
  description: ADAM system processed the USGS earthquake event (us6000lbdi, magnitude
    6.0, depth 125.735 km) and derived population exposure to ground motion intensity
    (MMI) by intersecting shakemap intensity zones with gridded population data, aggregating
    affected population counts by administrative divisions (ADM0-ADM2).
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
- href: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us6000lbdi
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
  description: 'Vanuatu: Earthquake - 6.0M - Sep 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/598daa99-a470-4ba9-85a3-b583adb62ff7/resource/75d7f619-9c43-48b4-b50b-5951675fbfa9/download/sm-us6000lbdi-sm-us6000lbdi-pop-estimation.csv
  format: null
  id: resource_75d7f619
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us6000lbdi-sm-us6000lbdi-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vut_wfpadam_earthquake60msep2023_20230928
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
  start: '2023-09-28'
temporal_resolution: null
title: 'Vanuatu: Earthquake - 6.0M - Sep 2023'
version: null
vulnerability: null
---
