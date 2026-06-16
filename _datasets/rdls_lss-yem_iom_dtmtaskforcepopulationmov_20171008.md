---
attributions:
- entity:
    affiliation: null
    email: null
    name: Inter-Cluster Coordination Mechanism (ICCM)
    url: https://data.humdata.org/dataset/dtm-task-force-on-population-movement-tfpm-yemen-16th-report-october-2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/dtm-task-force-on-population-movement-tfpm-yemen-16th-report-october-2017
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/dtm-task-force-on-population-movement-tfpm-yemen-16th-report-october-2017
dataset_id: rdls_lss-yem_iom_dtmtaskforcepopulationmov_20171008
description: 'The Task Force for Population Movement (TFPM) is a Technical Working
  Group to the Inter-Cluster Coordination Mechanism. (ICCM) The TFPM implements an
  information management tool that gathers data and location of displaced persons
  across Yemen. As of 01 Sep 2017, the TFPM has identified, 2,014,026 internally displaced
  persons (IDPs) (335,671 households) who have been displaced due to conflict since
  March 2015, dispersed across 21 governorates. For the same period, the TFPM has
  identified 956,076 returnees (159,346 households), across 20 governorates. As a
  result, 10.3% of the total population of Yemen has experienced the shock of displacement
  due to conflict in the last 30 months. The data collected is a compilation of data
  collection activities conducted through the period of May to August 2018. The data
  presents the best estimates of displacement and returnee movements in locations
  across Yemen.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/dtm-task-force-on-population-movement-tfpm-yemen-16th-report-october-2017]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The TFPM compiled displacement and returnee data from field data collection
    activities conducted May-August 2017 across Yemen governorates. Data represents
    best estimates of population movement locations and counts derived from multi-agency
    coordination and on-the-ground monitoring of internally displaced persons and
    returnee populations.
  sources:
  - id: source_1
    license: null
    name: Inter-Cluster Coordination Mechanism (ICCM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/dtm-task-force-on-population-movement-tfpm-yemen-16th-report-october-2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons due to conflict in Yemen since March
      2015
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Returnee populations across Yemen governorates
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: TASK FORCE ON POPULATION MOVEMENT | TFPM YEMEN | 16th Report - October
    2017 The Task Force for Population Movement (TFPM) is a Technical Working Group
    to the Inter-Cluster Coordination Mechanism. (ICCM) The TFPM implements an information
    management tool that gathers data and location of displaced persons across Yemen.
  download_url: https://data.humdata.org/dataset/51e83597-474d-40d7-bdd6-15ea4c9986b9/resource/c2e7482b-ff22-42c2-a4ab-0d308bcdebda/download/annex1_tfpm_16th_dataset_oct2017.xlsb
  format: null
  id: resource_c2e7482b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: annex1_tfpm_16th_dataset_oct2017.xlsb
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_iom_dtmtaskforcepopulationmov_20171008
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-08'
temporal_resolution: null
title: 'DTM: Task Force on Population Movement | TFPM Yemen | 16th Report - October
  2017'
version: null
vulnerability: null
---
