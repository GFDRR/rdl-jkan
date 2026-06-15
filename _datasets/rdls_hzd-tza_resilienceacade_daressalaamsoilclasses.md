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
dataset_id: rdls_hzd-tza_resilienceacade_daressalaamsoilclasses
description: 'The dataset is based on 731 soil sample points created in ArcGIS using
  a 2km by 2km regular grid on the whole of Dar es Salaam''s catchment area. Each
  sample point with a unique code to identify it. The surface soil dataset for the
  greater Dar es Salaam region of Tanzania. This was intended to support a geomorphological
  assessment taking into account soil characteristics for erosion and flood risk studies.
  A national-level soil profile had existed for Tanzania prior to this effort, but
  contained only a single sample from Dar es Salaam. This was not sufficient to analyse
  erosion potential across the city. A 2km grid was used which resulted in 731 sampling
  points being pre-established throughout the city.. [Source: This metadata record
  was automatically extracted from the GeoNode portal resilienceacademy]'
details: EPSG:4326 - WGS 84 - Geographic; Dar es Salaam and neighboring districts
  of Pwani region i.e. Bagamoyo, Kibaha and Kisarawe.
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
      calculation_method: inferred
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
  description: 88 points were not collected because they were inaccessible.
  sources:
  - id: source_1
    license: null
    name: Hilary_Mvungi
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://crd.resilienceacademy.ac.tz/catalogue/#/dataset/757
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: demorgan
  url: https://geonode.resilienceacademy.ac.tz
purpose: This data is primarily intended for use with erosion modeling. For users
  not equipped with erosion modeling skills and toolkits, and for sharing the results
  with the public, a visual map has been prepared that gives a good first impression
  of the characteristics of the soil..
referenced_by: []
resources:
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dar_es_salaam_soil_sediment_sampling
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Dar es Salaam Soil Classes (OGC WMS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:dar_es_salaam_soil_sediment_sampling&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dar_es_salaam_soil_sediment_sampling
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Dar es Salaam Soil Classes (OGC WFS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:dar_es_salaam_soil_sediment_sampling&outputFormat=application%2Fjson
  format: null
  id: resource_1
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
  description: Dar es Salaam Soil Classes (GeoPackage)
  download_url: https://crd.resilienceacademy.ac.tz/api/v2/assets/170/link
  format: null
  id: resource_2
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dar_es_salaam_soil_sediment_sampling
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Dar es Salaam Soil Classes (Zipped Shapefile)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_soil_sediment_sampling&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_3
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
  description: Dar es Salaam Soil Classes (GML 2.0)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_soil_sediment_sampling&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_4
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
  description: Dar es Salaam Soil Classes (GML 3.1.1)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_soil_sediment_sampling&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_5
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
  description: Dar es Salaam Soil Classes (CSV)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_soil_sediment_sampling&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_6
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
  description: Dar es Salaam Soil Classes (Excel)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_soil_sediment_sampling&outputFormat=excel&srs=EPSG%3A4326
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
  description: Dar es Salaam Soil Classes (JSON)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Adar_es_salaam_soil_sediment_sampling&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
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
schema: rdls-10
slug: rdls_hzd-tza_resilienceacade_daressalaamsoilclasses
spatial:
  bbox:
  - 38.91432
  - -7.19723
  - 39.5450133333
  - -6.5583533333
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019'
  start: '2018'
temporal_resolution: null
title: Dar es Salaam Soil Classes
version: null
vulnerability: null
---
