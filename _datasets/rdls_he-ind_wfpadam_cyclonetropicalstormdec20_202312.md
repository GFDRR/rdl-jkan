---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/india-cyclone-1001037
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/india-cyclone-1001037
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/india-cyclone-1001037
dataset_id: rdls_he-ind_wfpadam_cyclonetropicalstormdec20_202312
description: 'ADAM ID: 1001037_6 Cyclone (tropical storm) during the period Dec 03
  2023-Dec 04 2023 in India. It impacted 0 people.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/india-cyclone-1001037]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speeds at 60 km/h and
      90 km/h thresholds
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
  description: WFP ADAM system collected and processed geospatial data on the December
    2023 tropical cyclone event in India, generating cyclone track geometries with
    wind speed attributes and estimating population exposure at wind speed thresholds
    (60 km/h and 90 km/h) across administrative divisions for operational emergency
    response mapping.
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
- href: https://data.humdata.org/dataset/india-cyclone-1001037
  rel: source
loss: null
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
  description: 'India: Cyclone - Tropical storm - Dec 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/4f000868-164e-40ca-8519-e123bf320d69/resource/3ed80991-1272-48bb-8be1-08a65b757784/download/1001037-8-adam-ts-1001037-8-shp.zip
  format: null
  id: resource_3ed80991
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001037-8-adam-ts-1001037-8-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'India: Cyclone - Tropical storm - Dec 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/4f000868-164e-40ca-8519-e123bf320d69/resource/d50fff90-3231-470b-9eaa-2f5cee31bd81/download/1001037-8-adam-ts-1001037-8-pop-estimation.csv
  format: null
  id: resource_d50fff90
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001037-8-adam-ts-1001037-8-pop-estimation.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-ind_wfpadam_cyclonetropicalstormdec20_202312
spatial:
  bbox: null
  centroid: null
  countries:
  - IND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-04'
  start: '2023-12-03'
temporal_resolution: null
title: 'India: Cyclone - Tropical storm - Dec 2023'
version: null
vulnerability: null
---
