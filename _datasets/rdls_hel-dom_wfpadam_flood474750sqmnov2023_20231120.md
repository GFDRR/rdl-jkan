---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/dominican-republic-flood-fl-20231120-dom-00
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/dominican-republic-flood-fl-20231120-dom-00
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/dominican-republic-flood-fl-20231120-dom-00
dataset_id: rdls_hel-dom_wfpadam_flood474750sqmnov2023_20231120
description: 'ADAM ID: FL-20231120-DOM-00 Flood covering 47475.0 sq m on Nov 20 2023
  in Dominican Republic. It impacted 349525 people.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/dominican-republic-flood-fl-20231120-dom-00]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM collected and mapped observed flood extent (47,475 sq m) from
    the November 20, 2023 flood event in Dominican Republic. Flood boundaries were
    intersected with gridded population and cropland datasets to quantify directly
    affected population (349,525 people) and flooded agricultural area. Data were
    processed into geospatial formats (GeoJSON, GeoTIFF, GeoPackage) for operational
    response dashboards.
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
- href: https://data.humdata.org/dataset/dominican-republic-flood-fl-20231120-dom-00
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population affected by flood inundation
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
  description: 'Dominican Republic: Flood - 47475.0 sq m - Nov 2023 (GeoJSON File)'
  download_url: https://data.humdata.org/dataset/b9265db1-88a2-4dd0-99b5-778d02116ebc/resource/4c5e9067-0ba3-4f3a-a188-703efea15dcf/download/fl-20231120-dom-00.geojson
  format: null
  id: resource_4c5e9067
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231120-DOM-00.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Flood - 47475.0 sq m - Nov 2023 (GeoTIFF File)'
  download_url: https://data.humdata.org/dataset/b9265db1-88a2-4dd0-99b5-778d02116ebc/resource/212099e1-ea1f-4369-9af5-b74cef80fdea/download/fl-20231120-dom-00.tiff
  format: null
  id: resource_212099e1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231120-DOM-00.tiff
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Flood - 47475.0 sq m - Nov 2023 (Geopackage File)'
  download_url: https://data.humdata.org/dataset/b9265db1-88a2-4dd0-99b5-778d02116ebc/resource/10174472-e232-45be-97a9-f4942326fe93/download/fl-20231120-dom-00.gpkg
  format: null
  id: resource_10174472
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL-20231120-DOM-00.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Dominican Republic: Flood - 47475.0 sq m - Nov 2023 (Metadata File)'
  download_url: https://data.humdata.org/dataset/b9265db1-88a2-4dd0-99b5-778d02116ebc/resource/c9c24137-4d4a-4daa-ab5e-6a75fed5794d/download/metadata.txt
  format: null
  id: resource_c9c24137
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
slug: rdls_hel-dom_wfpadam_flood474750sqmnov2023_20231120
spatial:
  bbox: null
  centroid: null
  countries:
  - DOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-20'
temporal_resolution: null
title: 'Dominican Republic: Flood - 47475.0 sq m - Nov 2023'
version: null
vulnerability: null
---
