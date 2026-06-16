---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_brb_roads
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_brb_roads
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_brb_roads
dataset_id: rdls_exp-brb_hotosm_barbadosroadsexport_20260201
description: 'OpenStreetMap contains roughly 3.8 thousand km of roads in this region.
  Based on AI-mapped estimates, this is approximately 98 % of the total road length
  in the dataset region. The average age of data for the region is 1 year, 5 months
  ( Last edited 4 months ago ) and 3% of roads were added or updated in the last 6
  months. Read about what this summary means : indicators , metrics This theme includes
  all OpenStreetMap features in this area matching ( Learn what tags means here )
  : tags[''highway''] IS NOT NULL Features may have these attributes: name name:en
  highway surface smoothness width lanes oneway bridge layer source This dataset is
  one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap Team
  website for more information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_brb_roads]'
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
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Road network data sourced from OpenStreetMap contributors through volunteered
    geographic information, exported and standardized by the Humanitarian OpenStreetMap
    Team (HOT) into multiple geospatial formats (SHP, GeoJSON, KML, GeoPackage) with
    quality metrics indicating 98% coverage of total road length in the region.
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
- href: https://data.humdata.org/dataset/hotosm_brb_roads
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BRB/roads/lines/hotosm_brb_roads_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Barbados Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_3fd7b22a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_brb_roads_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BRB/roads/lines/hotosm_brb_roads_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Barbados Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_66297dad
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_brb_roads_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BRB/roads/lines/hotosm_brb_roads_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Barbados Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_0297e7a8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_brb_roads_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BRB/roads/lines/hotosm_brb_roads_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Barbados Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_2767da3c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_brb_roads_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BRB/roads/polygons/hotosm_brb_roads_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Barbados Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3bcb98f7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_brb_roads_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BRB/roads/polygons/hotosm_brb_roads_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Barbados Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_90db3ae6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_brb_roads_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BRB/roads/polygons/hotosm_brb_roads_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Barbados Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_7a49e2bd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_brb_roads_polygons_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BRB/roads/polygons/hotosm_brb_roads_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Barbados Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_a38e255b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_brb_roads_polygons_geojson.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-brb_hotosm_barbadosroadsexport_20260201
spatial:
  bbox: null
  centroid: null
  countries:
  - BRB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-02-01'
temporal_resolution: null
title: Barbados Roads (OpenStreetMap Export)
version: null
vulnerability: null
---
