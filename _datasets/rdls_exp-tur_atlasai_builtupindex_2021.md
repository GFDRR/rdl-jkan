---
attributions:
- entity:
    affiliation: null
    email: null
    name: Atlas of Human Settlements 2021
    url: https://data.humdata.org/dataset/turkey-built-up-index
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Atlas AI
  url: https://data.humdata.org/dataset/turkey-built-up-index
creator:
  affiliation: null
  email: null
  name: Atlas AI
  url: https://data.humdata.org/dataset/turkey-built-up-index
dataset_id: rdls_exp-tur_atlasai_builtupindex_2021
description: 'A scaled estimate of the extent of human presence in each 100 square
  meter unit area, inferred from buildings. Denoted by a decimal percentage between
  0 and 1 indicating how much of the 10m x 10m grid cell is covered by buildings.
  From the Atlas of Human Settlements 2021 @ Turkey.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/turkey-built-up-index]'
details: This limited public release covers the country of Turkey for the year 2021,
  showing the extent of human settlements. This geospatial data is a machine-learning
  inference-based product that meets stringent model quality tests but has not been
  physically ground-truthed in the field.
exposure:
- asset_type:
    description: Built-up area coverage derived from satellite imagery, expressed
      as a decimal percentage (0-1) of building presence per 10m x 10m grid cell
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
  description: Satellite imagery was processed using encoder-decoder deep convolutional
    neural networks and advanced computer vision techniques to infer building presence
    and extent. The output is a gridded built-up index at 10m resolution, with values
    scaled between 0 and 1 to represent the proportion of each grid cell covered by
    buildings, providing a spatial inventory of built infrastructure across Turkey.
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
- href: https://data.humdata.org/dataset/turkey-built-up-index
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
  description: 'Turkey: Built-up Index (built-up index for Turkey in 2021)'
  download_url: https://data.humdata.org/dataset/3f2a2f4e-d4ce-4f7c-ada6-adf50e647da8/resource/a6447533-2ac1-4a8f-af2f-9e9a4a726719/download/atlasai_ahs_turkey_2021_built_up_index.tif
  format: null
  id: resource_a6447533
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AtlasAI_AHS_Turkey_2021_Built_Up_Index.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tur_atlasai_builtupindex_2021
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
title: 'Turkey: Built-up Index'
version: null
vulnerability: null
---
