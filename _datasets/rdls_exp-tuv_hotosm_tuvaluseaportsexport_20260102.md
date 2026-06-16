---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_tuv_sea_ports
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_tuv_sea_ports
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_tuv_sea_ports
dataset_id: rdls_exp-tuv_hotosm_tuvaluseaportsexport_20260102
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''amenity''] = ''ferry_terminal'' OR tags[''building'']
  = ''ferry_terminal'' OR tags[''port''] IS NOT NULL Features may have these attributes:
  name name:en amenity building port operator:type addr:full addr:city source name:tvl
  This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_tuv_sea_ports]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Sea port facilities including ferry terminals and port infrastructure
      in Tuvalu
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
  description: OpenStreetMap features matching port-related tags (amenity=ferry_terminal,
    building=ferry_terminal, port=*) were extracted and exported by the Humanitarian
    OpenStreetMap Team for Tuvalu. The dataset represents a spatial inventory of critical
    maritime infrastructure assets derived from crowdsourced geographic data.
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
- href: https://data.humdata.org/dataset/hotosm_tuv_sea_ports
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/points/hotosm_tuv_sea_ports_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_09e60dd4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/lines/hotosm_tuv_sea_ports_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_abe6aead
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/polygons/hotosm_tuv_sea_ports_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_16e0c5f5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/points/hotosm_tuv_sea_ports_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_109a0c8d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/lines/hotosm_tuv_sea_ports_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_bb026e8a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/polygons/hotosm_tuv_sea_ports_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_695a2005
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/points/hotosm_tuv_sea_ports_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_deb76c62
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/lines/hotosm_tuv_sea_ports_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_7435291c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/polygons/hotosm_tuv_sea_ports_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_8db0f29b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/points/hotosm_tuv_sea_ports_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_42f061e1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/lines/hotosm_tuv_sea_ports_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_746ba129
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/TUV/sea_ports/polygons/hotosm_tuv_sea_ports_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Tuvalu Sea Ports (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_d953fc65
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_tuv_sea_ports_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tuv_hotosm_tuvaluseaportsexport_20260102
spatial:
  bbox: null
  centroid: null
  countries:
  - TUV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-02'
temporal_resolution: null
title: Tuvalu Sea Ports (OpenStreetMap Export)
version: null
vulnerability: null
---
