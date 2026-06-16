---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_sgp_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_sgp_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_sgp_buildings
dataset_id: rdls_exp-sgp_hotosm_singaorebuildingsexport_20260101
description: 'OpenStreetMap contains roughly 124.6 thousand buildings in this region.
  Based on AI-mapped estimates, this is approximately 63% of the total buildings.The
  average age of data for this region is 1 year, 8 months ( Last edited 3 months ago
  ) and 5% buildings were added or updated in the last 6 months. Read about what this
  summary means : indicators , metrics This theme includes all OpenStreetMap features
  in this area matching ( Learn what tags means here ) : tags[''building''] IS NOT
  NULL Features may have these attributes: name name:en building building:levels building:materials
  addr:full addr:housenumber addr:street addr:city office source name:ms name:zh name:ta
  This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_sgp_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and structural attributes for approximately 124,600
      buildings in Singapore
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
    for Singapore through the Humanitarian OpenStreetMap Team's raw data API. The
    dataset includes approximately 124,600 mapped buildings with structural metadata
    (levels, materials) and address information, representing an estimated 63% of
    total building stock based on AI-mapping validation.
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
- href: https://data.humdata.org/dataset/hotosm_sgp_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SGP/buildings/polygons/hotosm_sgp_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Singapore - Singaore Buildings (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_8ce6507c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_sgp_buildings_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SGP/buildings/polygons/hotosm_sgp_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Singapore - Singaore Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_f66603da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_sgp_buildings_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SGP/buildings/polygons/hotosm_sgp_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Singapore - Singaore Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_8bede99d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_sgp_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SGP/buildings/polygons/hotosm_sgp_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Singapore - Singaore Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_08cdd622
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_sgp_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-sgp_hotosm_singaorebuildingsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - SGP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Singapore - Singaore Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
