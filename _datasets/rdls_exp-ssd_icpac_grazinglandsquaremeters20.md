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
dataset_id: rdls_exp-ssd_icpac_grazinglandsquaremeters20
description: 'Grazing land map for South Sudan at 90 meters resolution (reference
  year: 2019). Each pixel represents the grazing land area in square meters. These
  data derive from ASAP rangeland mask (Version 03, Anomaly Hotspots of Agricultural
  Production, JRC) [Source: This metadata record was automatically extracted from
  the GeoNode portal icpac]'
details: null
exposure:
- asset_type: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
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
- href: https://geoportal.icpac.net/layers/ss_grazing_highres_area_def:geonode:ss_grazing_highres_area_def
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
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:ss_grazing_highres_area_def
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'South Sudan grazing land in square meters (2019) (OGC WMS: geonode
    Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:ss_grazing_highres_area_def&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:ss_grazing_highres_area_def
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'South Sudan grazing land in square meters (2019) (OGC WCS: geonode
    Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:ss_grazing_highres_area_def
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_icpac_grazinglandsquaremeters20
spatial:
  bbox:
  - 24.15208
  - 3.48042
  - 35.31875
  - 12.21875
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2019
  duration: null
  end: null
  start: null
temporal_resolution: null
title: South Sudan grazing land in square meters (2019)
version: null
vulnerability: null
---
