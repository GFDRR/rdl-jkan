---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Iraq
    url: https://data.humdata.org/dataset/dtm-iraq
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/dtm-iraq
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/dtm-iraq
dataset_id: rdls_el-irq_iom_dtmdatasetround33baseline_20151130
description: 'The DTM continually tracks and monitors displacement across Iraq allowing
  IOM to identify the locations to which IDPs have chosen to settle. The location
  and population of these IDPs are recorded and further in-depth assessments are conducted
  to identify the multi-sectorial needs of the displaced. Displacement data are presented
  on interactive maps below. Using the tabs you can check location based Displacements
  of 2014 starting from Governorates, Districts to location level. Plus, Accumulative
  development of displacement month by month until today.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/dtm-iraq]'
details: null
exposure:
- asset_type:
    description: Internally displaced persons (IDPs) population by location, governorate,
      and district across Iraq
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
license: CC-BY-4.0
lineage:
  description: IOM DTM (Displacement Tracking Matrix) Round 33 baseline dataset compiled
    from direct observational field assessments tracking IDP settlement locations
    and populations across Iraq since 2014. Data were collected through anecdotal
    and direct observation methods and aggregated by administrative level (governorate,
    district, location) with monthly accumulative tracking to establish baseline displacement
    patterns.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Iraq
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/dtm-iraq
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displacement counts of internally displaced persons from conflict
      in Iraq
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - IOM DTM Dataset Round 33 - Baseline data (Round 33 November
    2015)
  download_url: https://data.humdata.org/dataset/bf698220-d6f3-4706-9a6a-f32a1cd3041c/resource/f3674615-3096-444d-b6d8-bc3606e229c6/download/20151130_01_iom_dtm_publish_master_list.xlsx
  format: null
  id: resource_f3674615
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20151130_01_IOM_DTM_Publish_Master_List.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-irq_iom_dtmdatasetround33baseline_20151130
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-30'
temporal_resolution: null
title: Iraq - IOM DTM Dataset Round 33 - Baseline data
version: null
vulnerability: null
---
