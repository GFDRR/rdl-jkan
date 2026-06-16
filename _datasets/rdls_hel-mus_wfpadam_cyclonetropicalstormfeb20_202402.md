---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/mauritius-cyclone-1001052
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/mauritius-cyclone-1001052
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/mauritius-cyclone-1001052
dataset_id: rdls_hel-mus_wfpadam_cyclonetropicalstormfeb20_202402
description: 'ADAM ID: 1001052_19 Cyclone (tropical storm) during the period Feb 19
  2024-Feb 23 2024 in Miscellaneous (French) Indian Ocean Islands, Mauritius. It impacted
  0 people.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mauritius-cyclone-1001052]'
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
  description: ADAM collected observed tropical cyclone track and wind speed data
    from the February 2024 event in Mauritius. Population exposure was estimated by
    intersecting gridded population data with wind speed zones (60 km/h and 90 km/h
    thresholds) and aggregating by administrative divisions to quantify affected populations.
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
- href: https://data.humdata.org/dataset/mauritius-cyclone-1001052
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone winds during February 2024
      event
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
  description: 'Mauritius: Cyclone - Tropical storm - Feb 2024 (Shape File)'
  download_url: https://data.humdata.org/dataset/21c9fee6-4397-4706-bb85-9191fe9a490b/resource/c446b659-7fe7-417b-81bc-9266c9189e42/download/1001052-20-adam-ts-1001052-20-shp.zip
  format: null
  id: resource_c446b659
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001052-20-adam-ts-1001052-20-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritius: Cyclone - Tropical storm - Feb 2024 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/21c9fee6-4397-4706-bb85-9191fe9a490b/resource/2c9d2753-9081-40c6-9566-abdf7692a3c4/download/1001052-20-adam-ts-1001052-20-pop-estimation.csv
  format: null
  id: resource_2c9d2753
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001052-20-adam-ts-1001052-20-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mus_wfpadam_cyclonetropicalstormfeb20_202402
spatial:
  bbox: null
  centroid: null
  countries:
  - MUS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-02-23'
  start: '2024-02-19'
temporal_resolution: null
title: 'Mauritius: Cyclone - Tropical storm - Feb 2024'
version: null
vulnerability: null
---
