---
attributions:
- entity:
    affiliation: null
    email: null
    name: Government of Sudan (HAC)
    url: https://data.humdata.org/dataset/sudan-floods-27th-of-october-2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-floods-27th-of-october-2019
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-floods-27th-of-october-2019
dataset_id: rdls_lss-sdn_ochasdn_floods27thoctober2019_20191027
description: 'This excel sheet is from the government of Sudan (HAC) as of 27th of
  October 2019.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-floods-27th-of-october-2019]'
details: This data will be updated whenever there are new figures from the government
  of Sudan.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event impact data collected by the Government of Sudan's Humanitarian
    Aid Commission following the 27 October 2019 flooding event. The dataset contains
    direct impact records (affected population and building damage) compiled from
    government sources and provided to OCHA Sudan.
  sources:
  - id: source_1
    license: null
    name: Government of Sudan (HAC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-floods-27th-of-october-2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct population impact from flooding event on 27 October 2019
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding event on 27 October 2019
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is the Floods updated until the 27th of October 2019. The source
    is from government of Sudan (HAC).
  download_url: https://data.humdata.org/dataset/66ce8a8e-6f24-4beb-b880-4c3b31e87453/resource/5321ad89-3cb6-46c8-b5db-1be53895460b/download/floods_impact_27oct19.xlsx
  format: null
  id: resource_5321ad89
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Floods_Impact_27Oct19.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ochasdn_floods27thoctober2019_20191027
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-27'
temporal_resolution: null
title: Sudan Floods 27th of October 2019
version: null
vulnerability: null
---
