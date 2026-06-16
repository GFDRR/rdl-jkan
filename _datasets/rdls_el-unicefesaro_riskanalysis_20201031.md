---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/eastern-and-southern-africa-risk-analysis
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FEWSNET
    url: https://data.humdata.org/dataset/eastern-and-southern-africa-risk-analysis
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/eastern-and-southern-africa-risk-analysis
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNICEF
    url: https://data.humdata.org/dataset/eastern-and-southern-africa-risk-analysis
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/eastern-and-southern-africa-risk-analysis
creator:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/eastern-and-southern-africa-risk-analysis
dataset_id: rdls_el-unicefesaro_riskanalysis_20201031
description: 'Eastern and Southern Africa Risk Analysis based on Inform, FEWSNET,
  OCHA, UNICEF and others. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/eastern-and-southern-africa-risk-analysis]'
details: null
exposure:
- asset_type:
    description: Agricultural land and crop production areas vulnerable to drought
      in Eastern and Southern Africa
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Population dependent on agriculture and food production in drought-affected
      regions
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
  description: Multi-source risk analysis integrating drought hazard indicators from
    FEWSNET, humanitarian impact data from OCHA, vulnerability indices from INFORM,
    and population exposure data from UNICEF to assess food security and displacement
    risks across Eastern and Southern Africa at country level.
  sources:
  - id: source_1
    license: null
    name: INFORM
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: FEWSNET
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: UNICEF
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/eastern-and-southern-africa-risk-analysis
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity and agricultural impact from drought in Eastern and
      Southern Africa
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
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement resulting from drought-induced food insecurity
      and livelihood loss
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
        type: indirect
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
  description: Eastern and Southern Africa Risk Analysis based on Inform, FEWSNET,
    OCHA, UNICEF and others
  download_url: https://data.humdata.org/dataset/271ef920-e9dd-43c5-9ad6-e6553d29347c/resource/1d4d976f-c1e0-4c1f-bbd7-164d6ca11426/download/unicef-esaro-risk-analysis-oct-2020.xlsx
  format: null
  id: resource_1d4d976f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNICEF ESARO RISK ANALYSIS - Oct 2020.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-unicefesaro_riskanalysis_20201031
spatial:
  bbox: null
  centroid: null
  countries:
  - AGO
  - BWA
  - COM
  - DZA
  - ERI
  - ETH
  - KEN
  - LSO
  - MDG
  - MOZ
  - MUS
  - MWI
  - NAM
  - RWA
  - SYC
  - SOM
  - ZAF
  - SSD
  - SWZ
  - TZA
  - UGA
  - ZMB
  - ZWE
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-10-31'
temporal_resolution: null
title: Eastern and Southern Africa Risk Analysis
version: null
vulnerability: null
---
