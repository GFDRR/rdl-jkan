---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_bes_sea_ports
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bes_sea_ports
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bes_sea_ports
dataset_id: rdls_exp-bes_hotosm_bonairesinteustatiussabas_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''amenity''] = ''ferry_terminal'' OR tags[''building'']
  = ''ferry_terminal'' OR tags[''port''] IS NOT NULL Features may have these attributes:
  name name:en amenity building port operator:type addr:full addr:city source This
  dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_bes_sea_ports]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Sea port facilities including ferry terminals and port infrastructure
      in Bonaire, Sint Eustatius and Saba
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
  description: Sea port and ferry terminal features were extracted from OpenStreetMap
    using tag-based filtering (amenity='ferry_terminal', building='ferry_terminal',
    port IS NOT NULL) and exported in multiple geospatial formats (SHP, GeoJSON, GeoPackage,
    KML) by the Humanitarian OpenStreetMap Team for the Bonaire, Sint Eustatius and
    Saba region.
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
- href: https://data.humdata.org/dataset/hotosm_bes_sea_ports
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/points/hotosm_bes_sea_ports_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ESRI
    Shapefile)
  download_url: null
  format: null
  id: resource_5528fcbd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/lines/hotosm_bes_sea_ports_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ESRI
    Shapefile)
  download_url: null
  format: null
  id: resource_022592cb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/polygons/hotosm_bes_sea_ports_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ESRI
    Shapefile)
  download_url: null
  format: null
  id: resource_858c7867
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (Geopackage,
    SQLite compatible)
  download_url: https://export.hotosm.org/downloads/08dbd05b-8372-40d5-9665-0ca212ebe49f/hotosm_bes_sea_ports_gpkg.zip
  format: null
  id: resource_dd95a66e
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/points/hotosm_bes_sea_ports_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_03fc8c24
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/lines/hotosm_bes_sea_ports_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_3f5f6c01
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/polygons/hotosm_bes_sea_ports_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_725ffa65
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (.IMG
    for Garmin GPS Devices (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/08dbd05b-8372-40d5-9665-0ca212ebe49f/hotosm_bes_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_bd7063a5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/points/hotosm_bes_sea_ports_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_f71c9d4c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/lines/hotosm_bes_sea_ports_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_74be5362
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/polygons/hotosm_bes_sea_ports_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_e8f2b1cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/points/hotosm_bes_sea_ports_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_caa67cae
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/lines/hotosm_bes_sea_ports_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_d219da39
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/sea_ports/polygons/hotosm_bes_sea_ports_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_0abaffb5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_sea_ports_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bes_hotosm_bonairesinteustatiussabas_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - BES
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Bonaire, Sint Eustatius and Saba Sea Ports (OpenStreetMap Export)
version: null
vulnerability: null
---
