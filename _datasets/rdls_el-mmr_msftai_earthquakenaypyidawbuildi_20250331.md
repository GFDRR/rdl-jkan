---
attributions:
- entity:
    affiliation: null
    email: null
    name: Planet
    url: https://data.humdata.org/dataset/myanmar-earthquake-naypyidaw-building-damage-assessment-from-03-31-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/myanmar-earthquake-naypyidaw-building-damage-assessment-from-03-31-2025
creator:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/myanmar-earthquake-naypyidaw-building-damage-assessment-from-03-31-2025
dataset_id: rdls_el-mmr_msftai_earthquakenaypyidawbuildi_20250331
description: 'Microsoft AI for Good Lab ran their damage assessment AI models on images
  provided by Planet and have mapped out the affected buildings in Naypyidaw, Myanmar..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/myanmar-earthquake-naypyidaw-building-damage-assessment-from-03-31-2025]'
details: While the data provides a valuable first look, it should serve as a preliminary
  guide and will require on-the-ground verification for a complete understanding.
exposure:
- asset_type:
    description: Building footprints in Naypyidaw classified by damage state from
      earthquake
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
  description: Microsoft AI for Good Lab applied trained damage assessment AI models
    to Planet SkySat satellite imagery of Naypyidaw to automatically detect and classify
    earthquake-damaged buildings, producing a geospatial inventory of affected structures
    mapped to building footprints.
  sources:
  - id: source_1
    license: null
    name: Microsoft AI for Good Lab
    risk_data_type:
    - loss
    type: model
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
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/myanmar-earthquake-naypyidaw-building-damage-assessment-from-03-31-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from earthquake event in Naypyidaw
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: 'The images cover Naypyidaw, Myanmar. Analysis was done on Planet imagery
    captured 03/31/2025. -19,837 buildings with damage fraction between 0% and 20%
    -19 buildings with damage fraction between 40% and 60% -14 buildings with damage
    fraction between 60% and 80% -24 buildings with damage fraction between 80% and
    100% -70 buildings with damage fraction between 20% and 40% While the data provides
    a valuable first look, it should serve as a preliminary guide and will require
    on-the-ground verification for a complete understanding. The result file contains
    the following fields for each building footprint: -damage_pct_0m - the fraction
    of the building footprint''s area that is classified as damaged by our model -damaged
    - 1 if damage_pct_0m > 0 else 0 -unknown_pct - fraction of the pixels within the
    building footprint that we think are obstructed (clouds, smoke, haze, too dark
    to evaluate)'
  download_url: https://data.humdata.org/dataset/9f86fdc7-b4b3-4efc-a003-10134cdcd2ae/resource/a75f3991-02cd-4836-8b4f-b57f91cf1f6c/download/naypyidaw_myanmar_results_03313025_skysat.gpkg
  format: null
  id: resource_a75f3991
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: naypyidaw_myanmar_results_03313025_skysat.gpkg
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mmr_msftai_earthquakenaypyidawbuildi_20250331
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
  end: null
  start: '2025-03-31'
temporal_resolution: null
title: 'Myanmar Earthquake: Naypyidaw Building Damage Assessment'
version: null
vulnerability: null
---
