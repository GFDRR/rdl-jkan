---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP HungerMap
    url: https://data.humdata.org/dataset/wfp-hungermap-data-for-ukr
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-ukr
creator:
  affiliation: null
  email: null
  name: WFP - World Food Programme
  url: https://data.humdata.org/dataset/wfp-hungermap-data-for-ukr
dataset_id: rdls_lss-ukr_wfp_hungermapdata_2025
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wfp-hungermap-data-for-ukr]'
details: null
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: WFP's Hunger Monitoring Unit integrates multiple real-time data sources
    including food consumption scores (FCS), reduced coping strategy indices (RCSI),
    health access, and market access indicators at sub-national administrative levels.
    Machine learning-based predictive models estimate food security conditions in
    data-sparse areas. The resulting prevalence and affected population counts represent
    indirect impacts of underlying hazards (drought, conflict) on food security status.
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
- href: https://data.humdata.org/dataset/wfp-hungermap-data-for-ukr
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
  description: Ukraine - HungerMap data
  download_url: https://data.humdata.org/dataset/20171cfa-489e-491b-a2e9-fcedad17b10e/resource/ad4e9b2b-027b-4031-8569-b55fe5bdec32/download/wfp-hungermap-data-for-ukr.csv
  format: null
  id: resource_ad4e9b2b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-ukr.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine - HungerMap data long format
  download_url: https://data.humdata.org/dataset/20171cfa-489e-491b-a2e9-fcedad17b10e/resource/5121696d-70f6-4417-a2e4-020bcf0bef9c/download/wfp-hungermap-data-for-ukr-long.csv
  format: null
  id: resource_5121696d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: wfp-hungermap-data-for-ukr-long.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ukr_wfp_hungermapdata_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-02-02'
  start: '2025-01-04'
temporal_resolution: null
title: Ukraine - HungerMap data
version: null
vulnerability: null
---
