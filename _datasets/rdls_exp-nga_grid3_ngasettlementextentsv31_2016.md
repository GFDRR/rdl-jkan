---
attributions:
- entity:
    affiliation: null
    email: null
    name: Center for International Earth Science Information Network (CIESIN), Columbia
      University
    url: https://data.humdata.org/dataset/grid3-nga-settlement-extents-v3_1
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-nga-settlement-extents-v3_1
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-nga-settlement-extents-v3_1
dataset_id: rdls_exp-nga_grid3_ngasettlementextentsv31_2016
description: 'The GRID3 NGA - Settlement Extents v3.1 consists of a geographic representation
  of settlements in Nigeria, in two forms: 1) settlement polygons, and 2) spatial
  points depicting the centroids of settled grid cells at 3-arc seconds (or ~100 meters)
  contained within settlement polygons. Both layers include attributes as described
  in the codebooks. Data inputs and methodology are described in the data release
  notes. The current version supersedes GRID3 NGA - Settlement Extents v3.0; the following
  changes were made: -Corrections on imputed values for building count and building
  areas. -Edits to the data release notes Recommended Citation: Center for International
  Earth Science Information Network (CIESIN), Columbia University. 2024. GRID3 NGA
  - Settlement Extents v3.1. New York: GRID3. [URL]. Accessed [DAY MONTH YEAR].. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/grid3-nga-settlement-extents-v3_1]'
details: 'Terms of use: Users are free to download, store, access, use, copy, adapt,
  transform, alter, arrange, build upon, distribute and transmit this work and any
  derivative works. Attribution of the source must be provided, and further distribution
  of this work or derived work must maintain the same terms of data use and license
  as set forth in this Terms of Use. Copyright 2024. The Trustees of Columbia University
  in the City of New York. Data license: The data and accompanying document are licensed
  under a Creative Commons Attribution-ShareAlike 4.0 International, CC BY-SA 4.0
  (https://creativecommons.org/licenses/by-sa/4.0) and specified in legal code (https://creativecommons.org/licenses/by-sa/4.0/legalcode)
  Contacts and data queries: The authors of this dataset appreciate feedback regarding
  the data, including suggestions, discovery of errors, difficulties in using the
  data, and format preferences. For dataset-related questions, please send an email
  to: info@ciesin.columbia.edu'
exposure:
- asset_type:
    description: Building stock inventory with count and area attributes for settlements
      in Nigeria
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
    description: Spatial distribution of population within settled grid cells at 100-meter
      resolution
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
  description: Settlement extents were delineated from remote sensing imagery and
    gridded to 3-arc-second (~100 meter) cells. Building counts and areas were imputed
    for each grid cell within settlement polygons, with corrections applied in v3.1
    to improve accuracy of building-level exposure estimates for disaster risk assessment.
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
- href: https://data.humdata.org/dataset/grid3-nga-settlement-extents-v3_1
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
  description: Nigeria - GRID3 NGA - Settlement Extents v3.1 (A spatial layer representing
    the centroids of settled grid cells)
  download_url: https://data.humdata.org/dataset/af838671-b9a6-4ae9-8ed5-eea750b05597/resource/647d1fbd-f4a1-4d12-a182-3a497ef0faec/download/grid3_nga_settlement_grid_v3_1_gpkg.zip
  format: null
  id: resource_647d1fbd
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_NGA_settlement_grid_v3_1_gpkg.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nigeria - GRID3 NGA - Settlement Extents v3.1 (A spatial layer representing
    settlement polygons)
  download_url: https://data.humdata.org/dataset/af838671-b9a6-4ae9-8ed5-eea750b05597/resource/0a22d6fc-7f1f-4f50-aead-09ef7be0455d/download/grid3_nga_settlement_extents_v3_1_gpkg.zip
  format: null
  id: resource_0a22d6fc
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_NGA_settlement_extents_v3_1_gpkg.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nigeria - GRID3 NGA - Settlement Extents v3.1 (Contains information
    on data inputs, methodology, and code)
  download_url: https://data.humdata.org/dataset/af838671-b9a6-4ae9-8ed5-eea750b05597/resource/69549561-5f1f-45dd-b0b4-95d1c96fecdc/download/grid3-nga-settlement-extents-v3.1-data-release-notes-.pdf
  format: null
  id: resource_69549561
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3 NGA - Settlement Extents v3.1 - Data Release Notes .pdf
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nga_grid3_ngasettlementextentsv31_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2016-03-01'
temporal_resolution: null
title: Nigeria - GRID3 NGA - Settlement Extents v3.1
version: null
vulnerability: null
---
