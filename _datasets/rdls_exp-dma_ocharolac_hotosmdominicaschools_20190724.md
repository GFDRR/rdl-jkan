---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap contributors
    url: https://data.humdata.org/dataset/hotosm-dominica-schools
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-dominica-schools
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/hotosm-dominica-schools
dataset_id: rdls_exp-dma_ocharolac_hotosmdominicaschools_20190724
description: 'OpenStreetMap exports for use in GIS applications. This theme includes
  all OpenStreetMap features in this area matching: amenity IN (''kindergarten'',
  ''school'', ''college'', ''university'',''language_school'') OR office=''educational_institution''
  Features may have these attributes: name, amenity, isced:level, capacity Geometry
  types: point, polygon This dataset is one of many OpenStreetMap exports on HDX.
  See the Humanitarian OpenStreetMap Team website for more information.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hotosm-dominica-schools]'
details: Some of the school names are missing.
exposure:
- asset_type:
    description: Educational facility locations (schools, colleges, universities,
      language schools, kindergartens) with capacity and ISCED level attributes
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
    amenity and office tags matching kindergarten, school, college, university, and
    language_school categories. Features were filtered for Dominica and exported with
    attributes including name, capacity, and ISCED education level classification.
    Data is provided in shapefile and geopackage formats for GIS integration.
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
- href: https://data.humdata.org/dataset/hotosm-dominica-schools
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
  description: HOTOSM Dominica Schools (ESRI Shapefile)
  download_url: https://data.humdata.org/dataset/19ffdfe5-ded6-4310-b5f2-481a98c96a5c/resource/7b9b74b1-e1a2-4ce2-bd14-2913430abcd0/download/dma_schools_shp.zip
  format: null
  id: resource_7b9b74b1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dma_schools_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: HOTOSM Dominica Schools (GeoPackage)
  download_url: https://data.humdata.org/dataset/19ffdfe5-ded6-4310-b5f2-481a98c96a5c/resource/57c822d9-43f5-4714-b5c3-2f4ac132a326/download/dma_schools_gpkg.zip
  format: null
  id: resource_57c822d9
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dma_schools_gpkg.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-dma_ocharolac_hotosmdominicaschools_20190724
spatial:
  bbox: null
  centroid: null
  countries:
  - DMA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-07-24'
temporal_resolution: null
title: HOTOSM Dominica Schools
version: null
vulnerability: null
---
