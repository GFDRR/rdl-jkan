---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/nigeria-cdw-baseline-assessments-dec14-oct17
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/nigeria-cdw-baseline-assessments-dec14-oct17
dataset_id: rdls_el-nga_iom_nigeriacdwbaselineassessm_2014
description: 'Nigeria Baseline data from Dec 14 to Oct 17. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/nigeria-cdw-baseline-assessments-dec14-oct17]'
details: null
exposure:
- asset_type:
    description: Internally displaced persons and affected populations in Nigeria
      from baseline assessments
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
  description: IOM conducted sample survey-based baseline assessments of internally
    displaced persons across Nigeria from December 2014 to October 2017, documenting
    displacement counts and affected population characteristics through the Displacement
    Tracking Matrix methodology.
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
- href: https://data.humdata.org/dataset/nigeria-cdw-baseline-assessments-dec14-oct17
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flood-related displacement events
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nigeria_CDW_Baseline_Assessments_Dec14_Oct17 (Nigeria Baseline data
    from Dec 14 to Oct 17)
  download_url: https://data.humdata.org/dataset/ebb19588-8465-4507-8a14-e8b51038ca9f/resource/d7e53d2e-f613-4775-8c93-b73e241b5dca/download/nigeria_cdw_baseline_assessments_dec14_oct17.xlsx
  format: null
  id: resource_d7e53d2e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nigeria_CDW_Baseline_Assessments_Dec14_Oct17.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-nga_iom_nigeriacdwbaselineassessm_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2017-10-01'
  start: '2014-12-01'
temporal_resolution: null
title: Nigeria_CDW_Baseline_Assessments_Dec14_Oct17
version: null
vulnerability: null
---
