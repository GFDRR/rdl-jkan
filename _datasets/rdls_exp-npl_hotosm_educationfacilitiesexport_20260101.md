---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_npl_education_facilities
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_npl_education_facilities
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_npl_education_facilities
dataset_id: rdls_exp-npl_hotosm_educationfacilitiesexport_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''amenity''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') OR tags[''building''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') Features may have these attributes: name name:en amenity
  building operator:type capacity:persons addr:full addr:city source name:ne This
  dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_npl_education_facilities]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Education facilities (kindergartens, schools, colleges, universities)
      mapped as point and polygon geometries with capacity and operator information
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
  description: Education facility locations and attributes were extracted from OpenStreetMap
    using standardized amenity and building tags (kindergarten, school, college, university).
    Data was processed by HOT into multiple geospatial formats (SHP, GeoJSON, KML,
    GeoPackage, CSV) with point and polygon representations, including facility names,
    addresses, operator types, and capacity information for exposure assessment in
    Nepal.
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
- href: https://data.humdata.org/dataset/hotosm_npl_education_facilities
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NPL/education_facilities/points/hotosm_npl_education_facilities_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_d740c14d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NPL/education_facilities/polygons/hotosm_npl_education_facilities_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_2c6a6b15
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NPL/education_facilities/points/hotosm_npl_education_facilities_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_a8a0700d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NPL/education_facilities/polygons/hotosm_npl_education_facilities_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_1309f20a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NPL/education_facilities/points/hotosm_npl_education_facilities_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_bdf7a9d7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NPL/education_facilities/polygons/hotosm_npl_education_facilities_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_92a834cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_polygons_geojson.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (CSV Output along
    with centroid of feature)
  download_url: https://s3.us-east-1.amazonaws.com/exports-stage.hotosm.org/hotosm_npl_education_facilities_points_csv_csv_uid_cb07a970-3423-40a9-b54f-fef91ec6801a.zip
  format: null
  id: resource_6753b9a2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_points_csv.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (CSV Output along
    with centroid of feature)
  download_url: https://s3.us-east-1.amazonaws.com/exports-stage.hotosm.org/hotosm_npl_education_facilities_polygons_csv_csv_uid_9edd3064-3c43-4d13-b737-c629e20ae488.zip
  format: null
  id: resource_7433c4d8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_polygons_csv.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NPL/education_facilities/points/hotosm_npl_education_facilities_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_8b32c450
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NPL/education_facilities/polygons/hotosm_npl_education_facilities_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nepal Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_499915d8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_npl_education_facilities_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-npl_hotosm_educationfacilitiesexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Nepal Education Facilities (OpenStreetMap Export)
version: null
vulnerability: null
---
