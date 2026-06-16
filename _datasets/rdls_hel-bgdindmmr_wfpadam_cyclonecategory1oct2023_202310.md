---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/bangladesh-cyclone-1001029
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/bangladesh-cyclone-1001029
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/bangladesh-cyclone-1001029
dataset_id: rdls_hel-bgdindmmr_wfpadam_cyclonecategory1oct2023_202310
description: 'ADAM ID: 1001029_6 Cyclone (category 1) during the period Oct 23 2023-Oct
  24 2023 in Bangladesh, India, Myanmar. It impacted 3946522 people.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/bangladesh-cyclone-1001029]'
details: null
exposure:
- asset_type:
    description: Population exposed to cyclone wind speeds at multiple thresholds
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM system processed observed tropical cyclone track data and
    wind speed measurements to generate spatial hazard polygons with wind speed classifications.
    Population exposure was estimated by intersecting cyclone wind speed zones with
    gridded population data, stratified by wind speed thresholds (60, 90, 120 kph).
    Total affected population count aggregated across administrative divisions.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bangladesh-cyclone-1001029
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by Category 1 tropical cyclone
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
  description: 'Bangladesh: Cyclone - Category 1 - Oct 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/d60e3dfb-3195-41dd-bdad-34c8e1070f2b/resource/790ffabc-4ff6-45cf-ac8b-d934bb00529b/download/1001029-7-adam-ts-1001029-7-shp.zip
  format: null
  id: resource_790ffabc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001029-7-adam-ts-1001029-7-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Cyclone - Category 1 - Oct 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/d60e3dfb-3195-41dd-bdad-34c8e1070f2b/resource/b7eff828-e855-4f8d-bcbb-515c055e73f7/download/1001029-7-adam-ts-1001029-7-pop-estimation.csv
  format: null
  id: resource_b7eff828
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001029-7-adam-ts-1001029-7-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bgdindmmr_wfpadam_cyclonecategory1oct2023_202310
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  - IND
  - MMR
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-10-24'
  start: '2023-10-23'
temporal_resolution: null
title: 'Bangladesh: Cyclone - Category 1 - Oct 2023'
version: null
vulnerability: null
---
