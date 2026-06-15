---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ministry of Education (Yemen)
    url: https://data.humdata.org/dataset/affected-schools-in-yemen
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Education Cluster Yemen
  url: https://data.humdata.org/dataset/affected-schools-in-yemen
creator:
  affiliation: null
  email: null
  name: Education Cluster Yemen
  url: https://data.humdata.org/dataset/affected-schools-in-yemen
dataset_id: rdls_el-yem_edclyem_affectedschools_20170930
description: 'This dataset contains the location of affected schools by village, district,
  and governorate level. Includes number of students by gender, state of damage, school
  affected status, cause of damage, damage description, among other variables.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/affected-schools-in-yemen]'
details: null
exposure:
- asset_type:
    description: School facilities with location, structural characteristics, and
      damage state classification
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
- asset_type:
    description: Student population by gender attending affected schools
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: School damage registry compiled by the Ministry of Education and managed
    by the Education Cluster Yemen, documenting affected school locations, student
    populations by gender, damage state classifications, and damage causes through
    post-event facility assessments at village, district, and governorate administrative
    levels.
  sources:
  - id: source_1
    license: null
    name: Ministry of Education (Yemen)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/affected-schools-in-yemen
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct damage to school facilities from conflict-related violence
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
  description: Affected Schools at the Village Level in Yemen. (HXL tags)
  download_url: https://data.humdata.org/dataset/580a64d5-ac66-465a-857b-514a3b06d113/resource/af8d8c24-e947-4472-8c1b-d12cb5647495/download/affected-schools-update-september-2017.xlsx
  format: null
  id: resource_af8d8c24
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: affected-schools-update-september-2017.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Affected Schools at the Village Level in Yemen. This dataset contains
    the location of affected schools by village, district, and governorate level.
    Includes number of students by gender, state of damage, school affected status,
    cause of damage, damage description, among other variables.
  download_url: https://data.humdata.org/dataset/580a64d5-ac66-465a-857b-514a3b06d113/resource/fecc9135-7b3b-497f-b6e7-feae732e5c5b/download/affected-schools-update-september-2017.xlsx
  format: null
  id: resource_fecc9135
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Affected Schools Update (September-2017).xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-yem_edclyem_affectedschools_20170930
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
  start: '2017-09-30'
temporal_resolution: null
title: Affected Schools in Yemen
version: null
vulnerability: null
---
