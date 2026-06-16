---
attributions:
- entity:
    affiliation: null
    email: null
    name: Center for International Earth Science Information Network (CIESIN), Columbia
      University
    url: https://data.humdata.org/dataset/grid3-cog-settlement-extents-v3-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-cog-settlement-extents-v3-0
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-cog-settlement-extents-v3-0
dataset_id: rdls_exp-cog_grid3_cogsettlementextentsv30_2016
description: 'The GRID3 COG - Settlement Extents v3.0 consists of a geographic representation
  of settlements in Republic of the Congo, in two forms: (1) settlement polygons,
  and (2) spatial points depicting the centroids of settled grid cells at 3-arc seconds
  (or ~100 meters) contained within settlement polygons. Both layers include attributes
  as described in the codebooks. The current version supersedes GRID3 Republic of
  the Congo Settlement Extents, Version 02; the following changes were made: (1) Development
  of a new methodology to derive building counts and settlement polygons with open
  data. (2) Estimation of a probability value for settlement polygons (3) Addition
  of a building-area measure (4) Replacement of degree of urbanization with classification
  based on built-up areas, small settlement areas, and hamlets (5) Elimination of
  building-count ranges (6) Elimination of variable comparing to previous versions
  Recommended Citation: Center for International Earth Science Information Network
  (CIESIN), Columbia University. 2024. GRID3 COG - Settlement Extents v3.0. New York:
  GRID3. [URL]. Accessed [DAY MONTH YEAR].. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/grid3-cog-settlement-extents-v3-0]'
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
    description: Settled population distribution derived from building counts and
      settlement grid cells at 100-meter resolution
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
    description: Building stock inventory derived from open data within identified
      settlement extents
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
  description: Settlement extents and building counts were derived from open data
    using a new methodology to identify settled areas and generate spatial points
    at 3-arc second (~100 meter) resolution. Settlement polygons and grid cell centroids
    with building count attributes were produced to represent the spatial distribution
    of human settlements and structures across Republic of the Congo.
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
- href: https://data.humdata.org/dataset/grid3-cog-settlement-extents-v3-0
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
  description: Republic of Congo - GRID3 COG - Settlement Extents v3.0 (Contains information
    on data inputs, methodology, and codebooks)
  download_url: https://data.humdata.org/dataset/b539755e-32c8-4abc-bb28-c6fd8f05ae0e/resource/58265fac-cbdf-43ba-b76b-6e7fa0c11489/download/grid3-cog-settlement-extents-v3.0-data-release-notes-.pdf
  format: null
  id: resource_58265fac
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3 COG - Settlement Extents v3.0 - Data Release Notes .pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Congo - GRID3 COG - Settlement Extents v3.0 (A spatial
    layer representing settlement polygons)
  download_url: https://data.humdata.org/dataset/b539755e-32c8-4abc-bb28-c6fd8f05ae0e/resource/62fae024-e592-4603-b57e-19805fa97497/download/grid3_cog_settlement_extents_v3_0.zip
  format: null
  id: resource_62fae024
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_COG_settlement_extents_v3_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Congo - GRID3 COG - Settlement Extents v3.0 (A spatial
    layer representing the centroids of settled grid cells)
  download_url: https://data.humdata.org/dataset/b539755e-32c8-4abc-bb28-c6fd8f05ae0e/resource/9290ee08-4b07-420b-a00c-8ddce380a264/download/grid3_cog_settlement_grid_v3_0.zip
  format: null
  id: resource_9290ee08
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_COG_settlement_grid_v3_0.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cog_grid3_cogsettlementextentsv30_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - COG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Republic of Congo - GRID3 COG - Settlement Extents v3.0
version: null
vulnerability: null
---
