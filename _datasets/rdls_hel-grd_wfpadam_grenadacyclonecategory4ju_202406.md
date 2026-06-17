---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/grenada-cyclone-1001067
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/grenada-cyclone-1001067
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/grenada-cyclone-1001067
dataset_id: rdls_hel-grd_wfpadam_grenadacyclonecategory4ju_202406
description: 'ADAM ID: 1001067_3 Cyclone (category 4) during the period Jun 28 2024-Jun
  30 2024 in Grenada. It impacted 0 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/grenada-cyclone-1001067]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speeds at multiple thresholds
      (60, 90, 120 kph)
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
  description: WFP ADAM collected observed tropical cyclone track data and wind speed
    measurements for the Category 4 cyclone event in Grenada (June 28-30, 2024). Population
    exposure was estimated at multiple wind speed thresholds (60, 90, 120 kph) by
    intersecting the hazard field with gridded population data at administrative levels.
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
- href: https://data.humdata.org/dataset/grenada-cyclone-1001067
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone winds in Grenada
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
  description: 'Grenada: Cyclone - Category 4 - Jun 2024 (Shape File)'
  download_url: https://data.humdata.org/dataset/6f65ef94-a20e-4cc5-9c1e-790cc979264a/resource/7ed7a17a-b062-4c29-81bc-7b3e77482c7d/download/1001067-7-adam-ts-1001067-7-shp.zip
  format: null
  id: resource_7ed7a17a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001067-7-adam-ts-1001067-7-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Grenada: Cyclone - Category 4 - Jun 2024 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/6f65ef94-a20e-4cc5-9c1e-790cc979264a/resource/7c2a621f-fd2f-4c19-9d2b-40b305f25e4b/download/1001067-7-adam-ts-1001067-7-pop-estimation.csv
  format: null
  id: resource_7c2a621f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001067-7-adam-ts-1001067-7-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-grd_wfpadam_grenadacyclonecategory4ju_202406
spatial:
  bbox: null
  centroid: null
  countries:
  - GRD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-06-30'
  start: '2024-06-28'
temporal_resolution: null
title: 'Grenada: Cyclone - Category 4 - Jun 2024'
version: null
vulnerability: null
---
