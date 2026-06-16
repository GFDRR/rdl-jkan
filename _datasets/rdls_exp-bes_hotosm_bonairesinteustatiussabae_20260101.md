---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_bes_education_facilities
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bes_education_facilities
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bes_education_facilities
dataset_id: rdls_exp-bes_hotosm_bonairesinteustatiussabae_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''amenity''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') OR tags[''building''] IN (''kindergarten'', ''school'',
  ''college'', ''university'') Features may have these attributes: name name:en amenity
  building operator:type capacity:persons addr:full addr:city source This dataset
  is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_bes_education_facilities]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Education facilities (kindergartens, schools, colleges, universities)
      mapped as points and polygons with location and capacity attributes
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
  description: Education facilities in Bonaire, Sint Eustatius and Saba were extracted
    from OpenStreetMap using amenity and building tags matching kindergarten, school,
    college, and university classifications. Features were exported in multiple geospatial
    formats (SHP, GeoJSON, GeoPackage, KML) with attributes including facility name,
    operator type, capacity, and address information.
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
- href: https://data.humdata.org/dataset/hotosm_bes_education_facilities
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/education_facilities/points/hotosm_bes_education_facilities_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_7b03e5a8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_education_facilities_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/education_facilities/polygons/hotosm_bes_education_facilities_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_6fdad6a4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_education_facilities_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (Geopackage, SQLite compatible)
  download_url: https://export.hotosm.org/downloads/08dbd05b-8372-40d5-9665-0ca212ebe49f/hotosm_bes_education_facilities_gpkg.zip
  format: null
  id: resource_4a4caf12
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_education_facilities_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/education_facilities/points/hotosm_bes_education_facilities_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_651d52ee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_education_facilities_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/education_facilities/polygons/hotosm_bes_education_facilities_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_b51f5bf2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_education_facilities_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (.IMG for Garmin GPS Devices (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/08dbd05b-8372-40d5-9665-0ca212ebe49f/hotosm_bes_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_e40d73fa
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/education_facilities/points/hotosm_bes_education_facilities_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_6e4b8eec
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_education_facilities_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/education_facilities/polygons/hotosm_bes_education_facilities_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3c512b6c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_education_facilities_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/education_facilities/points/hotosm_bes_education_facilities_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_8ce3a3e4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_education_facilities_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/education_facilities/polygons/hotosm_bes_education_facilities_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap
    Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_51a2093d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_education_facilities_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bes_hotosm_bonairesinteustatiussabae_20260101
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
title: Bonaire, Sint Eustatius and Saba Education Facilities (OpenStreetMap Export)
version: null
vulnerability: null
---
