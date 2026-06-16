---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/ethiopia-flood-fl-20231121-eth-01
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/ethiopia-flood-fl-20231121-eth-01
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/ethiopia-flood-fl-20231121-eth-01
dataset_id: rdls_hel-eth_wfpadam_flood4184510sqmnov2023_20231121
description: 'ADAM ID: FL-20231121-ETH-01 Flood covering 418451.0 sq m on Nov 21 2023
  in Ethiopia. It impacted 295186 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-flood-fl-20231121-eth-01]'
details: null
exposure:
- asset_type:
    description: Cropland area exposed to flooding, including total croplands and
      flooded croplands
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Total population and directly affected population in flooded areas
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
  description: WFP ADAM system processed satellite imagery and geospatial data to
    delineate observed flood extent on November 21, 2023 in Ethiopia. The flood polygon
    was intersected with population and cropland datasets to quantify directly affected
    populations (295,186 people) and flooded agricultural area. Data is provided in
    multiple geospatial formats (GeoJSON, GeoTIFF, GeoPackage) for operational response
    mapping.
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
- href: https://data.humdata.org/dataset/ethiopia-flood-fl-20231121-eth-01
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct impact on cropland area from fluvial flooding
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
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
    id: loss_2
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
  description: 'Ethiopia: Flood - 418451.0 sq m - Nov 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/71829376-b8a9-4513-9ca7-cc4575cc5210/resource/f66114d1-9d70-4e23-bcb6-c56ed9ddfd08/download/fl-20231121-eth-01.geojson
  format: null
  id: resource_f66114d1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-ETH-01.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Flood - 418451.0 sq m - Nov 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/71829376-b8a9-4513-9ca7-cc4575cc5210/resource/cfcbf25b-686b-43ca-82ef-724237d473cc/download/fl-20231121-eth-01.tiff
  format: null
  id: resource_cfcbf25b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-ETH-01.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Flood - 418451.0 sq m - Nov 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/71829376-b8a9-4513-9ca7-cc4575cc5210/resource/96a00dc4-fbcc-497c-b140-f85adfe136c2/download/fl-20231121-eth-01.gpkg
  format: null
  id: resource_96a00dc4
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-ETH-01.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Flood - 418451.0 sq m - Nov 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/71829376-b8a9-4513-9ca7-cc4575cc5210/resource/b414f14e-4ccc-4fe2-9f54-d857661ade3d/download/metadata.txt
  format: null
  id: resource_b414f14e
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
slug: rdls_hel-eth_wfpadam_flood4184510sqmnov2023_20231121
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-21'
temporal_resolution: null
title: 'Ethiopia: Flood - 418451.0 sq m - Nov 2023'
version: null
vulnerability: null
---
