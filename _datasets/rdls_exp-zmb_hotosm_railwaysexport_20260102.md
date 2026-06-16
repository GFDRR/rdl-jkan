---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_zmb_railways
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_zmb_railways
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_zmb_railways
dataset_id: rdls_exp-zmb_hotosm_railwaysexport_20260102
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''railway''] IN (''rail'',''station'') Features
  may have these attributes: name name:en railway ele operator:type layer addr:full
  addr:city source This dataset is one of many OpenStreetMap exports on HDX . See
  the Humanitarian OpenStreetMap Team website for more information.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_zmb_railways]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Railway network infrastructure including rail lines and stations
      in Zambia
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
- href: https://data.humdata.org/dataset/hotosm_zmb_railways
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/ZMB/railways/points/hotosm_zmb_railways_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Zambia Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_2ab04275
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_zmb_railways_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/ZMB/railways/lines/hotosm_zmb_railways_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Zambia Railways (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_f4077d26
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_zmb_railways_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/ZMB/railways/points/hotosm_zmb_railways_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Zambia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_81931b41
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_zmb_railways_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/ZMB/railways/lines/hotosm_zmb_railways_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Zambia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_cd3bbd6a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_zmb_railways_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/ZMB/railways/lines/hotosm_zmb_railways_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Zambia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_0ea7f0c4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_zmb_railways_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/ZMB/railways/points/hotosm_zmb_railways_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Zambia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_24e2d21f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_zmb_railways_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/ZMB/railways/lines/hotosm_zmb_railways_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Zambia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_b42be26d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_zmb_railways_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/ZMB/railways/points/hotosm_zmb_railways_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Zambia Railways (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_042ebd86
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_zmb_railways_points_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-zmb_hotosm_railwaysexport_20260102
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-02'
temporal_resolution: null
title: Zambia Railways (OpenStreetMap Export)
version: null
vulnerability: null
---
