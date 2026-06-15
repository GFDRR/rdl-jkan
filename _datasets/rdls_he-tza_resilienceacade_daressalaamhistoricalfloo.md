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
dataset_id: rdls_he-tza_resilienceacade_daressalaamhistoricalfloo
description: 'The dataset comprises of flood history (years of flood occurence), flood
  depth, reasons for flooding, types of buildings, uses, whether residents were evacuated
  or not. All data points were collected by using ODK Collect.. [Source: This metadata
  record was automatically extracted from the GeoNode portal resilienceacademy]'
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
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: This is community generated data, therefore individuals were asked
    to reflect on historical flood extents; this comes with inherent subjectivity
    based on their memories.
  sources:
  - id: source_1
    license: null
    name: Hilary_Mvungi
    risk_data_type:
    - hazard
    - exposure
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://crd.resilienceacademy.ac.tz/catalogue/#/dataset/727
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Gideon Marandu
  url: https://geonode.resilienceacademy.ac.tz
purpose: "Historical flood extent covered areas that are mostly affected by floods\
  \ during rainy seasons. Households surveys were conducted to capture details in\
  \ subwards of the respective wards across the Msimbazi River rivers and streams\
  \ that outflow to the main river. The information captured aimed to know whether\
  \ the respondent had been affected by floods in the previous years, the flood depth\
  \ and flood occurrence years\u201A\xEE\xC5historical flood events.."
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Historical Flood Extent (CSV)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_extent&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_0
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
  description: Dar es Salaam Historical Flood Extent (GML 3.1.1)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_extent&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_1
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
  description: Dar es Salaam Historical Flood Extent (GeoJSON)
  download_url: https://crd.resilienceacademy.ac.tz/api/v2/assets/134/link
  format: null
  id: resource_2
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dar_es_salaam_historical_flood_extent
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dar_es_salaam_historical_flood_extent
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Dar es Salaam Historical Flood Extent (OGC WMS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:dar_es_salaam_historical_flood_extent&format=image%2Fpng
  format: null
  id: resource_3
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dar_es_salaam_historical_flood_extent
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Dar es Salaam Historical Flood Extent (OGC WFS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:dar_es_salaam_historical_flood_extent&outputFormat=application%2Fjson
  format: null
  id: resource_4
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
  description: Dar es Salaam Historical Flood Extent (GML 2.0)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_extent&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_5
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Historical Flood Extent (Excel)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_extent&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_6
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
  description: Dar es Salaam Historical Flood Extent (Zipped Shapefile)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_extent&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_7
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
  description: Dar es Salaam Historical Flood Extent (JSON)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_historical_flood_extent&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
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
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tza_resilienceacade_daressalaamhistoricalfloo
spatial:
  bbox:
  - 39.23025374
  - -6.83811
  - 39.28173
  - -6.7818033333
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
title: Dar es Salaam Historical Flood Extent
version: null
vulnerability: null
---
