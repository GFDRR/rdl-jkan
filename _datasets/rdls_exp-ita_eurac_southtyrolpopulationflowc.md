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
dataset_id: rdls_exp-ita_eurac_southtyrolpopulationflowc
description: 'Absolute difference between traffic counts in the 5-9 AM time interval
  (2021 averages) and the commuting population flow model output. [Source: This metadata
  record was automatically extracted from the GeoNode portal eurac]'
details: Data calculated with the GeoPandas Python library.
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Traffic data taken from the Statistical Office of the Autonomous Province
    of Bolzano/Bozen.
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
- href: https://maps.eurac.edu/catalogue/#/dataset/1117
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Piero Campalani
  url: https://maps.eurac.edu
purpose: Validate the commuting flow model with real traffic data.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Population flow comparison with traffic counts (GML 2.0)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_traffic_vs_flow_250tess_2021&outputFormat=gml2&srs=EPSG%3A25832
  format: null
  id: resource_0
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
  description: 'SOUTH TYROL: Population flow comparison with traffic counts (Excel)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_traffic_vs_flow_250tess_2021&outputFormat=excel&srs=EPSG%3A25832
  format: null
  id: resource_1
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
  description: 'SOUTH TYROL: Population flow comparison with traffic counts (JSON)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_traffic_vs_flow_250tess_2021&outputFormat=json&srs=EPSG%3A25832&srsName=EPSG%3A25832
  format: null
  id: resource_2
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Population flow comparison with traffic counts (Zipped
    Shapefile)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_traffic_vs_flow_250tess_2021&outputFormat=SHAPE-ZIP&srs=EPSG%3A25832&format_options=charset%3AUTF-8
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
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Population flow comparison with traffic counts (GML 3.1.1)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_traffic_vs_flow_250tess_2021&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A25832
  format: null
  id: resource_4
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:st_traffic_vs_flow_250tess_2021
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Population flow comparison with traffic counts (OGC WMS:
    EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:st_traffic_vs_flow_250tess_2021&format=image%2Fpng
  format: null
  id: resource_5
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:st_traffic_vs_flow_250tess_2021
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:25832
  description: 'SOUTH TYROL: Population flow comparison with traffic counts (OGC WFS:
    EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:st_traffic_vs_flow_250tess_2021&outputFormat=application%2Fjson
  format: null
  id: resource_6
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
  description: 'SOUTH TYROL: Population flow comparison with traffic counts (CSV)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Ast_traffic_vs_flow_250tess_2021&outputFormat=csv&srs=EPSG%3A25832
  format: null
  id: resource_7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ita_eurac_southtyrolpopulationflowc
spatial:
  bbox:
  - 613089.25
  - 5122687.5
  - 761288.125
  - 5207982.0
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
title: 'SOUTH TYROL: Population flow comparison with traffic counts'
version: null
vulnerability: null
---
