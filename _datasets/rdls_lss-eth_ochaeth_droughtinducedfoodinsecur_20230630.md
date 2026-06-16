---
attributions:
- entity:
    affiliation: null
    email: null
    name: Food Security Cluster
    url: https://data.humdata.org/dataset/ethiopia-targeted-populaton-food-cluster
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-targeted-populaton-food-cluster
creator:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-targeted-populaton-food-cluster
dataset_id: rdls_lss-eth_ochaeth_droughtinducedfoodinsecur_20230630
description: 'The dataset contains the number of people targeted by the food cluster
  in relation to drought in Ethiopia.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-targeted-populaton-food-cluster]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The Food Security Cluster aggregated multiple data sources and food
    security indicators to estimate the population affected by drought-induced food
    insecurity in Ethiopia. The dataset represents targeted beneficiaries requiring
    food assistance, derived from cluster-coordinated assessments and partner reporting.
  sources:
  - id: source_1
    license: null
    name: Food Security Cluster
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-targeted-populaton-food-cluster
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecure population targeted by food cluster response due to
      drought
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
        type: direct
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
  description: Ethiopia - Drought Induced Food Insecurity (Ethiopia Food Insecurity)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vRppQx8JTKkKRCKmzfnCMmTFEcvCpkbP9PdHs1sQTUyacmbsx8tlAXpgBLFce-lcehukreGGuXjA_4S/pub?gid=1859457158&single=true&output=csv
  format: null
  id: resource_f6f7f298
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ethiopia Food Insecurity
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_ochaeth_droughtinducedfoodinsecur_20230630
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
  start: '2023-06-30'
temporal_resolution: null
title: Ethiopia - Drought Induced Food Insecurity
version: null
vulnerability: null
---
