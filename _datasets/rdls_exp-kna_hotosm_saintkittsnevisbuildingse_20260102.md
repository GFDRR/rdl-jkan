---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_kna_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_kna_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_kna_buildings
dataset_id: rdls_exp-kna_hotosm_saintkittsnevisbuildingse_20260102
description: 'OpenStreetMap contains roughly 15.7 thousand buildings in this region.
  Based on AI-mapped estimates, this is approximately 51% of the total buildings.The
  average age of data for this region is 2 years ( Last edited 3 months ago ) and
  28% buildings were added or updated in the last 6 months. Read about what this summary
  means : indicators , metrics This theme includes all OpenStreetMap features in this
  area matching ( Learn what tags means here ) : tags[''building''] IS NOT NULL Features
  may have these attributes: name name:en building building:levels building:materials
  addr:full addr:housenumber addr:street addr:city office source This dataset is one
  of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap Team website
  for more information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_kna_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and structural attributes (type, levels, materials)
      for approximately 15,700 mapped buildings in Saint Kitts and Nevis
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
    for Saint Kitts and Nevis and exported in multiple geospatial formats (SHP, KML,
    GeoJSON, GeoPackage) by the Humanitarian OpenStreetMap Team. The dataset represents
    approximately 51% of estimated total buildings based on AI-mapping validation,
    with an average data age of 2 years and 28% of features updated within the last
    6 months.
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
- href: https://data.humdata.org/dataset/hotosm_kna_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/KNA/buildings/polygons/hotosm_kna_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Saint Kitts and Nevis Buildings (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_d6c4058d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_kna_buildings_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/KNA/buildings/polygons/hotosm_kna_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Saint Kitts and Nevis Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_870e6e8d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_kna_buildings_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/KNA/buildings/polygons/hotosm_kna_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Saint Kitts and Nevis Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_8ad21a9e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_kna_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/KNA/buildings/polygons/hotosm_kna_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Saint Kitts and Nevis Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_bffde09e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_kna_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-kna_hotosm_saintkittsnevisbuildingse_20260102
spatial:
  bbox: null
  centroid: null
  countries:
  - KNA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-02'
temporal_resolution: null
title: Saint Kitts and Nevis Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
