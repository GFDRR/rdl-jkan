---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP HungerMap
    url: https://data.humdata.org/dataset/wfp-hungermap-data-for-mrt
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-mrt
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-mrt
dataset_id: rdls_lss-mrt_wfp_hungermapdata_202403
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wfp-hungermap-data-for-mrt]'
details: null
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: WFP's Hunger Monitoring Unit conducts real-time food security monitoring
    using observed data from multiple sources (food security surveys, weather, conflict,
    nutrition) and machine learning-based predictive models to estimate food security
    status and prevalence indicators (FCS, RCSI, health access, market access) at
    administrative levels in Mauritania.
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
- href: https://data.humdata.org/dataset/wfp-hungermap-data-for-mrt
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity prevalence and affected population from drought and
      food security crises
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mauritania - HungerMap data
  download_url: https://data.humdata.org/dataset/6fe5ad08-aa68-4fed-89fd-733d6d7a1748/resource/40b1bdc7-f756-4d29-ba20-5080e8bed33a/download/wfp-hungermap-data-for-mrt.csv
  format: null
  id: resource_40b1bdc7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-mrt.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mauritania - HungerMap data long format
  download_url: https://data.humdata.org/dataset/6fe5ad08-aa68-4fed-89fd-733d6d7a1748/resource/9c617d00-7ba7-4920-be4c-a576cc310a1a/download/wfp-hungermap-data-for-mrt-long.csv
  format: null
  id: resource_9c617d00
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-mrt-long.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mrt_wfp_hungermapdata_202403
spatial:
  bbox: null
  centroid: null
  countries:
  - MRT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-03-18'
  start: '2024-03-11'
temporal_resolution: null
title: Mauritania - HungerMap data
version: null
vulnerability: null
---
