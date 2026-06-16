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
dataset_id: rdls_hzd-ken_rcmrd_kilififloodprevalence
description: 'The flood prevalence dataset quantifies the proportion of areas within
  kilifi that have historically been affected by flooding. It is useful for understanding
  the extent of communities impacted and guiding targeted interventions. [Source:
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
- href: https://geoportal.rcmrd.org/catalogue/#/dataset/470
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
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Flood_Prevalence2
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:32636
  description: 'Kilifi Flood Prevalence (OGC WMS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:Flood_Prevalence2&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Flood_Prevalence2
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:32636
  description: 'Kilifi Flood Prevalence (OGC WFS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:Flood_Prevalence2&outputFormat=application%2Fjson
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
- hazard
schema: rdls-10
slug: rdls_hzd-ken_rcmrd_kilififloodprevalence
spatial:
  bbox:
  - 1177321.2144
  - -444481.8443
  - 1307450.3628000002
  - -257106.54649999924
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
title: Kilifi Flood Prevalence
version: null
vulnerability: null
---
