---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/madagascar-cyclone-1000961
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/madagascar-cyclone-1000961
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/madagascar-cyclone-1000961
dataset_id: rdls_hel-mdgmoz_wfpadam_cyclonecategory1mar2023_2023
description: 'ADAM ID: 1000961_60 Cyclone (category 1) during the period Feb 06 2023-Mar
  12 2023 in Mozambique, Madagascar. It impacted 1327678 people.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/madagascar-cyclone-1000961]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone hazard in affected areas
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
  description: WFP ADAM system collected and mapped tropical cyclone track geometry
    and wind speed observations during the February-March 2023 cyclone event in Madagascar
    and Mozambique, integrating geospatial hazard data with population exposure to
    generate impact assessments of affected populations.
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
- href: https://data.humdata.org/dataset/madagascar-cyclone-1000961
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Category 1 tropical cyclone event
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
  description: 'Madagascar: Cyclone - Category 1 - Mar 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/2b416d3c-2808-4b22-b856-95b31ba5a7a7/resource/7a28b6ee-be29-44a0-804d-ee025d606c03/download/1000961-60-adam-ts-1000961-60-shp.zip
  format: null
  id: resource_7a28b6ee
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000961-60-adam-ts-1000961-60-shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdgmoz_wfpadam_cyclonecategory1mar2023_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  - MOZ
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-12'
  start: '2023-02-06'
temporal_resolution: null
title: 'Madagascar: Cyclone - Category 1 - Mar 2023'
version: null
vulnerability: null
---
