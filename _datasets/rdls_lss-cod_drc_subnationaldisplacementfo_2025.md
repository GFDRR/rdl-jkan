---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/democratic-republic-of-the-congo-subnational-displacement-forecasts
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/democratic-republic-of-the-congo-subnational-displacement-forecasts
creator:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/democratic-republic-of-the-congo-subnational-displacement-forecasts
dataset_id: rdls_lss-cod_drc_subnationaldisplacementfo_2025
description: 'Displacement forecasts for eastern Democratic Republic of the Congo
  at admin 2 level for the coming three month period based on the AHEAD model. The
  files contain three types of values: ''observed'' values are drawn from official
  sources on the numbers of displaced in each area. ''estimated'' values are model
  estimates of how displacement has evolved up until now, based on known values of
  conflict, food security, etc. ''forecasted'' values are model estimates of the next
  three months from the point of now.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/democratic-republic-of-the-congo-subnational-displacement-forecasts]'
details: The model structure treats the months with missing displacement data as additional
  parameters to be inferred and this allows us to work with datasets on displacement
  that contain gaps and missing information.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Observed IDP displacement counts from Danish Refugee Council and OCHA
    are integrated into a Bayesian state-space model that estimates current displacement
    evolution based on conflict and food security indicators, then generates probabilistic
    forecasts for the subsequent three-month period at admin-2 level.
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
    name: OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/democratic-republic-of-the-congo-subnational-displacement-forecasts
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Forecasted internally displaced persons from conflict in eastern
      Democratic Republic of the Congo
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
  description: Democratic Republic of the Congo - Subnational Displacement Forecasts
    (Eastern DR Congo - Displacement forecasts Jan26-Mar26.xlsx)
  download_url: https://data.humdata.org/dataset/fe805b93-c25c-4d23-badf-6da8430a77d0/resource/be1695ed-614c-480a-8463-cd9a5d55e56e/download/eastern-dr-congo-displacement-forecasts-jan26-mar26.xlsx
  format: null
  id: resource_be1695ed
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Eastern DR Congo - Displacement forecasts Jan26-Mar26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Democratic Republic of the Congo - Subnational Displacement Forecasts
    (Eastern DR Congo - Displacement forecasts Dec25-Feb26.xlsx)
  download_url: https://data.humdata.org/dataset/fe805b93-c25c-4d23-badf-6da8430a77d0/resource/d0bd6110-5c27-4c80-a58d-7554d34cd203/download/eastern-dr-congo-displacement-forecasts-dec25-feb26.xlsx
  format: null
  id: resource_d0bd6110
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Eastern DR Congo - Displacement forecasts Dec25-Feb26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Democratic Republic of the Congo - Subnational Displacement Forecasts
    (Eastern DR Congo - Displacement forecasts Nov25-Jan26.xlsx)
  download_url: https://data.humdata.org/dataset/fe805b93-c25c-4d23-badf-6da8430a77d0/resource/edcf5fb6-b981-46f6-83da-28777c78a63e/download/eastern-dr-congo-displacement-forecasts-nov25-jan26.xlsx
  format: null
  id: resource_edcf5fb6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Eastern DR Congo - Displacement forecasts Nov25-Jan26.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_drc_subnationaldisplacementfo_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2025-11-01'
temporal_resolution: null
title: Democratic Republic of the Congo - Subnational Displacement Forecasts
version: null
vulnerability: null
---
