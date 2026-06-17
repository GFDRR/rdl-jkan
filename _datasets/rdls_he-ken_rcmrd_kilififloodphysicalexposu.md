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
dataset_id: rdls_he-ken_rcmrd_kilififloodphysicalexposu
description: 'This dataset represents the spatial extent of areas in Kilifi county
  that are physically exposed to flooding. It highlights locations where the natural
  environment, infrastructure, and communities are vulnerable to direct flood impacts,
  providing a baseline for disaster preparedness and land-use planning. [Source: This
  metadata record was automatically extracted from the GeoNode portal rcmrd]'
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
- asset_type: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
    - exposure
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.rcmrd.org/catalogue/#/dataset/467
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
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Flood_Physical_Exposure4
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Kilifi Flood Physical Exposure (OGC WMS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:Flood_Physical_Exposure4&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.rcmrd.org/datasets/geonode:Flood_Physical_Exposure4
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Kilifi Flood Physical Exposure (OGC WCS: geonode Service)'
  download_url: https://geoportal.rcmrd.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__Flood_Physical_Exposure4
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
- exposure
schema: rdls-10
slug: rdls_he-ken_rcmrd_kilififloodphysicalexposu
spatial:
  bbox:
  - 39.04166666657907
  - -4.000000000034365
  - 40.29166666657856
  - -2.29166666670173
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
title: Kilifi Flood Physical Exposure
version: null
vulnerability: null
---
