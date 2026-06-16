---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_pcn_airports
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_pcn_airports
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_pcn_airports
dataset_id: rdls_exp-pcn_hotosm_pitcairnislandsairportsex_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''aeroway''] IS NOT NULL OR tags[''building'']
  = ''aerodrome'' OR tags[''emergency:helipad''] IS NOT NULL OR tags[''emergency'']
  = ''landing_site'' Features may have these attributes: name name:en aeroway building
  emergency emergency:helipad operator:type capacity:persons addr:full addr:city source
  This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_pcn_airports]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Airport and aerodrome facilities including runways, helipads, and
      landing sites
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
license: ODbL-1.0/
lineage:
  description: OpenStreetMap features matching aeroway, aerodrome building, emergency
    helipad, and emergency landing site tags were extracted for Pitcairn Islands and
    exported in multiple vector formats (SHP, KML, GeoJSON, GeoPackage) as points,
    lines, and polygons by the Humanitarian OpenStreetMap Team.
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
- href: https://data.humdata.org/dataset/hotosm_pcn_airports
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/points/hotosm_pcn_airports_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_f1f3d131
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/lines/hotosm_pcn_airports_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_cc5d3312
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/polygons/hotosm_pcn_airports_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_cfde8f0e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/points/hotosm_pcn_airports_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_d75e8f23
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/lines/hotosm_pcn_airports_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_b8475358
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/polygons/hotosm_pcn_airports_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_a9172586
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/points/hotosm_pcn_airports_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_64b28c7e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/lines/hotosm_pcn_airports_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3410af7b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/polygons/hotosm_pcn_airports_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_0463e3ea
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/points/hotosm_pcn_airports_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_6fca48b0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/lines/hotosm_pcn_airports_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_8c5a245c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PCN/airports/polygons/hotosm_pcn_airports_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Pitcairn Islands Airports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_a564301d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pcn_airports_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-pcn_hotosm_pitcairnislandsairportsex_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - PCN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Pitcairn Islands Airports (OpenStreetMap Export)
version: null
vulnerability: null
---
