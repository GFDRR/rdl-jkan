---
attributions:
- entity:
    affiliation: null
    email: null
    name: Fews.net IPC and Livelihoods
    url: https://data.humdata.org/dataset/haiti-population-food-security-outlook-and-livelihood-zones-by-admin-3-for-september-2016
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/haiti-population-food-security-outlook-and-livelihood-zones-by-admin-3-for-september-2016
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CNIGS Administrative Boundaries
    url: https://data.humdata.org/dataset/haiti-population-food-security-outlook-and-livelihood-zones-by-admin-3-for-september-2016
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/haiti-population-food-security-outlook-and-livelihood-zones-by-admin-3-for-september-2016
creator:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/haiti-population-food-security-outlook-and-livelihood-zones-by-admin-3-for-september-2016
dataset_id: rdls_el-hti_hdx_foodsecurityoutlookliveli_20160930
description: 'This dataset contains the integrated phase classification (IPC) for
  September 2016, and livelihood zones for Haiti, extracted to each administrative
  level 3 unit (sections). It also contains the population for each admin 3 unit based
  on WorldPop (2015 v2b UN adjusted). Source datasets: IPC and Livelihoods Administrative
  Boundaries (version released 6-Oct-2016). [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/haiti-population-food-security-outlook-and-livelihood-zones-by-admin-3-for-september-2016]'
details: null
exposure:
- asset_type:
    description: Residential population by administrative level 3 unit based on WorldPop
      2015 v2b UN adjusted
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: IPC food security classifications and livelihood zone attributes were
    extracted via spatial join from Fews.net source data to Haiti administrative level
    3 polygons. Population estimates were derived as zonal sums of WorldPop gridded
    population density (2015 v2b UN adjusted) within each admin 3 unit. The integrated
    dataset provides food security outlook and population exposure by livelihood zone
    at the section administrative level.
  sources:
  - id: source_1
    license: null
    name: Fews.net IPC and Livelihoods
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: CNIGS Administrative Boundaries
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-population-food-security-outlook-and-livelihood-zones-by-admin-3-for-september-2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Food insecurity classification (IPC) for population by livelihood
      zone
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
  description: Haiti Food Security Outlook, and Livelihood Zones by Admin 3 for September
    2016 (CSV)
  download_url: https://data.humdata.org/dataset/c61c7d46-0f42-44b4-9d39-142e5a1d4b19/resource/947d4b2d-93e7-44ba-a468-7c99a1a091f0/download/hti_ipc2016ml1_livelihoods_adm3.csv
  format: null
  id: resource_947d4b2d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_ipc2016ML1_livelihoods_adm3.csv
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-hti_hdx_foodsecurityoutlookliveli_20160930
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-09-30'
temporal_resolution: null
title: Haiti Food Security Outlook, and Livelihood Zones by Admin 3 for September
  2016
version: null
vulnerability: null
---
