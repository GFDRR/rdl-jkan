---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: ICPAC
  url: https://geoportal.icpac.net/api/v2/users/1000
creator:
  affiliation: null
  email: null
  name: ICPAC
  url: https://geoportal.icpac.net/api/v2/users/1000
dataset_id: rdls_exp-ken_icpac_cattledensity
description: 'Dairy and zebu cattle density data done at the third administrative
  level and derived from the 1995-1997 division dairy and zebu cattle density reports
  from the Ministry of Agriculture, Livestock Development and Marketing. [Source:
  This metadata record was automatically extracted from the GeoNode portal icpac]'
details: null
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
- asset_type: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: currency
      unit: USD
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: ICPAC
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.icpac.net/layers/data0:geonode:ken_cattledensity
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: ICPAC
  url: https://geoportal.icpac.net
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:ken_cattledensity
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Kenya - Cattle Density (OGC WMS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:ken_cattledensity&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:ken_cattledensity
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Kenya - Cattle Density (OGC WFS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:ken_cattledensity&outputFormat=application%2Fjson
  format: null
  id: resource_1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ken_icpac_cattledensity
spatial:
  bbox:
  - 33.90958023071289
  - -4.674901008605957
  - 40.685951232910156
  - 2.695521116256714
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2017
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Kenya - Cattle Density
version: null
vulnerability: null
---
