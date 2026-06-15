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
dataset_id: rdls_exp-tza_resilienceacade_mwanzaroads
description: 'This dataset contains information about roads in Mwanza city. This data
  resulted from a data cleaning exercise of existing road data in OpenStreetMap. This
  dataset was produced under the Community Mapping Urban risks in Mwanza project to
  support local stakeholders in disaster risk management. This dataset covers the
  Nyamagana and Ilemea municipalities in Mwanza City. Data processing was executed
  by Spatial Collective, OpenMap Development Tanzania (OMDTZ), Humanitarian OpenStreetMap
  Team (HOT), and students from IRDP and SAUT universities in Mwanza.. [Source: This
  metadata record was automatically extracted from the GeoNode portal resilienceacademy]'
details: 'WGS84, EPSG: 4326. Responsible parties'' contact information: Eng. Aron
  Kalondwa, kalondwaaron@yahoo.com; Justus, Muhando, justus@spatialcollective.com,
  Spatial Collective; Amour Nyalusi, amour.nyalusi@hotosm.org, OMDTZ..'
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
  description: This data resulted from a data cleaning exercise of existing road data
    in OpenStreetMap using the Maxar satelite imagery as the base layer. The imagery
    had a pixel size (spatial resolution) of 0.5 m. During the data cleaning, road
    geometries and overall topologies were fixed and new roads were also added. This
    dataset has been cleaned and quality checked by the project team. This dataset
    has some NULL attributes because these attribute values could not be ascertained
    from remote mapping methods used in the data cleaning exercise..
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
- href: https://crd.resilienceacademy.ac.tz/catalogue/#/dataset/612
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Msilikale Msilanga
  url: https://geonode.resilienceacademy.ac.tz
purpose: This data could be used by planning authorities to assist with local area
  development activities..
referenced_by: []
resources:
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:mwanza_roads
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Mwanza Roads (OGC WFS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:mwanza_roads&outputFormat=application%2Fjson
  format: null
  id: resource_0
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
  description: Mwanza Roads (GeoJSON)
  download_url: https://crd.resilienceacademy.ac.tz/api/v2/assets/9/link
  format: null
  id: resource_1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mwanza_roads
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:mwanza_roads
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Mwanza Roads (OGC WMS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:mwanza_roads&format=image%2Fpng
  format: null
  id: resource_2
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Mwanza Roads (Zipped Shapefile)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Amwanza_roads&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
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
  description: Mwanza Roads (GML 2.0)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Amwanza_roads&outputFormat=gml2&srs=EPSG%3A4326
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
  description: Mwanza Roads (GML 3.1.1)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Amwanza_roads&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
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
  description: Mwanza Roads (CSV)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Amwanza_roads&outputFormat=csv&srs=EPSG%3A4326
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
  description: Mwanza Roads (Excel)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Amwanza_roads&outputFormat=excel&srs=EPSG%3A4326
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
  description: Mwanza Roads (JSON)
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Amwanza_roads&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
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
slug: rdls_exp-tza_resilienceacade_mwanzaroads
spatial:
  bbox:
  - 32.8636547
  - -2.655194983069022
  - 33.08086004297584
  - -2.375680139182044
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020'
  start: '2020'
temporal_resolution: null
title: Mwanza Roads
version: null
vulnerability: null
---
