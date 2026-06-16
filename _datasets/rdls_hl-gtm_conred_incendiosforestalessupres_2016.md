---
attributions:
- entity:
    affiliation: null
    email: null
    name: CONRED Guatemala
    url: https://data.humdata.org/dataset/incendios-forestales-supresion
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: CONRED Guatemala (inactive)
  url: https://data.humdata.org/dataset/incendios-forestales-supresion
creator:
  affiliation: null
  email: null
  name: CONRED Guatemala (inactive)
  url: https://data.humdata.org/dataset/incendios-forestales-supresion
dataset_id: rdls_hl-gtm_conred_incendiosforestalessupres_2016
description: "Registro de incendios forestal y no forestal de Guatemala, desde los\
  \ a\xF1os 2017 al 2022, incluye informaci\xF3n geogr\xE1fica para y el \xE1rea quemada,\
  \ registro de SISMICEDE. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/incendios-forestales-supresion]"
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event wildfire registry compiled by CONRED Guatemala from 2017-2022,
    recording individual fire incidents with geographic coordinates and burned area
    measurements. Data aggregated annually and stored in SISMICEDE system for national
    disaster documentation.
  sources:
  - id: source_1
    license: null
    name: CONRED Guatemala
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/incendios-forestales-supresion
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Burned area extent from forest and non-forest wildfires
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
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
  description: "Registro de la temporada de incendios 2021-2022, registrado por la\
    \ Direcci\xF3n de Comando de Incidentes bajo la Subidrecci\xF3n de Incendios Forestales"
  download_url: https://drive.google.com/file/d/1bOkQlf-350A5a5l4FsvX66kDtmEkFK5E/view?usp=drive_web
  format: null
  id: resource_462564e4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Supresion-2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Registro de la temporada de incendios 2020-2021, registrado por la\
    \ Direcci\xF3n de Comando de Incidentes bajo la Subidrecci\xF3n de Incendios Forestales"
  download_url: https://drive.google.com/file/d/1N8EOvJ3E8P8ONF9_JSuVKLX_Jh6-6yBx/view?usp=drive_web
  format: null
  id: resource_61d63427
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Supresion-2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Registro de la temporada de incendios 2019-2020, registrado por la\
    \ Direcci\xF3n de Comando de Incidentes bajo la Subidrecci\xF3n de Incendios Forestales"
  download_url: https://drive.google.com/file/d/1EtWG2tStwScXk116y20FY8ybSdAIs9wc/view?usp=drive_web
  format: null
  id: resource_27093814
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Supresion-2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Registro de la temporada de incendios 2018-2019, registrado por la\
    \ Direcci\xF3n de Comando de Incidentes bajo la Subidrecci\xF3n de Incendios Forestales"
  download_url: https://drive.google.com/file/d/12lqq4RNiKF8AvXN1GPYRhc0GDkZHMi8r/view?usp=drive_web
  format: null
  id: resource_dac3ec81
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Supresion-2019.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Registro de la temporada de incendios 2017-2018, registrado por la\
    \ Direcci\xF3n de Comando de Incidentes bajo la Subidrecci\xF3n de Incendios Forestales"
  download_url: https://drive.google.com/file/d/1gSey6XPPblzKFYsHWE0AZgY86G9xiPbL/view?usp=drive_web
  format: null
  id: resource_68708515
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Supresion-2018.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Registro de la temporada de incendios 2016-2017, registrado por la\
    \ Direcci\xF3n de Comando de Incidentes bajo la Subidrecci\xF3n de Incendios Forestales"
  download_url: https://drive.google.com/file/d/1k_bTfKW5oSJHJWFGCn0_KT214Ichnc7w/view?usp=drive_web
  format: null
  id: resource_6a558fdc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Supresion-2017.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-gtm_conred_incendiosforestalessupres_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-06-30'
  start: '2016-11-01'
temporal_resolution: null
title: Guatemala - Incendios Forestales (SUPRESION)
version: null
vulnerability: null
---
