---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_bes_roads
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bes_roads
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_bes_roads
dataset_id: rdls_exp-bes_hotosm_bonairesinteustatiussabar_20260101
description: 'OpenStreetMap contains roughly 1.3 thousand km of roads in this region.
  Based on AI-mapped estimates, this is approximately 97 % of the total road length
  in the dataset region. The average age of data for the region is 2 years ( Last
  edited 3 months ago ) and 40% of roads were added or updated in the last 6 months.
  Read about what this summary means : indicators , metrics This theme includes all
  OpenStreetMap features in this area matching ( Learn what tags means here ) : tags[''highway'']
  IS NOT NULL Features may have these attributes: name name:en highway surface smoothness
  width lanes oneway bridge layer source This dataset is one of many OpenStreetMap
  exports on HDX . See the Humanitarian OpenStreetMap Team website for more information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_bes_roads]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Road network geometry and attributes including highway type, surface,
      width, and lanes
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
  description: Road network data was collected through OpenStreetMap volunteered geographic
    information contributions and processed by the Humanitarian OpenStreetMap Team's
    raw data API. The dataset represents approximately 1.3 thousand km of roads with
    97% estimated coverage of total road length in the region, with attributes including
    highway classification, surface type, width, lanes, and bridge indicators.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap contributors
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Humanitarian OpenStreetMap Team (HOT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hotosm_bes_roads
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/roads/lines/hotosm_bes_roads_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (ESRI
    Shapefile)
  download_url: null
  format: null
  id: resource_9a989b54
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_roads_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/roads/polygons/hotosm_bes_roads_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (ESRI
    Shapefile)
  download_url: null
  format: null
  id: resource_4f651668
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_roads_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (Geopackage,
    SQLite compatible)
  download_url: https://export.hotosm.org/downloads/08dbd05b-8372-40d5-9665-0ca212ebe49f/hotosm_bes_roads_gpkg.zip
  format: null
  id: resource_f5af2a35
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_roads_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/roads/lines/hotosm_bes_roads_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_7032b8ff
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_roads_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/roads/polygons/hotosm_bes_roads_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_8f8a0649
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_roads_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (.IMG
    for Garmin GPS Devices (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/08dbd05b-8372-40d5-9665-0ca212ebe49f/hotosm_bes_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_2ee87d28
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/roads/lines/hotosm_bes_roads_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_cac7751f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_roads_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/roads/lines/hotosm_bes_roads_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_2f89af0b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_roads_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/roads/polygons/hotosm_bes_roads_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_b3cb89c3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_roads_polygons_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BES/roads/polygons/hotosm_bes_roads_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export) (ZIP
    archive)
  download_url: null
  format: null
  id: resource_b6a1b76d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_bes_roads_polygons_geojson.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bes_hotosm_bonairesinteustatiussabar_20260101
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
title: Bonaire, Sint Eustatius and Saba Roads (OpenStreetMap Export)
version: null
vulnerability: null
---
