---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: piero.campalani@eurac.edu
  name: Piero Campalani
  url: https://maps.eurac.edu/api/v2/users/1060
creator:
  affiliation: null
  email: piero.campalani@eurac.edu
  name: Piero Campalani
  url: https://maps.eurac.edu/api/v2/users/1060
dataset_id: rdls_exp-ita_eurac_southtyrolhomeworktripste
description: 'Projection of home->work trips in South Tyrol onto OSM drivable roads
  network. Roads themselves are projected onto a 250m hexagonal tessellation. [Source:
  This metadata record was automatically extracted from the GeoNode portal eurac]'
details: 'Original trips data were projected onto the 250 hexagonal tessellation driven
  by resident population on one side, and by employees data on the other. Top 5 hexagonal
  cells were kept to project the trips, amounting to max 25 projected/estimated trips
  for each actual trip information. Trips are then projected onto the tessellated
  roads dataset through a Dijkstra shortest path based on the capacity of each road
  segment. Python libraries used: NetworkX, GeoPandas.'
exposure:
- asset_type: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
- asset_type: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Raw data provided by the Amt f\xC3\xBCr Arbeitsmarktbeobachtung/Ufficio\
    \ Osservazione Mercato del Lavoro of Bozen/Bolzano. Projected data is only an\
    \ approximation of people flow, and relies on several unverified assumptions."
  sources:
  - id: source_1
    license: null
    name: Piero Campalani
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/1122
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Piero Campalani
  url: https://maps.eurac.edu
purpose: Have an estimation of people flow during home->work commutes, and viceversa.
referenced_by: []
resources:
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:st_pop_flow_rds_ln_s3_apb_250m
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Home->work trips on tessellated roads network (OGC WMS:
    EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:st_pop_flow_rds_ln_s3_apb_250m&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:st_pop_flow_rds_ln_s3_apb_250m
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Home->work trips on tessellated roads network (OGC WFS:
    EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:st_pop_flow_rds_ln_s3_apb_250m&outputFormat=application%2Fjson
  format: null
  id: resource_1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: EO_CDR Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Home->work trips on tessellated roads network (Zipped
    Shapefile)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_pop_flow_rds_ln_s3_apb_250m&outputFormat=SHAPE-ZIP&srs=EPSG%3A25832&format_options=charset%3AUTF-8
  format: null
  id: resource_2
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
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Home->work trips on tessellated roads network (GML 2.0)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_pop_flow_rds_ln_s3_apb_250m&outputFormat=gml2&srs=EPSG%3A25832
  format: null
  id: resource_3
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
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Home->work trips on tessellated roads network (GML 3.1.1)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_pop_flow_rds_ln_s3_apb_250m&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A25832
  format: null
  id: resource_4
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
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Home->work trips on tessellated roads network (CSV)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_pop_flow_rds_ln_s3_apb_250m&outputFormat=csv&srs=EPSG%3A25832
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
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Home->work trips on tessellated roads network (Excel)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_pop_flow_rds_ln_s3_apb_250m&outputFormat=excel&srs=EPSG%3A25832
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
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Home->work trips on tessellated roads network (JSON)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_pop_flow_rds_ln_s3_apb_250m&outputFormat=json&srs=EPSG%3A25832&srsName=EPSG%3A25832
  format: null
  id: resource_7
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
slug: rdls_exp-ita_eurac_southtyrolhomeworktripste
spatial:
  bbox:
  - 611926.0
  - 5122555.5
  - 757565.6875
  - 5214566.0
  centroid: null
  countries:
  - ITA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2022
  duration: null
  end: null
  start: null
temporal_resolution: null
title: 'SOUTH TYROL: Home->work trips on tessellated roads network'
version: null
vulnerability: null
---
