---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000lfn5
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000lfn5
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000lfn5
dataset_id: rdls_hl-afg_wfpadam_earthquake63moct2023_20231015
description: 'ADAM ID: eq_us6000lfn5 Magnitude 6.3 earthquake at 8.219 depth occurred
  on Oct 15 2023 in 22km SW of Koshk. It impacted 1185926 people. The epicentre was
  at latitude 34.6171 longitude 62.0517.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000lfn5]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: ADAM system processed the USGS earthquake event (us6000lfn5) by overlaying
    observed ground motion intensity (MMI) zones with gridded population data to estimate
    affected population counts by administrative division and intensity level.
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
- href: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000lfn5
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
  description: 'Afghanistan: Earthquake - 6.3M - Oct 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/dbe0f6e6-38f7-4453-9d3b-6ab08f874038/resource/5324bc31-fd11-40b5-b9aa-10496b168e4a/download/sm-us6000lfn5-sm-us6000lfn5-pop-estimation.csv
  format: null
  id: resource_5324bc31
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us6000lfn5-sm-us6000lfn5-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_wfpadam_earthquake63moct2023_20231015
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-15'
temporal_resolution: null
title: 'Afghanistan: Earthquake - 6.3M - Oct 2023'
version: null
vulnerability: null
---
