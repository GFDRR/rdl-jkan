---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_jor_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_jor_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_jor_buildings
dataset_id: rdls_exp-jor_hotosm_buildingsexport_20260101
description: 'OpenStreetMap contains roughly 232.3 thousand buildings in this region.
  Based on AI-mapped estimates, this is approximately 18% of the total buildings.The
  average age of data for this region is 4 years ( Last edited 3 months ago ) and
  4% buildings were added or updated in the last 6 months. Read about what this summary
  means : indicators , metrics This theme includes all OpenStreetMap features in this
  area matching ( Learn what tags means here ) : tags[''building''] IS NOT NULL Features
  may have these attributes: name name:en building building:levels building:materials
  addr:full addr:housenumber addr:street addr:city office source name:ar This dataset
  is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_jor_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and stock inventory across Jordan with structural
      attributes including building type, levels, and materials
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
license: ODbL-1.0/
lineage:
  description: Building footprints and attributes were extracted from OpenStreetMap
    volunteered geographic information for Jordan. Data quality was assessed using
    AI-mapping estimates and temporal metadata (last edit dates, update frequency).
    The dataset represents approximately 232.3 thousand mapped buildings with structural
    attributes including building type, levels, and materials, suitable for exposure
    assessment in disaster risk analysis.
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
- href: https://data.humdata.org/dataset/hotosm_jor_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JOR/buildings/polygons/hotosm_jor_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Jordan Buildings (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_c53ffa57
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jor_buildings_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jordan Buildings (OpenStreetMap Export) (Geopackage, SQLite compatible)
  download_url: https://export.hotosm.org/downloads/1dc393d5-62ca-44b0-99a0-c876900089bf/hotosm_jor_buildings_gpkg.zip
  format: null
  id: resource_9a6baff2
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jor_buildings_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JOR/buildings/polygons/hotosm_jor_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Jordan Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_86bd77cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jor_buildings_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jordan Buildings (OpenStreetMap Export) (.IMG for Garmin GPS Devices
    (All OSM layers for area))
  download_url: https://export.hotosm.org/downloads/1dc393d5-62ca-44b0-99a0-c876900089bf/hotosm_jor_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_ad8819a2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jor_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JOR/buildings/polygons/hotosm_jor_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Jordan Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_3ffb375f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jor_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/JOR/buildings/polygons/hotosm_jor_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Jordan Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_6774905e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_jor_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jor_hotosm_buildingsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - JOR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Jordan Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
