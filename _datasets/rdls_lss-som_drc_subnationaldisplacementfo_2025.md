---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM & UNHCR
    url: https://data.humdata.org/dataset/somalia-subnational-displacement-forecasts
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/somalia-subnational-displacement-forecasts
creator:
  affiliation: null
  email: null
  name: Danish Refugee Council
  url: https://data.humdata.org/dataset/somalia-subnational-displacement-forecasts
dataset_id: rdls_lss-som_drc_subnationaldisplacementfo_2025
description: 'Displacement forecasts for Somalia at admin 2 level for the coming three
  month period based on the AHEAD model. The files contain two types of values: ''data''
  values are drawn from official sources on the numbers of displaced in each area.
  ''model'' values are model estimates of how displacement is projected to evolve
  in the next three to four months from the point of now.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/somalia-subnational-displacement-forecasts]'
details: The model structure treats the months with missing displacement data as additional
  parameters to be inferred and this allows us to work with datasets on displacement
  that contain gaps and missing information.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Official IDP counts from IOM and UNHCR are integrated into a Bayesian
    state-space model (AHEAD) to generate probabilistic forecasts of displacement
    evolution over 3-4 month horizons. Displacement is disaggregated by triggering
    hazard type (conflict, drought, flood) at Somalia admin 2 (district) level, with
    model outputs including point estimates and confidence intervals.
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
    name: IOM & UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-subnational-displacement-forecasts
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Conflict-induced internal displacement forecasts at admin 2 level
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
  - asset_category: population
    asset_dimension: population
    description: Drought-induced internal displacement forecasts at admin 2 level
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
  - asset_category: population
    asset_dimension: population
    description: Flood-induced internal displacement forecasts at admin 2 level
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
  description: Somalia - Subnational Displacement Forecasts (Somalia - Displacement
    forecasts Dec25 + Q1 26.xlsx)
  download_url: https://data.humdata.org/dataset/ebf888df-66b6-4a2f-ae4f-de777eb52c20/resource/3c1f4304-bd71-430e-9619-2a85b98f4db1/download/somalia-displacement-forecasts-dec25-q1-26.xlsx
  format: null
  id: resource_3c1f4304
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia - Displacement forecasts Dec25 + Q1 26.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Subnational Displacement Forecasts (Somalia - Displacement
    forecasts Q4 2025.xlsx)
  download_url: https://data.humdata.org/dataset/ebf888df-66b6-4a2f-ae4f-de777eb52c20/resource/a2682b8e-1d6e-4fde-a4be-2304ac04bbc9/download/somalia-displacement-forecasts-q4-2025.xlsx
  format: null
  id: resource_a2682b8e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia - Displacement forecasts Q4 2025.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_drc_subnationaldisplacementfo_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2025-09-01'
temporal_resolution: null
title: Somalia - Subnational Displacement Forecasts
version: null
vulnerability: null
---
