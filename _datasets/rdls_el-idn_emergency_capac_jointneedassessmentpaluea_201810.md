---
attributions:
- entity:
    affiliation: null
    email: null
    name: Emergency Capacity Building (ECB) Indonesia
    url: https://data.humdata.org/dataset/raw-data-of-joint-need-assessment-palu-earthquake-tsunami-28-september-2018
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Emergency Capacity Building (ECB) Indonesia (inactive)
  url: https://data.humdata.org/dataset/raw-data-of-joint-need-assessment-palu-earthquake-tsunami-28-september-2018
creator:
  affiliation: null
  email: null
  name: Emergency Capacity Building (ECB) Indonesia (inactive)
  url: https://data.humdata.org/dataset/raw-data-of-joint-need-assessment-palu-earthquake-tsunami-28-september-2018
dataset_id: rdls_el-idn_emergency_capac_jointneedassessmentpaluea_201810
description: 'excel data. link to the power BI dashboard Data live online: https://bit.ly/2RnUd7x.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/raw-data-of-joint-need-assessment-palu-earthquake-tsunami-28-september-2018]'
details: data collect from the period of October 3-8, 2018
exposure:
- asset_type:
    description: Building stock assessed in Palu affected by earthquake and tsunami
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
    description: Population in Palu assessed for needs following earthquake and tsunami
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
license: CC-BY-4.0
lineage:
  description: Joint needs assessment data collected via sample survey methodology
    in Palu, Indonesia following the September 2018 earthquake and tsunami. The dataset
    captures post-event impact information on buildings and population affected, compiled
    into an Excel database with live Power BI dashboard visualization for humanitarian
    response planning.
  sources:
  - id: source_1
    license: null
    name: Emergency Capacity Building (ECB) Indonesia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/raw-data-of-joint-need-assessment-palu-earthquake-tsunami-28-september-2018
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake in Palu
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tsunami in Palu
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: null
      trigger: null
      type: tsunami
    id: loss_2
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake in Palu
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by tsunami in Palu
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: null
      trigger: null
      type: tsunami
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Indonesia - Joint Need Assessment Palu Earthquake & Tsunami (Joint
    Need Assessment for Palu earthquake and tsunami.)
  download_url: https://data.humdata.org/dataset/d7339e25-c9d4-4df6-b2cc-14c5d4b68280/resource/d07fa84d-83c1-4d9e-9113-2ace48fc6575/download/raw-data_9oct.xlsx
  format: null
  id: resource_d07fa84d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: raw-data_9oct.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-idn_emergency_capac_jointneedassessmentpaluea_201810
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-10-08'
  start: '2018-10-03'
temporal_resolution: null
title: Indonesia - Joint Need Assessment Palu Earthquake & Tsunami
version: null
vulnerability: null
---
