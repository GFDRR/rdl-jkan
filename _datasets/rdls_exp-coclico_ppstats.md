---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Geography Institute, Kiel University
  url: www.uni-kiel.de
creator:
  affiliation: null
  email: null
  name: Geography Institute, Kiel University
  url: www.uni-kiel.de
dataset_id: rdls_exp-coclico_ppstats
description: 'Projections of Exposed People provides insights into current and future
  population exposure to coastal flooding, combining population and flood projections
  to guide risk assessments and adaptation planning. [Source: This metadata record
  was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure:
- asset_type:
    description: population number
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
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Projections of Exposed People provides insights into current and future
    population exposure to coastal flooding, combining population and flood projections
    to guide risk assessments and adaptation planning.
  sources:
  - id: source_1
    license: null
    name: Geography Institute, Kiel University
    risk_data_type:
    - exposure
    type: dataset
    url: www.uni-kiel.de
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
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Geography Institute, Kiel University
  url: www.uni-kiel.de
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: In preparation
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/pp_stats/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/pp_stats/collection.json
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
  title: 'STAC Collection: CoCliCo - People Exposure - statistics [pp_stats]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Fpp_stats.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - People Exposure - statistics
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
  description: CoCliCo - People Exposure - statistics (Snapshot of the collection's
    STAC items exported to GeoParquet format.)
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/pp_stats/pop_stats.parquet
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
slug: rdls_exp-coclico_ppstats
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
title: CoCliCo - People Exposure - statistics
version: null
vulnerability: null
---
