---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_jpn_airports
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_jpn_airports
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_jpn_airports
dataset_id: rdls_exp-jpn_hotosm_airportsexport_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''aeroway''] IS NOT NULL OR tags[''building'']
  = ''aerodrome'' OR tags[''emergency:helipad''] IS NOT NULL OR tags[''emergency'']
  = ''landing_site'' Features may have these attributes: name name:en aeroway building
  emergency emergency:helipad operator:type capacity:persons addr:full addr:city source
  name:ja This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_jpn_airports]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Airport and aerodrome facilities including runways, helipads, and
      landing sites with geographic location and operational attributes
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
  description: Airport and aerodrome infrastructure features were extracted from OpenStreetMap
    using tag-based filtering (aeroway, building=aerodrome, emergency:helipad, emergency=landing_site).
    The dataset provides point, line, and polygon geometries with facility attributes
    sourced from volunteer contributors and published in multiple geospatial formats
    for disaster risk exposure assessment.
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
- href: https://data.humdata.org/dataset/hotosm_jpn_airports
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/points/hotosm_jpn_airports_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_870321ab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/points/hotosm_jpn_airports_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_179d6ca9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/points/hotosm_jpn_airports_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_f04c67a6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/points/hotosm_jpn_airports_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_ca28ca2d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/lines/hotosm_jpn_airports_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_bd78308e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/lines/hotosm_jpn_airports_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_d13d635f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/lines/hotosm_jpn_airports_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_9a6cb089
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/lines/hotosm_jpn_airports_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3cfeef0d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/polygons/hotosm_jpn_airports_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_a65b1e19
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/polygons/hotosm_jpn_airports_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_bb0a3c1e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/polygons/hotosm_jpn_airports_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_d725f4b5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JPN/airports/polygons/hotosm_jpn_airports_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Japan Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_2ab2bb65
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jpn_airports_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jpn_hotosm_airportsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - JPN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Japan Airports (OpenStreetMap Export)
version: null
vulnerability: null
---
