---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/somalia-flood-fl-20231121-som-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/somalia-flood-fl-20231121-som-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/somalia-flood-fl-20231121-som-00
dataset_id: rdls_hel-som_wfpadam_flood9225550sqmnov2023_20231121
description: 'ADAM ID: FL-20231121-SOM-00 Flood covering 922555.0 sq m on Nov 21 2023
  in Somalia. It impacted 450428 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-flood-fl-20231121-som-00]'
details: null
exposure:
- asset_type:
    description: Total population in the flooded area by administrative division
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
- asset_type:
    description: Cropland area within the flooded zone
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM collected and analyzed geospatial data following the November
    21, 2023 flood event in Somalia, mapping observed flood extent (922,555 sq m)
    and intersecting with population and cropland layers to quantify direct impacts.
    The dataset integrates administrative boundaries, population distribution, and
    land use data to produce impact dashboards and response assessments.
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
- href: https://data.humdata.org/dataset/somalia-flood-fl-20231121-som-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by fluvial flooding event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural loss from flooded cropland area
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: 'Somalia: Flood - 922555.0 sq m - Nov 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/ca8063d7-758e-48f0-8b78-58624be8181b/resource/1e89d1a9-452d-44a7-ab76-6e0b3ef1de32/download/fl-20231121-som-00.geojson
  format: null
  id: resource_1e89d1a9
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-SOM-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Flood - 922555.0 sq m - Nov 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/ca8063d7-758e-48f0-8b78-58624be8181b/resource/404e60d8-595d-41d5-b6df-443d1dc38746/download/fl-20231121-som-00.tiff
  format: null
  id: resource_404e60d8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-SOM-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Flood - 922555.0 sq m - Nov 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/ca8063d7-758e-48f0-8b78-58624be8181b/resource/d688f237-2153-43a1-ac93-e54d797e39fc/download/fl-20231121-som-00.gpkg
  format: null
  id: resource_d688f237
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-SOM-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Flood - 922555.0 sq m - Nov 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/ca8063d7-758e-48f0-8b78-58624be8181b/resource/0bd8142d-5a00-4b2f-b620-79bd396a92f7/download/metadata.txt
  format: null
  id: resource_0bd8142d
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: metadata.txt
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-som_wfpadam_flood9225550sqmnov2023_20231121
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-21'
temporal_resolution: null
title: 'Somalia: Flood - 922555.0 sq m - Nov 2023'
version: null
vulnerability: null
---
