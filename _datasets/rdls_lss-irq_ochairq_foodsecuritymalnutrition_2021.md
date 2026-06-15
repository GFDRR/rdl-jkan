---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP HungerMap LIVE
    url: https://data.humdata.org/dataset/food-security-malnutrition
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Iraq (inactive)
  url: https://data.humdata.org/dataset/food-security-malnutrition
creator:
  affiliation: null
  email: null
  name: OCHA Iraq (inactive)
  url: https://data.humdata.org/dataset/food-security-malnutrition
dataset_id: rdls_lss-irq_ochairq_foodsecuritymalnutrition_2021
description: 'Food Security Indicators for Iraq. The data is extracted from HungerMap
  LIVE Website.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/food-security-malnutrition]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Food security and malnutrition indicators are extracted manually from
    the WFP HungerMap LIVE platform and updated bi-weekly. The data represents population-level
    impact assessments of food insecurity and malnutrition conditions, primarily driven
    by drought and conflict-related disruptions to food systems.
  sources:
  - id: source_1
    license: null
    name: WFP HungerMap LIVE
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/food-security-malnutrition
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity and malnutrition prevalence in population affected
      by drought conditions
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://hungermap.wfp.org/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Food Security and malnutrition (Food Security)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTTYdtK7ggHdEGYmqh2ZnclChC-d6fN_KZVG2A2x0Cgs5DpGRTm35McZOG1h4L0OWs7dp6WboJX4pOw/pub?gid=1192665978&single=true&output=csv
  format: null
  id: resource_36f4e534
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Food Security
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - Food Security and malnutrition (Food Security & Malnutrition)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vTTYdtK7ggHdEGYmqh2ZnclChC-d6fN_KZVG2A2x0Cgs5DpGRTm35McZOG1h4L0OWs7dp6WboJX4pOw/pub?gid=1871189161&single=true&output=csv
  format: null
  id: resource_ce568bdb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Food Security & Malnutrition
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-irq_ochairq_foodsecuritymalnutrition_2021
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
  end: '2023-02-23'
  start: '2021-07-07'
temporal_resolution: null
title: Iraq - Food Security and malnutrition
version: null
vulnerability: null
---
