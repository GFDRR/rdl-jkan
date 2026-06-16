---
attributions:
- entity:
    affiliation: null
    email: null
    name: Center for International Earth Science Information Network (CIESIN), Columbia
      University
    url: https://data.humdata.org/dataset/grid3-shn-settlement-extents-v3-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-shn-settlement-extents-v3-0
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-shn-settlement-extents-v3-0
dataset_id: rdls_exp-shn_grid3_shnsettlementextentsv30_2016
description: 'The GRID3 SHN - Settlement Extents v3.0 consists of a geographic representation
  of settlements in Saint Helena, Ascension and Tristan da Cunha, in two forms: (1)
  settlement polygons, and (2) spatial points depicting the centroids of settled grid
  cells at 3-arc seconds (or ~100 meters) contained within settlement polygons. Both
  layers include attributes as described in the codebooks. Recommended Citation: Center
  for International Earth Science Information Network (CIESIN), Columbia University.
  2024. GRID3 SHN - Settlement Extents v3.0. New York: GRID3. [URL]. Accessed [DAY
  MONTH YEAR].. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/grid3-shn-settlement-extents-v3-0]'
details: 'Terms of use: Users are free to download, store, access, use, copy, adapt,
  transform, alter, arrange, build upon, distribute and transmit this work and any
  derivative works. Attribution of the source must be provided, and further distribution
  of this work or derived work must maintain the same terms of data use and license
  as set forth in this Terms of Use. Copyright 2024. The Trustees of Columbia University
  in the City of New York. Data license: The data and accompanying document are licensed
  under a Creative Commons Attribution-ShareAlike 4.0 International, CC BY-SA 4.0
  (https://creativecommons.org/licenses/by-sa/4.0) and specified in legal code (CC-BY-SA-4.0legalcode).
  Contacts and data queries: The authors of this dataset appreciate feedback regarding
  the data, including suggestions, discovery of errors, difficulties in using the
  data, and format preferences. For dataset-related questions, please send an email
  to: info@ciesin.columbia.edu'
exposure:
- asset_type:
    description: Settled population distribution represented as grid cells and settlement
      polygons at ~100 meter resolution
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: Settlement extents were delineated from satellite imagery and ancillary
    data sources, then gridded at 3-arc second (~100 meter) resolution to produce
    both polygon-based settlement boundaries and point-based grid cell centroids representing
    settled areas in Saint Helena, Ascension, and Tristan da Cunha.
  sources:
  - id: source_1
    license: null
    name: Center for International Earth Science Information Network (CIESIN), Columbia
      University
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/grid3-shn-settlement-extents-v3-0
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
  description: Saint Helena - GRID3 SHN - Settlement Extents v3.0 (Contains information
    on data inputs, methodology, and codebooks)
  download_url: https://data.humdata.org/dataset/37b29c11-c1bd-48fe-9e0f-a2f41ef77540/resource/510eca8b-4b37-4fd9-a037-ef5ba3377d97/download/grid3-shn-settlement-extents-v3.0-data-release-notes-.pdf
  format: null
  id: resource_510eca8b
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3 SHN - Settlement Extents v3.0 - Data Release Notes .pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Helena - GRID3 SHN - Settlement Extents v3.0 (A spatial layer
    representing settlement polygons)
  download_url: https://data.humdata.org/dataset/37b29c11-c1bd-48fe-9e0f-a2f41ef77540/resource/346c0504-aa53-488a-9eb6-f14b4ac9a0ee/download/grid3_shn_settlement_extents_v3_0.zip
  format: null
  id: resource_346c0504
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_SHN_settlement_extents_v3_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Helena - GRID3 SHN - Settlement Extents v3.0 (A spatial layer
    representing the centroids of settled grid cells)
  download_url: https://data.humdata.org/dataset/37b29c11-c1bd-48fe-9e0f-a2f41ef77540/resource/6cefb81a-5715-4471-bea1-f4225cdd8762/download/grid3_shn_settlement_grid_v3_0.zip
  format: null
  id: resource_6cefb81a
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_SHN_settlement_grid_v3_0.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-shn_grid3_shnsettlementextentsv30_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - SHN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Saint Helena - GRID3 SHN - Settlement Extents v3.0
version: null
vulnerability: null
---
