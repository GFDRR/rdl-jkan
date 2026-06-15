---
attributions:
- entity:
    affiliation: null
    email: null
    name: Emergency Nutrition Coordination Unit (ENCU)
    url: https://data.humdata.org/dataset/ethiopia-nutrition-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-nutrition-0
creator:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-nutrition-0
dataset_id: rdls_lss-eth_ochaeth_hotspotworedas_20160330
description: 'Hotspot woreda classification is derived using six multisector indicators,
  including agriculture and nutrition, agreed at regional and federal levels. A hotspot
  matrix is often used as a proxy for the acute Integrated Phase Food Security Classification
  (IPC) and is indicative of food security and nutrition status. Hotspot woredas require
  urgent humanitarian response.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-nutrition-0]'
details: '**Languages:** EN'
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Hotspot woreda classification derived from six multisector indicators
    (agriculture, nutrition, health, education, markets, population) agreed at regional
    and federal levels. The hotspot matrix serves as a proxy for acute Integrated
    Phase Food Security Classification (IPC) to identify woredas with critical food
    security and nutrition vulnerabilities requiring urgent humanitarian intervention.
  sources:
  - id: source_1
    license: null
    name: Emergency Nutrition Coordination Unit (ENCU)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-nutrition-0
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity and nutrition vulnerability in drought-affected woredas
      classified via multisector indicators
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
  description: This table has a total of 443 woredas have been prioritized in three
    categories (priority 1, 2 and 3) by different sectors (Health, Nutrition, WASH,
    Agriculture, Market, Education, Child Protection & GBV).
  download_url: https://data.humdata.org/dataset/7cc9a5cc-91e8-4f3e-9b53-d4b399d775b0/resource/8b4e2e45-30da-4817-bc5f-a9ad58b82b2e/download/eth_hotspot_woredas_mar2016.xls
  format: null
  id: resource_8b4e2e45
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Eth_Hotspot_Woredas_Mar2016.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_ochaeth_hotspotworedas_20160330
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-03-30'
temporal_resolution: null
title: Ethiopia - Hot Spot Woredas
version: null
vulnerability: null
---
