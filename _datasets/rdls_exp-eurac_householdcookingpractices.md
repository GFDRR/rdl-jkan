---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: daniele_antonucci@eurac.edu
  name: Daniele Antonucci
  url: https://maps.eurac.edu/api/v2/users/1004
creator:
  affiliation: null
  email: andrea.vianello@eurac.edu
  name: Andrea Vianello
  url: https://maps.eurac.edu/api/v2/users/1000
dataset_id: rdls_exp-eurac_householdcookingpractices
description: 'This Layer shows the share of fuels in the final energy consumption
  in the residential sector for coocking. The Frequency is annual. [Source: This metadata
  record was automatically extracted from the GeoNode portal eurac]'
details: 'title=Energy_consumption_in_households'' Title: ''Share of fuels in the
  final energy consumption in the residential sector for coocking'' Time frequency:
  ''Annual'' Unit of measure:''%'''
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
license: CC-BY-4.0
lineage:
  description: Data is take from the Eurostat is the Dataset available on Eurostat
    portal https://ec.europa.eu/eurostat/statistics-explained/index.php? The table
    is merged with the NUTS0 layer.
  sources:
  - id: source_1
    license: null
    name: Andrea Vianello
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/189
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Andrea Vianello
  url: https://maps.eurac.edu
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Household Cooking Practices (GML 2.0)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Acooking_household_gwh&outputFormat=gml2&srs=EPSG%3A4326
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
  description: Household Cooking Practices (GML 3.1.1)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Acooking_household_gwh&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
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
  description: Household Cooking Practices (CSV)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Acooking_household_gwh&outputFormat=csv&srs=EPSG%3A4326
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
  description: Household Cooking Practices (Excel)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Acooking_household_gwh&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_3
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
  description: Household Cooking Practices (JSON)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Acooking_household_gwh&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_4
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:cooking_household_gwh
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Household Cooking Practices (OGC WMS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:cooking_household_gwh&format=image%2Fpng
  format: null
  id: resource_5
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:cooking_household_gwh
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Household Cooking Practices (OGC WFS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:cooking_household_gwh&outputFormat=application%2Fjson
  format: null
  id: resource_6
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
  description: Household Cooking Practices (Zipped Shapefile)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Acooking_household_gwh&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
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
slug: rdls_exp-eurac_householdcookingpractices
spatial:
  bbox:
  - -31.2679100036621
  - 27.6384792327881
  - 44.8203735351562
  - 71.1841659545898
  centroid: null
  countries:
  - ALB
  - AND
  - AUT
  - BEL
  - BGR
  - BIH
  - BLR
  - CHE
  - CYP
  - CZE
  - DEU
  - DNK
  - ESP
  - EST
  - FIN
  - FRA
  - GBR
  - GRC
  - HRV
  - HUN
  - IRL
  - ISL
  - ITA
  - LIE
  - LTU
  - LUX
  - LVA
  - MCO
  - MDA
  - MKD
  - MLT
  - MNE
  - NLD
  - NOR
  - POL
  - PRT
  - ROU
  - RUS
  - SMR
  - SRB
  - SVK
  - SVN
  - SWE
  - UKR
  - VAT
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018'
  start: '2018'
temporal_resolution: null
title: Household Cooking Practices
version: null
vulnerability: null
---
