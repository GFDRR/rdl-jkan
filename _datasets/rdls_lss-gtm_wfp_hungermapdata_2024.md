---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP HungerMap
    url: https://data.humdata.org/dataset/wfp-hungermap-data-for-gtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-gtm
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-gtm
dataset_id: rdls_lss-gtm_wfp_hungermapdata_2024
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wfp-hungermap-data-for-gtm]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP's Hunger Monitoring Unit conducts real-time food security monitoring
    using observed data from multiple sources (food security surveys, weather, conflict,
    hazards, nutrition, economic indicators). Machine learning-based predictive models
    estimate food security conditions in data-sparse areas. The resulting indicators
    (FCS, RCSI, health access, market access prevalence) are aggregated at administrative
    levels to monitor hunger magnitude and severity.
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
- href: https://data.humdata.org/dataset/wfp-hungermap-data-for-gtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity prevalence and affected population from drought and
      other hazards affecting food security
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
  description: Guatemala - HungerMap data
  download_url: https://data.humdata.org/dataset/70ddaacb-b379-4920-9e42-64e620683414/resource/42359b49-fd4d-40cf-acf8-d5f2a67d1261/download/wfp-hungermap-data-for-gtm.csv
  format: null
  id: resource_42359b49
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-gtm.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Guatemala - HungerMap data long format
  download_url: https://data.humdata.org/dataset/70ddaacb-b379-4920-9e42-64e620683414/resource/955553bc-e892-47df-9da6-812b0ac1ee47/download/wfp-hungermap-data-for-gtm-long.csv
  format: null
  id: resource_955553bc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-gtm-long.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_wfp_hungermapdata_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-25'
  start: '2024-12-04'
temporal_resolution: null
title: Guatemala - HungerMap data
version: null
vulnerability: null
---
