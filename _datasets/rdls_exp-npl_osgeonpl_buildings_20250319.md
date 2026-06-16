---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/osgeonepal_npl_buildings
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Microsoft Global ML Buildings
    url: https://data.humdata.org/dataset/osgeonepal_npl_buildings
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Google Open Buildings
    url: https://data.humdata.org/dataset/osgeonepal_npl_buildings
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Esri Community Maps
    url: https://data.humdata.org/dataset/osgeonepal_npl_buildings
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OSGeo Nepal
  url: https://data.humdata.org/dataset/osgeonepal_npl_buildings
creator:
  affiliation: null
  email: null
  name: OSGeo Nepal
  url: https://data.humdata.org/dataset/osgeonepal_npl_buildings
dataset_id: rdls_exp-npl_osgeonpl_buildings_20250319
description: 'This dataset includes building footprints from the Overture Buildings
  theme. Sources include OSM, Microsoft Global ML Buildings, Google Open Buildings,
  and Esri Community Maps. Read more at https://docs.overturemaps.org/guides/buildings/.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/osgeonepal_npl_buildings]'
details: Includes building data from OSM (ODbL), Microsoft (ODbL), Google (CC BY),
  and Esri (CC BY). Final dataset is ODbL-licensed. Attribution and share-alike required.
  Data might contain errors and was processed and published using the Overture public
  release via the overture2hdx package.
exposure:
- asset_type:
    description: Building footprints and structure inventory across Nepal derived
      from multiple open geospatial sources
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Building footprints were aggregated from four independent sources (OSM,
    Microsoft ML, Google Open Buildings, Esri Community Maps) through the Overture
    Maps standardization framework. The dataset provides unified building structure
    geometry across Nepal in vector format (GeoPackage and Shapefile), enabling exposure
    assessment for disaster risk applications.
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
    name: Microsoft Global ML Buildings
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Google Open Buildings
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_4
    license: null
    name: Esri Community Maps
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/osgeonepal_npl_buildings
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
  description: Nepal - Buildings (Buildings data in GPKG format)
  download_url: https://data.humdata.org/dataset/f47f74f6-8624-42ac-bceb-1c46ef4599a1/resource/f5278cec-c8a0-4e68-96a7-895c4f474f75/download/osgeonepal_npl_buildings_gpkg.zip
  format: null
  id: resource_f5278cec
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: osgeonepal_npl_buildings_gpkg.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Buildings (Buildings data in SHP format)
  download_url: https://data.humdata.org/dataset/f47f74f6-8624-42ac-bceb-1c46ef4599a1/resource/6203007e-0961-47b5-adb1-460e3935c22c/download/osgeonepal_npl_buildings_shp.zip
  format: null
  id: resource_6203007e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: osgeonepal_npl_buildings_shp.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-npl_osgeonpl_buildings_20250319
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
title: Nepal - Buildings
version: null
vulnerability: null
---
