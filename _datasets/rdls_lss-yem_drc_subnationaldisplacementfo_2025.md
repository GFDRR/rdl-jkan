---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/yemen-subnational-displacement-forecasts
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/yemen-subnational-displacement-forecasts
creator:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/yemen-subnational-displacement-forecasts
dataset_id: rdls_lss-yem_drc_subnationaldisplacementfo_2025
description: 'Displacement forecasts for Yemen at admin 2 level for the coming three
  month period based on the AHEAD model. The files contain two types of values: ''observed''
  values are drawn from official sources on the numbers of new displacements in each
  area. ''forecasted'' values are model estimates of the next three months from the
  point of now.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-subnational-displacement-forecasts]'
details: The model structure treats the months with missing displacement data as additional
  parameters to be inferred and this allows us to work with datasets on displacement
  that contain gaps and missing information.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Observed displacement data from Danish Refugee Council and IOM are
    integrated into a Bayesian state-space model (AHEAD) to generate probabilistic
    forecasts of new displacements at the district level for three-month periods.
    The model outputs include point estimates and uncertainty bounds (lower/upper
    bounds) for displacement counts.
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
- href: https://data.humdata.org/dataset/yemen-subnational-displacement-forecasts
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Forecasted internally displaced persons from conflict-driven displacement
      in Yemen
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
  description: Yemen - Subnational Displacement Forecasts (Yemen - Displacement forecasts
    Jan26-Mar26.xlsx)
  download_url: https://data.humdata.org/dataset/2c827065-1da3-4415-8f2b-53dafebcb1f6/resource/746d0cc6-b6e7-45ed-b118-c197227e28ea/download/yemen-displacement-forecasts-jan26-mar26.xlsx
  format: null
  id: resource_746d0cc6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Yemen - Displacement forecasts Jan26-Mar26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Yemen - Subnational Displacement Forecasts (Yemen - Displacement forecasts
    Dec25-Feb26.xlsx)
  download_url: https://data.humdata.org/dataset/2c827065-1da3-4415-8f2b-53dafebcb1f6/resource/1808d683-70ee-45bc-b436-3fac895b21c3/download/yemen-displacement-forecasts-dec25-feb26.xlsx
  format: null
  id: resource_1808d683
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Yemen - Displacement forecasts Dec25-Feb26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Yemen - Subnational Displacement Forecasts (Yemen - Displacement forecasts
    Nov25-Jan26.xlsx)
  download_url: https://data.humdata.org/dataset/2c827065-1da3-4415-8f2b-53dafebcb1f6/resource/5c91abc1-d452-46bb-9bf2-0bd33f628e5a/download/yemen-displacement-forecasts-nov25-jan26.xlsx
  format: null
  id: resource_5c91abc1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Yemen - Displacement forecasts Nov25-Jan26.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_drc_subnationaldisplacementfo_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2025-11-01'
temporal_resolution: null
title: Yemen - Subnational Displacement Forecasts
version: null
vulnerability: null
---
