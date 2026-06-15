---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_gmb_education_facilities
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_gmb_education_facilities
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_gmb_education_facilities
dataset_id: rdls_exp-gmb_hotosm_educationfacilitiesexport_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''amenity''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') OR tags[''building''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') Features may have these attributes: name name:en amenity
  building operator:type capacity:persons addr:full addr:city source This dataset
  is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_gmb_education_facilities]'
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
    Data were exported by the Humanitarian OpenStreetMap Team (HOT) in multiple geospatial
    formats (SHP, KML, GeoJSON, GeoPackage) as point and polygon geometries with facility
    metadata including name, operator type, and capacity.
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
- href: https://data.humdata.org/dataset/hotosm_gmb_education_facilities
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GMB/education_facilities/points/hotosm_gmb_education_facilities_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Gambia Education Facilities (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_128c02d8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_gmb_education_facilities_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GMB/education_facilities/polygons/hotosm_gmb_education_facilities_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Gambia Education Facilities (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_fbd49afe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_gmb_education_facilities_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GMB/education_facilities/points/hotosm_gmb_education_facilities_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Gambia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_d0783958
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_gmb_education_facilities_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GMB/education_facilities/polygons/hotosm_gmb_education_facilities_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Gambia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3adf079d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_gmb_education_facilities_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GMB/education_facilities/points/hotosm_gmb_education_facilities_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Gambia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_85cd17c0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_gmb_education_facilities_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GMB/education_facilities/polygons/hotosm_gmb_education_facilities_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Gambia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_b1853215
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_gmb_education_facilities_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GMB/education_facilities/points/hotosm_gmb_education_facilities_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Gambia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_5b4c8fb7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_gmb_education_facilities_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/GMB/education_facilities/polygons/hotosm_gmb_education_facilities_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Gambia Education Facilities (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_49205db8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_gmb_education_facilities_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gmb_hotosm_educationfacilitiesexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - GMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Gambia Education Facilities (OpenStreetMap Export)
version: null
vulnerability: null
---
