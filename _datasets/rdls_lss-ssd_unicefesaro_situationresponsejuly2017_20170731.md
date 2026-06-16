---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNICEF Country Office Situation Report
    url: https://data.humdata.org/dataset/unicef-south-sudan-situation-and-response-31-july-2017
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FEWSNET Food Security Classification
    url: https://data.humdata.org/dataset/unicef-south-sudan-situation-and-response-31-july-2017
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNOCHA
    url: https://data.humdata.org/dataset/unicef-south-sudan-situation-and-response-31-july-2017
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/unicef-south-sudan-situation-and-response-31-july-2017
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/unicef-south-sudan-situation-and-response-31-july-2017
creator:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/unicef-south-sudan-situation-and-response-31-july-2017
dataset_id: rdls_lss-ssd_unicefesaro_situationresponsejuly2017_20170731
description: 'This infographics is about South Sudan Situation and needs. It also
  shown UNICEF targets/results and HAC Funding as of 31 July 2017. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unicef-south-sudan-situation-and-response-31-july-2017]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Situation report aggregating food security classifications from FEWSNET,
    displacement data from IOM, and humanitarian needs assessments from UNICEF CO
    and UNOCHA as of July 2017 to document the humanitarian impact of drought-driven
    food insecurity in South Sudan.
  sources:
  - id: source_1
    license: null
    name: UNICEF Country Office Situation Report
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: FEWSNET Food Security Classification
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: UNOCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unicef-south-sudan-situation-and-response-31-july-2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by food insecurity classified by IPC phase
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
    description: Internally displaced persons from drought-related food insecurity
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
  description: Excel Database relating to UNICEF South Sudan Situation and Response
    Infographics
  download_url: https://data.humdata.org/dataset/c92c5884-7009-490b-be50-82f50d2a2ee3/resource/974b46a0-400f-4704-a309-df03ed96daf5/download/regional-db_aug16-esaro.xlsx
  format: null
  id: resource_974b46a0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Regional db_aug16- ESARO.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_unicefesaro_situationresponsejuly2017_20170731
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-07-31'
temporal_resolution: null
title: UNICEF South Sudan Situation and Response July 2017
version: null
vulnerability: null
---
