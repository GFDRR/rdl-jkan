---
attributions:
- entity:
    affiliation: null
    email: null
    name: Planet
    url: https://data.humdata.org/dataset/indonesia-floods-building-damage-assessment-in-sumatra
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/indonesia-floods-building-damage-assessment-in-sumatra
creator:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/indonesia-floods-building-damage-assessment-in-sumatra
dataset_id: rdls_lss-idn_msftai_floodsbuildingdamageasses_2025
description: 'Microsoft AI for Good Lab ran their damage assessment AI models on images
  provided by Planet and have mapped out the affected buildings in Sumatra, Indonesia..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indonesia-floods-building-damage-assessment-in-sumatra]'
details: While the data provides a valuable first look, it should serve as a preliminary
  guide and will require on-the-ground verification for a complete understanding.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Microsoft AI for Good Lab applied their damage assessment AI models
    to PlanetScope satellite imagery acquired over flood-affected areas in Sumatra,
    Indonesia to automatically detect and classify damaged buildings. The model outputs
    were mapped to building footprints and exported as vector (GeoPackage) and raster
    (GeoTIFF) products.
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
- href: https://data.humdata.org/dataset/indonesia-floods-building-damage-assessment-in-sumatra
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from flooding in Sumatra derived
      from AI analysis of satellite imagery
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
  description: 'Indonesia Floods: Building Damage Assessment in Sumatra (GeoPackage)'
  download_url: https://data.humdata.org/dataset/717ffe11-4cc3-4e2d-afbe-faaa17d5a9ce/resource/ec0b1aae-e63f-4666-bdfc-649084073325/download/planetscope_11_29_buildings_clipped_predictions.gpkg
  format: null
  id: resource_ec0b1aae
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: planetscope_11_29_buildings_clipped_predictions.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'We ran a flood model on PlanetScope imagery captured on November 29th
    over parts of Sumatra. There were a total of 1,200,652 building footprints in
    the area we analyzed. Of these: 98,236 were covered by clouds, leaving 1,102,416
    remaining for analysis Our model estimates 56,111 (5.1%) directly intersect with
    the flood predictions and 130,760 (11.9%) have flood predictions within 20m. We
    independently labeled 130 building footprints (of size > 50 sq m) based on whether
    we saw visible flooding around the building, and estimate 83,525 buildings affected
    (9.2% of the set of >50 sq m) with a 95% CI of [38330, 128719] buildings. Our
    model has a recall of 0.58 and precision of 1.0 compared to this set of labels.
    For this set of results we have also released our model predictions. This file
    contains a value of ''3'' where the model estimates flooding and ''4'' where the
    model estimates cloud coverage. You can see this layer in the visualizer.'
  download_url: https://data.humdata.org/dataset/717ffe11-4cc3-4e2d-afbe-faaa17d5a9ce/resource/5639fce3-118a-4508-88ab-4bd8b6ef7102/download/planetscope_11_29_predictions_combined.tif
  format: null
  id: resource_5639fce3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: planetscope_11_29_predictions_combined.tif
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-idn_msftai_floodsbuildingdamageasses_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-08'
  start: '2025-11-29'
temporal_resolution: null
title: 'Indonesia Floods: Building Damage Assessment in Sumatra'
version: null
vulnerability: null
---
