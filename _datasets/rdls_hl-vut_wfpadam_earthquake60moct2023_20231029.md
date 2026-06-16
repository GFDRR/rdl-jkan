---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000l7b6
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000l7b6
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000l7b6
dataset_id: rdls_hl-vut_wfpadam_earthquake60moct2023_20231029
description: 'ADAM ID: eq_us7000l7b6 Magnitude 6.0 earthquake at 79.858 depth occurred
  on Oct 29 2023 in 51km W of Imanaka. It impacted 10 people. The epicentre was at
  latitude -19.415 longitude 168.7704.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000l7b6]'
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
  description: ADAM system processed the USGS earthquake event (us7000l7b6) with magnitude
    6.0 and depth 79.858 km, derived ground motion intensity (MMI) estimates, and
    intersected with population data to estimate affected populations by administrative
    division and intensity level (MMI 3-4).
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
- href: https://data.humdata.org/dataset/vanuatu-earthquake-eq-us7000l7b6
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
  description: 'Vanuatu: Earthquake - 6.0M - Oct 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/5931d34b-d323-4ce8-a604-d2d8c12b6075/resource/90704fc0-e557-4a30-bc87-795b040fc6ed/download/sm-us7000l7b6-sm-us7000l7b6-pop-estimation.csv
  format: null
  id: resource_90704fc0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000l7b6-sm-us7000l7b6-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vut_wfpadam_earthquake60moct2023_20231029
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
  start: '2023-10-29'
temporal_resolution: null
title: 'Vanuatu: Earthquake - 6.0M - Oct 2023'
version: null
vulnerability: null
---
