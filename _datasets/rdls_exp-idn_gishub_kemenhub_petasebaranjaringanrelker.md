---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Pusdatin
  url: https://gishub.kemenhub.go.id/catalogue/#/dataset/10
creator:
  affiliation: null
  email: null
  name: Pusdatin
  url: https://gishub.kemenhub.go.id/catalogue/#/dataset/10
dataset_id: rdls_exp-idn_gishub_kemenhub_petasebaranjaringanrelker
description: 'Data rel kereta api adalah data yang menggambarkan jaringan rel kereta
  api di suatu wilayah. Data ini dapat digunakan untuk mengetahui tingkat konektivitas
  suatu wilayah dengan wilayah lain melalui jalur kereta api. [Source: This metadata
  record was automatically extracted from the GeoNode portal gishub_kemenhub]'
details: null
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: Pusdatin
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://gishub.kemenhub.go.id/catalogue/#/dataset/10
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Pusdatin
  url: https://gishub.kemenhub.go.id
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Peta Sebaran Jaringan Rel Kereta Api (JSON)
  download_url: https://sigita-csw.kemenhub.go.id/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=kereta%3ARELKA_LN&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_0
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
  description: Peta Sebaran Jaringan Rel Kereta Api (Zipped Shapefile)
  download_url: https://sigita-csw.kemenhub.go.id/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=kereta%3ARELKA_LN&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: https://gishub.kemenhub.go.id/datasets/geonode:RELKA_LN
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Peta Sebaran Jaringan Rel Kereta Api (OGC WMS: kereta Service)'
  download_url: https://sigita-csw.kemenhub.go.id/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:RELKA_LN&format=image%2Fpng
  format: null
  id: resource_2
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: kereta Service'
- access_url: https://gishub.kemenhub.go.id/datasets/geonode:RELKA_LN
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Peta Sebaran Jaringan Rel Kereta Api (OGC WFS: kereta Service)'
  download_url: https://sigita-csw.kemenhub.go.id/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:RELKA_LN&outputFormat=application%2Fjson
  format: null
  id: resource_3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: kereta Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Peta Sebaran Jaringan Rel Kereta Api (GML 2.0)
  download_url: https://sigita-csw.kemenhub.go.id/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=kereta%3ARELKA_LN&outputFormat=gml2&srs=EPSG%3A4326
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
  description: Peta Sebaran Jaringan Rel Kereta Api (GML 3.1.1)
  download_url: https://sigita-csw.kemenhub.go.id/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=kereta%3ARELKA_LN&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
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
  description: Peta Sebaran Jaringan Rel Kereta Api (CSV)
  download_url: https://sigita-csw.kemenhub.go.id/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=kereta%3ARELKA_LN&outputFormat=csv&srs=EPSG%3A4326
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
  description: Peta Sebaran Jaringan Rel Kereta Api (Excel)
  download_url: https://sigita-csw.kemenhub.go.id/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=kereta%3ARELKA_LN&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-idn_gishub_kemenhub_petasebaranjaringanrelker
spatial:
  bbox:
  - 97.975830078125
  - -8.496374130249023
  - 119.76305389404297
  - 4.175422668457031
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2025
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Peta Sebaran Jaringan Rel Kereta Api
version: null
vulnerability: null
---
