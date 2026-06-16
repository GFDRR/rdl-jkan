---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_slb_roads
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_slb_roads
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_slb_roads
dataset_id: rdls_exp-slb_hotosm_roadsexport_20260102
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''highway''] IS NOT NULL Features may have
  these attributes: name name:en highway surface smoothness width lanes oneway bridge
  layer source This dataset is one of many OpenStreetMap exports on HDX . See the
  Humanitarian OpenStreetMap Team website for more information.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_slb_roads]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Road network geometry and attributes including highway classification,
      surface type, and structural characteristics
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
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Road network data extracted from OpenStreetMap using highway tag filtering
    and exported in multiple geospatial formats (SHP, GeoJSON, KML, GeoPackage) by
    the Humanitarian OpenStreetMap Team. The dataset represents the spatial inventory
    of road infrastructure with attributes including surface type, lanes, and bridge
    presence.
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
- href: https://data.humdata.org/dataset/hotosm_slb_roads
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SLB/roads/lines/hotosm_slb_roads_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Solomon Islands Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_969ef0bc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_slb_roads_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SLB/roads/lines/hotosm_slb_roads_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Solomon Islands Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_5cca4644
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_slb_roads_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SLB/roads/lines/hotosm_slb_roads_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Solomon Islands Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_9cabc8c5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_slb_roads_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SLB/roads/lines/hotosm_slb_roads_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Solomon Islands Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_06554163
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_slb_roads_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SLB/roads/polygons/hotosm_slb_roads_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Solomon Islands Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_8a612150
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_slb_roads_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SLB/roads/polygons/hotosm_slb_roads_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Solomon Islands Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_150bfa46
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_slb_roads_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SLB/roads/polygons/hotosm_slb_roads_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Solomon Islands Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_55104a73
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_slb_roads_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SLB/roads/polygons/hotosm_slb_roads_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Solomon Islands Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_d0b4ce68
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_slb_roads_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-slb_hotosm_roadsexport_20260102
spatial:
  bbox: null
  centroid: null
  countries:
  - SLB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-02'
temporal_resolution: null
title: Solomon Islands Roads (OpenStreetMap Export)
version: null
vulnerability: null
---
