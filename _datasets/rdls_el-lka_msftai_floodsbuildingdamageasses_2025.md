---
attributions:
- entity:
    affiliation: null
    email: null
    name: Planet
    url: https://data.humdata.org/dataset/sri-lanka-floods-building-damage-assessment-in-colombo
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/sri-lanka-floods-building-damage-assessment-in-colombo
creator:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/sri-lanka-floods-building-damage-assessment-in-colombo
dataset_id: rdls_el-lka_msftai_floodsbuildingdamageasses_2025
description: 'Microsoft AI for Good Lab ran their damage assessment AI models on images
  provided by Planet and have mapped out the affected buildings in Colombo, Sri Lanka..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sri-lanka-floods-building-damage-assessment-in-colombo]'
details: While the data provides a valuable first look, it should serve as a preliminary
  guide and will require on-the-ground verification for a complete understanding.
exposure:
- asset_type:
    description: Building footprints in Colombo, Sri Lanka mapped and classified by
      damage status using AI-based analysis of satellite imagery
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Planet satellite imagery of Colombo, Sri Lanka was acquired around
    the flood event and processed through Microsoft AI for Good Lab's damage assessment
    AI models to classify buildings as damaged or undamaged. The resulting geopackage
    contains building-level damage predictions derived from change detection between
    pre- and post-event imagery, supporting rapid post-disaster impact assessment.
  sources:
  - id: source_1
    license: null
    name: Planet
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
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
- href: https://data.humdata.org/dataset/sri-lanka-floods-building-damage-assessment-in-colombo
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from Sri Lanka floods in Colombo,
      derived from AI model predictions on Planet satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: 'We ran a flood model on PlanetScope imagery captured on November 30th
    over part of Colombo, Sri Lanka. There were a total of 656,656 building footprints
    in the area we analyzed. Of these: 7,071 were covered by clouds, leaving 649,584
    for analysis Our model estimates 34,144 (5.3%) have flood predictions within 20m.
    We independently labeled 139 building footprints (of size > 50 sq m) based on
    whether we saw visible flooding around the building, and estimate 24,181 buildings
    affected (5.0% of the set of >50 sq m) with a 95% CI of [6664, 41697] buildings.
    Our model has a recall of 0.86 and precision of 0.75 compared to this set of labels.'
  download_url: https://data.humdata.org/dataset/04c95b2c-7472-4516-80f7-b6ed950a5255/resource/eccceb3c-e98d-40d7-9526-2574e564268b/download/planetscope_srilanka_11_30_buildings_clipped_predictions.gpkg
  format: null
  id: resource_eccceb3c
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: planetscope_srilanka_11_30_buildings_clipped_predictions.gpkg
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-lka_msftai_floodsbuildingdamageasses_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - LKA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-09'
  start: '2025-11-30'
temporal_resolution: null
title: 'Sri Lanka Floods: Building Damage Assessment in Colombo'
version: null
vulnerability: null
---
