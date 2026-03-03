---
catalog: null
contact_point:
  email: gobs@aeee.in
  id: attribution_contact
  name: Alliance for an Energy Efficient Economy (AEEE)
  url: https://gobs.aeee.in/
creator:
  email: gobs@aeee.in
  id: attribution_creator
  name: Alliance for an Energy Efficient Economy (AEEE)
  url: https://gobs.aeee.in/
dataset_id: rdls_exp-ceew_india_buildings
description: A geospatial dataset of building stock and height for building-level
  analysis in India.
details: This dataset is derived from the Google Open Buildings dataset (v3 footprints,
  v1 height) and is not based on official surveys; the building_floor attribute is
  an estimate calculated by dividing building_height by a 3-meter standard, with raw
  height also provided for custom analysis. Building land use is a proxy based on
  OpenStreetMap (OSM) tags, as official digitized function data is broadly unavailable.
  A supervised machine learning model (Random Forest) was employed to predict and
  impute land use for buildings lacking an original OSM tag. Key transparency fields,
  is_predicted and prediction_confidence, are included to allow users to filter the
  data based on the ML model's output. To ensure data quality, the dataset excludes
  buildings with a confidence level below 0.75 or heights outside the 2.4m to 100m
  range.
exposure:
- category: buildings
  dimension: content
  quantity_kind: area
  taxonomy: GED4ALL
extra_attributions: []
hazard: null
license: ODbL-1.0
loss: null
project:
  name: GOBS
  url: https://gobs.aeee.in/
publisher:
  email: gobs@aeee.in
  id: attribution_publisher
  name: Alliance for an Energy Efficient Economy (AEEE)
  url: https://gobs.aeee.in/
purpose: To support sustainable development and climate adaptation analysis, including
  resilience, carbon, cooling, solar, and retrofit applications.
resources:
- coordinate_system: EPSG:4326
  description: A geospatial dataset of building stock and height for building-level
    analysis in India.
  download_url: https://gobs.aeee.in/downloads
  format: CSV (csv)
  id: resource_1
  media_type: null
  spatial_resolution: null
  temporal: null
  title: India Geospatial Open Building Stack (GOBS)
risk_data_type:
- exposure
schema: rdl-03
slug: rdls_exp-ceew_india_buildings
spatial:
  countries:
  - IND
  scale: national
title: India Geospatial Open Building Stack (GOBS)
version: '1'
vulnerability: null
---
