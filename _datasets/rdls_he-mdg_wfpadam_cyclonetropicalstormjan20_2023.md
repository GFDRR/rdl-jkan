---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/madagascar-cyclone-1001040
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/madagascar-cyclone-1001040
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/madagascar-cyclone-1001040
dataset_id: rdls_he-mdg_wfpadam_cyclonetropicalstormjan20_2023
description: 'ADAM ID: 1001040_10 Cyclone (tropical storm) during the period Dec 31
  2023-Jan 03 2024 in Madagascar. It impacted 0 people.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/madagascar-cyclone-1001040]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM system collected and mapped tropical cyclone track data and
    wind speed observations from the January 2024 Madagascar event. Geospatial hazard
    data (shapefile with wind_speed field) was integrated with administrative boundary
    population data to estimate population exposure at wind speed thresholds of 60
    km/h and 90 km/h.
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
- href: https://data.humdata.org/dataset/madagascar-cyclone-1001040
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
  description: 'Madagascar: Cyclone - Tropical storm - Jan 2024 (Shape File)'
  download_url: https://data.humdata.org/dataset/b2b4c3eb-da43-4e84-a596-28b0b6dd0aa0/resource/a0fb7379-5f57-48ef-b442-6e98052f8cf0/download/1001040-13-adam-ts-1001040-13-shp.zip
  format: null
  id: resource_a0fb7379
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001040-13-adam-ts-1001040-13-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Cyclone - Tropical storm - Jan 2024 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/b2b4c3eb-da43-4e84-a596-28b0b6dd0aa0/resource/c340199e-0d49-42d5-a3e4-e2188e1fe3d8/download/1001040-13-adam-ts-1001040-13-pop-estimation.csv
  format: null
  id: resource_c340199e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001040-13-adam-ts-1001040-13-pop-estimation.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mdg_wfpadam_cyclonetropicalstormjan20_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-01-03'
  start: '2023-12-31'
temporal_resolution: null
title: 'Madagascar: Cyclone - Tropical storm - Jan 2024'
version: null
vulnerability: null
---
