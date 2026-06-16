---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/hotosm_bhs_roads
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bhs_roads
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bhs_roads
dataset_id: rdls_exp-bhs_hotosm_bahamasroadsexport_20260201
description: 'OpenStreetMap contains roughly 11.9 thousand km of roads in this region.
  Based on AI-mapped estimates, this is approximately 71 % of the total road length
  in the dataset region. The average age of data for the region is 6 years ( Last
  edited 4 months ago ) and 5% of roads were added or updated in the last 6 months.
  Read about what this summary means : indicators , metrics This theme includes all
  OpenStreetMap features in this area matching ( Learn what tags means here ) : tags[''highway'']
  IS NOT NULL Features may have these attributes: name name:en highway surface smoothness
  width lanes oneway bridge layer source This dataset is one of many OpenStreetMap
  exports on HDX . See the Humanitarian OpenStreetMap Team website for more information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_bhs_roads]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Road network in the Bahamas with geometric and attribute data including
      surface type, lanes, and bridge information
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
      quantity_kind: length
      unit: null
hazard: null
license: ODbL-1.0/
lineage:
  description: Road network data was extracted from OpenStreetMap by the Humanitarian
    OpenStreetMap Team (HOT) using their raw-data-api, representing approximately
    11.9 thousand km of mapped roads with attributes including highway classification,
    surface type, width, lanes, and bridge status. The dataset reflects volunteer
    contributions with an average data age of 6 years and 5% of roads updated within
    the last 6 months.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hotosm_bhs_roads
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BHS/roads/lines/hotosm_bhs_roads_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_4fbe28f7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_roads_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BHS/roads/polygons/hotosm_bhs_roads_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_d78dc5c0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_roads_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (Geopackage, SQLite compatible)
  download_url: https://export.hotosm.org/downloads/23f31c59-10d1-43f3-94db-6752ad72ab5f/hotosm_bhs_roads_gpkg.zip
  format: null
  id: resource_4b7b6aa7
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_roads_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BHS/roads/lines/hotosm_bhs_roads_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_b0f96e1b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_roads_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BHS/roads/polygons/hotosm_bhs_roads_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_132bb1f3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_roads_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (.IMG for Garmin GPS Devices (All
    OSM layers for area))
  download_url: https://export.hotosm.org/downloads/23f31c59-10d1-43f3-94db-6752ad72ab5f/hotosm_bhs_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_e66d72c5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BHS/roads/lines/hotosm_bhs_roads_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_49029aef
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_roads_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BHS/roads/lines/hotosm_bhs_roads_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_48dc707c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_roads_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BHS/roads/polygons/hotosm_bhs_roads_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_e34086a5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_roads_polygons_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BHS/roads/polygons/hotosm_bhs_roads_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bahamas Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_bb3bb5a8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bhs_roads_polygons_geojson.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bhs_hotosm_bahamasroadsexport_20260201
spatial:
  bbox: null
  centroid: null
  countries:
  - BHS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-02-01'
temporal_resolution: null
title: Bahamas Roads (OpenStreetMap Export)
version: null
vulnerability: null
---
