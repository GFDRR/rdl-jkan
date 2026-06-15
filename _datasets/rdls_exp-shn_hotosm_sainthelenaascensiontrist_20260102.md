---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_shn_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_shn_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_shn_buildings
dataset_id: rdls_exp-shn_hotosm_sainthelenaascensiontrist_20260102
description: 'OpenStreetMap contains roughly 4.6 thousand buildings in this region.
  Based on AI-mapped estimates, this is approximately 76% of the total buildings.The
  average age of data for this region is 3 years ( Last edited 3 months ago ) and
  2% buildings were added or updated in the last 6 months. Read about what this summary
  means : indicators , metrics This theme includes all OpenStreetMap features in this
  area matching ( Learn what tags means here ) : tags[''building''] IS NOT NULL Features
  may have these attributes: name name:en building building:levels building:materials
  addr:full addr:housenumber addr:street addr:city office source This dataset is one
  of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap Team website
  for more information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_shn_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and structural attributes (type, levels, materials,
      address) for approximately 4,600 buildings in Saint Helena, Ascension and Tristan
      da Cunha
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
  description: Building footprints and attributes were extracted from OpenStreetMap,
    a crowdsourced geographic database maintained by volunteer contributors. The Humanitarian
    OpenStreetMap Team processed and validated the data, estimating approximately
    76% coverage of total buildings in the region based on AI-mapped estimates. Data
    were exported in multiple standard geospatial formats (Shapefile, GeoPackage,
    GeoJSON, KML) with structural attributes including building type, number of levels,
    materials, and address information.
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
- href: https://data.humdata.org/dataset/hotosm_shn_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SHN/buildings/polygons/hotosm_shn_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Saint Helena, Ascension and Tristan da Cunha Buildings (OpenStreetMap
    Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_1df2b629
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_shn_buildings_polygons_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Helena, Ascension and Tristan da Cunha Buildings (OpenStreetMap
    Export) (Geopackage, SQLite compatible)
  download_url: https://export.hotosm.org/downloads/175bcc57-88d9-4f17-84cb-e28f47c0d95f/hotosm_shn_buildings_gpkg.zip
  format: null
  id: resource_6509b0c9
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_shn_buildings_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SHN/buildings/polygons/hotosm_shn_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Saint Helena, Ascension and Tristan da Cunha Buildings (OpenStreetMap
    Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_47ff8ee4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_shn_buildings_polygons_kml.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Helena, Ascension and Tristan da Cunha Buildings (OpenStreetMap
    Export) (.IMG for Garmin GPS Devices (All OSM layers for area))
  download_url: http://export.hotosm.org/downloads/34e93d78-298a-415d-ac76-88c15e3b0162/hotosm_shn_gmapsupp_img.zip
  format: Garmin IMG
  id: resource_70a30dd0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_shn_gmapsupp_img.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SHN/buildings/polygons/hotosm_shn_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Saint Helena, Ascension and Tristan da Cunha Buildings (OpenStreetMap
    Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_5ce65cd5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_shn_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/SHN/buildings/polygons/hotosm_shn_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Saint Helena, Ascension and Tristan da Cunha Buildings (OpenStreetMap
    Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_66e08bce
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_shn_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-shn_hotosm_sainthelenaascensiontrist_20260102
spatial:
  bbox: null
  centroid: null
  countries:
  - SHN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-02'
temporal_resolution: null
title: Saint Helena, Ascension and Tristan da Cunha Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
