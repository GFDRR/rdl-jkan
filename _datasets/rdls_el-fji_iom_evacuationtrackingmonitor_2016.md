---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/fiji-evacuation-tracking-monitoring-cycle-2
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/fiji-evacuation-tracking-monitoring-cycle-2
dataset_id: rdls_el-fji_iom_evacuationtrackingmonitor_2016
description: 'Information Package for Fiji Evacuation Tracking & Monitoring Cycle
  2. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/fiji-evacuation-tracking-monitoring-cycle-2]'
details: null
exposure:
- asset_type:
    description: Evacuated population tracked across monitoring sites in Fiji
    id: population
    scheme: null
    title: null
    uri: null
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
  description: Census-based site assessment data collected by IOM during Fiji evacuation
    tracking and monitoring cycle 2, documenting displaced populations at evacuation
    sites and their humanitarian needs in response to cyclone impacts.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/fiji-evacuation-tracking-monitoring-cycle-2
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from cyclone evacuation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Fiji Evacuation Tracking & Monitoring Cycle 2 - Site Assessment data
    (Excel)
  download_url: https://data.humdata.org/dataset/c39e836e-8dc3-4b89-996a-c7a3d31cf50c/resource/f83b2f21-027d-4752-af7f-45f11f7293ef/download/etm-cycle-2-complete-dataset-sanitized.xlsx
  format: null
  id: resource_f83b2f21
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: etm-cycle-2-complete-dataset-sanitized
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Fiji Evacuation Tracking & Monitoring Cycle 2 - Site Assessment data
    (Fiji ETM Cycle2 Interactive Map.kmz)
  download_url: https://data.humdata.org/dataset/c39e836e-8dc3-4b89-996a-c7a3d31cf50c/resource/6bd2dcde-668c-48ad-aab0-c36faee87d38/download/fiji-etm-cycle2-interactive-map.kmz
  format: null
  id: resource_6bd2dcde
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Fiji ETM Cycle2 Interactive Map.kmz
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-fji_iom_evacuationtrackingmonitor_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - FJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-06-21'
  start: '2016-05-31'
temporal_resolution: null
title: Fiji Evacuation Tracking & Monitoring Cycle 2 - Site Assessment data
version: null
vulnerability: null
---
