---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: hillaryhanselim7@gmail.com
  name: Hilary_Mvungi
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1549
creator:
  affiliation: null
  email: hillaryhanselim7@gmail.com
  name: Hilary_Mvungi
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1549
dataset_id: rdls_exp-tza_resilienceacade_daressalaamhistoricalfloo
description: 'This dataset comprises of flood depth history experienced by the local
  people living in Dar es Salaam''s most flood-prone areas during rainy seasons. More
  specifically, the local residents were surveyed in eleven wards located nearby the
  Msimbazi river and river streams. Historical records consists of the years of flood
  occurence, flood depth, reasons for flooding, types of buildings affected and whether
  residents moved from the area or not. The aim was to collect a comprehensive data
  set about people''s experiences and whether they were affected by floodings in previous
  years or not. Data was collected by Ramani Huria project, hosted by Humanitarian
  OpenStreetMap Team (HOT). Local residents were interviewed with a structured survey
  and their answers were recorded with the coordinate information of their homes.
  ODK Collect toolkit was used as the collection tool.. [Source: This metadata record
  was automatically extracted from the GeoNode portal resilienceacademy]'
details: EPSG:4326 - WGS 84 - Geographic; 11 wards in Dar es Salaam (Hananasif, Ilala,
  Buguruni, Magomeni, Kigogo, Mchikichini, Jangwani, Ndugumbi, Mzimuni, Tabata, and
  Upanga Maghahribi)..
exposure:
- asset_type: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Individuals were asked to reflect on historical flood extents; therefore
    there is inherent subjectivity in their memories. Logging errors in flood depth
    values. Flood depth values over 850 can be considered as logging errors..
  sources:
  - id: source_1
    license: null
    name: Hilary_Mvungi
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://crd.resilienceacademy.ac.tz/catalogue/#/dataset/733
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Yusouf
  url: https://geonode.resilienceacademy.ac.tz
purpose: This data set was created to better understand how yearly floodings affects
  the local residents in the flood-prone areas of Dar es Salaam. This data set can
  be used in any purposes in community development, research or education..
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Historical Flood Depths (Dbf)
  download_url: https://crd.resilienceacademy.ac.tz/api/v2/assets/140/link
  format: Dbf
  id: resource_0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dar_es_salaam_historical_flood_depths
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Historical Flood Depths (GML 2.0)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_depths&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_1
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dar_es_salaam_historical_flood_depths
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Dar es Salaam Historical Flood Depths (OGC WMS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:dar_es_salaam_historical_flood_depths&format=image%2Fpng
  format: null
  id: resource_2
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dar_es_salaam_historical_flood_depths
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Dar es Salaam Historical Flood Depths (OGC WFS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:dar_es_salaam_historical_flood_depths&outputFormat=application%2Fjson
  format: null
  id: resource_3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Historical Flood Depths (Zipped Shapefile)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_depths&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Historical Flood Depths (CSV)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_depths&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Historical Flood Depths (GML 3.1.1)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_depths&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_6
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Historical Flood Depths (Excel)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_depths&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Historical Flood Depths (JSON)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_depths&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_8
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-tza_resilienceacade_daressalaamhistoricalfloo
spatial:
  bbox:
  - 39.23142273
  - -6.8351383
  - 39.27407872
  - -6.7907416667
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018'
  start: '2017'
temporal_resolution: null
title: Dar es Salaam Historical Flood Depths
version: null
vulnerability: null
---
