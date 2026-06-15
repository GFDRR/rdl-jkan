---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Microsoft
  url: https://planetarycomputer.microsoft.com/dataset/ms-buildings
creator:
  affiliation: null
  email: null
  name: Microsoft
  url: https://planetarycomputer.microsoft.com/dataset/ms-buildings
dataset_id: rdls_exp-crstac_microsoftbuildingfootprints_buildings
description: 'Building footprint polygon geometries located around the world [Source:
  This metadata record was automatically extracted from the STAC catalog climate-risk-stac
  (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: building footprints
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
license: https://spdx.org/licenses/ODbL-1.0.html
lineage:
  description: Building footprint polygon geometries located around the world
  sources:
  - id: source_underlying_1
    license: null
    name: Satellite (Maxar and Airbus imagery)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/microsoft/GlobalMLBuildingFootprints
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Microsoft
  url: https://planetarycomputer.microsoft.com/dataset/ms-buildings
purpose: 'data access via API; example: https://planetarycomputer.microsoft.com/dataset/ms-buildings#Example-Notebook'
referenced_by: []
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/buildings/microsoft-building-footprints/buildings/buildings.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Microsoft Building Footprints - Buildings'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Microsoft Building Footprints - Buildings - data file
  download_url: https://planetarycomputer.microsoft.com/dataset/ms-buildings
  format: null
  id: resource_data-file_1
  media_type: application/x-parquet
  spatial: null
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Microsoft Building Footprints - Buildings - data file
- access_url: https://github.com/microsoft/GlobalMLBuildingFootprints
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Microsoft Building Footprints - Buildings (Code link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_microsoftbuildingfootprints_buildings
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023'
  start: '2023'
temporal_resolution: null
title: Microsoft Building Footprints - Buildings
version: null
vulnerability: null
---
