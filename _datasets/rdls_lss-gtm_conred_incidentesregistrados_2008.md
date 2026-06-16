---
attributions:
- entity:
    affiliation: null
    email: null
    name: "CONRED Guatemala (Sistema Nacional de Gesti\xF3n de Riesgos)"
    url: https://data.humdata.org/dataset/incidentesguatemala
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: CONRED Guatemala (inactive)
  url: https://data.humdata.org/dataset/incidentesguatemala
creator:
  affiliation: null
  email: null
  name: CONRED Guatemala (inactive)
  url: https://data.humdata.org/dataset/incidentesguatemala
dataset_id: rdls_lss-gtm_conred_incidentesregistrados_2008
description: "Incidentes registrados en Guatemala por el Sistema Nacional de Gesti\xF3\
  n de Riesgos, desde los a\xF1os 2008 al 2022, Bajo la plataforma de SISMICEDE, y\
  \ este a su vez se comparte como parte de los esfuerzos de trasparentar las acciones\
  \ en Gesti\xF3n de Riesgo. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/incidentesguatemala]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event incident records compiled by Guatemala's National Risk Management
    System (CONRED) through the SISMICEDE platform, documenting disaster impacts including
    affected populations and infrastructure damage across multiple hazard types from
    2008 to 2022.
  sources:
  - id: source_1
    license: null
    name: "CONRED Guatemala (Sistema Nacional de Gesti\xF3n de Riesgos)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/incidentesguatemala
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Affected population and infrastructure from flood incidents
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Affected population and infrastructure from landslide incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Affected population and infrastructure from strong wind incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Affected population and infrastructure from volcanic incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_4
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2022)'
  download_url: https://drive.google.com/file/d/1rVppthu4DrCAXMfnmd8IVgtyVMASrNOn/view?usp=drive_web
  format: null
  id: resource_a393351a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2021)'
  download_url: https://drive.google.com/file/d/1cp1PYLD0Pate8PBQ5trvOjobbAIoAKzF/view?usp=drive_web
  format: null
  id: resource_9cfbbf86
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Incidentes-2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2020)'
  download_url: https://drive.google.com/file/d/192CQFVBGiGxwDgbOjcX8EMlh1CJtycq7/view?usp=drive_web
  format: null
  id: resource_06b4cd48
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Incidentes-2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2019)'
  download_url: https://drive.google.com/file/d/19-s62t1EgUseqQ3NXbZAPuKB4H_2FW3n/view?usp=drive_web
  format: null
  id: resource_acc9034c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Incidentes-2019.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2018)'
  download_url: https://drive.google.com/file/d/10RbqzIVlilRpTmOdkfLjSxrmZTO-lFzT/view?usp=drive_web
  format: null
  id: resource_9939cf02
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Incidentes-2018.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2017)'
  download_url: https://drive.google.com/file/d/1n9P2y0EXHBwt8qn8fCQAd1eReDkfTcqd/view?usp=drive_web
  format: null
  id: resource_aaabcb7d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2017.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2016)'
  download_url: https://drive.google.com/file/d/1aIw2MjIrcG9oBeknmJeXg3sNwUMumgLx/view?usp=drive_web
  format: null
  id: resource_13807e1e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2016.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2015)'
  download_url: https://drive.google.com/file/d/1K9QUTnYii74dKAJEgb6Ohwe0FSUZ7OpH/view?usp=drive_web
  format: null
  id: resource_f7ee3e3b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2015.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2014)'
  download_url: https://drive.google.com/file/d/15klz9zQzdwp96zJMYPiNPZmeOS7tk3lc/view?usp=drive_web
  format: null
  id: resource_764b627c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2014.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2013)'
  download_url: https://drive.google.com/file/d/1Vppg67a_vZhPEDFlQUyAOjUL-L9vNzt0/view?usp=drive_web
  format: null
  id: resource_cb170111
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2013.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2012)'
  download_url: https://drive.google.com/file/d/1duf7XIfrjiS6xkJfgSz9M7pEyN5c6gzh/view?usp=drive_web
  format: null
  id: resource_b76d8ab9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2012.xls
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2011)'
  download_url: https://drive.google.com/file/d/1Hl_qdlNYjDkIOLSCGWxCuUTo-SqMQ8Tj/view?usp=drive_web
  format: null
  id: resource_466ce436
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2011.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2010)'
  download_url: https://drive.google.com/file/d/1j9-wZq2z2vVSZiSioIK6KreqYcAUz_eL/view?usp=drive_web
  format: null
  id: resource_ef7e0643
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2010.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2009)'
  download_url: https://drive.google.com/file/d/1li0hxsH__tzwxeTrLpww-AyuDiJy_w2H/view?usp=drive_web
  format: null
  id: resource_606ffe92
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2009.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guatemala: Incidentes Registrados (Registro de incidentes registrados
    por la CONRED en 2008)'
  download_url: https://drive.google.com/file/d/1ONxeQg70MPLNk79-IaWYgc3H481iYto9/view?usp=drive_web
  format: null
  id: resource_e7de1c64
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: incidentes-2008.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_conred_incidentesregistrados_2008
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
  end: '2022-12-31'
  start: '2008-01-01'
temporal_resolution: null
title: 'Guatemala: Incidentes Registrados'
version: null
vulnerability: null
---
