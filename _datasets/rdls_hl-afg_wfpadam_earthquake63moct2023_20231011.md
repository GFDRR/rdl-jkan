---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000len8
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000len8
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000len8
dataset_id: rdls_hl-afg_wfpadam_earthquake63moct2023_20231011
description: 'ADAM ID: eq_us6000len8 Magnitude 6.3 earthquake at 10.0 depth occurred
  on Oct 11 2023 in 25km SW of Koshk. It impacted 996999 people. The epicentre was
  at latitude 34.5798 longitude 62.0717.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000len8]'
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
license: CC-BY-SA-4.0
lineage:
  description: 'ADAM system processed the USGS earthquake event (ADAM ID: eq_us6000len8,
    magnitude 6.3, 11 October 2023) and generated a shakemap with Modified Mercalli
    Intensity (MMI) zones. Population exposure data was overlaid on MMI intensity
    classes to estimate affected population counts by administrative division and
    intensity level.'
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
- href: https://data.humdata.org/dataset/afghanistan-earthquake-eq-us6000len8
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
  download_url: https://data.humdata.org/dataset/eebbd8a8-3844-4525-a045-081b0abde89b/resource/23924bac-113a-4e0f-81ec-7adbae1f46b1/download/sm-us6000len8-sm-us6000len8-pop-estimation.csv
  format: null
  id: resource_23924bac
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us6000len8-sm-us6000len8-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_wfpadam_earthquake63moct2023_20231011
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
  start: '2023-10-11'
temporal_resolution: null
title: 'Afghanistan: Earthquake - 6.3M - Oct 2023'
version: null
vulnerability: null
---
