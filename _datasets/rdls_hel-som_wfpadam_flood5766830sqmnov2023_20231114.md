---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/somalia-flood-fl-20231114-som-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/somalia-flood-fl-20231114-som-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/somalia-flood-fl-20231114-som-00
dataset_id: rdls_hel-som_wfpadam_flood5766830sqmnov2023_20231114
description: 'ADAM ID: FL-20231114-SOM-00 Flood covering 576683.0 sq m on Nov 14 2023
  in Somalia. It impacted 320755 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-flood-fl-20231114-som-00]'
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
    description: Population directly affected by the flood event
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
  description: WFP ADAM collected and mapped observed flood extent and socio-economic
    impacts following the 14 November 2023 flood event in Somalia. Geospatial flood
    boundaries were intersected with population and cropland datasets to quantify
    directly affected populations (320,755 people) and flooded cropland area. The
    resulting multi-format dataset (GeoJSON, GeoTIFF, GeoPackage) provides post-event
    loss assessment for humanitarian response.
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
- href: https://data.humdata.org/dataset/somalia-flood-fl-20231114-som-00
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
    description: Direct cropland loss from observed flood inundation
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
  description: 'Somalia: Flood - 576683.0 sq m - Nov 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/598b87ec-3f17-4051-91f9-a86124f811eb/resource/8f7fdd98-8ceb-4a43-a644-3bdaf638fc57/download/fl-20231114-som-00.geojson
  format: null
  id: resource_8f7fdd98
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231114-SOM-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Flood - 576683.0 sq m - Nov 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/598b87ec-3f17-4051-91f9-a86124f811eb/resource/d5d7c3ca-f9d6-438b-b32f-eb885762893c/download/fl-20231114-som-00.tiff
  format: null
  id: resource_d5d7c3ca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231114-SOM-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Flood - 576683.0 sq m - Nov 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/598b87ec-3f17-4051-91f9-a86124f811eb/resource/36a3ed4e-c7b7-417f-b432-6db2ab62776c/download/fl-20231114-som-00.gpkg
  format: null
  id: resource_36a3ed4e
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231114-SOM-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia: Flood - 576683.0 sq m - Nov 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/598b87ec-3f17-4051-91f9-a86124f811eb/resource/002bb4a4-7193-417f-ad30-d31d2c4433eb/download/metadata.txt
  format: null
  id: resource_002bb4a4
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
slug: rdls_hel-som_wfpadam_flood5766830sqmnov2023_20231114
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
  start: '2023-11-14'
temporal_resolution: null
title: 'Somalia: Flood - 576683.0 sq m - Nov 2023'
version: null
vulnerability: null
---
