---
attributions:
- entity:
    affiliation: null
    email: null
    name: Center for International Earth Science Information Network (CIESIN), Columbia
      University
    url: https://data.humdata.org/dataset/grid3-ago-settlement-extents-v3-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-ago-settlement-extents-v3-0
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-ago-settlement-extents-v3-0
dataset_id: rdls_exp-ago_grid3_agosettlementextentsv30_2016
description: 'The GRID3 AGO - Settlement Extents v3.0 consists of a geographic representation
  of settlements in Angola, in two forms: (1) settlement polygons, and (2) spatial
  points depicting the centroids of settled grid cells at 3-arc seconds (or ~100 meters)
  contained within settlement polygons. Both layers include attributes as described
  in the codebooks. The current version supersedes GRID3 Angola Settlement Extents,
  Version 02; the following changes were made: (1) Development of a new methodology
  to derive building counts and settlement polygons with open data. (2) Estimation
  of a probability value for settlement polygons (3) Addition of a building-area measure
  (4) Replacement of degree of urbanization with classification based on built-up
  areas, small settlement areas, and hamlets (5) Elimination of building-count ranges
  (6) Elimination of variable comparing to previous versions Recommended Citation:
  Center for International Earth Science Information Network (CIESIN), Columbia University.
  2024. GRID3 AGO - Settlement Extents v3.0. New York: GRID3. [URL]. Accessed [DAY
  MONTH YEAR].. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/grid3-ago-settlement-extents-v3-0]'
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
    description: Residential population distribution across settlements derived from
      building counts and gridded settlement extents
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
    description: Building stock inventory estimated from open data within settlement
      polygons at ~100 meter resolution
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
    using a new methodology to generate settlement polygons and gridded population
    estimates at 3-arc second (~100 meter) resolution. Spatial points represent centroids
    of settled grid cells within settlement boundaries, with probability values assigned
    to characterize settlement confidence.
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
- href: https://data.humdata.org/dataset/grid3-ago-settlement-extents-v3-0
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
  description: Angola - GRID3 AGO - Settlement Extents v3.0 (A spatial layer representing
    settlement polygons.)
  download_url: https://data.humdata.org/dataset/98dfe29a-8f4e-4cc7-ab16-89e00b0dc26b/resource/fde81e27-2e2e-4485-9619-70e8a10eda07/download/grid3_ago_settlement_extents_v3_0.zip
  format: null
  id: resource_fde81e27
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_AGO_settlement_extents_v3_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Angola - GRID3 AGO - Settlement Extents v3.0 (A spatial layer representing
    the centroids of settled grid cells.)
  download_url: https://data.humdata.org/dataset/98dfe29a-8f4e-4cc7-ab16-89e00b0dc26b/resource/42b48766-78cc-43e3-9cfd-a7538cd14540/download/grid3_ago_settlement_grid_v3_0.zip
  format: null
  id: resource_42b48766
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_AGO_settlement_grid_v3_0.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Angola - GRID3 AGO - Settlement Extents v3.0 (Contains information
    on data inputs, methodology, and codebooks.)
  download_url: https://data.humdata.org/dataset/98dfe29a-8f4e-4cc7-ab16-89e00b0dc26b/resource/893a4c32-2e31-498e-b825-0b555c682672/download/grid3-ago-settlement-extents-v3.0-data-release-notes-.pdf
  format: null
  id: resource_893a4c32
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3 AGO - Settlement Extents v3.0 - Data Release Notes .pdf
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ago_grid3_agosettlementextentsv30_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - AGO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Angola - GRID3 AGO - Settlement Extents v3.0
version: null
vulnerability: null
---
