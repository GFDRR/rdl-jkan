---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ministry of Disaster Management and Relief of the Government of Bangladesh
    url: https://data.humdata.org/dataset/inform-subnational-model-of-bangladesh
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: United Nations Resident Coordinator office in Bangladesh
    url: https://data.humdata.org/dataset/inform-subnational-model-of-bangladesh
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNDRR
    url: https://data.humdata.org/dataset/inform-subnational-model-of-bangladesh
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UN in Bangladesh
  url: https://data.humdata.org/dataset/inform-subnational-model-of-bangladesh
creator:
  affiliation: null
  email: null
  name: UN in Bangladesh
  url: https://data.humdata.org/dataset/inform-subnational-model-of-bangladesh
dataset_id: rdls_el-bgd_unbgd_informsubnationalmodel_2023
description: 'The Bangladesh INFORM model provides a solid baseline for risk indexing
  and monitoring in each of Bangladesh''s 64 districts (2nd administrative tier) and
  553 Upazilas and/or Thanas (3rd administrative tier). The index has been developed
  under coordination of Ministry of Disaster Management and Relief of the Government
  of Bangladesh and United Nations Resident Coordinator office in Bangladesh, with
  support from UNDRR.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/inform-subnational-model-of-bangladesh]'
details: null
exposure:
- asset_type:
    description: Subnational population exposure and vulnerability indexed across
      64 districts and 553 upazilas/thanas
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
      quantity_kind: index
      unit: null
- asset_type:
    description: Economic and development indicators contributing to risk assessment
      at district and upazila levels
    id: economic_indicator
    scheme: null
    title: null
    uri: null
  category: economic_indicator
  id: exposure_2
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: index
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: The INFORM subnational risk index for Bangladesh integrates hazard
    exposure, vulnerability, and coping capacity data at district and upazila administrative
    levels, developed through coordination between the Government of Bangladesh, UNRCO,
    and UNDRR. The index synthesizes direct observational data and anecdotal information
    to produce composite risk scores for 64 districts and 553 administrative subdivisions,
    enabling baseline risk monitoring and comparison across subnational geographies.
  sources:
  - id: source_1
    license: null
    name: Ministry of Disaster Management and Relief of the Government of Bangladesh
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: United Nations Resident Coordinator office in Bangladesh
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: UNDRR
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-subnational-model-of-bangladesh
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Modeled risk index combining hazard, exposure, and vulnerability
      for flood-prone populations
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Modeled risk index combining hazard, exposure, and vulnerability
      for earthquake-prone populations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  - asset_category: population
    asset_dimension: population
    description: Modeled risk index combining hazard, exposure, and vulnerability
      for cyclone-prone populations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The INFORM Risk Index for 2022 contains all the source data and the
    calculation steps for functional levels, categories, and dimensions on admin level
    2.
  download_url: https://data.humdata.org/dataset/78e579a9-9c34-4c05-b36d-78b68f9aebe8/resource/0dbe4cba-004a-4ee2-92e5-5cde09600a3e/download/inform_sub-national-risk-index-for-bangladesh_-2022_admin-level-2_v1.xlsx
  format: null
  id: resource_0dbe4cba
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_Sub-national Risk Index for Bangladesh_ 2022_Admin Level-2_V1.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The INFORM Risk Index for 2022 contains all the source data and the
    calculation steps for functional levels, categories, and dimensions on admin level
    3.
  download_url: https://data.humdata.org/dataset/78e579a9-9c34-4c05-b36d-78b68f9aebe8/resource/f3594557-45c8-4200-a1b6-83f75cb36fa3/download/inform_sub-national-risk-index-for-bangladesh_-2022_admin-level-3_v1.xlsx
  format: null
  id: resource_f3594557
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_Sub-national Risk Index for Bangladesh_ 2022_Admin Level 3_V1.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bgd_unbgd_informsubnationalmodel_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-05-01'
  start: '2023-05-01'
temporal_resolution: null
title: INFORM subnational model of Bangladesh
version: null
vulnerability: null
---
