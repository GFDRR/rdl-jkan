---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_grc_railways
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_grc_railways
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_grc_railways
dataset_id: rdls_exp-grc_hotosm_railwaysexport_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''railway''] IN (''rail'',''station'') Features
  may have these attributes: name name:en railway ele operator:type layer addr:full
  addr:city source name:el This dataset is one of many OpenStreetMap exports on HDX
  . See the Humanitarian OpenStreetMap Team website for more information.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_grc_railways]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Railway network infrastructure including rail lines and stations
      in Greece
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Railway infrastructure data extracted from OpenStreetMap using feature
    tags for rail lines and stations, provided in multiple geospatial formats (SHP,
    GeoJSON, KML, GeoPackage) by the Humanitarian OpenStreetMap Team. The dataset
    represents a spatial inventory of transportation infrastructure assets without
    hazard or impact components.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap contributors
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hotosm_grc_railways
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GRC/railways/lines/hotosm_grc_railways_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Greece Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_91b0aafb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_grc_railways_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GRC/railways/lines/hotosm_grc_railways_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Greece Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_12807d20
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_grc_railways_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GRC/railways/points/hotosm_grc_railways_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Greece Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_6eab0f74
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_grc_railways_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GRC/railways/points/hotosm_grc_railways_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Greece Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3dd02d9a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_grc_railways_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GRC/railways/lines/hotosm_grc_railways_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Greece Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_17cd14dc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_grc_railways_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GRC/railways/points/hotosm_grc_railways_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Greece Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_ee7567bd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_grc_railways_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GRC/railways/lines/hotosm_grc_railways_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Greece Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_ad888d41
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_grc_railways_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GRC/railways/points/hotosm_grc_railways_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Greece Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_37bc42aa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_grc_railways_points_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-grc_hotosm_railwaysexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - GRC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Greece Railways (OpenStreetMap Export)
version: null
vulnerability: null
---
