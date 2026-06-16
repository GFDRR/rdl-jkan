---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_caf_airports
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_caf_airports
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_caf_airports
dataset_id: rdls_exp-caf_hotosm_airportsexport_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''aeroway''] IS NOT NULL OR tags[''building'']
  = ''aerodrome'' OR tags[''emergency:helipad''] IS NOT NULL OR tags[''emergency'']
  = ''landing_site'' Features may have these attributes: name name:en aeroway building
  emergency emergency:helipad operator:type capacity:persons addr:full addr:city source
  name:fr name:sg This dataset is one of many OpenStreetMap exports on HDX . See the
  Humanitarian OpenStreetMap Team website for more information.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_caf_airports]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Airport and aerodrome facilities including runways, helipads, and
      landing sites in Central African Republic
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
      quantity_kind: count
      unit: count
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: OpenStreetMap features matching aeroway tags, aerodrome buildings,
    emergency helipads, and landing sites were extracted and exported by the Humanitarian
    OpenStreetMap Team (HOT) for Central African Republic. The dataset provides multi-format
    geospatial representations (points, lines, polygons) of aviation infrastructure
    with attributes including facility names, operators, and capacity information.
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
- href: https://data.humdata.org/dataset/hotosm_caf_airports
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/points/hotosm_caf_airports_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_88329090
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/lines/hotosm_caf_airports_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_577bc679
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/polygons/hotosm_caf_airports_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_b6169968
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (Geopackage,
    SQLite compatible)
  download_url: https://export.hotosm.org/downloads/05c2ab45-488a-4b64-ac70-5a93a56c581a/hotosm_caf_airports_gpkg.zip
  format: null
  id: resource_9f69154f
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/points/hotosm_caf_airports_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_084d6c34
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/lines/hotosm_caf_airports_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_6941890e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/polygons/hotosm_caf_airports_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_72941e23
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (.IMG for
    Garmin GPS Devices (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/05c2ab45-488a-4b64-ac70-5a93a56c581a/hotosm_caf_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_00b0f71e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/points/hotosm_caf_airports_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3fdd6e6a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/lines/hotosm_caf_airports_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_155cf128
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/polygons/hotosm_caf_airports_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_46feae40
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/points/hotosm_caf_airports_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_59801a07
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/lines/hotosm_caf_airports_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_e3d25ab9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CAF/airports/polygons/hotosm_caf_airports_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Central African Republic Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_25b29cfc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_caf_airports_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-caf_hotosm_airportsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Central African Republic Airports (OpenStreetMap Export)
version: null
vulnerability: null
---
