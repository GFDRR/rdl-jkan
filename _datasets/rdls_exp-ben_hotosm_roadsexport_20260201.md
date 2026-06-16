---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_ben_roads
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_ben_roads
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_ben_roads
dataset_id: rdls_exp-ben_hotosm_roadsexport_20260201
description: 'OpenStreetMap contains roughly 79.7 thousand km of roads in this region.
  Based on AI-mapped estimates, this is approximately 35 % of the total road length
  in the dataset region. The average age of data for the region is 4 years ( Last
  edited 4 months ago ) and 11% of roads were added or updated in the last 6 months.
  Read about what this summary means : indicators , metrics This theme includes all
  OpenStreetMap features in this area matching ( Learn what tags means here ) : tags[''highway'']
  IS NOT NULL Features may have these attributes: name name:en highway surface smoothness
  width lanes oneway bridge layer source name:fr This dataset is one of many OpenStreetMap
  exports on HDX . See the Humanitarian OpenStreetMap Team website for more information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_ben_roads]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Road network geometry and attributes including highway type, surface,
      lanes, and bridges
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
  description: Road network data extracted from OpenStreetMap for Benin, containing
    approximately 79.7 thousand km of mapped roads with attributes including highway
    classification, surface type, lanes, and bridge indicators. Data represents volunteered
    geographic information with average age of 4 years and 11% updated within the
    last 6 months.
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
- href: https://data.humdata.org/dataset/hotosm_ben_roads
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BEN/roads/lines/hotosm_ben_roads_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Benin Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_792a615d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ben_roads_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BEN/roads/lines/hotosm_ben_roads_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Benin Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_2cb1fa5d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ben_roads_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BEN/roads/lines/hotosm_ben_roads_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Benin Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_78f9c4a7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ben_roads_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BEN/roads/lines/hotosm_ben_roads_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Benin Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_5396f7c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ben_roads_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BEN/roads/polygons/hotosm_ben_roads_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Benin Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_13ee2fab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ben_roads_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BEN/roads/polygons/hotosm_ben_roads_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Benin Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_a006da17
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ben_roads_polygons_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BEN/roads/polygons/hotosm_ben_roads_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Benin Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_37f24a29
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ben_roads_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/BEN/roads/polygons/hotosm_ben_roads_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Benin Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_49094ec5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ben_roads_polygons_geojson.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ben_hotosm_roadsexport_20260201
spatial:
  bbox: null
  centroid: null
  countries:
  - BEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-02-01'
temporal_resolution: null
title: Benin Roads (OpenStreetMap Export)
version: null
vulnerability: null
---
