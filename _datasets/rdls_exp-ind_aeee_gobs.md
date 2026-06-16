---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: gobs@aeee.in
  name: Alliance for an Energy Efficient Economy (AEEE)
  url: https://gobs.aeee.in/
creator:
  affiliation: null
  email: gobs@aeee.in
  name: Alliance for an Energy Efficient Economy (AEEE)
  url: https://gobs.aeee.in/
dataset_id: rdls_exp-ind_aeee_gobs
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
- asset_type:
    description: Buildings classified using the GED4ALL taxonomy. Footprints and height
      data from the Google Open Buildings v3 and 2.5D datasets; land use attributed
      via OpenStreetMap tags and a Random Forest ML model for untagged buildings.
    id: bui
    scheme: GED4ALL
    title: Building taxonomy
    uri: https://wiki.openstreetmap.org/wiki/GED4ALL
  category: buildings
  id: exp_metrics_1
  metrics:
  - dimension: structure
    id: metric_area
    measurement:
      quantity_kind: area
      unit: square_metre
  - dimension: structure
    id: metric_perimeter
    measurement:
      quantity_kind: length
      unit: metre
  - dimension: structure
    id: metric_height
    measurement:
      quantity_kind: length
      unit: metre
  - dimension: structure
    id: metric_floors
    measurement:
      quantity_kind: count
      unit: count
  - dimension: index
    id: metric_landuse
    measurement:
      quantity_kind: index
      unit: null
  - dimension: structure
    id: metric_builtup
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Building footprint, height, and land use dataset for India produced
    by the Alliance for an Energy Efficient Economy (AEEE). Building footprints and
    height data were sourced from the Google Open Buildings v3 dataset and the Google
    Open Building 2.5D Temporal Dataset (v1), which are derived from high-resolution
    satellite imagery using deep learning models. Building heights were converted
    to estimated floor counts using a 3-metre standard floor height. Quality filters
    exclude buildings with a model confidence below 0.75 or heights outside the 2.4
    m to 100 m range. Land use classification used OpenStreetMap (OSM) building tags
    as primary labels; for buildings lacking an OSM tag, land use was predicted using
    a supervised Random Forest machine learning model trained on OSM-labelled buildings.
    Prediction confidence and an is_predicted flag are retained in the output to support
    data quality filtering.
  sources:
  - id: source_1
    license: https://creativecommons.org/licenses/by/4.0/
    name: Google Open Buildings dataset (v3)
    risk_data_type: null
    type: dataset
    url: https://sites.research.google/gr/open-buildings/
    used_in: exposure
  - id: source_2
    license: https://creativecommons.org/licenses/by/4.0/
    name: Google Open Building 2.5D Temporal Dataset (v1)
    risk_data_type: null
    type: dataset
    url: https://sites.research.google/gr/open-buildings/temporal/
    used_in: exposure
  - id: source_3
    license: https://opendatacommons.org/licenses/odbl/1-0/
    name: OpenStreetMap
    risk_data_type: null
    type: dataset
    url: https://www.openstreetmap.org/
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: GOBS
  url: https://gobs.aeee.in/
publisher:
  affiliation: null
  email: gobs@aeee.in
  name: Alliance for an Energy Efficient Economy (AEEE)
  url: https://gobs.aeee.in/
purpose: To support sustainable development and climate adaptation analysis, including
  resilience, carbon, cooling, solar, and retrofit applications.
referenced_by:
- author_names:
  - Jindal R
  - Johnson J
  - Kumar S
  date_published: '2025-11-01'
  doi: null
  id: reference_1
  name: GOBS
  url: https://gobs.aeee.in/
resources:
- access_url: https://gobs.aeee.in/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: A geospatial dataset of building stock and height for building-level
    analysis in India.
  download_url: https://gobs.aeee.in/downloads
  format: null
  id: resource_1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: India Geospatial Open Building Stack (GOBS)
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ind_aeee_gobs
spatial:
  bbox: null
  centroid: null
  countries:
  - IND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: India Geospatial Open Building Stack (GOBS)
version: '1'
vulnerability: null
---
