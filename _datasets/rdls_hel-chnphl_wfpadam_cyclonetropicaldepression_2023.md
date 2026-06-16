---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/china-cyclone-1000999
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-cyclone-1000999
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-cyclone-1000999
dataset_id: rdls_hel-chnphl_wfpadam_cyclonetropicaldepression_2023
description: 'ADAM ID: 1000999_23 Cyclone (tropical depression) during the period
  Aug 23 2023-Sep 03 2023 in China, Philippines. It impacted 36487954 people.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/china-cyclone-1000999]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speeds at multiple thresholds
      (60, 90, 120 kph)
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
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: ADAM collected observed tropical cyclone track and wind speed data
    for the tropical depression event (Aug 23 - Sep 3, 2023). Wind speed thresholds
    (60, 90, 120 kph) were intersected with gridded population data to estimate exposed
    and affected populations at administrative levels. The resulting shapefile contains
    cyclone track geometry with wind speeds and population estimates, while the CSV
    provides administrative-level population breakdowns by wind speed threshold.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
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
- href: https://data.humdata.org/dataset/china-cyclone-1000999
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by tropical depression cyclone event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: 'China: Cyclone - Tropical depression - Sep 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/4e9511c2-31dc-4b56-b2fe-df707ac52950/resource/4a9d95ec-ef80-4b44-b119-07cceef277df/download/1000999-44-adam-ts-1000999-44-shp.zip
  format: null
  id: resource_4a9d95ec
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000999-44-adam-ts-1000999-44-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China: Cyclone - Tropical depression - Sep 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/4e9511c2-31dc-4b56-b2fe-df707ac52950/resource/13666208-41d3-4c32-a840-aeae67526b30/download/1000999-44-adam-ts-1000999-44-pop-estimation.csv
  format: null
  id: resource_13666208
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000999-44-adam-ts-1000999-44-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-chnphl_wfpadam_cyclonetropicaldepression_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - CHN
  - PHL
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-09-03'
  start: '2023-08-23'
temporal_resolution: null
title: 'China: Cyclone - Tropical depression - Sep 2023'
version: null
vulnerability: null
---
