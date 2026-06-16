---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_pry_education_facilities
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_pry_education_facilities
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_pry_education_facilities
dataset_id: rdls_exp-pry_hotosm_educationfacilitiesexport_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''amenity''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') OR tags[''building''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') Features may have these attributes: name name:en amenity
  building operator:type capacity:persons addr:full addr:city source name:es name:gn
  This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_pry_education_facilities]'
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
license: ODbL-1.0/
lineage:
  description: Education facility locations and attributes were extracted from OpenStreetMap
    using standardized amenity and building tags (kindergarten, school, college, university).
    Data were converted to multiple geospatial formats (SHP, GeoJSON, GeoPackage,
    KML, Garmin IMG) with both point and polygon representations, preserving facility
    names, addresses, operator types, and capacity information.
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
- href: https://data.humdata.org/dataset/hotosm_pry_education_facilities
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRY/education_facilities/points/hotosm_pry_education_facilities_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_61137495
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_education_facilities_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRY/education_facilities/polygons/hotosm_pry_education_facilities_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_eb5b2f82
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_education_facilities_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (Geopackage, SQLite
    compatible)
  download_url: https://export.hotosm.org/downloads/0e83b263-b9f4-467a-8f9b-41661d084fd6/hotosm_pry_education_facilities_gpkg.zip
  format: null
  id: resource_b4e5feb9
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_education_facilities_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRY/education_facilities/points/hotosm_pry_education_facilities_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_c24520b2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_education_facilities_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRY/education_facilities/polygons/hotosm_pry_education_facilities_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_79ab2ec8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_education_facilities_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (.IMG for Garmin
    GPS Devices (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/0e83b263-b9f4-467a-8f9b-41661d084fd6/hotosm_pry_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_c22e6205
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRY/education_facilities/points/hotosm_pry_education_facilities_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_cd5974a3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_education_facilities_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRY/education_facilities/polygons/hotosm_pry_education_facilities_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_65e72958
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_education_facilities_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRY/education_facilities/points/hotosm_pry_education_facilities_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_dfd20bcd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_education_facilities_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRY/education_facilities/polygons/hotosm_pry_education_facilities_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Paraguay Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3a763811
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pry_education_facilities_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-pry_hotosm_educationfacilitiesexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - PRY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Paraguay Education Facilities (OpenStreetMap Export)
version: null
vulnerability: null
---
