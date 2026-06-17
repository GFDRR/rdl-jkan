---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/china-cyclone-1000985
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-cyclone-1000985
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-cyclone-1000985
dataset_id: rdls_hel-chnphl_wfpadam_cyclonecategory1jul2023_202307
description: 'ADAM ID: 1000985_9 Cyclone (category 1) during the period Jul 21 2023-Jul
  28 2023 in China, Philippines. It impacted 23921068 people.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/china-cyclone-1000985]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone hazard in affected areas
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
  type: strong_wind
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system collected and analyzed geospatial cyclone track data
    with wind speed measurements and overlaid population exposure data to generate
    alerts and impact dashboards for the July 2023 Category 1 cyclone event affecting
    China and Philippines.
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
- href: https://data.humdata.org/dataset/china-cyclone-1000985
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by Category 1 tropical cyclone event
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
        type: total
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
  description: 'China: Cyclone - Category 1 - Jul 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/c2cd7ab4-da41-48ec-aaec-2a0c38a0218f/resource/d1c090b2-36c8-4d04-a79d-59d55768bfac/download/1000985-28-adam-ts-1000985-28-shp.zip
  format: null
  id: resource_d1c090b2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000985-28-adam-ts-1000985-28-shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-chnphl_wfpadam_cyclonecategory1jul2023_202307
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
  end: '2023-07-28'
  start: '2023-07-21'
temporal_resolution: null
title: 'China: Cyclone - Category 1 - Jul 2023'
version: null
vulnerability: null
---
