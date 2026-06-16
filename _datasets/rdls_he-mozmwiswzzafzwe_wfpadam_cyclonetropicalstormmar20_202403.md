---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/mozambique-cyclone-1001053
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/mozambique-cyclone-1001053
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/mozambique-cyclone-1001053
dataset_id: rdls_he-mozmwiswzzafzwe_wfpadam_cyclonetropicalstormmar20_202403
description: 'ADAM ID: 1001053_10 Cyclone (tropical storm) during the period Mar 03
  2024-Mar 13 2024 in Mozambique, South Africa, Eswatini, Zimbabwe, Malawi. It impacted
  0 people.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-cyclone-1001053]'
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
  description: ADAM collected and mapped observed tropical cyclone track data and
    wind speed measurements from the March 2024 cyclone event. Population exposure
    was estimated by intersecting wind speed thresholds (60 km/h and 90 km/h) with
    gridded population data at administrative levels (ADM0-ADM2), producing both spatial
    vector data and tabular population estimates by wind speed zone.
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
- href: https://data.humdata.org/dataset/mozambique-cyclone-1001053
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
  description: 'Mozambique: Cyclone - Tropical storm - Mar 2024 (Shape File)'
  download_url: https://data.humdata.org/dataset/3342649b-1740-40c3-8246-4ed362b28bbc/resource/fea886c3-9ec5-48b0-9ccb-8d092f4f5f1f/download/1001053-15-adam-ts-1001053-15-shp.zip
  format: null
  id: resource_fea886c3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001053-15-adam-ts-1001053-15-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Cyclone - Tropical storm - Mar 2024 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/3342649b-1740-40c3-8246-4ed362b28bbc/resource/6fc0e690-f91a-449c-9513-c9c7a7a9cfb6/download/1001053-15-adam-ts-1001053-15-pop-estimation.csv
  format: null
  id: resource_6fc0e690
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001053-15-adam-ts-1001053-15-pop-estimation.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mozmwiswzzafzwe_wfpadam_cyclonetropicalstormmar20_202403
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  - ZAF
  - SWZ
  - ZWE
  - MWI
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-03-13'
  start: '2024-03-03'
temporal_resolution: null
title: 'Mozambique: Cyclone - Tropical storm - Mar 2024'
version: null
vulnerability: null
---
