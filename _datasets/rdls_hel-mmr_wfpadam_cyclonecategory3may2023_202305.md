---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/myanmar-cyclone-1000970
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/myanmar-cyclone-1000970
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/myanmar-cyclone-1000970
dataset_id: rdls_hel-mmr_wfpadam_cyclonecategory3may2023_202305
description: 'ADAM ID: 1000970_6 Cyclone (category 3) during the period May 11 2023-May
  14 2023 in Myanmar. It impacted 2643150 people.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/myanmar-cyclone-1000970]'
details: null
exposure:
- asset_type:
    description: Population exposed to cyclone hazard in Myanmar
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
  description: WFP ADAM system collected and mapped observed tropical cyclone track
    data and wind speed measurements during the May 2023 cyclone event in Myanmar,
    integrating geospatial hazard information with population exposure data to quantify
    affected populations for emergency response.
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
- href: https://data.humdata.org/dataset/myanmar-cyclone-1000970
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Category 3 cyclone in Myanmar (2,643,150 people)
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
  description: 'Myanmar: Cyclone - Category 3 - May 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/e45b9caa-9dba-45bc-93c7-d88deb017554/resource/667a218f-d000-46b2-91b7-d7eaa1ec8e9c/download/1000970-15-adam-ts-1000970-15-shp.zip
  format: null
  id: resource_667a218f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000970-15-adam-ts-1000970-15-shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mmr_wfpadam_cyclonecategory3may2023_202305
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-05-14'
  start: '2023-05-11'
temporal_resolution: null
title: 'Myanmar: Cyclone - Category 3 - May 2023'
version: null
vulnerability: null
---
