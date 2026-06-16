---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/philippines-cyclone-1000999
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-cyclone-1000999
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-cyclone-1000999
dataset_id: rdls_hel-phl_wfpadam_cyclonecategory4aug2023_202308
description: 'A cyclone (category 4) during the period Aug 23 2023-Aug 29 2023 in
  Philippines. It impacted 3624 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/philippines-cyclone-1000999]'
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
  event_sets:
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
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM collected observed tropical cyclone track geometry and wind
    speed data for the August 2023 Category 4 typhoon event in the Philippines. Population
    exposure was estimated within the affected area using spatial analysis, and affected
    population counts were derived from the intersection of cyclone impact zones with
    population data.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-cyclone-1000999
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Category 4 tropical cyclone
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
  description: 'Philippines: Cyclone - Category 4 - Aug 2023 (Shape File)'
  download_url: https://adam-project-prod.s3-eu-west-1.amazonaws.com/adam_ts/events/2023/08/1000999_23/ADAM_TS_1000999_23_shp.zip
  format: null
  id: resource_431dfa5a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ADAM_TS_1000999_23_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines: Cyclone - Category 4 - Aug 2023 (Population Estimation)'
  download_url: https://adam-project-prod.s3-eu-west-1.amazonaws.com/adam_ts/events/2023/08/1000999_23/ADAM_TS_1000999_23_pop_estimation.csv
  format: null
  id: resource_6b0b077a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ADAM_TS_1000999_23_pop_estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_wfpadam_cyclonecategory4aug2023_202308
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
  end: '2023-08-29'
  start: '2023-08-23'
temporal_resolution: null
title: 'Philippines: Cyclone - Category 4 - Aug 2023'
version: null
vulnerability: null
---
