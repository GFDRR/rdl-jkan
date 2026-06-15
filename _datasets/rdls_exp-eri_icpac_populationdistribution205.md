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
dataset_id: rdls_exp-eri_icpac_populationdistribution205
description: 'Population distribution for Eritrea at 90 meters resolution (2050).
  This layer contains the number of people per pixel and it is based on the population
  distribution data from WorldPop top-down modelling methods (https://www.worldpop.org/methods/populations)
  adjusted to match United Nations national population projection for 2050. [Source:
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
- href: https://geoportal.icpac.net/layers/er_pop_2050_unadj_constrained_def:geonode:er_pop_2050_unadj_constrained_def
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
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:er_pop_2050_unadj_constrained_def
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Eritrea population distribution for 2050 (OGC WMS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:er_pop_2050_unadj_constrained_def&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:er_pop_2050_unadj_constrained_def
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Eritrea population distribution for 2050 (OGC WCS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:er_pop_2050_unadj_constrained_def
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
slug: rdls_exp-eri_icpac_populationdistribution205
spatial:
  bbox:
  - 36.43875
  - 12.35708
  - 43.13792
  - 18.00625
  centroid: null
  countries:
  - ERI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2021
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Eritrea population distribution for 2050
version: null
vulnerability: null
---
