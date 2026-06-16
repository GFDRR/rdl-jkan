---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/hotosm-haiti-schools
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-haiti-schools
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-haiti-schools
dataset_id: rdls_exp-hti_ocharolac_hotosmschools_20191127
description: 'OpenStreetMap exports for use in GIS applications. This theme includes
  all OpenStreetMap features in this area matching: amenity IN (''kindergarten'',
  ''school'', ''college'', ''university'',''language_school'') OR office=''educational_institution''
  Features may have these attributes: name, amenity, isced:level, capacity Geometry
  types: point, polygon This dataset is one of many OpenStreetMap exports on HDX.
  See the Humanitarian OpenStreetMap Team website for more information.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hotosm-haiti-schools]'
details: Some of the school names are missing.
exposure:
- asset_type:
    description: Educational facility locations and infrastructure (schools, colleges,
      universities, language schools, kindergartens) with capacity and classification
      attributes
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
    amenity and office tags matching kindergarten, school, college, university, language
    school, and educational institution classifications. Features were exported as
    point and polygon geometries with associated attributes (name, capacity, ISCED
    level) for Haiti and provided in shapefile and geopackage formats for GIS applications.
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
- href: https://data.humdata.org/dataset/hotosm-haiti-schools
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
  description: HOTOSM Haiti Schools (ESRI Shapefile)
  download_url: https://data.humdata.org/dataset/2ed85a3f-370d-47fa-aae8-f8863c4cbb5c/resource/5a0d2934-5ee6-4f85-9c61-c55f745b5d14/download/hti_schools_shp.zip
  format: null
  id: resource_5a0d2934
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_schools_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HOTOSM Haiti Schools (GeoPackage)
  download_url: https://data.humdata.org/dataset/2ed85a3f-370d-47fa-aae8-f8863c4cbb5c/resource/a672e92e-86e4-4b3e-83ec-59da02ebdbd2/download/hti_schools_gpkg.zip
  format: null
  id: resource_a672e92e
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_schools_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-hti_ocharolac_hotosmschools_20191127
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-27'
temporal_resolution: null
title: HOTOSM Haiti Schools
version: null
vulnerability: null
---
