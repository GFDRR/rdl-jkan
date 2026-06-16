---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/colombia-mapaton-nacional-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/colombia-mapaton-nacional-2025
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/colombia-mapaton-nacional-2025
dataset_id: rdls_exp-col_hotosm_mapatonnacional_2025
description: "Archivo contiene las construcciones mapeadas durante el mapat\u8D38\
  n nacional de Colombia 2025. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/colombia-mapaton-nacional-2025]"
details: null
exposure:
- asset_type:
    description: Building footprints and structural attributes mapped during the national
      mapathon, including building type, roof material, and access information
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Building footprints and structural attributes were collected through
    a national crowdsourced mapping event (mapathon) coordinated by HOT using OpenStreetMap
    as the data platform. The mapped features include building classification, roof
    materials, addresses, and access information, compiled into standardized vector
    formats (Shapefile and GeoJSON) for disaster risk exposure assessment.
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
    name: Humanitarian OpenStreetMap Team (HOT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-mapaton-nacional-2025
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
  description: "Colombia Mapat\u8D38n Nacional (Shapefile)"
  download_url: https://data.humdata.org/dataset/71cc88d3-b0e0-4904-aee4-f8c707d934ce/resource/f78aab05-eddc-4fd1-af27-b67d31526d88/download/edificios_mapaton.zip
  format: null
  id: resource_f78aab05
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: edificios_mapaton.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia Mapat\u8D38n Nacional (GeoJSON)"
  download_url: https://data.humdata.org/dataset/71cc88d3-b0e0-4904-aee4-f8c707d934ce/resource/745afd0a-f688-41da-8a78-7c2d735ed1c5/download/edificios_mapaton.geojson
  format: null
  id: resource_745afd0a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: edificios_mapaton.geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-col_hotosm_mapatonnacional_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-21'
  start: '2025-06-01'
temporal_resolution: null
title: "Colombia Mapat\u8D38n Nacional"
version: null
vulnerability: null
---
