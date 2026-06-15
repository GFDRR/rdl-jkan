---
attributions:
- entity:
    affiliation: null
    email: null
    name: Planet
    url: https://data.humdata.org/dataset/tornado-arkansas-building-damage-assessment-from-03-17-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/tornado-arkansas-building-damage-assessment-from-03-17-2025
creator:
  affiliation: null
  email: null
  name: Microsoft AI for Good Lab
  url: https://data.humdata.org/dataset/tornado-arkansas-building-damage-assessment-from-03-17-2025
dataset_id: rdls_lss-usa_msftai_tornadoarkansasbuildingda_20250317
description: 'Microsoft AI for Good Lab ran their damage assessment AI models on images
  provided by Planet and have mapped out the affected buildings in Arkansas.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/tornado-arkansas-building-damage-assessment-from-03-17-2025]'
details: While the data provides a valuable first look, it should serve as a preliminary
  guide and will require on-the-ground verification for a complete understanding.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Microsoft AI for Good Lab applied trained damage assessment AI models
    to Planet satellite imagery of tornado-affected areas in Jacksonport and Cave
    City, Arkansas on March 17, producing building-level damage classifications and
    spatial mapping of affected structures.
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
- href: https://data.humdata.org/dataset/tornado-arkansas-building-damage-assessment-from-03-17-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tornado assessed via AI-based damage
      classification on satellite imagery
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
  description: 'Results from 03/17/2025 using Planet imagery. This AOI includes Jackson
    County. 6,609 structures with damage fraction between 0% and 20% 71 structures
    with damage fraction between 20% and 40% 27 structures with damage fraction between
    40% and 60% 18 structures with damage fraction between 60% and 80% 21 structures
    with damage fraction between 80% and 100% The result file contains the following
    fields for each building footprint: damage_pct_0m - the fraction of the building
    footprint''s area that is classified as damaged by our model damaged - 1 if damage_pct_0m
    > 0 else 0 unknown_pct - fraction of the pixels within the building footprint
    that we think are obstructed (clouds, smoke, haze, too dark to evaluate)'
  download_url: https://data.humdata.org/dataset/1541a32a-6b1c-4242-92ed-cef4e1f6d0c5/resource/26832af6-15df-4e42-ab8f-3c13df584eb8/download/jacksonport_march_17_results.gpkg
  format: null
  id: resource_26832af6
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jacksonport_march_17_results.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Results from 03/17/2025 using Planet imagery. This AOI includes Cave
    City. 2,269 buildings with damage fraction between 0% and 20% 11 buildings with
    damage fraction between 20% and 40% 10 buildings with damage fraction between
    40% and 60% 10 buildings with damage fraction between 60% and 80% 42 buildings
    with damage fraction between 80% and 100% The result file contains the following
    fields for each building footprint: damage_pct_0m - the fraction of the building
    footprint''s area that is classified as damaged by our model damaged - 1 if damage_pct_0m
    > 0 else 0 unknown_pct - fraction of the pixels within the building footprint
    that we think are obstructed (clouds, smoke, haze, too dark to evaluate)'
  download_url: https://data.humdata.org/dataset/1541a32a-6b1c-4242-92ed-cef4e1f6d0c5/resource/b48e3975-a86b-471c-9408-764bc00943c1/download/cave_city_march_17_results.gpkg
  format: null
  id: resource_b48e3975
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cave_city_march_17_results.gpkg
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-usa_msftai_tornadoarkansasbuildingda_20250317
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
  end: null
  start: '2025-03-17'
temporal_resolution: null
title: United States - Tornado Arkansas - Building Damage Assessment
version: null
vulnerability: null
---
