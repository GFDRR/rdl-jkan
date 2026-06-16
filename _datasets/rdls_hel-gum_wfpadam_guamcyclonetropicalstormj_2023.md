---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/guam-cyclone-1000972
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/guam-cyclone-1000972
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/guam-cyclone-1000972
dataset_id: rdls_hel-gum_wfpadam_guamcyclonetropicalstormj_2023
description: 'A cyclone (tropical storm) during the period May 20 2023-Jun 03 2023
  in Guam. It impacted 171500 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/guam-cyclone-1000972]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone winds in Guam
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
  description: WFP ADAM system collected and analyzed geospatial data on the tropical
    cyclone track, wind speeds, and affected population during the May 20 - June 3,
    2023 event in Guam. The dataset integrates observed hazard parameters (wind speed,
    cyclone classification) with exposure data (population counts by area) to support
    operational response dashboards.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/guam-cyclone-1000972
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone winds during June 2023 event
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
  description: 'Guam: Cyclone - Tropical storm - Jun 2023 (Shape File)'
  download_url: https://adam-project-prod.s3-eu-west-1.amazonaws.com/adam_ts/events/2023/06/1000972_57/ADAM_TS_1000972_57_shp.zip
  format: null
  id: resource_9e8834a0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ADAM_TS_1000972_57_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-gum_wfpadam_guamcyclonetropicalstormj_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - GUM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-06-03'
  start: '2023-05-20'
temporal_resolution: null
title: 'Guam: Cyclone - Tropical storm - Jun 2023'
version: null
vulnerability: null
---
