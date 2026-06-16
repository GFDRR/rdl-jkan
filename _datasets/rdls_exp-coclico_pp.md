---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
dataset_id: rdls_exp-coclico_pp
description: 'Population projections (regionalised) provide insights into current
  and future population dynamics. The produced grids have a spatial resolution of
  30*30 arcsecond (approx. 1 km at the equator) and represent the population count
  per cell Spatial coverage: European countries Sources: IIASA SSP3.0-Database Common
  usage: Supports (future) exposure assessments, policy planning, urban and coastal
  analysis, helps prioritize investments and land-use decisions. More Info about the
  dataset: User Handbook. Variants in the source dataset - scenarios: SSP1, SSP2,
  SSP5 - Climate scenarios based on IPCC''s Shared Socioeconomic Pathways (SSPs).
  High-end (if applicable) refers to P83 of SSP5-8.5, taking into account low-confidence
  processes. Other scenarios use the P50; time: 2010, 2030, 2050, 2100 - Time slice
  applied to the data. Either present-day (2010) or future state representing medium
  (2030 till 2050) and long term (2050 till 2100) outlook. Metric unit: deltares:units=people.
  [Source: This metadata record was automatically extracted from the STAC catalog
  coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
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
  description: 'Population projections (regionalised) provide insights into current
    and future population dynamics. The produced grids have a spatial resolution of
    30*30 arcsecond (approx. 1 km at the equator) and represent the population count
    per cell Spatial coverage: European countries Sources: IIASA SSP3.0-Database Common
    usage: Supports (future) exposure assessments, policy planning, urban and coastal
    analysis, helps prioritize investments and land-use decisions. More Info about
    the dataset: User Handbook'
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - exposure
    type: dataset
    url: https://deltares.nl
    used_in: exposure
  - id: source_2
    license: null
    name: Geographisches Institut, Kiel University
    risk_data_type:
    - exposure
    type: dataset
    url: www.uni-kiel.de
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/pp/collection.json
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
  title: 'STAC Collection: CoCliCo - Population Projections [pp]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Fpp.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Population Projections
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
- access_url: https://coclico.avi.deltares.nl/geoserver/gwc/service/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&LAYER=pp:pop_fp_LAU_EPSG4326&STYLE=&TILEMATRIX=EPSG:900913:{z}&TILEMATRIXSET=EPSG:900913&FORMAT=application/vnd.mapbox-vector-tile&TILECOL={x}&TILEROW={y}
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Population Projections (Geoserver Parquet link)
  download_url: null
  format: null
  id: resource_geoserverlink
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Geoserver Parquet link
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Population Projections (Snapshot of the collection's STAC
    items exported to GeoParquet format.)
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
slug: rdls_exp-coclico_pp
spatial:
  bbox:
  - -25.397916667
  - 33.849583333000005
  - 45.268750000000004
  - 71.799583333
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022'
  start: '2022'
temporal_resolution: null
title: CoCliCo - Population Projections
version: null
vulnerability: null
---
