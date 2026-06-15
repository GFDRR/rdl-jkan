---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000lfmi
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000lfmi
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000lfmi
dataset_id: rdls_hl-phl_wfpadam_earthquake60mdec2023_20231202
description: 'ADAM ID: eq_us7000lfmi Magnitude 6.0 earthquake at 49.093 depth occurred
  on Dec 02 2023 in 56km E of Hinatuan. It impacted 6315 people. The epicentre was
  at latitude 8.3525 longitude 126.8427.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000lfmi]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    earthquake:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM system processed observed earthquake parameters (magnitude
    6.0, epicenter location, depth) and integrated gridded population data to estimate
    affected population counts stratified by Modified Mercalli Intensity (MMI) levels
    across administrative divisions in Davao Oriental province.
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
- href: https://data.humdata.org/dataset/philippines-earthquake-eq-us7000lfmi
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking across MMI intensity
      levels
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
  description: 'Philippines: Earthquake - 6.0M - Dec 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/ecc66016-eba8-4ead-a59d-3aecb5659c57/resource/b720bc5f-acf1-40cd-ba65-4ba11c040674/download/sm-us7000lfmi-sm-us7000lfmi-pop-estimation.csv
  format: null
  id: resource_b720bc5f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000lfmi-sm-us7000lfmi-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_wfpadam_earthquake60mdec2023_20231202
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
  start: '2023-12-02'
temporal_resolution: null
title: 'Philippines: Earthquake - 6.0M - Dec 2023'
version: null
vulnerability: null
---
