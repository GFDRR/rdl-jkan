---
attributions:
- entity:
    affiliation: null
    email: null
    name: DFAT
    url: https://data.humdata.org/dataset/health-facility-building-damage-status-as-of-28-may-2018
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CARDNO
    url: https://data.humdata.org/dataset/health-facility-building-damage-status-as-of-28-may-2018
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WHO
    url: https://data.humdata.org/dataset/health-facility-building-damage-status-as-of-28-may-2018
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NDOH
    url: https://data.humdata.org/dataset/health-facility-building-damage-status-as-of-28-may-2018
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ICRC
    url: https://data.humdata.org/dataset/health-facility-building-damage-status-as-of-28-may-2018
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UN in Papua New Guinea
  url: https://data.humdata.org/dataset/health-facility-building-damage-status-as-of-28-may-2018
creator:
  affiliation: null
  email: null
  name: UN in Papua New Guinea
  url: https://data.humdata.org/dataset/health-facility-building-damage-status-as-of-28-may-2018
dataset_id: rdls_el-png_unpng_healthfacilitybuildingdam_20180529
description: 'Health Facility Building Damage Status - data source from DFAT, CARDNO,
  WHO, NDOH and ICRC. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/health-facility-building-damage-status-as-of-28-may-2018]'
details: null
exposure:
- asset_type:
    description: Health facility building stock with structural damage assessment
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
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
  description: Health facility building damage status compiled from multi-agency assessments
    (DFAT, CARDNO, WHO, NDOH, ICRC) following a disaster event in Papua New Guinea.
    Data aggregates structural damage observations and operational status of health
    facilities into a registry format for humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: DFAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: CARDNO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: WHO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: NDOH
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: ICRC
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/health-facility-building-damage-status-as-of-28-may-2018
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage to health facilities from earthquake
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
  description: Papua New Guinea - Health Facility Building Damage Status (180528_Health
    Facility Status.xlsx)
  download_url: https://data.humdata.org/dataset/a957bea9-aaa3-44b2-85f2-a8534007bb7c/resource/1f4410a7-2795-439f-b464-8443a1c49d08/download/180528_health-facility-status.xlsx
  format: null
  id: resource_1f4410a7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 180528_Health Facility Status.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-png_unpng_healthfacilitybuildingdam_20180529
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
  start: '2018-05-29'
temporal_resolution: null
title: Papua New Guinea - Health Facility Building Damage Status
version: null
vulnerability: null
---
