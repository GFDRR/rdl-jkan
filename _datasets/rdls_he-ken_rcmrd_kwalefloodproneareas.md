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
dataset_id: rdls_he-ken_rcmrd_kwalefloodproneareas
description: 'This dataset indicates the geographic areas in Kwale County, that are
  particularly susceptible to flooding based on terrain, hydrology, and historical
  patterns. It provides a county-level view of potential flood hotspots for planning
  settlement development, infrastructure investment, and disaster risk reduction.
  [Source: This metadata record was automatically extracted from the GeoNode portal
  rcmrd]'
details: null
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
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
    - exposure
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.rcmrd.org/catalogue/#/dataset/464
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
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Flood_Prone_Areas0
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:32636
  description: 'Kwale Flood Prone Areas (OGC WMS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:Flood_Prone_Areas0&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Flood_Prone_Areas0
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:32636
  description: 'Kwale Flood Prone Areas (OGC WFS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:Flood_Prone_Areas0&outputFormat=application%2Fjson
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
- exposure
schema: rdls-10
slug: rdls_he-ken_rcmrd_kwalefloodproneareas
spatial:
  bbox:
  - 1148585.0976
  - -520034.88529999927
  - 1238900.0498000002
  - -396355.33220000006
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
title: Kwale Flood Prone Areas
version: null
vulnerability: null
---
