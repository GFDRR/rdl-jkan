---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/jamaica-cyclone-1001067
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/jamaica-cyclone-1001067
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/jamaica-cyclone-1001067
dataset_id: rdls_hel-wfpadam_cyclonecategory1jul2024_2024
description: 'ADAM ID: 1001067_27 Cyclone (category 1) during the period Jun 28 2024-Jul
  06 2024 in Haiti, Grenada, Jamaica, Trinidad and Tobago, Saint Vincent and the Grenadines,
  Mexico, Belize, United States. It impacted 0 people.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/jamaica-cyclone-1001067]'
details: null
exposure:
- asset_type:
    description: Population exposed to cyclone wind speeds at 60, 90, and 120 km/h
      thresholds by administrative division
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
  description: WFP ADAM system collected and mapped observed tropical cyclone track
    geometry and wind speed parameters for the July 2024 Caribbean cyclone event.
    Population exposure was estimated by intersecting wind speed zones (60, 90, 120
    km/h) with gridded population data at administrative division levels to quantify
    affected populations across eight countries.
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
- href: https://data.humdata.org/dataset/jamaica-cyclone-1001067
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone winds at multiple speed thresholds
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
  description: 'Jamaica: Cyclone - Category 1 - Jul 2024 (Shape File)'
  download_url: https://data.humdata.org/dataset/3599f96a-6b59-494f-be05-b4441600489e/resource/3a878d2f-6a40-4f04-b887-34a1fa1946a0/download/1001067-31-adam-ts-1001067-31-shp.zip
  format: null
  id: resource_3a878d2f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001067-31-adam-ts-1001067-31-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Jamaica: Cyclone - Category 1 - Jul 2024 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/3599f96a-6b59-494f-be05-b4441600489e/resource/d83a1023-c738-436b-84cb-600162ee38bd/download/1001067-31-adam-ts-1001067-31-pop-estimation.csv
  format: null
  id: resource_d83a1023
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001067-31-adam-ts-1001067-31-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-wfpadam_cyclonecategory1jul2024_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  - GRD
  - JAM
  - TTO
  - VCT
  - MEX
  - BLZ
  - USA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-07-06'
  start: '2024-06-28'
temporal_resolution: null
title: 'Jamaica: Cyclone - Category 1 - Jul 2024'
version: null
vulnerability: null
---
