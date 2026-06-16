---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/osgeonepal_npl_roads
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: TomTom
    url: https://data.humdata.org/dataset/osgeonepal_npl_roads
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OSGeo Nepal
  url: https://data.humdata.org/dataset/osgeonepal_npl_roads
creator:
  affiliation: null
  email: null
  name: OSGeo Nepal
  url: https://data.humdata.org/dataset/osgeonepal_npl_roads
dataset_id: rdls_exp-npl_osgeonpl_roads_20250319
description: 'This dataset includes road networks (e.g., highways, local roads) from
  the Overture Transportation theme, sourced from OpenStreetMap and TomTom. Read more
  at https://docs.overturemaps.org/guides/transportation/. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/osgeonepal_npl_roads]'
details: Contains roads from OSM and TomTom via Overture. Licensed under ODbL v1.0.
  Attribution and share-alike required. Data might contain errors and was processed
  and published using the Overture public release via the overture2hdx package.
exposure:
- asset_type:
    description: Road network infrastructure including highways and local roads with
      geometric representation
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Road network data compiled from OpenStreetMap and TomTom sources through
    the Overture Transportation theme, providing geometric representation of highways
    and local roads across Nepal in standardized geopackage and shapefile formats.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: TomTom
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/osgeonepal_npl_roads
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
  description: Nepal - Roads (Roads data in GPKG format)
  download_url: https://data.humdata.org/dataset/99471d5a-560e-4389-a669-c7d788daf058/resource/a6b579d5-b8d9-4d17-8bd5-74ccd2ad769c/download/osgeonepal_npl_roads_gpkg.zip
  format: null
  id: resource_a6b579d5
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: osgeonepal_npl_roads_gpkg.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Roads (Roads data in SHP format)
  download_url: https://data.humdata.org/dataset/99471d5a-560e-4389-a669-c7d788daf058/resource/b90d31df-9c0d-404a-a730-619a9cfb86f5/download/osgeonepal_npl_roads_shp.zip
  format: null
  id: resource_b90d31df
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: osgeonepal_npl_roads_shp.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-npl_osgeonpl_roads_20250319
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-03-19'
temporal_resolution: null
title: Nepal - Roads
version: null
vulnerability: null
---
