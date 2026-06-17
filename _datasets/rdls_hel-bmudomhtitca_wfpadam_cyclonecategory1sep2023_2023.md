---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/haiti-cyclone-1000996
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/haiti-cyclone-1000996
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/haiti-cyclone-1000996
dataset_id: rdls_hel-bmudomhtitca_wfpadam_cyclonecategory1sep2023_2023
description: 'ADAM ID: 1000996_7 Cyclone (category 1) during the period Aug 20 2023-Sep
  01 2023 in Bermuda, Turks and Caicos Islands, Dominican Republic, Haiti. It impacted
  0 people.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/haiti-cyclone-1000996]'
details: null
exposure:
- asset_type:
    description: Population exposed to cyclone wind speeds above 60 km/h threshold
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
  description: ADAM collected observed tropical cyclone track and wind speed data
    for the September 2023 event across the Caribbean region. Population exposure
    was estimated by intersecting cyclone wind speed fields with gridded population
    data and administrative boundaries, stratified by wind speed thresholds (60 km/h).
    The dataset aggregates hazard observations and exposure estimates to support operational
    emergency response dashboards.
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
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-cyclone-1000996
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone winds
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
  description: 'Haiti: Cyclone - Category 1 - Sep 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/695d1de6-44d3-43ad-bc3b-35a421fca231/resource/c396c843-d5cc-4ce7-ace7-926b74d4b4a8/download/1000996-49-adam-ts-1000996-49-shp.zip
  format: null
  id: resource_c396c843
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000996-49-adam-ts-1000996-49-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Haiti: Cyclone - Category 1 - Sep 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/695d1de6-44d3-43ad-bc3b-35a421fca231/resource/3ab73dae-6cc6-4a15-9b02-850032928fa3/download/1000996-49-adam-ts-1000996-49-pop-estimation.csv
  format: null
  id: resource_3ab73dae
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000996-49-adam-ts-1000996-49-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bmudomhtitca_wfpadam_cyclonecategory1sep2023_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  - DOM
  - TCA
  - BMU
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-09-01'
  start: '2023-08-20'
temporal_resolution: null
title: 'Haiti: Cyclone - Category 1 - Sep 2023'
version: null
vulnerability: null
---
