---
attributions:
- entity:
    affiliation: null
    email: null
    name: Center for International Earth Science Information Network (CIESIN), Columbia
      University
    url: https://data.humdata.org/dataset/grid3-bwa-settlement-extents-v3-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-bwa-settlement-extents-v3-0
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-bwa-settlement-extents-v3-0
dataset_id: rdls_exp-bwa_grid3_bwasettlementextentsv30_2016
description: 'The GRID3 BWA - Settlement Extents v3.0 consists of a geographic representation
  of settlements in Botswana, in two forms: (1) settlement polygons, and (2) spatial
  points depicting the centroids of settled grid cells at 3-arc seconds (or ~100 meters)
  contained within settlement polygons. Both layers include attributes as described
  in the codebooks. The current version supersedes GRID3 Botswana Settlement Extents,
  Version 02; the following changes were made: (1) Development of a new methodology
  to derive building counts and settlement polygons with open data. (2) Estimation
  of a probability value for settlement polygons (3) Addition of a building-area measure
  (4) Replacement of degree of urbanization with classification based on built-up
  areas, small settlement areas, and hamlets (5) Elimination of building-count ranges
  (6) Elimination of variable comparing to previous versions Recommended Citation:
  Center for International Earth Science Information Network (CIESIN), Columbia University.
  2024. GRID3 BWA - Settlement Extents v3.0. New York: GRID3. [URL]. Accessed [DAY
  MONTH YEAR].. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/grid3-bwa-settlement-extents-v3-0]'
details: 'Terms of use: Users are free to download, store, access, use, copy, adapt,
  transform, alter, arrange, build upon, distribute and transmit this work and any
  derivative works. Attribution of the source must be provided, and further distribution
  of this work or derived work must maintain the same terms of data use and license
  as set forth in this Terms of Use. Copyright 2024. The Trustees of Columbia University
  in the City of New York. Data license: The data and accompanying document are licensed
  under a Creative Commons Attribution-ShareAlike 4.0 International, CC BY-SA 4.0
  (https://creativecommons.org/licenses/by-sa/4.0) and specified in legal code (https://creativecommons.org/licenses/by-sa/4.0/legalcode).
  Contacts and data queries: The authors of this dataset appreciate feedback regarding
  the data, including suggestions, discovery of errors, difficulties in using the
  data, and format preferences. For dataset-related questions, please send an email
  to: info@ciesin.columbia.edu'
exposure:
- asset_type:
    description: Building footprints and counts derived from open data within settlement
      polygons across Botswana
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
- asset_type:
    description: Estimated population distribution at 100-meter grid resolution within
      settled areas
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Settlement extents were derived using a new open-data methodology to
    generate building counts and settlement polygons. Spatial points represent centroids
    of settled grid cells at 3-arc seconds (~100 meters) resolution within settlement
    polygons, with associated building and population attributes. The dataset provides
    a geographic representation of human settlements and built-up areas across Botswana
    for exposure assessment.
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
- href: https://data.humdata.org/dataset/grid3-bwa-settlement-extents-v3-0
  rel: source
loss:
  losses: []
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
  description: Botswana - GRID3 BWA - Settlement Extents v3.0 (Contains information
    on data inputs, methodology, and codebooks)
  download_url: https://data.humdata.org/dataset/56af2a5c-c5aa-460e-9efb-95667f47d5e4/resource/225e64df-fd45-4aff-bc1b-ccc837885947/download/grid3-bwa-settlement-extents-v3.0-data-release-notes-.pdf
  format: null
  id: resource_225e64df
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3 BWA - Settlement Extents v3.0 - Data Release Notes .pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Botswana - GRID3 BWA - Settlement Extents v3.0 (A spatial layer representing
    the centroids of settled grid cells)
  download_url: https://data.humdata.org/dataset/56af2a5c-c5aa-460e-9efb-95667f47d5e4/resource/ec13a10b-e0ae-43b0-87a7-eb5a4ae8a96a/download/grid3_bfa_settlement_grid_v3_0.zip
  format: null
  id: resource_ec13a10b
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_BFA_settlement_grid_v3_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Botswana - GRID3 BWA - Settlement Extents v3.0 (A spatial layer representing
    settlement polygons)
  download_url: https://data.humdata.org/dataset/56af2a5c-c5aa-460e-9efb-95667f47d5e4/resource/1399cc78-5fdb-4b97-a88d-2cd2ef63fbd8/download/grid3_bwa_settlement_extents_v3_0.zip
  format: null
  id: resource_1399cc78
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_BWA_settlement_extents_v3_0.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bwa_grid3_bwasettlementextentsv30_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - BWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Botswana - GRID3 BWA - Settlement Extents v3.0
version: null
vulnerability: null
---
