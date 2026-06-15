---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/ethiopia-flood-fl-20231109-eth-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/ethiopia-flood-fl-20231109-eth-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/ethiopia-flood-fl-20231109-eth-00
dataset_id: rdls_hel-eth_wfpadam_flood2057530sqmnov2023_20231109
description: 'ADAM ID: FL-20231109-ETH-00 Flood covering 205753.0 sq m on Nov 09 2023
  in Ethiopia. It impacted 95847 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-flood-fl-20231109-eth-00]'
details: null
exposure:
- asset_type:
    description: Cropland area affected by flooding
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
    description: Population directly affected by flood inundation
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM collected and analyzed geospatial data following the November
    9, 2023 flood event in Ethiopia. Flood extent was mapped from satellite or field
    observations and intersected with population and cropland datasets to quantify
    direct impacts. The resulting geodataset includes administrative boundaries, affected
    population counts, flooded area measurements, and cropland damage assessments.
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
- href: https://data.humdata.org/dataset/ethiopia-flood-fl-20231109-eth-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population impact from observed flood event in November 2023
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
    description: Direct cropland loss from flood inundation
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
  description: 'Ethiopia: Flood - 205753.0 sq m - Nov 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/d1c913c5-9b25-400f-bba4-6db3e0c2121a/resource/479221ae-07af-4937-819d-38e43e61a9f9/download/fl-20231109-eth-00.geojson
  format: null
  id: resource_479221ae
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231109-ETH-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Flood - 205753.0 sq m - Nov 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/d1c913c5-9b25-400f-bba4-6db3e0c2121a/resource/2c17bf20-49ee-4ce7-83ad-4b102b1c10d4/download/fl-20231109-eth-00.tiff
  format: null
  id: resource_2c17bf20
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231109-ETH-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Flood - 205753.0 sq m - Nov 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/d1c913c5-9b25-400f-bba4-6db3e0c2121a/resource/9e6abcd6-746a-4fee-b8d2-a3cc20f23b84/download/fl-20231109-eth-00.gpkg
  format: null
  id: resource_9e6abcd6
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231109-ETH-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Flood - 205753.0 sq m - Nov 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/d1c913c5-9b25-400f-bba4-6db3e0c2121a/resource/853ed1c1-d0a1-4498-b5ac-d2e8c005d75b/download/metadata.txt
  format: null
  id: resource_853ed1c1
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
slug: rdls_hel-eth_wfpadam_flood2057530sqmnov2023_20231109
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
  start: '2023-11-09'
temporal_resolution: null
title: 'Ethiopia: Flood - 205753.0 sq m - Nov 2023'
version: null
vulnerability: null
---
