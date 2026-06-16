---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_bvt_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bvt_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bvt_buildings
dataset_id: rdls_exp-bvt_hotosm_bouvetislandbuildingsexpo_20260101
description: 'OpenStreetMap contains roughly 0 buildings in this region. The average
  age of data for this region is 3 years ( Last edited 8 months ago ) Read about what
  this summary means : indicators , metrics This theme includes all OpenStreetMap
  features in this area matching ( Learn what tags means here ) : tags[''building'']
  IS NOT NULL Features may have these attributes: name name:en building building:levels
  building:materials addr:full addr:housenumber addr:street addr:city office source
  name:no This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_bvt_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and polygons extracted from OpenStreetMap for
      Bouvet Island
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
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
  description: Building geometries were extracted from OpenStreetMap using the Humanitarian
    OpenStreetMap Team's raw data API, filtering for all features with the 'building'
    tag. Data were exported in multiple vector formats (SHP, KML, GeoJSON, Geopackage)
    for accessibility. The dataset represents the current state of OSM building coverage
    for this region as of the last edit 8 months prior to publication.
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
- href: https://data.humdata.org/dataset/hotosm_bvt_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BVT/buildings/polygons/hotosm_bvt_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bouvet Island Buildings (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_0420d909
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bvt_buildings_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BVT/buildings/polygons/hotosm_bvt_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bouvet Island Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_f110eee9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bvt_buildings_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BVT/buildings/polygons/hotosm_bvt_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bouvet Island Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_fae49896
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bvt_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BVT/buildings/polygons/hotosm_bvt_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bouvet Island Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_9ca2677b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bvt_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bvt_hotosm_bouvetislandbuildingsexpo_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - BVT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Bouvet Island Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
