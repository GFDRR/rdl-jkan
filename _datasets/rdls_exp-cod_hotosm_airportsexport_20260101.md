---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_cod_airports
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_cod_airports
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_cod_airports
dataset_id: rdls_exp-cod_hotosm_airportsexport_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''aeroway''] IS NOT NULL OR tags[''building'']
  = ''aerodrome'' OR tags[''emergency:helipad''] IS NOT NULL OR tags[''emergency'']
  = ''landing_site'' Features may have these attributes: name name:en aeroway building
  emergency emergency:helipad operator:type capacity:persons addr:full addr:city source
  name:fr This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_cod_airports]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Airport and aerodrome facilities including runways, helipads, and
      landing sites with geometric representation
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
    Features were exported in multiple geometric formats (points, lines, polygons)
    and coordinate systems by the Humanitarian OpenStreetMap Team, providing a spatial
    inventory of critical aviation infrastructure assets.
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
- href: https://data.humdata.org/dataset/hotosm_cod_airports
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/points/hotosm_cod_airports_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ESRI
    Shapefile)
  download_url: null
  format: null
  id: resource_a7b9c40c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/lines/hotosm_cod_airports_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ESRI
    Shapefile)
  download_url: null
  format: null
  id: resource_e2d56ed3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/polygons/hotosm_cod_airports_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ESRI
    Shapefile)
  download_url: null
  format: null
  id: resource_89634f17
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/points/hotosm_cod_airports_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_fdda0155
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/lines/hotosm_cod_airports_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_6008700d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/polygons/hotosm_cod_airports_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_fb9b14cf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/points/hotosm_cod_airports_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_0fc33278
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/lines/hotosm_cod_airports_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_17994e4e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/polygons/hotosm_cod_airports_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_b2b2688d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/points/hotosm_cod_airports_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_0449f35e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/lines/hotosm_cod_airports_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_465d672f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/COD/airports/polygons/hotosm_cod_airports_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Democratic Republic of the Congo Airports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_7401bf8c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_cod_airports_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cod_hotosm_airportsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Democratic Republic of the Congo Airports (OpenStreetMap Export)
version: null
vulnerability: null
---
