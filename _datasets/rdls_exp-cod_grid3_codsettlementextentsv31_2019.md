---
attributions:
- entity:
    affiliation: null
    email: null
    name: Center for International Earth Science Information Network (CIESIN)
    url: https://data.humdata.org/dataset/grid3-cod-settlement-extents-v3-1
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-cod-settlement-extents-v3-1
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/grid3-cod-settlement-extents-v3-1
dataset_id: rdls_exp-cod_grid3_codsettlementextentsv31_2019
description: "The GRID3 COD - Settlement Extents v3.1 consists of a geographic representation\
  \ of settlements in the Democratic Republic of the Congo, in two forms: 1) settlement\
  \ polygons, and 2) spatial points depicting the centroids of settled grid cells\
  \ at 3-arc seconds (or ~100 meters) contained within settlement polygons. Both layers\
  \ include attributes as described in the codebooks. Data inputs and methodology\
  \ to derive the 2 layers are described in this document. The current version supersedes\
  \ GRID3 COD - Settlement Extents v3.0; the following changes were made: \u25CF Corrections\
  \ on imputed values for building count and building areas. \u25CF Corrections on\
  \ probability values from field-collected data \u25CF Edits in the Data Release\
  \ Notes. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/grid3-cod-settlement-extents-v3-1]"
details: CIESIN, Columbia University, and its co-authors follow procedures designed
  to ensure that data disseminated by the project are of reasonable quality. If, despite
  these procedures, users encounter apparent errors or misstatements in the data,
  they should contact CIESIN, info@ciesin.columbia.edu. CIESIN, Columbia University,
  its co-authors, and their sponsors do not guarantee the accuracy, reliability, or
  completeness of any data provided. We provide these data without warranty of any
  kind whatsoever, either expressed or implied, and shall not be liable for incidental,
  consequential, or special damages arising out of the use of any data provided.
exposure:
- asset_type:
    description: Spatial distribution of settled population represented as grid cells
      and settlement polygons at ~100 meter resolution
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Settlement extents were derived from satellite imagery and ancillary
    geospatial data to create polygon boundaries and 3-arc-second (~100 meter) grid
    cell centroids representing settled areas. The dataset provides a spatial inventory
    of population distribution across settlements in the DRC, enabling exposure assessment
    for disaster risk applications.
  sources:
  - id: source_1
    license: null
    name: Center for International Earth Science Information Network (CIESIN)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/grid3-cod-settlement-extents-v3-1
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
  description: DR Congo - GRID3 COD - Settlement Extents v3.1 (A spatial layer representing
    the centroids of settled grid cells.)
  download_url: https://data.humdata.org/dataset/335743dd-f27f-4382-9586-c5bfdf281aa0/resource/c87b6a5a-7a80-4ccb-85b3-c995a659e2f8/download/grid3_cod_settlement_grid_v3_1_gpkg.zip
  format: null
  id: resource_c87b6a5a
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_COD_settlement_grid_v3_1_gpkg.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DR Congo - GRID3 COD - Settlement Extents v3.1 (A spatial layer representing
    settlement polygons.)
  download_url: https://data.humdata.org/dataset/335743dd-f27f-4382-9586-c5bfdf281aa0/resource/cd6afdc2-fbd1-43cb-bc92-d1c7b3aed0cc/download/grid3_cod_settlement_extents_v3_1_gpkg.zip
  format: null
  id: resource_cd6afdc2
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3_COD_settlement_extents_v3_1_gpkg.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data inputs and methodology to derive the 2 layers are described in
    this document.
  download_url: https://data.humdata.org/dataset/335743dd-f27f-4382-9586-c5bfdf281aa0/resource/92aad250-d38b-4ff7-ab1e-63a005e81701/download/grid3-cod-settlement-extents-v3.1-data-release-notes.pdf
  format: null
  id: resource_92aad250
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GRID3 COD - Settlement Extents v3.1 - Data Release Notes.pdf
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cod_grid3_codsettlementextentsv31_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2019-01-01'
temporal_resolution: null
title: DR Congo - GRID3 COD - Settlement Extents v3.1
version: null
vulnerability: null
---
