---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/hotosm-guyana-schools
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-guyana-schools
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-guyana-schools
dataset_id: rdls_exp-guy_ocharolac_hotosmschools_20191126
description: 'OpenStreetMap exports for use in GIS applications. This theme includes
  all OpenStreetMap features in this area matching: amenity IN (''kindergarten'',
  ''school'', ''college'', ''university'',''language_school'') OR office=''educational_institution''
  Features may have these attributes: name, amenity, isced:level, capacity Geometry
  types: point, polygon This dataset is one of many OpenStreetMap exports on HDX.
  See the Humanitarian OpenStreetMap Team website for more information.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hotosm-guyana-schools]'
details: Some of the school names and their classifications are missing.
exposure:
- asset_type:
    description: Educational facilities (schools, colleges, universities, language
      schools, kindergartens) with point and polygon geometries
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
license: ODbL-1.0/
lineage:
  description: Educational facility locations were extracted from OpenStreetMap using
    amenity and office tags matching kindergarten, school, college, university, language_school,
    and educational_institution categories. Features were exported with attributes
    including name, amenity type, ISCED education level, and capacity, provided in
    shapefile and geopackage formats for GIS analysis.
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
- href: https://data.humdata.org/dataset/hotosm-guyana-schools
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
  description: HOTOSM Guyana Schools (ESRI Shapefile)
  download_url: https://data.humdata.org/dataset/d7431335-3834-4495-90c2-13150f007814/resource/e61fcd88-00eb-4ccf-a29a-88dff5bdba2b/download/guy_schools_1_shp.zip
  format: null
  id: resource_e61fcd88
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_schools_1_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HOTOSM Guyana Schools (GeoPackage)
  download_url: https://data.humdata.org/dataset/d7431335-3834-4495-90c2-13150f007814/resource/7b2b088a-4363-48e0-baee-af749172e615/download/guy_schools_1_gpkg.zip
  format: null
  id: resource_7b2b088a
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guy_schools_1_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-guy_ocharolac_hotosmschools_20191126
spatial:
  bbox: null
  centroid: null
  countries:
  - GUY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-26'
temporal_resolution: null
title: HOTOSM Guyana Schools
version: null
vulnerability: null
---
