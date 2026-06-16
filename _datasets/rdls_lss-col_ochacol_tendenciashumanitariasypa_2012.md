---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Oficina de las Naciones Unidas para la Coordinaci\xF3n de Asuntos Humanitarios\
      \ (OCHA)"
    url: https://data.humdata.org/dataset/tendencias-humanitarias-y-paz
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Equipo Humanitario de Pa\xEDs"
    url: https://data.humdata.org/dataset/tendencias-humanitarias-y-paz
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/tendencias-humanitarias-y-paz
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/tendencias-humanitarias-y-paz
dataset_id: rdls_lss-col_ochacol_tendenciashumanitariasypa_2012
description: "El informe 'Tendencias Humanitarias y Paz noviembre 2012 - junio 2015'\
  \ es elaborado y publicado por la Oficina de las Naciones Unidas para la Coordinaci\xF3\
  n de Asuntos Humanitarios (OCHA) en colaboraci\xF3n con socios del Equipo Humanitario\
  \ de Pa\xEDs y del Sistema de Naciones Unidas en Colombia, a quienes se les ha compartido\
  \ este documento para sus contribuciones. Este documento responde a un ejercicio\
  \ de monitoreo de la situaci\xF3n humanitaria y pretende destacar las tendencias\
  \ principales registradas tanto por las agencias humanitarias as\xED como por las\
  \ fuentes oficiales, en un periodo de 32 meses mientras estaban en curso las conversaciones\
  \ en La Habana entre el Gobierno nacional y las FARC-EP. La mayor\xEDa de los datos\
  \ reportados corresponde a registros y denuncias recibidas por instituciones oficiales\
  \ y datos consolidados por OCHA a partir de diversas fuentes, con corte a junio\
  \ de 2015.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/tendencias-humanitarias-y-paz]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: This dataset aggregates humanitarian monitoring data from OCHA and
    humanitarian partners in Colombia documenting conflict-related impacts (displacement,
    homicides, kidnappings, extortion, sexual violence, armed actions, and mine incidents)
    collected through registry methodology from November 2012 to June 2015. Data is
    disaggregated by geography, perpetrator actors, and demographic characteristics
    to track humanitarian trends during the complex emergency.
  sources:
  - id: source_1
    license: null
    name: "Oficina de las Naciones Unidas para la Coordinaci\xF3n de Asuntos Humanitarios\
      \ (OCHA)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "Equipo Humanitario de Pa\xEDs"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tendencias-humanitarias-y-paz
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from armed conflict and violence
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
    description: Homicides and deaths from armed conflict and violence
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by kidnappings, extortion, sexual violence, and
      armed actions
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
  description: 'Colombia: Tendencias Humanitarias y Paz (Excel)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/b1f0dfb8-8074-4aa5-9021-ffd3a9f2eeb4/download/mapatendencias2015iv2.xlsx
  format: null
  id: resource_b1f0dfb8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mapa_Tendencias_2015_I_v2.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Tasa Extorsiones.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/f85c364b-33fd-47d4-964c-fae1c47c47aa/download/tasa-extorsiones.xlsx
  format: null
  id: resource_f85c364b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tasa Extorsiones.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Tasa Extorsiones Geografico.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/bc033ac1-6dc0-4152-9e4c-d21eaf839621/download/tasa-extorsiones-geografico.xlsx
  format: null
  id: resource_bc033ac1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tasa Extorsiones Geografico.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Excel)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/902b4064-c4ee-413c-b962-296ea36498c3/download/extorsion.xlsx
  format: null
  id: resource_902b4064
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Extorsion.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (IDPs Totales.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/5400d1b9-25f6-43c0-b58f-882c63035390/download/idps-totales.xlsx
  format: null
  id: resource_5400d1b9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDPs Totales.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (IDPs Geografico.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/8c867e32-f246-47bb-b537-f6307c6b3a2d/download/idps-geografico.xlsx
  format: null
  id: resource_8c867e32
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDPs Geografico.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (IDPs Actores.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/4ed157d4-90fc-45ff-a883-25c3ad81a22b/download/idps-actores.xlsx
  format: null
  id: resource_4ed157d4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDPs Actores.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Excel)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/70394c13-8012-4d19-b973-7ad050202551/download/secuestros.xlsx
  format: null
  id: resource_70394c13
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Secuestros.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Secuestros Geografico.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/f24ea053-c95f-4205-b3da-75d54b7197a5/download/secuestros-geografico.xlsx
  format: null
  id: resource_f24ea053
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Secuestros Geografico.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Tasa de Secuestros.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/c290767f-5915-4189-9041-54031afd1b88/download/tasa-de-secuestros.xlsx
  format: null
  id: resource_c290767f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tasa de Secuestros.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Homicidios Geografico.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/fe10c505-f49a-4d85-ac0d-f8c84d245385/download/homicidios-geografico.xlsx
  format: null
  id: resource_fe10c505
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Homicidios Geografico.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Homicidios ACNUR.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/47841a8b-a473-4e24-bcee-60cb8f8991d9/download/homicidios-acnur.xlsx
  format: null
  id: resource_47841a8b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Homicidios ACNUR.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Tasa de Homicidios.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/e1e359fa-11aa-49c6-9d89-d3d930de54c9/download/tasa-de-homicidios.xlsx
  format: null
  id: resource_e1e359fa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tasa de Homicidios.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Excel)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/16452581-c06e-4b59-9c39-12da72082961/download/accesoconfinamiento.xlsx
  format: null
  id: resource_16452581
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Acceso_Confinamiento.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Excel)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/913cccfa-2db1-4d9f-a602-81ff484223e6/download/accesogeografico.xlsx
  format: null
  id: resource_913cccfa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Acceso_geografico.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Delitos Sexuales.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/943adb81-9d63-408b-93e6-282a339235fa/download/delitos-sexuales.xlsx
  format: null
  id: resource_943adb81
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Delitos Sexuales.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Delitos Sexuales_geografico.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/08530ab8-bac6-44f1-bd58-3c5f1efe73a8/download/delitos-sexualesgeografico.xlsx
  format: null
  id: resource_08530ab8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Delitos Sexuales_geografico.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Violencia sexual INML.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/a7eaac9c-9b40-4cd4-8a60-e8e54ca4c883/download/violencia-sexual-inml.xlsx
  format: null
  id: resource_a7eaac9c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Violencia sexual INML.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Acciones Armadas UNDSS.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/00827186-8382-469a-bec9-ece4e0ba4951/download/acciones-armadas-undss.xlsx
  format: null
  id: resource_00827186
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Acciones Armadas UNDSS.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Excel)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/61ebbbff-3bed-4ef1-95bf-86aaeea23eb5/download/minas.xlsx
  format: null
  id: resource_61ebbbff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Minas.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Minas geografico.xlsx)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/e8bc49bb-af18-40f1-8dd2-0c87ab0b9943/download/minas-geografico.xlsx
  format: null
  id: resource_e8bc49bb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Minas geografico.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: Tendencias Humanitarias y Paz (Excel)'
  download_url: https://data.humdata.org/dataset/3f173ccd-2e52-4542-9547-df5a42b7b223/resource/a40a302b-e2c9-4933-973b-b6ba587246c0/download/respuesta.xlsx
  format: null
  id: resource_a40a302b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Respuesta.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_tendenciashumanitariasypa_2012
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
  end: '2015-06-30'
  start: '2012-11-01'
temporal_resolution: null
title: 'Colombia: Tendencias Humanitarias y Paz'
version: null
vulnerability: null
---
