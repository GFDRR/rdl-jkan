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
dataset_id: rdls_exp-uga_icpac_croplandsquaremeters2019
description: 'Crop land map for Uganda at 90 meters resolution (reference year: 2019).
  Each pixel represents the crop land area in square meters. These data derive from
  ASAP crop mask (Version 03, Anomaly Hotspots of Agricultural Production, JRC) [Source:
  This metadata record was automatically extracted from the GeoNode portal icpac]'
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
- href: https://geoportal.icpac.net/layers/ug_crop_highres_def:geonode:ug_crop_highres_def
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
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:ug_crop_highres_def
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Uganda cropland in square meters (2019) (OGC WMS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:ug_crop_highres_def&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:ug_crop_highres_def
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Uganda cropland in square meters (2019) (OGC WCS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:ug_crop_highres_def
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
slug: rdls_exp-uga_icpac_croplandsquaremeters2019
spatial:
  bbox:
  - 29.57125
  - -1.47875
  - 35.00042
  - 4.23458
  centroid: null
  countries:
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2019
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Uganda cropland in square meters (2019)
version: null
vulnerability: null
---
