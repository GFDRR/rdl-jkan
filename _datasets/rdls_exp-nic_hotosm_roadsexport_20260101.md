---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_nic_roads
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_nic_roads
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_nic_roads
dataset_id: rdls_exp-nic_hotosm_roadsexport_20260101
description: 'OpenStreetMap contains roughly 68.8 thousand km of roads in this region.
  Based on AI-mapped estimates, this is approximately 57 % of the total road length
  in the dataset region. The average age of data for the region is 1 year, 8 months
  ( Last edited 3 months ago ) and 20% of roads were added or updated in the last
  6 months. Read about what this summary means : indicators , metrics This theme includes
  all OpenStreetMap features in this area matching ( Learn what tags means here )
  : tags[''highway''] IS NOT NULL Features may have these attributes: name name:en
  highway surface smoothness width lanes oneway bridge layer source name:es This dataset
  is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_nic_roads]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Road network with geometry and attributes including surface type,
      lanes, and bridge classification
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
  description: Road network data extracted from OpenStreetMap via the Humanitarian
    OpenStreetMap Team's raw data API, representing approximately 68.8 thousand km
    of mapped roads with attributes including highway type, surface condition, width,
    and lanes. Data quality assessed through AI-mapping estimates and temporal metadata
    tracking.
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
- href: https://data.humdata.org/dataset/hotosm_nic_roads
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIC/roads/lines/hotosm_nic_roads_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_4ff5497c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_roads_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIC/roads/polygons/hotosm_nic_roads_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_3b5a4d53
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_roads_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (Geopackage, SQLite compatible)
  download_url: https://export.hotosm.org/downloads/09220cd4-9cf1-468e-a556-51ec197c83f0/hotosm_nic_roads_gpkg.zip
  format: null
  id: resource_2835e10f
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_roads_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIC/roads/lines/hotosm_nic_roads_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_b202732b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_roads_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIC/roads/polygons/hotosm_nic_roads_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_95c9e725
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_roads_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (.IMG for Garmin GPS Devices
    (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/09220cd4-9cf1-468e-a556-51ec197c83f0/hotosm_nic_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_cc7bfb47
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIC/roads/lines/hotosm_nic_roads_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_2686b2fe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_roads_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIC/roads/lines/hotosm_nic_roads_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_11d36b71
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_roads_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIC/roads/polygons/hotosm_nic_roads_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_e948e845
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_roads_polygons_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIC/roads/polygons/hotosm_nic_roads_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Nicaragua Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_c6383956
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_nic_roads_polygons_geojson.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nic_hotosm_roadsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - NIC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Nicaragua Roads (OpenStreetMap Export)
version: null
vulnerability: null
---
