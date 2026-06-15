---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/south-sudan-subnational-displacement-forecasts
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/south-sudan-subnational-displacement-forecasts
creator:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/south-sudan-subnational-displacement-forecasts
dataset_id: rdls_lss-ssd_drc_subnationaldisplacementfo_2025
description: 'Displacement forecasts for South Sudan at admin 2 level for the coming
  three month period based on the AHEAD model. The files contain three types of values:
  ''observed'' values are drawn from official sources on the numbers of displaced
  in each area. ''estimated'' values are model estimates of how displacement has evolved
  up until now, based on known values of conflict, food security, etc. ''forecasted''
  values are model estimates of the next three months from the point of now.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-subnational-displacement-forecasts]'
details: The model structure treats the months with missing displacement data as additional
  parameters to be inferred and this allows us to work with datasets on displacement
  that contain gaps and missing information.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Observed IDP counts from Danish Refugee Council and IOM are input to
    a Bayesian state-space model (AHEAD) that estimates current displacement evolution
    based on conflict and food security indicators, then generates probabilistic forecasts
    for the subsequent three-month period with uncertainty bounds.
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
- href: https://data.humdata.org/dataset/south-sudan-subnational-displacement-forecasts
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Forecasted internally displaced persons from conflict-driven displacement
      using Bayesian state-space model
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
  description: South Sudan - Subnational Displacement Forecasts (South Sudan - Displacement
    forecasts Jan26-Mar26.xlsx)
  download_url: https://data.humdata.org/dataset/be3c828d-ae53-46cb-93de-176083bb8f80/resource/e1056a11-f88e-4b51-b786-e05c778339ed/download/south-sudan-displacement-forecasts-jan26-mar26.xlsx
  format: null
  id: resource_e1056a11
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: South Sudan - Displacement forecasts Jan26-Mar26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan - Subnational Displacement Forecasts (South Sudan - Displacement
    forecasts Dec25-Feb26.xlsx)
  download_url: https://data.humdata.org/dataset/be3c828d-ae53-46cb-93de-176083bb8f80/resource/9c051539-10c2-41cf-a510-4ff06aee1b2e/download/south-sudan-displacement-forecasts-dec25-feb26.xlsx
  format: null
  id: resource_9c051539
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: South Sudan - Displacement forecasts Dec25-Feb26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan - Subnational Displacement Forecasts (South Sudan - Displacement
    forecasts Nov25-Jan26.xlsx)
  download_url: https://data.humdata.org/dataset/be3c828d-ae53-46cb-93de-176083bb8f80/resource/60ab8762-e994-49a9-ad30-3d381ceb7001/download/south-sudan-displacement-forecasts-nov25-jan26.xlsx
  format: null
  id: resource_60ab8762
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: South Sudan - Displacement forecasts Nov25-Jan26.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_drc_subnationaldisplacementfo_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2025-11-01'
temporal_resolution: null
title: South Sudan - Subnational Displacement Forecasts
version: null
vulnerability: null
---
