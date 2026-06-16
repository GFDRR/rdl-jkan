---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: motimb@utu.fi
  name: Monica Timbuka
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1550
creator:
  affiliation: null
  email: motimb@utu.fi
  name: Monica Timbuka
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1550
dataset_id: rdls_exp-tza_resilienceacade_zanzibarurbanwestroadnetw
description: 'The road network of Zanzibar Urban West categorized according to the
  OpenStreetMap highway classification.. [Source: This metadata record was automatically
  extracted from the GeoNode portal resilienceacademy]'
details: EPSG:32737 - WGS 84 / UTM zone 37S.
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
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: This dataset is a representation of the roads that exist on OpenStreetMap
    as at October 2019. Most of the roads were added by students from the State University
    of Zanzibar from digitizing roads as seen from high resolution 7cm drone imagery.
    Due to the changing nature of the city, this dataset needs to be constantly updated
    to reflect the changes on the ground..
  sources:
  - id: source_1
    license: null
    name: Monica Timbuka
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://crd.resilienceacademy.ac.tz/catalogue/#/dataset/654
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Ramadhani
  url: https://geonode.resilienceacademy.ac.tz
purpose: This dataset supports urban planning, climate risk assessment, and resilience
  building in Zanzibar.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32737
  description: Zanzibar Urban West Road Network (JSON)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aroad_network&outputFormat=json&srs=EPSG%3A32737&srsName=EPSG%3A32737
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
  coordinate_system: EPSG:32737
  description: Zanzibar Urban West Road Network (CSV)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aroad_network&outputFormat=csv&srs=EPSG%3A32737
  format: null
  id: resource_1
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
  coordinate_system: EPSG:32737
  description: Zanzibar Urban West Road Network (Prj)
  download_url: https://crd.resilienceacademy.ac.tz/api/v2/assets/52/link
  format: Prj
  id: resource_2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: road_network
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:road_network
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:32737
  description: 'Zanzibar Urban West Road Network (OGC WMS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:road_network&format=image%2Fpng
  format: null
  id: resource_3
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:road_network
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:32737
  description: 'Zanzibar Urban West Road Network (OGC WFS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:road_network&outputFormat=application%2Fjson
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
  coordinate_system: EPSG:32737
  description: Zanzibar Urban West Road Network (Zipped Shapefile)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aroad_network&outputFormat=SHAPE-ZIP&srs=EPSG%3A32737&format_options=charset%3AUTF-8
  format: null
  id: resource_5
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
  coordinate_system: EPSG:32737
  description: Zanzibar Urban West Road Network (GML 2.0)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aroad_network&outputFormat=gml2&srs=EPSG%3A32737
  format: null
  id: resource_6
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
  coordinate_system: EPSG:32737
  description: Zanzibar Urban West Road Network (GML 3.1.1)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aroad_network&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A32737
  format: null
  id: resource_7
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
  coordinate_system: EPSG:32737
  description: Zanzibar Urban West Road Network (Excel)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Aroad_network&outputFormat=excel&srs=EPSG%3A32737
  format: null
  id: resource_8
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
slug: rdls_exp-tza_resilienceacade_zanzibarurbanwestroadnetw
spatial:
  bbox:
  - 520592.0538941766
  - 9313205.752102077
  - 525148.9389363538
  - 9322100.43126823
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2020
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Zanzibar Urban West Road Network
version: null
vulnerability: null
---
