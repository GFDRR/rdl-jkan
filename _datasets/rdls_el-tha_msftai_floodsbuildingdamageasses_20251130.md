---
attributions:
- entity:
    affiliation: null
    email: null
    name: Planet
    url: https://data.humdata.org/dataset/thailand-floods-building-damage-assessment-in-hat-yai
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/thailand-floods-building-damage-assessment-in-hat-yai
creator:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/thailand-floods-building-damage-assessment-in-hat-yai
dataset_id: rdls_el-tha_msftai_floodsbuildingdamageasses_20251130
description: 'Microsoft AI for Good Lab ran their damage assessment AI models on images
  provided by Planet and have mapped out the affected buildings in Hat Yai, Thailand..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/thailand-floods-building-damage-assessment-in-hat-yai]'
details: While the data provides a valuable first look, it should serve as a preliminary
  guide and will require on-the-ground verification for a complete understanding.
exposure:
- asset_type:
    description: Building footprints and structures mapped in Hat Yai affected by
      flooding
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
  description: Microsoft AI for Good Lab applied their damage assessment AI models
    to Planet satellite imagery of Hat Yai, Thailand to automatically detect and map
    building damage from flooding. The resulting building predictions were clipped
    to the affected area and exported as a geopackage for spatial analysis.
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
- href: https://data.humdata.org/dataset/thailand-floods-building-damage-assessment-in-hat-yai
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from flooding in Hat Yai derived
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
  description: 'The images cover Hat Yai, Thailand. Analysis was done on Planet SkySat
    imagery captured 11/30/2025. Total buildings from Overture Maps: 70,516 Intersected
    by flood predictions: 1,671 Water within 20 meters: 3,219 Separately we labeled
    a random selection of 139 building footprints with area greater than 50 sq meters
    as flooded vs. not-flooded based on visible flood waters around the building and
    estimate that a total of 2005 buildings are affected (N=46439 buildings that are
    larger than 50 sq m) with a 95% CI of [432, 3577]. Overall, low damage in the
    city, but heavy flooding in the fields and along the river north of the city.'
  download_url: https://data.humdata.org/dataset/a01fa127-a633-49d6-bd2a-f4520cd83987/resource/35fb5e62-18c0-4723-8c1c-58c741232cc3/download/20251130_004309_ssc12_building_predictions_clipped.gpkg
  format: null
  id: resource_35fb5e62
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20251130_004309_ssc12_building_predictions_clipped.gpkg
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-tha_msftai_floodsbuildingdamageasses_20251130
spatial:
  bbox: null
  centroid: null
  countries:
  - THA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-11-30'
temporal_resolution: null
title: 'Thailand Floods: Building Damage Assessment in Hat Yai'
version: null
vulnerability: null
---
