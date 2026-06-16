---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_niu_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_niu_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_niu_buildings
dataset_id: rdls_exp-niu_hotosm_niuebuildingsexport_20260101
description: 'OpenStreetMap contains roughly 1.9 thousand buildings in this region.
  Based on AI-mapped estimates, this is approximately 100% of the total buildings.The
  average age of data for this region is 4 years ( Last edited 4 months ago ) and
  2% buildings were added or updated in the last 6 months. Read about what this summary
  means : indicators , metrics This theme includes all OpenStreetMap features in this
  area matching ( Learn what tags means here ) : tags[''building''] IS NOT NULL Features
  may have these attributes: name name:en building building:levels building:materials
  addr:full addr:housenumber addr:street addr:city office source name:niu This dataset
  is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_niu_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and structural attributes (type, levels, materials)
      for approximately 1,900 buildings in Niue
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
  description: Building footprints and attributes were sourced from OpenStreetMap
    volunteered geographic information and validated using AI-mapping estimates to
    assess coverage completeness (approximately 100% of total buildings). Data were
    exported by the Humanitarian OpenStreetMap Team in multiple geospatial formats
    with metadata on data age and recent update frequency.
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
- href: https://data.humdata.org/dataset/hotosm_niu_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIU/buildings/polygons/hotosm_niu_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Niue Buildings (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_0b3312c6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_niu_buildings_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIU/buildings/polygons/hotosm_niu_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Niue Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_466fbf05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_niu_buildings_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue Buildings (OpenStreetMap Export) (.IMG for Garmin GPS Devices
    (All OSM layers for area))
  download_url: http://export.hotosm.org/downloads/fbe91430-ff6b-4bff-910e-82f2937985ad/hotosm_niu_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_708f78d3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_niu_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIU/buildings/polygons/hotosm_niu_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Niue Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_85cd34f3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_niu_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/NIU/buildings/polygons/hotosm_niu_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Niue Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_9ef2aabf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_niu_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-niu_hotosm_niuebuildingsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - NIU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Niue Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
