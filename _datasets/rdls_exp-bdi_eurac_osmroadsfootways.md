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
dataset_id: rdls_exp-bdi_eurac_osmroadsfootways
description: 'All roads and footways of Burundi from OpenStreetMap (OSM). [Source:
  This metadata record was automatically extracted from the GeoNode portal eurac]'
details: 'Contains information from OpenStreetMap, which is made available here under
  the Open Database License (ODbL). OSM Overpass query: ----------------------- [''highway''!~''abandoned|construction|planned|platform|proposed|raceway'']
  [''service''!~''private''] -----------------------'
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
hazard: null
license: ODbL-1.0/
lineage:
  description: None.
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
- href: https://maps.eurac.edu/catalogue/#/dataset/624
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Piero Campalani
  url: https://maps.eurac.edu
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'BURUNDI: OSM roads and footways (Zipped Shapefile)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_all_roads&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_0
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
  description: 'BURUNDI: OSM roads and footways (Excel)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_all_roads&outputFormat=excel&srs=EPSG%3A4326
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
  coordinate_system: EPSG:4326
  description: 'BURUNDI: OSM roads and footways (JSON)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_all_roads&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
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
  coordinate_system: EPSG:4326
  description: 'BURUNDI: OSM roads and footways (GML 3.1.1)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_all_roads&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_3
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
  description: 'BURUNDI: OSM roads and footways (GML 2.0)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_all_roads&outputFormat=gml2&srs=EPSG%3A4326
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
  description: 'BURUNDI: OSM roads and footways (CSV)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_all_roads&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_all_roads
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'BURUNDI: OSM roads and footways (OGC WMS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:bdi_all_roads&format=image%2Fpng
  format: null
  id: resource_6
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_all_roads
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'BURUNDI: OSM roads and footways (OGC WFS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:bdi_all_roads&outputFormat=application%2Fjson
  format: null
  id: resource_7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: EO_CDR Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bdi_eurac_osmroadsfootways
spatial:
  bbox:
  - 29.0021057128906
  - -4.46676969528198
  - 30.8435230255127
  - -2.32193064689636
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2021
  duration: null
  end: null
  start: null
temporal_resolution: null
title: 'BURUNDI: OSM roads and footways'
version: null
vulnerability: null
---
