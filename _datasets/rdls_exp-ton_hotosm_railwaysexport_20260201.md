---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_ton_railways
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_ton_railways
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_ton_railways
dataset_id: rdls_exp-ton_hotosm_railwaysexport_20260201
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''railway''] IN (''rail'',''station'') Features
  may have these attributes: name name:en railway ele operator:type layer addr:full
  addr:city source This dataset is one of many OpenStreetMap exports on HDX . See
  the Humanitarian OpenStreetMap Team website for more information.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_ton_railways]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Railway network infrastructure including rail lines and stations
      in Tonga
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
license: ODbL-1.0/
lineage:
  description: Railway infrastructure data extracted from OpenStreetMap using feature
    tags for rail lines and stations, provided in multiple geospatial formats (SHP,
    GeoJSON, GeoPackage, KML) by the Humanitarian OpenStreetMap Team for Tonga.
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
- href: https://data.humdata.org/dataset/hotosm_ton_railways
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TON/railways/points/hotosm_ton_railways_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_48266eb8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TON/railways/lines/hotosm_ton_railways_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_c9f9e9f8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_lines_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: https://export.hotosm.org/downloads/08459714-73ee-459c-a9aa-63545a86d554/hotosm_ton_railways_polygons_shp.zip
  format: null
  id: resource_6f44c6ea
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (Geopackage, SQLite compatible)
  download_url: https://export.hotosm.org/downloads/08459714-73ee-459c-a9aa-63545a86d554/hotosm_ton_railways_gpkg.zip
  format: null
  id: resource_20868f33
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TON/railways/points/hotosm_ton_railways_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_7b952e57
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TON/railways/lines/hotosm_ton_railways_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_e69e1e0d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_lines_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (Google Earth .KML)
  download_url: https://export.hotosm.org/downloads/08459714-73ee-459c-a9aa-63545a86d554/hotosm_ton_railways_polygons_kml.zip
  format: null
  id: resource_a5312c71
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (.IMG for Garmin GPS Devices
    (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/08459714-73ee-459c-a9aa-63545a86d554/hotosm_ton_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_37aaab00
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TON/railways/lines/hotosm_ton_railways_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_dd65dc1f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TON/railways/points/hotosm_ton_railways_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_60d558c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TON/railways/lines/hotosm_ton_railways_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_37d867e8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TON/railways/points/hotosm_ton_railways_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tonga Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_c7cd0891
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ton_railways_points_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ton_hotosm_railwaysexport_20260201
spatial:
  bbox: null
  centroid: null
  countries:
  - TON
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-02-01'
temporal_resolution: null
title: Tonga Railways (OpenStreetMap Export)
version: null
vulnerability: null
---
