---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP HungerMap
    url: https://data.humdata.org/dataset/wfp-hungermap-data-for-yem
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-yem
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-yem
dataset_id: rdls_lss-yem_wfp_hungermapdata_2025
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wfp-hungermap-data-for-yem]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP's Hunger Monitoring Unit integrates multiple data sources including
    food security surveys (FCS, RCSI), health and market access indicators, weather
    data, conflict information, and macro-economic indicators. Machine learning models
    estimate food security conditions in data-sparse areas. The resulting indicators
    (prevalence and affected population counts) are aggregated at administrative levels
    to monitor hunger severity in near real-time.
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
- href: https://data.humdata.org/dataset/wfp-hungermap-data-for-yem
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
  description: Yemen - HungerMap data
  download_url: https://data.humdata.org/dataset/6ff7ff93-5d58-41c4-877f-8939f2dda1eb/resource/3c5108fd-6614-420f-a2c7-da50be04dd08/download/wfp-hungermap-data-for-yem.csv
  format: null
  id: resource_3c5108fd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-yem.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Yemen - HungerMap data long format
  download_url: https://data.humdata.org/dataset/6ff7ff93-5d58-41c4-877f-8939f2dda1eb/resource/842dafc3-dcff-4637-8e72-295c07aeb044/download/wfp-hungermap-data-for-yem-long.csv
  format: null
  id: resource_842dafc3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-yem-long.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_wfp_hungermapdata_2025
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
  end: '2026-01-30'
  start: '2025-01-06'
temporal_resolution: null
title: Yemen - HungerMap data
version: null
vulnerability: null
---
