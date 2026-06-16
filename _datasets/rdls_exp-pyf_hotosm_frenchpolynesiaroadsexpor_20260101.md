---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_pyf_roads
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_pyf_roads
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_pyf_roads
dataset_id: rdls_exp-pyf_hotosm_frenchpolynesiaroadsexpor_20260101
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''highway''] IS NOT NULL Features may have
  these attributes: name name:en highway surface smoothness width lanes oneway bridge
  layer source name:fr This dataset is one of many OpenStreetMap exports on HDX .
  See the Humanitarian OpenStreetMap Team website for more information.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_pyf_roads]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Road network geometry and attributes including highway classification,
      surface type, and structural properties
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
  description: Road network data extracted from OpenStreetMap using feature filtering
    on highway tags, compiled and distributed by Humanitarian OpenStreetMap Team (HOT)
    in multiple geospatial formats (SHP, GeoJSON, KML, GeoPackage) for French Polynesia.
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
- href: https://data.humdata.org/dataset/hotosm_pyf_roads
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PYF/roads/lines/hotosm_pyf_roads_lines_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: French Polynesia Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_3aedc223
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pyf_roads_lines_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PYF/roads/lines/hotosm_pyf_roads_lines_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: French Polynesia Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_79672a5d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pyf_roads_lines_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PYF/roads/lines/hotosm_pyf_roads_lines_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: French Polynesia Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_e72de2f4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pyf_roads_lines_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PYF/roads/lines/hotosm_pyf_roads_lines_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: French Polynesia Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_868cdfb7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pyf_roads_lines_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PYF/roads/polygons/hotosm_pyf_roads_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: French Polynesia Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_6f85326c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pyf_roads_polygons_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PYF/roads/polygons/hotosm_pyf_roads_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: French Polynesia Roads (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_acd40429
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pyf_roads_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PYF/roads/polygons/hotosm_pyf_roads_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: French Polynesia Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_a40befe3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pyf_roads_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/PYF/roads/polygons/hotosm_pyf_roads_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: French Polynesia Roads (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_704251cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_pyf_roads_polygons_geojson.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-pyf_hotosm_frenchpolynesiaroadsexpor_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - PYF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: French Polynesia Roads (OpenStreetMap Export)
version: null
vulnerability: null
---
