---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP ADAM
    url: https://data.humdata.org/dataset/philippines-cyclone-1001032
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-cyclone-1001032
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/philippines-cyclone-1001032
dataset_id: rdls_he-phl_wfpadam_cyclonetropicaldepression_202311
description: 'ADAM ID: 1001032_4 Cyclone (tropical depression) during the period Nov
  12 2023-Nov 13 2023 in . It impacted 0 people.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/philippines-cyclone-1001032]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone winds
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
  description: WFP ADAM collected and mapped geospatial data on a tropical depression
    event occurring November 12-13, 2023 in the Philippines, including cyclone track
    geometry, wind speed measurements, and population exposure. The dataset represents
    observed hazard characteristics from this specific event.
  sources:
  - id: source_1
    license: null
    name: WFP ADAM
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-cyclone-1001032
  rel: source
loss:
  losses: []
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
  description: 'Philippines: Cyclone - Tropical depression - Nov 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/c8d4ab35-e0b6-405b-9cc4-fe3e709a7132/resource/45f62a1a-5c15-4c6f-b88a-ae11b8f26dbf/download/1001032-6-adam-ts-1001032-6-shp.zip
  format: null
  id: resource_45f62a1a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001032-6-adam-ts-1001032-6-shp.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-phl_wfpadam_cyclonetropicaldepression_202311
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
  end: '2023-11-13'
  start: '2023-11-12'
temporal_resolution: null
title: 'Philippines: Cyclone - Tropical depression - Nov 2023'
version: null
vulnerability: null
---
