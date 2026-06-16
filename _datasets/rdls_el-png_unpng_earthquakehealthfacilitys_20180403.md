---
attributions:
- entity:
    affiliation: null
    email: null
    name: WHO
    url: https://data.humdata.org/dataset/papua-new-guinea-earthquake-health-facility-status
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NDOH
    url: https://data.humdata.org/dataset/papua-new-guinea-earthquake-health-facility-status
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UN in Papua New Guinea
  url: https://data.humdata.org/dataset/papua-new-guinea-earthquake-health-facility-status
creator:
  affiliation: null
  email: null
  name: UN in Papua New Guinea
  url: https://data.humdata.org/dataset/papua-new-guinea-earthquake-health-facility-status
dataset_id: rdls_el-png_unpng_earthquakehealthfacilitys_20180403
description: 'Papua New Guinea Earthquake Health Facility Status as of 3 April 2018.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/papua-new-guinea-earthquake-health-facility-status]'
details: null
exposure:
- asset_type:
    description: Health facility infrastructure and operational status
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Health facility status data collected by WHO and Papua New Guinea's
    National Department of Health following the April 2018 earthquake, documenting
    facility-level damage and operational impacts through post-event assessment and
    registry updates.
  sources:
  - id: source_1
    license: null
    name: WHO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: NDOH
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/papua-new-guinea-earthquake-health-facility-status
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to health facilities from earthquake ground motion
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Papua New Guinea Earthquake Health Facility Status_030418.xlsx
  download_url: https://data.humdata.org/dataset/3f3b4b2f-60c8-4d03-ac74-aa7fd606b0d7/resource/06305035-6d3b-4ea0-8947-9e394ff0d644/download/png-earthquake-health-facility-status_030418.xlsx
  format: null
  id: resource_06305035
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Papua New Guinea Earthquake Health Facility Status_030418.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-png_unpng_earthquakehealthfacilitys_20180403
spatial:
  bbox: null
  centroid: null
  countries:
  - PNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-04-03'
temporal_resolution: null
title: Papua New Guinea Earthquake Health Facility Status
version: null
vulnerability: null
---
