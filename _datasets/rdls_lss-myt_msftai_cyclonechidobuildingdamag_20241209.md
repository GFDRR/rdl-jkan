---
attributions:
- entity:
    affiliation: null
    email: null
    name: Planet Labs satellite imagery
    url: https://data.humdata.org/dataset/building-damage-assessment-in-passamanty-mayotte-after-cyclone-chido
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Microsoft AI for Good Lab damage assessment models
    url: https://data.humdata.org/dataset/building-damage-assessment-in-passamanty-mayotte-after-cyclone-chido
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/building-damage-assessment-in-passamanty-mayotte-after-cyclone-chido
creator:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/building-damage-assessment-in-passamanty-mayotte-after-cyclone-chido
dataset_id: rdls_lss-myt_msftai_cyclonechidobuildingdamag_20241209
description: 'We ran our damage assessment AI models on images provided by Planet
  and have mapped out the affected buildings. The images cover Passamainty in Mayotte.
  We assessed 3,875 buildings in the area, with damage levels as follows: 1,426 buildings
  are between 0% and 20% damaged 136 buildings are between 20% and 40% damaged 92
  buildings are between 40% and 60% damaged 62 buildings are between 60% and 80% damaged
  2,159 buildings are between 80% and 100% damaged. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/building-damage-assessment-in-passamanty-mayotte-after-cyclone-chido]'
details: While the data provides a valuable first look, it should serve as a preliminary
  guide and will require on-the-ground verification for a complete understanding.
  Any building classified as >0% damaged likely has nearby debris and should be further
  inspected.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Microsoft AI for Good Lab applied trained damage assessment machine
    learning models to Planet satellite imagery of Passamanty, Mayotte following Cyclone
    Chido to classify 3,875 buildings into six damage categories (0-20%, 20-40%, 40-60%,
    60-80%, 80-100% damage). The resulting damage counts and spatial building footprints
    were mapped in geopackage format for post-event impact assessment.
  sources:
  - id: source_1
    license: null
    name: Planet Labs satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Microsoft AI for Good Lab damage assessment models
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/building-damage-assessment-in-passamanty-mayotte-after-cyclone-chido
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone (Cyclone Chido) assessed
      via AI damage classification models
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
  description: 'Cyclone Chido: Building Damage Assessment in Passamanty, Mayotte (The
    extent of available imagery in the AOI.)'
  download_url: https://data.humdata.org/dataset/4b96001b-845a-4739-89a2-51225b762d2e/resource/1a2d0251-bb73-4191-bdfc-c1bc9145ef45/download/mayotte_0_extent.gpkg
  format: null
  id: resource_1a2d0251
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mayotte_0_extent.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cyclone Chido: Building Damage Assessment in Passamanty, Mayotte (Results
    that outline the building damage assessment footprints in the AOI.)'
  download_url: https://data.humdata.org/dataset/4b96001b-845a-4739-89a2-51225b762d2e/resource/8950a27f-5f1a-4415-a9b5-861feb7e9cdb/download/mayotte_0_outputs.gpkg
  format: null
  id: resource_8950a27f
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mayotte_0_outputs.gpkg
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-myt_msftai_cyclonechidobuildingdamag_20241209
spatial:
  bbox: null
  centroid: null
  countries:
  - MYT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-12-09'
temporal_resolution: null
title: 'Cyclone Chido: Building Damage Assessment in Passamanty, Mayotte'
version: null
vulnerability: null
---
