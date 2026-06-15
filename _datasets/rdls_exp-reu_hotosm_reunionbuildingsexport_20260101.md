---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_reu_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_reu_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_reu_buildings
dataset_id: rdls_exp-reu_hotosm_reunionbuildingsexport_20260101
description: 'OpenStreetMap contains roughly 462.8 thousand buildings in this region.
  Based on AI-mapped estimates, this is approximately 86% of the total buildings.The
  average age of data for this region is 1 year, 11 months ( Last edited 3 months
  ago ) and 1% buildings were added or updated in the last 6 months. Read about what
  this summary means : indicators , metrics This theme includes all OpenStreetMap
  features in this area matching ( Learn what tags means here ) : tags[''building'']
  IS NOT NULL Features may have these attributes: name name:en building building:levels
  building:materials addr:full addr:housenumber addr:street addr:city office source
  name:fr This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_reu_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and structural attributes (levels, materials)
      for approximately 462.8 thousand buildings in Reunion
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
    for Reunion Island. Data quality was assessed using AI-mapped estimates indicating
    86% coverage of total buildings. The dataset includes structural attributes (levels,
    materials) and address information derived from crowdsourced mapping contributions.
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
- href: https://data.humdata.org/dataset/hotosm_reu_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/REU/buildings/polygons/hotosm_reu_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: "R\xE9union - Reunion Buildings (OpenStreetMap Export) (ESRI Shapefile)"
  download_url: null
  format: null
  id: resource_6bff070c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_reu_buildings_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Reunion Buildings (OpenStreetMap Export) (Geopackage,\
    \ SQLite compatible)"
  download_url: https://export.hotosm.org/downloads/06c3ca3c-34ff-48f0-8d8c-b46ac2d9d8d8/hotosm_reu_buildings_gpkg.zip
  format: null
  id: resource_91480f6a
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_reu_buildings_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/REU/buildings/polygons/hotosm_reu_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: "R\xE9union - Reunion Buildings (OpenStreetMap Export) (ZIP archive)"
  download_url: null
  format: null
  id: resource_34eea040
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_reu_buildings_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Reunion Buildings (OpenStreetMap Export) (.IMG for Garmin\
    \ GPS Devices (All OSM layers for area))"
  download_url: http://export.hotosm.org/downloads/5d75a496-ce41-4b05-b4aa-7e5e3398c2b4/hotosm_reu_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_336b3ee6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_reu_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/REU/buildings/polygons/hotosm_reu_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: "R\xE9union - Reunion Buildings (OpenStreetMap Export) (ZIP archive)"
  download_url: null
  format: null
  id: resource_21bebaa3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_reu_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/REU/buildings/polygons/hotosm_reu_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: "R\xE9union - Reunion Buildings (OpenStreetMap Export) (ZIP archive)"
  download_url: null
  format: null
  id: resource_971d5f06
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_reu_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-reu_hotosm_reunionbuildingsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - REU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: "R\xE9union - Reunion Buildings (OpenStreetMap Export)"
version: null
vulnerability: null
---
