---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_mkd_railways
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_mkd_railways
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_mkd_railways
dataset_id: rdls_exp-mkd_hotosm_railwaysexport_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''railway''] IN (''rail'',''station'') Features
  may have these attributes: name name:en railway ele operator:type layer addr:full
  addr:city source name:mk name:sq This dataset is one of many OpenStreetMap exports
  on HDX . See the Humanitarian OpenStreetMap Team website for more information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_mkd_railways]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Railway network infrastructure including rail lines and stations
      in North Macedonia
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
    tags matching railway=rail and railway=station, exported in multiple geospatial
    formats (SHP, GeoJSON, GeoPackage, KML) with attributes including name, operator
    type, elevation, and administrative location information.
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
- href: https://data.humdata.org/dataset/hotosm_mkd_railways
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MKD/railways/lines/hotosm_mkd_railways_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_24510228
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_lines_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: https://export.hotosm.org/downloads/1b531526-fb0e-4df3-aa5a-926587acd3bc/hotosm_mkd_railways_polygons_shp.zip
  format: null
  id: resource_1b71cb74
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (Geopackage, SQLite
    compatible)
  download_url: https://export.hotosm.org/downloads/1b531526-fb0e-4df3-aa5a-926587acd3bc/hotosm_mkd_railways_gpkg.zip
  format: null
  id: resource_fd4b8eba
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MKD/railways/lines/hotosm_mkd_railways_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_2157551a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_lines_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (Google Earth .KML)
  download_url: https://export.hotosm.org/downloads/1b531526-fb0e-4df3-aa5a-926587acd3bc/hotosm_mkd_railways_polygons_kml.zip
  format: null
  id: resource_ebba5941
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (.IMG for Garmin GPS
    Devices (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/1b531526-fb0e-4df3-aa5a-926587acd3bc/hotosm_mkd_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_5e69ed40
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MKD/railways/lines/hotosm_mkd_railways_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_f20459f5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MKD/railways/points/hotosm_mkd_railways_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_af522ac9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MKD/railways/points/hotosm_mkd_railways_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_b7c99bab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MKD/railways/points/hotosm_mkd_railways_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_e8b3e333
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MKD/railways/lines/hotosm_mkd_railways_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_1c6fd085
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/MKD/railways/points/hotosm_mkd_railways_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Macedonia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_64191667
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mkd_railways_points_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mkd_hotosm_railwaysexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - MKD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: North Macedonia Railways (OpenStreetMap Export)
version: null
vulnerability: null
---
