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
dataset_id: rdls_exp-autita_eurac_sudagoosthospitalsaccessi
description: "Hospital accessibility indicator calculated on the OSM drivable roads\
  \ over the trans-national area composed of Alto Adige / S\xFCdtirol, Agordino (Belluno,\
  \ Italy), and Osttirol (Lienz districit, Austria). [Source: This metadata record\
  \ was automatically extracted from the GeoNode portal eurac]"
details: The data has been computed with the pandana/OSMnx Python libraries stack.
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
license: CC-BY-4.0
lineage:
  description: For the topological structure of the data, see https://wiki.openstreetmap.org/wiki/Quality_assurance.
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
- href: https://maps.eurac.edu/catalogue/#/dataset/768
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Piero Campalani
  url: https://maps.eurac.edu
purpose: Visualize distance on road to nearest health facility.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "S\xFCd-Ago-Ost: Hospitals accessibility on OSM drivable roads (GML\
    \ 2.0)"
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Asudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc&outputFormat=gml2&srs=EPSG%3A4326
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
  coordinate_system: EPSG:4326
  description: "S\xFCd-Ago-Ost: Hospitals accessibility on OSM drivable roads (GML\
    \ 3.1.1)"
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Asudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
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
  description: "S\xFCd-Ago-Ost: Hospitals accessibility on OSM drivable roads (CSV)"
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Asudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_2
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
  description: "S\xFCd-Ago-Ost: Hospitals accessibility on OSM drivable roads (Excel)"
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Asudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:sudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: "S\xFCd-Ago-Ost: Hospitals accessibility on OSM drivable roads (OGC\
    \ WMS: EO_CDR Service)"
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:sudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc&format=image%2Fpng
  format: null
  id: resource_4
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:sudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: "S\xFCd-Ago-Ost: Hospitals accessibility on OSM drivable roads (OGC\
    \ WFS: EO_CDR Service)"
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:sudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc&outputFormat=application%2Fjson
  format: null
  id: resource_5
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
  coordinate_system: EPSG:4326
  description: "S\xFCd-Ago-Ost: Hospitals accessibility on OSM drivable roads (JSON)"
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Asudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_6
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
  description: "S\xFCd-Ago-Ost: Hospitals accessibility on OSM drivable roads (Zipped\
    \ Shapefile)"
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Asudagoost_tran_rds_ln_s4_osm_pp_drive_hospacc&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-autita_eurac_sudagoosthospitalsaccessi
spatial:
  bbox:
  - 10.4131050109863
  - 46.1985321044922
  - 12.936466217041
  - 47.1235694885254
  centroid: null
  countries:
  - AUT
  - ITA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021'
  start: '2021'
temporal_resolution: null
title: "S\xFCd-Ago-Ost: Hospitals accessibility on OSM drivable roads"
version: null
vulnerability: null
---
