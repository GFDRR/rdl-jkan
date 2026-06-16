---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_dom_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_dom_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_dom_buildings
dataset_id: rdls_exp-dom_hotosm_buildingsexport_20260101
description: 'OpenStreetMap contains roughly 230.8 thousand buildings in this region.
  Based on AI-mapped estimates, this is approximately 9% of the total buildings.The
  average age of data for this region is 3 years ( Last edited 3 months ago ) and
  7% buildings were added or updated in the last 6 months. Read about what this summary
  means : indicators , metrics This theme includes all OpenStreetMap features in this
  area matching ( Learn what tags means here ) : tags[''building''] IS NOT NULL Features
  may have these attributes: name name:en building building:levels building:materials
  addr:full addr:housenumber addr:street addr:city office source name:es This dataset
  is one of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap
  Team website for more information.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_dom_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Building footprints and stock inventory across Dominican Republic
      with structural attributes including building type, levels, and materials
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
  description: Building footprints were extracted from OpenStreetMap for Dominican
    Republic through the Humanitarian OpenStreetMap Team's raw data API. The dataset
    contains approximately 230.8 thousand buildings with structural attributes (type,
    levels, materials) and address information derived from crowdsourced mapping contributions,
    with an average data age of 3 years and 7% of features updated within the last
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
- href: https://data.humdata.org/dataset/hotosm_dom_buildings
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/DOM/buildings/polygons/hotosm_dom_buildings_polygons_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Dominican Republic Buildings (OpenStreetMap Export) (ESRI Shapefile)
  download_url: null
  format: null
  id: resource_e7bae368
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_dom_buildings_polygons_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/DOM/buildings/polygons/hotosm_dom_buildings_polygons_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Dominican Republic Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_ce7c3112
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_dom_buildings_polygons_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/DOM/buildings/polygons/hotosm_dom_buildings_polygons_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Dominican Republic Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_467f079c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_dom_buildings_polygons_geojson.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/DOM/buildings/polygons/hotosm_dom_buildings_polygons_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Dominican Republic Buildings (OpenStreetMap Export) (ZIP archive)
  download_url: null
  format: null
  id: resource_b1b0c3b7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_dom_buildings_polygons_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-dom_hotosm_buildingsexport_20260101
spatial:
  bbox: null
  centroid: null
  countries:
  - DOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2026-01-01'
temporal_resolution: null
title: Dominican Republic Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
