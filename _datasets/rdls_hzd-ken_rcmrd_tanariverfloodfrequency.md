---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Claire Maina
  url: https://geoportal.rcmrd.org/api/v2/users/1004
creator:
  affiliation: null
  email: null
  name: Claire Maina
  url: https://geoportal.rcmrd.org/api/v2/users/1004
dataset_id: rdls_hzd-ken_rcmrd_tanariverfloodfrequency
description: 'This dataset maps the frequency of past flood events across Tana River
  county, derived fromhistorical records and observations. It shows areas that have
  experienced recurrent flooding,helping identify flood-prone zones and prioritize
  mitigation actions.The data represents Tana River County''s flood frequency. [Source:
  This metadata record was automatically extracted from the GeoNode portal rcmrd]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: Claire Maina
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.rcmrd.org/catalogue/#/dataset/458
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Claire Maina
  url: https://geoportal.rcmrd.org
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Flood_Frequency2
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Tana River Flood Frequency (OGC WMS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:Flood_Frequency2&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Flood_Frequency2
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Tana River Flood Frequency (OGC WCS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__Flood_Frequency2
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
slug: rdls_hzd-ken_rcmrd_tanariverfloodfrequency
spatial:
  bbox:
  - 38.41249999999914
  - -3.070833333333659
  - 40.73749999999913
  - 0.004166666666324
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2024
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Tana River Flood Frequency
version: null
vulnerability: null
---
