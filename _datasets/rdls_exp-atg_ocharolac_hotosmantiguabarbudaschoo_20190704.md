---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm-antigua-and-barbuda-schools-openstreetmap-export
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-antigua-and-barbuda-schools-openstreetmap-export
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-antigua-and-barbuda-schools-openstreetmap-export
dataset_id: rdls_exp-atg_ocharolac_hotosmantiguabarbudaschoo_20190704
description: 'OpenStreetMap exports for use in GIS applications. This theme includes
  all OpenStreetMap features in this area matching: amenity IN (''kindergarten'',
  ''school'', ''college'', ''university'',''language_school'') OR office=''educational_institution''
  Features may have these attributes: name, amenity, isced:level, capacity Geometry
  types: point, polygon This dataset is one of many OpenStreetMap exports on HDX.
  See the Humanitarian OpenStreetMap Team website for more information.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hotosm-antigua-and-barbuda-schools-openstreetmap-export]'
details: Some of the school names are missing.
exposure:
- asset_type:
    description: Educational facility locations (schools, colleges, universities,
      language schools, kindergartens) with capacity and classification level attributes
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
    amenity and office tags matching kindergarten, school, college, university, and
    language_school categories. Features were exported as point and polygon geometries
    with attributes including name, capacity, and ISCED education level for use in
    GIS applications.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap contributors
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hotosm-antigua-and-barbuda-schools-openstreetmap-export
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
  description: HOTOSM Antigua and Barbuda Schools (ESRI Shapefile)
  download_url: https://data.humdata.org/dataset/424407ed-35df-452a-bddb-84b5fbbd2445/resource/5c15d68c-99c5-41b2-ab22-09b1cdd96d3f/download/atg_schools_shp.zip
  format: null
  id: resource_5c15d68c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atg_schools_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HOTOSM Antigua and Barbuda Schools (GeoPackage)
  download_url: https://data.humdata.org/dataset/424407ed-35df-452a-bddb-84b5fbbd2445/resource/60dbe423-872a-44cd-8755-4dc805da2b83/download/atg_schools_gpkg.zip
  format: null
  id: resource_60dbe423
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atg_schools_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-atg_ocharolac_hotosmantiguabarbudaschoo_20190704
spatial:
  bbox: null
  centroid: null
  countries:
  - ATG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-07-04'
temporal_resolution: null
title: HOTOSM Antigua and Barbuda Schools
version: null
vulnerability: null
---
