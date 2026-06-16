---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/zambia-flood-fl-20230301-zmb-01
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/zambia-flood-fl-20230301-zmb-01
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/zambia-flood-fl-20230301-zmb-01
dataset_id: rdls_hel-zmb_wfpadam_flood23027330sqmmar2023_20230301
description: 'ADAM ID: FL-20230301-ZMB-01 Flood covering 2302733.0 sq m on Mar 01
  2023 in Zambia. It impacted 332389 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/zambia-flood-fl-20230301-zmb-01]'
details: null
exposure:
- asset_type:
    description: Total population in flood-affected administrative areas
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
    description: Cropland area affected by flood inundation
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
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system collected post-event geospatial data and socio-economic
    information following the March 2023 flood in Zambia. Flood extent was mapped
    and overlaid with population and cropland datasets to derive direct impact metrics
    including affected population count and flooded cropland area. Data delivered
    in multiple formats (GeoJSON, GeoTIFF, GeoPackage) with administrative boundary
    attribution.
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
- href: https://data.humdata.org/dataset/zambia-flood-fl-20230301-zmb-01
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by March 2023 flood event in Zambia
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
    description: Direct cropland area loss from flood inundation
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
  description: 'Zambia: Flood - 2302733.0 sq m - Mar 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/ee1c81ba-929a-4d19-b718-863e09687a19/resource/67eababd-a120-4642-ba00-5c8bae9d2a43/download/fl-20230301-zmb-01.geojson
  format: null
  id: resource_67eababd
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230301-ZMB-01.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 2302733.0 sq m - Mar 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/ee1c81ba-929a-4d19-b718-863e09687a19/resource/c764122e-5dc8-4c76-b392-53d027ec1d95/download/fl-20230301-zmb-01.tiff
  format: null
  id: resource_c764122e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230301-ZMB-01.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 2302733.0 sq m - Mar 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/ee1c81ba-929a-4d19-b718-863e09687a19/resource/2f75c837-6c7a-4d5f-b9fd-0ee988642dd5/download/fl-20230301-zmb-01.gpkg
  format: null
  id: resource_2f75c837
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20230301-ZMB-01.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Flood - 2302733.0 sq m - Mar 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/ee1c81ba-929a-4d19-b718-863e09687a19/resource/6351e742-9df9-425e-b35e-ba9a9020ca55/download/metadata.txt
  format: null
  id: resource_6351e742
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
slug: rdls_hel-zmb_wfpadam_flood23027330sqmmar2023_20230301
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-01'
temporal_resolution: null
title: 'Zambia: Flood - 2302733.0 sq m - Mar 2023'
version: null
vulnerability: null
---
