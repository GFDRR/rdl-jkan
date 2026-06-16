---
attributions:
- entity:
    affiliation: null
    email: null
    name: Atlas of Human Settlements 2021
    url: https://data.humdata.org/dataset/turkey-settlement-map
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Atlas AI
  url: https://data.humdata.org/dataset/turkey-settlement-map
creator:
  affiliation: null
  email: null
  name: Atlas AI
  url: https://data.humdata.org/dataset/turkey-settlement-map
dataset_id: rdls_exp-tur_atlasai_settlementmap_2021
description: "A vector representation of the built-up surface, spatially aggregated\
  \ within a 50m radius. From the Atlas of Human Settlements 2021 @ T\xFCrkiye.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/turkey-settlement-map]"
details: "This limited public release covers the country of T\xFCrkiye for the year\
  \ 2021, showing the extent of human settlements. This geospatial data is a machine-learning\
  \ inference-based product that meets stringent model quality tests but has not been\
  \ physically ground-truthed in the field."
exposure:
- asset_type:
    description: Built-up settlement areas mapped from satellite imagery at 50m spatial
      resolution
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
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: "Satellite imagery was processed using encoder-decoder deep convolutional\
    \ neural networks and advanced computer vision techniques to identify and delineate\
    \ built-up surfaces, which were then spatially aggregated within 50m radius buffers\
    \ to create a vector settlement map for T\xFCrkiye in 2021."
  sources:
  - id: source_1
    license: null
    name: Atlas of Human Settlements 2021
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/turkey-settlement-map
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
  description: "T\xFCrkiye: Settlement Map (Settlement map of T\xFCrkiye in 2021)"
  download_url: https://data.humdata.org/dataset/c69bb578-4041-4db0-8080-4168b767fc6b/resource/4da6910e-1fa5-4080-83a8-5636706d2e3f/download/atlasai_ahs_turkey_2021_built_up_settlement_map.geojson
  format: null
  id: resource_4da6910e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AtlasAI_AHS_Turkey_2021_Built_Up_Settlement_Map.geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tur_atlasai_settlementmap_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: "T\xFCrkiye: Settlement Map"
version: null
vulnerability: null
---
