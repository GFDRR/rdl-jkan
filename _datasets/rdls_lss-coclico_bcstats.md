---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: BRGM
  url: www.brgm.fr
creator:
  affiliation: null
  email: null
  name: BRGM
  url: www.brgm.fr
dataset_id: rdls_lss-coclico_bcstats
description: 'Projections of the cost of buildings exposed to coastal flooding, integrating
  future flood risk models and current buildings. [Source: This metadata record was
  automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Projections of the cost of buildings exposed to coastal flooding, integrating
    future flood risk models and current buildings.
  sources:
  - id: source_1
    license: null
    name: BRGM
    risk_data_type:
    - loss
    type: dataset
    url: www.brgm.fr
    used_in: loss
  - id: source_2
    license: null
    name: Deltares
    risk_data_type:
    - loss
    type: dataset
    url: https://deltares.nl
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: null
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: EUR
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: BRGM
  url: www.brgm.fr
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: In preparation
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/bc_stats/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/bc_stats/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - Damage Costs - statistics [bc_stats]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Fbc_stats.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Damage Costs - statistics
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thumbnail
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Damage Costs - statistics (Snapshot of the collection's STAC
    items exported to GeoParquet format.)
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/bc_stats/bc_stats.parquet
  format: null
  id: resource_geoparquetstacitems
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoParquet STAC items
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-coclico_bcstats
spatial:
  bbox:
  - -81.12146941539005
  - -29.12357316038395
  - 93.1752791130622
  - 37.855412297701754
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2010'
  start: '2010'
temporal_resolution: null
title: CoCliCo - Damage Costs - statistics
version: null
vulnerability: null
---
