---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/uganda-subnational-displacement-forecasts
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/uganda-subnational-displacement-forecasts
creator:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/uganda-subnational-displacement-forecasts
dataset_id: rdls_lss-uga_drc_subnationaldisplacementfo_2025
description: 'Three-month settlement-level projections for South Sudanese refugees
  and asylum seekers in Uganda based on the AHEAD model. The files contain two types
  of values: ''observed'' values are drawn from official sources on the numbers of
  displaced in each area. ''forecasted'' values are model estimates of the next three
  months from the point of now.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/uganda-subnational-displacement-forecasts]'
details: The model structure treats the months with missing displacement data as additional
  parameters to be inferred and this allows us to work with datasets on displacement
  that contain gaps and missing information.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Settlement-level displacement data for South Sudanese refugees in Uganda
    were collected from official sources (UNHCR, DRC) and processed through a Bayesian
    state-space model (AHEAD) to generate three-month probabilistic forecasts with
    confidence bounds. The dataset contains both observed historical displacement
    counts and model-based projections for refugee populations across Ugandan settlements.
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
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/uganda-subnational-displacement-forecasts
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Forecasted displacement of South Sudanese refugees and asylum seekers
      in Uganda settlements
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Uganda - Subnational Displacement Forecasts (Uganda - Displacement
    forecasts Jan26-Mar26.xlsx)
  download_url: https://data.humdata.org/dataset/3ef38c14-9696-459d-9789-60049df190d0/resource/c52acd92-c907-4aaa-ac9d-96b6cb2ad035/download/uganda-displacement-forecasts-jan26-mar26.xlsx
  format: null
  id: resource_c52acd92
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Uganda - Displacement forecasts Jan26-Mar26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda - Subnational Displacement Forecasts (Uganda - Displacement
    forecasts Dec25-Feb26.xlsx)
  download_url: https://data.humdata.org/dataset/3ef38c14-9696-459d-9789-60049df190d0/resource/c26f05a5-2373-49cc-9daa-584f8a92abdc/download/uganda-displacement-forecasts-dec25-feb26.xlsx
  format: null
  id: resource_c26f05a5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Uganda - Displacement forecasts Dec25-Feb26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda - Subnational Displacement Forecasts (Uganda - Displacement
    forecasts Nov25-Jan26.xlsx)
  download_url: https://data.humdata.org/dataset/3ef38c14-9696-459d-9789-60049df190d0/resource/8656f7bf-413e-4a8c-8939-dc919fb65eeb/download/uganda-displacement-forecasts-nov25-jan26.xlsx
  format: null
  id: resource_8656f7bf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Uganda - Displacement forecasts Nov25-Jan26.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-uga_drc_subnationaldisplacementfo_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2025-11-01'
temporal_resolution: null
title: Uganda - Subnational Displacement Forecasts
version: null
vulnerability: null
---
