---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP HungerMap
    url: https://data.humdata.org/dataset/wfp-hungermap-data-for-tcd
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-tcd
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-tcd
dataset_id: rdls_lss-tcd_wfp_hungermapdata_20240105
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wfp-hungermap-data-for-tcd]'
details: null
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: WFP's Hunger Monitoring Unit conducts real-time food security monitoring
    using observed data from multiple sources (food security surveys, weather, conflict,
    nutrition) and machine learning-based predictive models to estimate food security
    status and prevalence indicators (FCS, RCSI, health access, market access) at
    administrative levels in Chad.
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
- href: https://data.humdata.org/dataset/wfp-hungermap-data-for-tcd
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
  description: Chad - HungerMap data
  download_url: https://data.humdata.org/dataset/33b6ad8d-8b90-4fc6-a6b6-299bbb0f6eaf/resource/9f946773-77ca-46eb-b414-0b338e48e993/download/wfp-hungermap-data-for-tcd.csv
  format: null
  id: resource_9f946773
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-tcd.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - HungerMap data long format
  download_url: https://data.humdata.org/dataset/33b6ad8d-8b90-4fc6-a6b6-299bbb0f6eaf/resource/a954ee22-9be6-4f52-bba3-e3497212faa3/download/wfp-hungermap-data-for-tcd-long.csv
  format: null
  id: resource_a954ee22
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-tcd-long.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tcd_wfp_hungermapdata_20240105
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-01-05'
temporal_resolution: null
title: Chad - HungerMap data
version: null
vulnerability: null
---
