---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/ethiopia-flood-fl-20231114-eth-01
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/ethiopia-flood-fl-20231114-eth-01
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/ethiopia-flood-fl-20231114-eth-01
dataset_id: rdls_hel-eth_wfpadam_flood10163650sqmnov2023_20231114
description: 'ADAM ID: FL-20231114-ETH-01 Flood covering 1016365.0 sq m on Nov 14
  2023 in Ethiopia. It impacted 534273 people.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/ethiopia-flood-fl-20231114-eth-01]'
details: null
exposure:
- asset_type:
    description: Cropland area affected by flooding, including total croplands and
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
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM collected and analyzed geospatial data following the November
    14, 2023 flood event in Ethiopia. Flood extent was mapped from satellite or field
    observations, overlaid with population and cropland datasets to quantify directly
    affected populations and agricultural losses. The resulting dataset integrates
    hazard extent, exposure inventories, and observed impact metrics.
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
- href: https://data.humdata.org/dataset/ethiopia-flood-fl-20231114-eth-01
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population impact from observed flood event affecting 534,273
      people
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
    description: Direct agricultural loss from flooding of cropland areas
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
  description: 'Ethiopia: Flood - 1016365.0 sq m - Nov 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/4d7162e5-82ea-4270-953f-af981e2f447a/resource/b6181efe-55e2-4db7-9309-41a027d65a76/download/fl-20231114-eth-01.geojson
  format: null
  id: resource_b6181efe
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231114-ETH-01.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Flood - 1016365.0 sq m - Nov 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/4d7162e5-82ea-4270-953f-af981e2f447a/resource/03c9eaf1-ce30-45a1-b9ee-e67d7dd054b3/download/fl-20231114-eth-01.tiff
  format: null
  id: resource_03c9eaf1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231114-ETH-01.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Flood - 1016365.0 sq m - Nov 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/4d7162e5-82ea-4270-953f-af981e2f447a/resource/dcd92bc6-423d-48fb-920c-cfdc6e8d4223/download/fl-20231114-eth-01.gpkg
  format: null
  id: resource_dcd92bc6
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231114-ETH-01.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Flood - 1016365.0 sq m - Nov 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/4d7162e5-82ea-4270-953f-af981e2f447a/resource/6dacd340-6ec9-4d6c-b55e-c2e114fe919b/download/metadata.txt
  format: null
  id: resource_6dacd340
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
slug: rdls_hel-eth_wfpadam_flood10163650sqmnov2023_20231114
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
  start: '2023-11-14'
temporal_resolution: null
title: 'Ethiopia: Flood - 1016365.0 sq m - Nov 2023'
version: null
vulnerability: null
---
