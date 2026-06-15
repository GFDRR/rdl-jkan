---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_hrv_education_facilities
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_hrv_education_facilities
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_hrv_education_facilities
dataset_id: rdls_exp-hrv_hotosm_educationfacilitiesexport_20260201
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''amenity''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') OR tags[''building''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') Features may have these attributes: name name:en amenity
  building operator:type capacity:persons addr:full addr:city source name:hr This
  dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_hrv_education_facilities]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Education facilities (kindergartens, schools, colleges, universities)
      in Croatia extracted from OpenStreetMap, represented as points and polygons
      with attributes including name, amenity type, building type, operator, capacity,
      and address.
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
  description: Education facility data was extracted from OpenStreetMap using tag
    filters for amenity and building types associated with educational use (kindergarten,
    school, college, university) over Croatia. The export was produced by the Humanitarian
    OpenStreetMap Team (HOT) and delivered in multiple geospatial formats (SHP, GeoJSON,
    GPKG, KML) for use in humanitarian and disaster risk contexts.
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
- href: https://data.humdata.org/dataset/hotosm_hrv_education_facilities
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/HRV/education_facilities/points/hotosm_hrv_education_facilities_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_9b22d284
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_education_facilities_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/HRV/education_facilities/polygons/hotosm_hrv_education_facilities_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_c96fd7be
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_education_facilities_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (Geopackage, SQLite
    compatible)
  download_url: https://export.hotosm.org/downloads/21c2fd5b-432d-4aea-a036-8e6f9e91037a/hotosm_hrv_education_facilities_gpkg.zip
  format: null
  id: resource_45ba3095
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_education_facilities_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/HRV/education_facilities/points/hotosm_hrv_education_facilities_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_f61fd4e5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_education_facilities_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/HRV/education_facilities/polygons/hotosm_hrv_education_facilities_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_fcb4de49
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_education_facilities_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (.IMG for Garmin
    GPS Devices (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/21c2fd5b-432d-4aea-a036-8e6f9e91037a/hotosm_hrv_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_7d6e5462
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/HRV/education_facilities/points/hotosm_hrv_education_facilities_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_55f1b242
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_education_facilities_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/HRV/education_facilities/polygons/hotosm_hrv_education_facilities_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_c7c3ff95
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_education_facilities_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/HRV/education_facilities/points/hotosm_hrv_education_facilities_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_96bb1bc4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_education_facilities_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/HRV/education_facilities/polygons/hotosm_hrv_education_facilities_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Croatia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_cc0b9952
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_hrv_education_facilities_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-hrv_hotosm_educationfacilitiesexport_20260201
spatial:
  bbox: null
  centroid: null
  countries:
  - HRV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-02-01'
temporal_resolution: null
title: Croatia Education Facilities (OpenStreetMap Export)
version: null
vulnerability: null
---
