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
dataset_id: rdls_hzd-icpac_estimatedriskindexmultipl
description: 'This dataset includes an estimate of the regional risk induced by multiple
  hazards (tropical cyclone, flood and landslide induced by precipitations). Unit
  is estimated risk index from 1 (low) to 5 (extreme) [Source: This metadata record
  was automatically extracted from the GeoNode portal icpac]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: ICPAC
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.icpac.net/layers/estimated_risk_index_for_multiple_hazards:geonode:estimated_risk_index_for_multiple_hazards
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
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:estimated_risk_index_for_multiple_hazards
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'estimated_risk_index_for_multiple_hazards (OGC WMS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:estimated_risk_index_for_multiple_hazards&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:estimated_risk_index_for_multiple_hazards
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'estimated_risk_index_for_multiple_hazards (OGC WCS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:estimated_risk_index_for_multiple_hazards
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
- hazard
schema: rdls-10
slug: rdls_hzd-icpac_estimatedriskindexmultipl
spatial:
  bbox:
  - 21.838947
  - -11.745699999877004
  - 51.481733061948006
  - 23.14286
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: 2019
  duration: null
  end: null
  start: null
temporal_resolution: null
title: estimated_risk_index_for_multiple_hazards
version: null
vulnerability: null
---
