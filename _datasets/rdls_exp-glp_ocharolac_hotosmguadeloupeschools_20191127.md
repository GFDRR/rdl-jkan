---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/hotosm-guadeloupe-schools
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-guadeloupe-schools
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-guadeloupe-schools
dataset_id: rdls_exp-glp_ocharolac_hotosmguadeloupeschools_20191127
description: 'OpenStreetMap exports for use in GIS applications. This theme includes
  all OpenStreetMap features in this area matching: amenity IN (''kindergarten'',
  ''school'', ''college'', ''university'',''language_school'') OR office=''educational_institution''
  Features may have these attributes: name, amenity, isced:level, capacity Geometry
  types: point, polygon This dataset is one of many OpenStreetMap exports on HDX.
  See the Humanitarian OpenStreetMap Team website for more information.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hotosm-guadeloupe-schools]'
details: A few of the school names are missing.
exposure:
- asset_type:
    description: Educational facility locations (schools, colleges, universities,
      language schools, kindergartens) in Guadeloupe with point and polygon geometries
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
      quantity_kind: count
      unit: count
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Educational facility locations were extracted from OpenStreetMap using
    feature filters for amenity types (kindergarten, school, college, university,
    language_school) and office type (educational_institution). Data were exported
    as point and polygon geometries with attributes including name, amenity type,
    ISCED education level, and facility capacity for use in GIS applications.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hotosm-guadeloupe-schools
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
  description: HOTOSM Guadeloupe Schools (ESRI Shapefile)
  download_url: https://data.humdata.org/dataset/c9c25e09-2835-4e18-95ce-1cdfc009ec81/resource/8cf82cfb-60b5-4719-8b53-ab50b171e219/download/glp_schools_shp.zip
  format: null
  id: resource_8cf82cfb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_schools_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HOTOSM Guadeloupe Schools (GeoPackage)
  download_url: https://data.humdata.org/dataset/c9c25e09-2835-4e18-95ce-1cdfc009ec81/resource/c014d8af-7bae-4c09-a23a-1e1a73819f10/download/glp_schools_gpkg.zip
  format: null
  id: resource_c014d8af
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: glp_schools_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-glp_ocharolac_hotosmguadeloupeschools_20191127
spatial:
  bbox: null
  centroid: null
  countries:
  - GLP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-27'
temporal_resolution: null
title: HOTOSM Guadeloupe Schools
version: null
vulnerability: null
---
