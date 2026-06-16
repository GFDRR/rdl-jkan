---
attributions:
- entity:
    affiliation: null
    email: null
    name: Center for International Earth Science Information Network (CIESIN), Columbia
      University
    url: https://data.humdata.org/dataset/grid3-civ-settlement-extents-v3-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-civ-settlement-extents-v3-0
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-civ-settlement-extents-v3-0
dataset_id: rdls_exp-civ_grid3_civsettlementextentsv30_2016
description: "The GRID3 CIV - Settlement Extents v3.0 consists of a geographic representation\
  \ of settlements in C\xF4te d'Ivoire, in two forms: (1) settlement polygons, and\
  \ (2) spatial points depicting the centroids of settled grid cells at 3-arc seconds\
  \ (or ~100 meters) contained within settlement polygons. Both layers include attributes\
  \ as described in the codebooks. The current version supersedes GRID3 C\xF4te d'Ivoire\
  \ Settlement Extents, Version 02; the following changes were made: (1) Development\
  \ of a new methodology to derive building counts and settlement polygons with open\
  \ data. (2) Estimation of a probability value for settlement polygons (3) Addition\
  \ of a building-area measure (4) Replacement of degree of urbanization with classification\
  \ based on built-up areas, small settlement areas, and hamlets (5) Elimination of\
  \ building-count ranges (6) Elimination of variable comparing to previous versions\
  \ Recommended Citation: Center for International Earth Science Information Network\
  \ (CIESIN), Columbia University. 2024. GRID3 CIV - Settlement Extents v3.0. New\
  \ York: GRID3. [URL]. Accessed [DAY MONTH YEAR].. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/grid3-civ-settlement-extents-v3-0]"
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
    description: Gridded population distribution at 100-meter resolution derived from
      settlement extents and building counts
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
- asset_type:
    description: Building counts per settlement grid cell estimated from open data
      sources
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Settlement extents were derived from open data sources using a new\
    \ methodology to estimate building counts and generate settlement polygons. Population\
    \ and building inventories were spatially gridded at 100-meter resolution (3 arc-seconds)\
    \ to create exposure layers for disaster risk assessment in C\xF4te d'Ivoire."
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
- href: https://data.humdata.org/dataset/grid3-civ-settlement-extents-v3-0
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
  description: "C\xF4te d'Ivoire - GRID3 CIV - Settlement Extents v3.0 (Contains information\
    \ on data inputs, methodology, and codebooks)"
  download_url: https://data.humdata.org/dataset/c6f323bd-4fba-47e0-9296-7f9e088b8d21/resource/e29f6e06-36a7-47b2-addb-5f12a6337821/download/grid3-civ-settlement-extents-v3.0-data-release-notes-.pdf
  format: null
  id: resource_e29f6e06
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3 CIV - Settlement Extents v3.0 - Data Release Notes .pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - GRID3 CIV - Settlement Extents v3.0 (A spatial\
    \ layer representing settlement polygons)"
  download_url: https://data.humdata.org/dataset/c6f323bd-4fba-47e0-9296-7f9e088b8d21/resource/182543f0-79cf-4eea-add1-f14c00af81a2/download/grid3_civ_settlement_extents_v3_0.zip
  format: null
  id: resource_182543f0
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_CIV_settlement_extents_v3_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire - GRID3 CIV - Settlement Extents v3.0 (A spatial\
    \ layer representing the centroids of settled grid cells)"
  download_url: https://data.humdata.org/dataset/c6f323bd-4fba-47e0-9296-7f9e088b8d21/resource/0618e69c-4d2c-4939-8df3-16504d3fabf7/download/grid3_civ_settlement_grid_v3_0.zip
  format: null
  id: resource_0618e69c
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_CIV_settlement_grid_v3_0.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-civ_grid3_civsettlementextentsv30_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - CIV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: "C\xF4te d'Ivoire - GRID3 CIV - Settlement Extents v3.0"
version: null
vulnerability: null
---
