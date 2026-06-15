---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP HungerMap
    url: https://data.humdata.org/dataset/wfp-hungermap-data-for-irq
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-irq
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-irq
dataset_id: rdls_lss-irq_wfp_hungermapdata_2024
description: 'HungerMapLIVE is the World Food Programme (WFP)''s global hunger monitoring
  system. It combines key metrics from various data sources - such as food security
  information, weather, population size, conflict, hazards, nutrition information
  and macro-economic data - to help assess, monitor and predict the magnitude and
  severity of hunger in near real-time. The resulting analysis is displayed on an
  interactive map that helps WFP staff, key decision makers and the broader humanitarian
  community to make more informed and timely decisions relating to food security.
  The platform covers 94 countries, including countries where WFP has operations as
  well as most lower and lower-middle income countries (as classified by the World
  Bank).. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wfp-hungermap-data-for-irq]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP's Hunger Monitoring Unit integrates real-time food security survey
    data, weather information, conflict events, and macro-economic indicators through
    machine learning models to estimate food insecurity prevalence and affected population
    counts at sub-national administrative levels in Iraq.
  sources:
  - id: source_1
    license: null
    name: WFP HungerMap
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp-hungermap-data-for-irq
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity prevalence and affected population from drought and
      food security stress
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
  description: Iraq - HungerMap data
  download_url: https://data.humdata.org/dataset/abb50e50-fddd-4891-a40a-8444e5121918/resource/00e4cab2-6726-4c93-a7bc-6ea3e381f71e/download/wfp-hungermap-data-for-irq.csv
  format: null
  id: resource_00e4cab2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-irq.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - HungerMap data long format
  download_url: https://data.humdata.org/dataset/abb50e50-fddd-4891-a40a-8444e5121918/resource/1d0b7732-b63d-4379-bd39-76466a18bfcf/download/wfp-hungermap-data-for-irq-long.csv
  format: null
  id: resource_1d0b7732
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-irq-long.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-irq_wfp_hungermapdata_2024
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
  end: '2024-10-05'
  start: '2024-05-04'
temporal_resolution: null
title: Iraq - HungerMap data
version: null
vulnerability: null
---
