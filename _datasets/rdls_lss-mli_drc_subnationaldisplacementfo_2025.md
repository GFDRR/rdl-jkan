---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/mali-subnational-displacement-forecasts
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/mali-subnational-displacement-forecasts
creator:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/mali-subnational-displacement-forecasts
dataset_id: rdls_lss-mli_drc_subnationaldisplacementfo_2025
description: 'Displacement forecasts for Mali at admin 1 level for the coming three
  month period based on the AHEAD model. The files contain three types of values:
  ''observed'' values are drawn from official sources on the numbers of displaced
  in each area. ''estimated'' values are model estimates of how displacement has evolved
  up until now, based on known values of conflict, food security, etc. ''forecasted''
  values are model estimates of the next three months from the point of now.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mali-subnational-displacement-forecasts]'
details: The model structure treats the months with missing displacement data as additional
  parameters to be inferred and this allows us to work with datasets on displacement
  that contain gaps and missing information.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Displacement data compiled from official sources (observed values)
    and processed through a Bayesian state-space model incorporating conflict and
    food security indicators to generate estimated historical and forecasted IDP numbers
    at admin-1 level for three-month forecast periods.
  sources:
  - id: source_1
    license: null
    name: Danish Refugee Council
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mali-subnational-displacement-forecasts
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons forecasted from conflict and food security
      drivers using Bayesian state-space model
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://danishrefugeecouncil.shinyapps.io/DRC_AHEAD_Dashboard/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mali - Subnational Displacement Forecasts (Mali - Displacement forecasts
    Jan26-Mar26.xlsx)
  download_url: https://data.humdata.org/dataset/79277aab-7bd9-4433-9bed-0eeca193db62/resource/30bd829e-757b-47f3-bfe9-ac7e2ed7421a/download/mali-displacement-forecasts-jan26-mar26.xlsx
  format: null
  id: resource_30bd829e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mali - Displacement forecasts Jan26-Mar26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mali - Subnational Displacement Forecasts (Mali - Displacement forecasts
    Deb25-Feb26.xlsx)
  download_url: https://data.humdata.org/dataset/79277aab-7bd9-4433-9bed-0eeca193db62/resource/01a9e36b-b543-47ca-a1f0-8d7b7077f216/download/mali-displacement-forecasts-deb25-feb26.xlsx
  format: null
  id: resource_01a9e36b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mali - Displacement forecasts Deb25-Feb26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mali - Subnational Displacement Forecasts (Mali - Displacement forecasts
    Nov25-Jan26.xlsx)
  download_url: https://data.humdata.org/dataset/79277aab-7bd9-4433-9bed-0eeca193db62/resource/d913da46-dc15-44b4-b315-e31cd1d5c4e4/download/mali-displacement-forecasts-nov25-jan26.xlsx
  format: null
  id: resource_d913da46
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mali - Displacement forecasts Nov25-Jan26.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_drc_subnationaldisplacementfo_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2025-11-01'
temporal_resolution: null
title: Mali - Subnational Displacement Forecasts
version: null
vulnerability: null
---
