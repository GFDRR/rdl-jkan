---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/ai-osm-buildings-in-camarines-sur-1-nov-2020
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: AI predictions on Bing Maps images
    url: https://data.humdata.org/dataset/ai-osm-buildings-in-camarines-sur-1-nov-2020
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/ai-osm-buildings-in-camarines-sur-1-nov-2020
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/ai-osm-buildings-in-camarines-sur-1-nov-2020
dataset_id: rdls_exp-phl_nlrc510_aiosmbuildingscamarinessu_20201101
description: 'OpenStreetMap buildings of Camarines Sur (as of 1-nov-2020) and AI predictions
  on Bing Maps images (approximately 2016-2019). Produced in support of Philippines
  Red Cross for typhoon Goni (1-nov-2020) Coordinate reference system: WGS 84 / EPSG:4326.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ai-osm-buildings-in-camarines-sur-1-nov-2020]'
details: Several buildings still missing, model makes mistakes.
exposure:
- asset_type:
    description: Building footprints in Camarines Sur derived from OpenStreetMap and
      AI predictions on Bing Maps imagery, produced in support of Typhoon Goni response
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
license: CC-BY-4.0
lineage:
  description: "Building footprints were compiled by combining OpenStreetMap data\
    \ (snapshot: 1 November 2020) with AI-predicted building outlines derived from\
    \ Bing Maps imagery (circa 2016\u20132019) using a machine learning model developed\
    \ by Netherlands Red Cross \u2013 510. The dataset was produced to support Philippines\
    \ Red Cross disaster response operations for Typhoon Goni, providing a spatial\
    \ inventory of the building stock in Camarines Sur."
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: AI predictions on Bing Maps images
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ai-osm-buildings-in-camarines-sur-1-nov-2020
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
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Philippines - AI + OSM buildings in Camarines Sur (1-nov-2020) (Coordinate
    reference system: WGS 84 / EPSG:4326)'
  download_url: https://data.humdata.org/dataset/01b9f63c-3dbd-44fa-a188-6ee00542cb07/resource/c1c3427f-0d01-48b4-a071-bdce46b3ccc2/download/buildings_merged.geojson
  format: null
  id: resource_c1c3427f
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AI_and_OSM_buildings.geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-phl_nlrc510_aiosmbuildingscamarinessu_20201101
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-01'
temporal_resolution: null
title: Philippines - AI + OSM buildings in Camarines Sur (1-nov-2020)
version: null
vulnerability: null
---
