---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm_ner_ruwa_water
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_ner_ruwa_water
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_ner_ruwa_water
dataset_id: rdls_exp-ner_hotosm_ruwawateraccessruralexpor_2022
description: 'This dataset contains data about water points in Fakara and Ngonga District
  in Niger. The field data was collected as part of the open map grant to support
  mapping water infrastructure and functionality in the Sahel Region. The data contains
  information about water usage, location of water points, types of water points,
  cost of accessing water (with a fee or not), operational status and operator. This
  theme includes all OpenStreetMap features in this area matching ( Learn what tags
  means here ) : tags[''amenity''] = ''drinking_water'' Features may have these attributes:
  access addr:city addr:district addr:place amenity description fee man_made opening_hours
  operational_status operator:type ownership seasonal source usage water:condition
  This dataset is one of many OpenStreetMap exports on HDX . See the Humanitarian
  OpenStreetMap Team website for more information.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hotosm_ner_ruwa_water]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure:
- asset_type:
    description: Water point infrastructure (wells, boreholes, hand pumps) with operational
      status and access characteristics
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
      quantity_kind: count
      unit: count
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Water point infrastructure data was collected through volunteered geographic
    information via OpenStreetMap mapping activities in rural Niger's Sahel region.
    Features were extracted from OSM using amenity=drinking_water tags and include
    location geometry, water point type, operational status, usage patterns, and access
    cost information. The dataset serves as an exposure inventory for water infrastructure
    vulnerability assessment in water-scarce regions.
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
- href: https://data.humdata.org/dataset/hotosm_ner_ruwa_water
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
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_ner_ruwa/water/points/hotosm_ner_ruwa_water_points_shp.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: 'RUWA: Water Access in Rural Niger (OpenStreetMap Export) (ESRI Shapefile)'
  download_url: null
  format: null
  id: resource_f6341060
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ner_ruwa_water_points_shp.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_ner_ruwa/water/points/hotosm_ner_ruwa_water_points_gpkg.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: 'RUWA: Water Access in Rural Niger (OpenStreetMap Export) (ZIP archive)'
  download_url: null
  format: null
  id: resource_76e60eed
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ner_ruwa_water_points_gpkg.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_ner_ruwa/water/points/hotosm_ner_ruwa_water_points_kml.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: 'RUWA: Water Access in Rural Niger (OpenStreetMap Export) (ZIP archive)'
  download_url: null
  format: null
  id: resource_193d937b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ner_ruwa_water_points_kml.zip
- access_url: https://s3.dualstack.us-east-1.amazonaws.com/production-raw-data-api/ISO3/hotosm_ner_ruwa/water/points/hotosm_ner_ruwa_water_points_geojson.zip
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: 'RUWA: Water Access in Rural Niger (OpenStreetMap Export) (ZIP archive)'
  download_url: null
  format: null
  id: resource_75fab80d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_ner_ruwa_water_points_geojson.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ner_hotosm_ruwawateraccessruralexpor_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-02-01'
  start: '2022-12-01'
temporal_resolution: null
title: 'RUWA: Water Access in Rural Niger (OpenStreetMap Export)'
version: null
vulnerability: null
---
