---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/congo-flood-fl-20231121-cog-02
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/congo-flood-fl-20231121-cog-02
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/congo-flood-fl-20231121-cog-02
dataset_id: rdls_hel-cog_wfpadam_flood3460990sqmnov2023_20231121
description: 'ADAM ID: FL-20231121-COG-02 Flood covering 346099.0 sq m on Nov 21 2023
  in Congo. It impacted 43821 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/congo-flood-fl-20231121-cog-02]'
details: null
exposure:
- asset_type:
    description: Total population in the flood-affected area
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
    description: Cropland area within the flood extent
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
  description: WFP ADAM collected and analyzed geospatial data following the November
    21, 2023 flood event in Congo. Flood extent was mapped from satellite or field
    observations, overlaid with population and cropland datasets to quantify direct
    impacts. The resulting geodataset includes flood polygon geometry, affected population
    counts (43,821 people), and flooded cropland area.
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
- href: https://data.humdata.org/dataset/congo-flood-fl-20231121-cog-02
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by the November 2023 flood event
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
  description: 'Congo: Flood - 346099.0 sq m - Nov 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/2e836911-cd65-4afb-ac67-ba73b17ad01c/resource/3f04db0c-54ca-49ac-a57a-0fcc514b9f92/download/fl-20231121-cog-02.geojson
  format: null
  id: resource_3f04db0c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-COG-02.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Congo: Flood - 346099.0 sq m - Nov 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/2e836911-cd65-4afb-ac67-ba73b17ad01c/resource/a3ad18d3-b5df-4a3f-b586-140c4b3fbdf6/download/fl-20231121-cog-02.tiff
  format: null
  id: resource_a3ad18d3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-COG-02.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Congo: Flood - 346099.0 sq m - Nov 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/2e836911-cd65-4afb-ac67-ba73b17ad01c/resource/ead405e9-d947-402c-8aef-06979f7e4bc2/download/fl-20231121-cog-02.gpkg
  format: null
  id: resource_ead405e9
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231121-COG-02.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Congo: Flood - 346099.0 sq m - Nov 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/2e836911-cd65-4afb-ac67-ba73b17ad01c/resource/1f3e85a8-64f8-4683-aa2c-945addb74aaf/download/metadata.txt
  format: null
  id: resource_1f3e85a8
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
slug: rdls_hel-cog_wfpadam_flood3460990sqmnov2023_20231121
spatial:
  bbox: null
  centroid: null
  countries:
  - COG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-21'
temporal_resolution: null
title: 'Congo: Flood - 346099.0 sq m - Nov 2023'
version: null
vulnerability: null
---
