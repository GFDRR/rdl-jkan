---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Hunger Monitoring Unit
    url: https://data.humdata.org/dataset/wfp-hungermap-data-for-syr
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-syr
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-syr
dataset_id: rdls_lss-syr_wfp_arabrepublichungermapdata_2025
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wfp-hungermap-data-for-syr]'
details: null
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: WFP's Hunger Monitoring Unit integrates multiple real-time food security
    data sources (FCS, RCSI, health/market access indicators) with machine learning-based
    predictive models to estimate food insecurity prevalence and affected populations
    at sub-national administrative levels in Syria, enabling near real-time monitoring
    of hunger severity.
  sources:
  - id: source_1
    license: null
    name: WFP Hunger Monitoring Unit
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wfp-hungermap-data-for-syr
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity prevalence and affected population from drought and
      conflict-driven food security deterioration
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
  description: Syrian Arab Republic - HungerMap data
  download_url: https://data.humdata.org/dataset/5be668ad-8702-4f89-a64d-69dfdaad4d98/resource/2a08c1c4-a951-40cd-8c2b-240e7b1df0d1/download/wfp-hungermap-data-for-syr.csv
  format: null
  id: resource_2a08c1c4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-syr.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Syrian Arab Republic - HungerMap data long format
  download_url: https://data.humdata.org/dataset/5be668ad-8702-4f89-a64d-69dfdaad4d98/resource/87759e84-0165-40bc-b3d3-103fa63cfbe8/download/wfp-hungermap-data-for-syr-long.csv
  format: null
  id: resource_87759e84
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-syr-long.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_wfp_arabrepublichungermapdata_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2025-01-06'
temporal_resolution: null
title: Syrian Arab Republic - HungerMap data
version: null
vulnerability: null
---
