---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/colombia-retornados-por-desplazamiento
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/colombia-retornados-por-desplazamiento
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/colombia-retornados-por-desplazamiento
dataset_id: rdls_lss-col_ochacol_retornadospordesplazamien_2021
description: 'Retornados por desplazamiento forzado. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/colombia-retornados-por-desplazamiento]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Registry data compiled by humanitarian partners documenting internally
    displaced persons (IDPs) and returnees from forced displacement events in Colombia.
    Data includes displacement events categorized by type (confinement, disaster),
    affected populations disaggregated by demographics (gender, age, ethnicity), and
    geographic origin at departmental and municipal levels, with status tracking as
    of 12 January 2024.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-retornados-por-desplazamiento
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displaced by forced displacement events including confinement
      and disasters
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
  - asset_category: population
    asset_dimension: population
    description: Population displaced by convective storm and disaster events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia Retornados por Desplazamiento (Estado de desplazamientos 2024)
  download_url: https://data.humdata.org/dataset/3cce0af3-bb8a-488b-985a-5f76f9da9913/resource/4f6a8430-d096-417b-9ce9-d0441fc7e18d/download/desplazamientos-segun-estado-2024.xlsx
  format: null
  id: resource_4f6a8430
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Desplazamientos segun estado 2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia Retornados por Desplazamiento (Desplazados retornados corte
    12-01-2024)
  download_url: https://data.humdata.org/dataset/3cce0af3-bb8a-488b-985a-5f76f9da9913/resource/ae834513-2690-4551-a915-cb3c5756a1d8/download/desplazados_retornados_corte_12012024.xlsx
  format: null
  id: resource_ae834513
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: desplazados_retornados_corte_12012024.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_retornadospordesplazamien_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-11-20'
  start: '2021-01-01'
temporal_resolution: null
title: Colombia Retornados por Desplazamiento
version: null
vulnerability: null
---
