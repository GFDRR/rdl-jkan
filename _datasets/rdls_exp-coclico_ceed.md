---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Institute for Environmental Studies, Vrije Universiteit Amsterdam
  url: www.ivm.nl
creator:
  affiliation: null
  email: null
  name: Institute for Environmental Studies, Vrije Universiteit Amsterdam
  url: www.ivm.nl
dataset_id: rdls_exp-coclico_ceed
description: 'EU-wide high-resolution object-based maps of economic assets and infrastructure
  systems in coastal flood-prone areas that combined the automated extraction of asset
  using supervised DL algorithms applied to satellite imagery and opensource database.
  Dataset is divided over NUTS2 polygons. [Source: This metadata record was automatically
  extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
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
license: CC-BY-4.0
lineage:
  description: EU-wide high-resolution object-based maps of economic assets and infrastructure
    systems in coastal flood-prone areas that combined the automated extraction of
    asset using supervised DL algorithms applied to satellite imagery and opensource
    database. Dataset is divided over NUTS2 polygons.
  sources:
  - id: source_1
    license: null
    name: Institute for Environmental Studies, Vrije Universiteit Amsterdam
    risk_data_type:
    - exposure
    type: dataset
    url: www.ivm.nl
    used_in: exposure
  - id: source_2
    license: null
    name: Deltares
    risk_data_type:
    - exposure
    type: dataset
    url: https://deltares.nl
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Institute for Environmental Studies, Vrije Universiteit Amsterdam
  url: www.ivm.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/ceed/collection.json
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
  title: 'STAC Collection: CoCliCo - Coastal European Exposure Database [ceed]'
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/ceed.jpeg
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Coastal European Exposure Database
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/jpeg
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
  description: CoCliCo - Coastal European Exposure Database (Snapshot of the collection's
    STAC items exported to GeoParquet format.)
  download_url: gs://coclico-data-public/coclico/items/ceed.parquet
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
- exposure
schema: rdls-10
slug: rdls_exp-coclico_ceed
spatial:
  bbox:
  - -11.045382150506173
  - 34.269110172112164
  - 34.53596939451993
  - 71.03953129412078
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021'
  start: '2021'
temporal_resolution: null
title: CoCliCo - Coastal European Exposure Database
version: null
vulnerability: null
---
