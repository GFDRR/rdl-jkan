---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_prk_roads
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_prk_roads
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_prk_roads
dataset_id: rdls_exp-prk_hotosm_roadsexport_20260101
description: 'OpenStreetMap contains roughly 116.0 thousand km of roads in this region.
  Based on AI-mapped estimates, this is approximately 92 % of the total road length
  in the dataset region. The average age of data for the region is 4 years ( Last
  edited 3 months ago ) and 14% of roads were added or updated in the last 6 months.
  Read about what this summary means : indicators , metrics This theme includes all
  OpenStreetMap features in this area matching ( Learn what tags means here ) : tags[''highway'']
  IS NOT NULL Features may have these attributes: name name:en highway surface smoothness
  width lanes oneway bridge layer source name:ko This dataset is one of many OpenStreetMap
  exports on HDX . See the Humanitarian OpenStreetMap Team website for more information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_prk_roads]'
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
    information contributions and exported by the Humanitarian OpenStreetMap Team.
    The dataset includes 116,000 km of roads with attributes such as highway classification,
    surface type, width, and lanes, representing approximately 92% of total road length
    in the region based on AI-mapped estimates.
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
- href: https://data.humdata.org/dataset/hotosm_prk_roads
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRK/roads/lines/hotosm_prk_roads_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Korea Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_769245a4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_prk_roads_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRK/roads/lines/hotosm_prk_roads_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Korea Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_e8a89cf3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_prk_roads_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRK/roads/lines/hotosm_prk_roads_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Korea Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_f64b6bc0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_prk_roads_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRK/roads/lines/hotosm_prk_roads_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Korea Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_a6ec26be
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_prk_roads_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRK/roads/polygons/hotosm_prk_roads_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Korea Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_9d5f2710
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_prk_roads_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRK/roads/polygons/hotosm_prk_roads_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Korea Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_32200901
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_prk_roads_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRK/roads/polygons/hotosm_prk_roads_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Korea Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_66f41ce3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_prk_roads_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PRK/roads/polygons/hotosm_prk_roads_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: North Korea Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_385d307c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_prk_roads_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-prk_hotosm_roadsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - PRK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: North Korea Roads (OpenStreetMap Export)
version: null
vulnerability: null
---
