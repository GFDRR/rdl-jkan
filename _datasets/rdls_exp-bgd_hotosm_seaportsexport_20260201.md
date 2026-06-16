---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_bgd_sea_ports
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bgd_sea_ports
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bgd_sea_ports
dataset_id: rdls_exp-bgd_hotosm_seaportsexport_20260201
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''amenity''] = ''ferry_terminal'' OR tags[''building'']
  = ''ferry_terminal'' OR tags[''port''] IS NOT NULL Features may have these attributes:
  name name:en amenity building port operator:type addr:full addr:city source name:bn
  This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_bgd_sea_ports]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Sea ports, ferry terminals, and port infrastructure facilities in
      Bangladesh with spatial geometry and operational attributes
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
  description: OpenStreetMap features matching port and ferry terminal tags were extracted
    for Bangladesh and exported by the Humanitarian OpenStreetMap Team (HOT) in multiple
    vector formats (SHP, GeoJSON, KML, GeoPackage) with point, line, and polygon geometries.
    The dataset provides a spatial inventory of critical maritime infrastructure assets
    with attributes including facility names, operators, and addresses.
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
- href: https://data.humdata.org/dataset/hotosm_bgd_sea_ports
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/points/hotosm_bgd_sea_ports_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_25340de6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/lines/hotosm_bgd_sea_ports_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_e653b177
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/polygons/hotosm_bgd_sea_ports_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_68e300cd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/points/hotosm_bgd_sea_ports_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_503650ed
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/lines/hotosm_bgd_sea_ports_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_58555903
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/polygons/hotosm_bgd_sea_ports_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_2e5b0679
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/points/hotosm_bgd_sea_ports_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_5ead03b8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/lines/hotosm_bgd_sea_ports_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_1c574739
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/polygons/hotosm_bgd_sea_ports_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_0c5568b6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/points/hotosm_bgd_sea_ports_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_0929f7b3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/lines/hotosm_bgd_sea_ports_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_c724f335
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BGD/sea_ports/polygons/hotosm_bgd_sea_ports_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bangladesh Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_275551f9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bgd_sea_ports_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bgd_hotosm_seaportsexport_20260201
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-02-01'
temporal_resolution: null
title: Bangladesh Sea Ports (OpenStreetMap Export)
version: null
vulnerability: null
---
