---
attributions:
- entity:
    affiliation: null
    email: null
    name: Maxar
    url: https://data.humdata.org/dataset/eaton-fire-altadena-damage-assessment-from-1-10
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Planet
    url: https://data.humdata.org/dataset/eaton-fire-altadena-damage-assessment-from-1-10
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/eaton-fire-altadena-damage-assessment-from-1-10
creator:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/eaton-fire-altadena-damage-assessment-from-1-10
dataset_id: rdls_el-usa_msftai_lafireseatonfirejanuary20_202501
description: 'We ran our damage assessment AI models on images provided by Maxar and
  Planet and have mapped out the affected buildings. The images cover Eaton fire.
  Analysis was done on: 1) Maxar imagery captured 01/10 2) Planet imagery captured
  1/11 Latest results show the following. 156,102 buildings in study area 8,682 estimated
  damaged. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/eaton-fire-altadena-damage-assessment-from-1-10]'
details: While the data provides a valuable first look, it should serve as a preliminary
  guide and will require on-the-ground verification for a complete understanding.
exposure:
- asset_type:
    description: Building stock inventory in the Eaton fire study area with 156,102
      buildings mapped
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: High-resolution satellite imagery from Maxar (01/10/2025) and Planet
    (01/11/2025) was processed through Microsoft AI for Good Lab's damage assessment
    AI models to automatically detect and classify building damage in the Eaton fire
    study area, resulting in damage predictions for 8,682 of 156,102 mapped buildings.
  sources:
  - id: source_1
    license: null
    name: Maxar
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Planet
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Microsoft AI for Good Lab
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/eaton-fire-altadena-damage-assessment-from-1-10
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from wildfire assessed via AI analysis of
      satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
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
  description: 'Results from 01/11 using Planet imagery. 156,102 buildings in study
    area 8,682 estimated damaged The result file contains the following fields for
    each building footprint: damage_pct_0m - the fraction of the building footprint''s
    area that is classified as damaged by our model damage_pct_10m - total damaged
    area within a 10m buffer of the building footprint (including the footprint itself)
    / building footprint''s area (this can be >1.0 but we clip to 1.0) damage_pct_20m
    - same as above but with a 20m buffer damaged - 1 if damage_pct_0m > 0 else 0
    unknown_pct - fraction of the pixels within the building footprint that we think
    are obstructed (clouds, smoke, haze, too dark to evaluate)'
  download_url: https://data.humdata.org/dataset/0fd186e9-5e47-4c74-8510-4518506db51e/resource/8b69f288-8554-4e79-ba01-076f8dd1189b/download/eaton_planet_1_11_25_damage_predictions.gpkg
  format: null
  id: resource_8b69f288
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eaton_planet_1_11_25_damage_predictions.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Results from 01/10 using Maxar imagery. 31,356 buildings in this AOI:
    27,202 in the 0-20 bucket 4,154 in the >20 bucket (4602 with damage>0) The result
    file contains the following fields for each building footprint: damage_pct_0m
    - the fraction of the building footprint''s area that is classified as damaged
    by our model damage_pct_10m - total damaged area within a 10m buffer of the building
    footprint (including the footprint itself) / building footprint''s area (this
    can be >1.0 but we clip to 1.0) damage_pct_20m - same as above but with a 20m
    buffer damaged - 1 if damage_pct_0m > 0 else 0 unknown_pct - fraction of the pixels
    within the building footprint that we think are obstructed (clouds, smoke, haze,
    too dark to evaluate)'
  download_url: https://data.humdata.org/dataset/0fd186e9-5e47-4c74-8510-4518506db51e/resource/fca461b7-4dbf-4fc3-867a-88b25910abe6/download/eaton_jan_10_rgb_damage_predictions.gpkg
  format: null
  id: resource_fca461b7
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eaton_jan_10_rgb_damage_predictions.gpkg
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-usa_msftai_lafireseatonfirejanuary20_202501
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-01-11'
  start: '2025-01-10'
temporal_resolution: null
title: 'United States - LA Fires - Eaton fire January 2025: Building Damage Assessment'
version: null
vulnerability: null
---
