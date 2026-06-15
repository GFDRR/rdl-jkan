---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/japan-cyclone-1000986
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/japan-cyclone-1000986
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/japan-cyclone-1000986
dataset_id: rdls_hel-jpn_wfpadam_cyclonetropicaldepression_2023
description: 'A cyclone (tropical depression) during the period Jul 27 2023-Aug 10
  2023 in Japan. It impacted 1141318 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/japan-cyclone-1000986]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone winds in affected areas
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
  description: ADAM collected geospatial cyclone track data (shapefile with wind speed
    attributes) and integrated it with population distribution data to estimate affected
    populations during the tropical depression event of July 27-August 10, 2023 in
    Japan. The system processed observed meteorological parameters and spatial overlays
    to generate impact assessments.
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
- href: https://data.humdata.org/dataset/japan-cyclone-1000986
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone event in Japan
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
  description: 'Japan: Cyclone - Tropical depression - Aug 2023 (Shape File)'
  download_url: https://adam-project-prod.s3-eu-west-1.amazonaws.com/adam_ts/events/2023/08/1000986_59/ADAM_TS_1000986_59_shp.zip
  format: null
  id: resource_e9e59ef5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ADAM_TS_1000986_59_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Japan: Cyclone - Tropical depression - Aug 2023 (Population Estimation)'
  download_url: https://adam-project-prod.s3-eu-west-1.amazonaws.com/adam_ts/events/2023/08/1000986_59/ADAM_TS_1000986_59_pop_estimation.csv
  format: null
  id: resource_56bae613
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ADAM_TS_1000986_59_pop_estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-jpn_wfpadam_cyclonetropicaldepression_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - JPN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-08-10'
  start: '2023-07-27'
temporal_resolution: null
title: 'Japan: Cyclone - Tropical depression - Aug 2023'
version: null
vulnerability: null
---
