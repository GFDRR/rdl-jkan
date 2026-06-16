---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/madagascar-cyclone-1000957
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/madagascar-cyclone-1000957
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/madagascar-cyclone-1000957
dataset_id: rdls_he-mdg_wfpadam_cyclonetropicalstormjan20_202301
description: 'ADAM ID: 1000957_6 Cyclone (tropical storm) during the period Jan 18
  2023-Jan 29 2023 in Madagascar. It impacted 0 people.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/madagascar-cyclone-1000957]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone hazard in Madagascar
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
    wind speed measurements for the January 2023 cyclone event in Madagascar. The
    shapefile contains event episode information, cyclone classification, wind speed
    measurements, and population exposure data aggregated from operational emergency
    response monitoring.
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
- href: https://data.humdata.org/dataset/madagascar-cyclone-1000957
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
  description: 'Madagascar: Cyclone - Tropical storm - Jan 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/3931bb8b-332a-4449-b989-bb7d75fcfb73/resource/a0a434b0-5d2c-4822-8e7c-e2df231e6655/download/1000957-42-adam-ts-1000957-42-shp.zip
  format: null
  id: resource_a0a434b0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000957-42-adam-ts-1000957-42-shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mdg_wfpadam_cyclonetropicalstormjan20_202301
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
  end: '2023-01-29'
  start: '2023-01-18'
temporal_resolution: null
title: 'Madagascar: Cyclone - Tropical storm - Jan 2023'
version: null
vulnerability: null
---
