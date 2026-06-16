---
attributions:
- entity:
    affiliation: null
    email: null
    name: Atlas of Human Settlements 2021
    url: https://data.humdata.org/dataset/turkey-built-up-surface
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Atlas AI
  url: https://data.humdata.org/dataset/turkey-built-up-surface
creator:
  affiliation: null
  email: null
  name: Atlas AI
  url: https://data.humdata.org/dataset/turkey-built-up-surface
dataset_id: rdls_exp-tur_atlasai_builtupsurface_2021
description: 'Built-up presence (binary) in a 10m x 10m grid. From the Atlas of Human
  Settlements 2021 @ Turkey.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/turkey-built-up-surface]'
details: This limited public release covers the country of Turkey for the year 2021,
  showing the extent of human settlements. This geospatial data is a machine-learning
  inference-based product that meets stringent model quality tests but has not been
  physically ground-truthed in the field.
exposure:
- asset_type:
    description: Built-up surface presence mapped at 10m resolution using satellite
      imagery and deep learning
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
  description: Built-up surface presence was derived from satellite imagery analysis
    using advanced deep convolutional neural networks with encoder-decoder architecture
    and computer vision techniques to classify 10m x 10m grid cells as built-up or
    non-built-up across Turkey in 2021. The resulting binary raster represents spatial
    distribution of human settlements and infrastructure.
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
- href: https://data.humdata.org/dataset/turkey-built-up-surface
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
  description: 'Turkey: Built-up Surface (built-up surface of Turkey in 2021)'
  download_url: https://data.humdata.org/dataset/a68ee99b-f282-411d-a508-793e87bf314b/resource/94645617-18a9-452e-98f2-3c6d4d91cb46/download/atlasai_ahs_turkey_2021_built_up_surface.tif
  format: null
  id: resource_94645617
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AtlasAI_AHS_Turkey_2021_Built_Up_Surface.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tur_atlasai_builtupsurface_2021
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
title: 'Turkey: Built-up Surface'
version: null
vulnerability: null
---
