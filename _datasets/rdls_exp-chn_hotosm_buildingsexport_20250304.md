---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_chn_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_chn_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_chn_buildings
dataset_id: rdls_exp-chn_hotosm_buildingsexport_20250304
description: 'This theme includes all OpenStreetMap features in this area matching
  ( Learn what tags means here ) : tags[''building''] IS NOT NULL Features may have
  these attributes: name name:en building building:levels building:materials addr:full
  addr:housenumber addr:street addr:city office source name:zh This dataset is one
  of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap Team website
  for more information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_chn_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and structural attributes (levels, type) from
      OpenStreetMap
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
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Building footprints and attributes were extracted from OpenStreetMap
    using feature queries on the 'building' tag. The dataset represents a spatial
    inventory of structures with available metadata on building type and number of
    levels, suitable for exposure assessment in disaster risk analysis.
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
- href: https://data.humdata.org/dataset/hotosm_chn_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CHN/buildings/polygons/hotosm_chn_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: China Buildings (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_af179769
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_chn_buildings_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CHN/buildings/polygons/hotosm_chn_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: China Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_176d0581
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_chn_buildings_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CHN/buildings/polygons/hotosm_chn_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: China Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_54fca3ba
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_chn_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/CHN/buildings/polygons/hotosm_chn_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: China Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_6910e2b2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_chn_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-chn_hotosm_buildingsexport_20250304
spatial:
  bbox: null
  centroid: null
  countries:
  - CHN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-03-04'
temporal_resolution: null
title: China Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
