---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_vut_populated_places
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_vut_populated_places
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_vut_populated_places
dataset_id: rdls_exp-vut_hotosm_populatedplacesexport_20260102
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''place''] IN (''isolated_dwelling'', ''town'',
  ''village'', ''hamlet'', ''city'') OR tags[''landuse''] IN (''residential'') Features
  may have these attributes: name name:en place landuse population is_in source name:fr
  name:bis This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_vut_populated_places]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Populated places (cities, towns, villages, hamlets, isolated dwellings)
      with point and polygon geometries
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: ODbL-1.0/
lineage:
  description: OpenStreetMap features matching place tags (isolated_dwelling, town,
    village, hamlet, city) and residential landuse were extracted for Vanuatu by HOT
    and exported in multiple geospatial formats (points and polygons). The dataset
    includes population attributes where available from OSM contributors.
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
- href: https://data.humdata.org/dataset/hotosm_vut_populated_places
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/VUT/populated_places/points/hotosm_vut_populated_places_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Vanuatu Populated Places (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_794a0bd2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_vut_populated_places_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/VUT/populated_places/points/hotosm_vut_populated_places_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Vanuatu Populated Places (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3485e1f1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_vut_populated_places_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/VUT/populated_places/points/hotosm_vut_populated_places_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Vanuatu Populated Places (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_f2088c05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_vut_populated_places_points_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/VUT/populated_places/points/hotosm_vut_populated_places_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Vanuatu Populated Places (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_05f0a32b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_vut_populated_places_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/VUT/populated_places/polygons/hotosm_vut_populated_places_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Vanuatu Populated Places (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_1f581b06
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_vut_populated_places_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/VUT/populated_places/polygons/hotosm_vut_populated_places_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Vanuatu Populated Places (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_7b9c583c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_vut_populated_places_polygons_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/VUT/populated_places/polygons/hotosm_vut_populated_places_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Vanuatu Populated Places (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_ce1c9859
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_vut_populated_places_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/VUT/populated_places/polygons/hotosm_vut_populated_places_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Vanuatu Populated Places (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_59c6043f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_vut_populated_places_polygons_shp.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-vut_hotosm_populatedplacesexport_20260102
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-02'
temporal_resolution: null
title: Vanuatu Populated Places (OpenStreetMap Export)
version: null
vulnerability: null
---
