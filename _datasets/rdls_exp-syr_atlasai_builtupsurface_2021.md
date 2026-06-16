---
attributions:
- entity:
    affiliation: null
    email: null
    name: Atlas of Human Settlements 2021
    url: https://data.humdata.org/dataset/syria-built-up-surface
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Atlas AI
  url: https://data.humdata.org/dataset/syria-built-up-surface
creator:
  affiliation: null
  email: null
  name: Atlas AI
  url: https://data.humdata.org/dataset/syria-built-up-surface
dataset_id: rdls_exp-syr_atlasai_builtupsurface_2021
description: 'Built-up presence (binary) in a 10m x 10m grid. From the Atlas of Human
  Settlements 2021 @ Syria.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/syria-built-up-surface]'
details: 'This limited public release covers the countries of Turkey and Syria for
  the year 2021, showing the extent of human settlements. This geospatial data is
  a machine-learning inference-based product that meets stringent model quality tests
  but has not been physically ground-truthed in the field. Glide: EQ-2023-000015-TUR'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Built-up surface presence was derived from satellite imagery analysis
    using advanced deep learning (encoder-decoder CNNs) and computer vision techniques
    to classify 10m x 10m grid cells as built-up or non-built-up across Syria. The
    resulting binary raster represents spatial distribution of building infrastructure
    without hazard or impact context.
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
- href: https://data.humdata.org/dataset/syria-built-up-surface
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
  description: 'Syria: Built-up Surface (built-up surface of Syria in 2021)'
  download_url: https://data.humdata.org/dataset/3428bc49-dcff-41e9-848c-ef0d1b374cc0/resource/5435ef3c-9517-45e7-ac4f-bc0e69584a60/download/atlasai_ahs_turkey_2021_built_up_surface.tif
  format: null
  id: resource_5435ef3c
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
slug: rdls_exp-syr_atlasai_builtupsurface_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: 'Syria: Built-up Surface'
version: null
vulnerability: null
---
