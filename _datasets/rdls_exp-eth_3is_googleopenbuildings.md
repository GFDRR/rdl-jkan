---
attributions:
- entity:
    affiliation: null
    email: null
    name: Google Open Buildings
    url: https://data.humdata.org/dataset/ethiopia-google-open-buildings-10m
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-google-open-buildings-10m
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-google-open-buildings-10m
dataset_id: rdls_exp-eth_3is_googleopenbuildings
description: 'Building footprints are useful for a range of important applications,
  from population estimation, urban planning and humanitarian response, to environmental
  and climate science. This large-scale open dataset contains the outlines of buildings
  derived from high-resolution satellite imagery in order to support these types of
  uses. For each building in this dataset we include the polygon describing its footprint
  on the ground, a confidence score indicating how sure we are that this is a building,
  and a Plus Code corresponding to the centre of the building. There is no information
  about the type of building, its street address, or any details other than its geometry.
  More information at Google Open Buildings. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-google-open-buildings-10m]'
details: null
exposure:
- asset_type:
    description: Building footprints derived from high-resolution satellite imagery
      with confidence scores
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
  description: Building footprints were extracted from high-resolution satellite imagery
    using remote sensing methods. Each building polygon includes a confidence score
    indicating detection certainty and a Plus Code for spatial reference. The dataset
    supports population estimation, urban planning, and humanitarian response applications.
  sources:
  - id: source_1
    license: null
    name: Google Open Buildings
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-google-open-buildings-10m
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
  description: Ethiopia - Google Open Buildings (Original data extracted from Google)
  download_url: https://data.humdata.org/dataset/1ec0495f-cedf-4d18-aa8e-ccbf5ed8a457/resource/43a7779c-0208-4c45-9c69-51f3742481f1/download/open_buildings_v3_points_wb_10m_eth.zip
  format: null
  id: resource_43a7779c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: open_buildings_v3_points_wb_10m_ETH.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-eth_3is_googleopenbuildings
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Ethiopia - Google Open Buildings
version: null
vulnerability: null
---
