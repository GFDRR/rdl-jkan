---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a Victimas (UARIV)"
    url: https://data.humdata.org/dataset/da
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Unidad Nacional para La Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    url: https://data.humdata.org/dataset/da
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Instituto Nacional de Medicina Legal (INML)
    url: https://data.humdata.org/dataset/da
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Direcci\xF3n de Polic\xEDa Judicial (DIJIN)"
    url: https://data.humdata.org/dataset/da
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/da
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/da
dataset_id: rdls_lss-col_ochacol_datosinfogramas2014_2014
description: "El infograma es producido semestralmente desde 2006, usando informaci\xF3\
  n proveniente de la Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a Victimas\
  \ UARIV, el Programa Presidencial para la Acci\xF3n Integral contra Minas Antipersonal\
  \ PAICMA, la Unidad Nacional para La Gesti\xF3n del Riesgo de Desastres UNGRD, la\
  \ Direcci\xF3n de Polic\xEDa Judicial (DIJIN), el Instituto Nacional de Medicina\
  \ Legal (INML), el Observatorio de DDHH y DIH, la Vicepresidencia de la Rep\xFA\
  blica y la Universidad Santo Tom\xE1s -OCHA. Analizar tendencias en las diferentes\
  \ situaciones humanitarias hace parte del principal objetivo del Infograma de Situaci\xF3\
  n Humanitaria. Este documento presenta mapas, gr\xE1ficas y estad\xEDsticas que\
  \ reflejan la situaci\xF3n humanitaria en Colombia. Permite al usuario analizar\
  \ nacionalmente las tendencias de fen\xF3menos como el desplazamiento interno, Minas\
  \ anti personal y munici\xF3n sin explotar, desastres naturales, homicidios, desaparecidos\
  \ y el \xCDndice de Riesgo de la Situaci\xF3n Humanitaria.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/da]"
details: "El \xCDndice de Riesgo de Situaci\xF3n Humanitaria (IRSH) se calcul\xF3\
  \ s\xF3lo para el primer semestre del a\xF1o 2014 porque en la actualidad se est\xE1\
  \ trabajando en una versi\xF3n mejorada de este \xEDndice."
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Semi-annual infograms compiled from 2006 onwards by aggregating observational
    data from multiple Colombian government agencies (UARIV, UNGRD, INML, DIJIN) and
    humanitarian organizations (OCHA) to track humanitarian trends including disaster
    impacts, displacement, and affected populations. Data represents direct observational
    records from institutional sources integrated into a consolidated humanitarian
    overview.
  sources:
  - id: source_1
    license: null
    name: "Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a Victimas (UARIV)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "Unidad Nacional para La Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Instituto Nacional de Medicina Legal (INML)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: "Direcci\xF3n de Polic\xEDa Judicial (DIJIN)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/da
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding and other natural disasters
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displaced by flooding and natural disasters
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
        metric: displaced
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Fatalities from flooding and natural disasters
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
        metric: casualty_count
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Datos Infogramas 2014 (Base de datos infograma I Sem 2014.csv)
  download_url: https://data.humdata.org/dataset/4cd10b87-dc63-4f49-a21f-1109264069cf/resource/8a072fb8-e218-420b-8dbf-8c0e615fab66/download/base-de-datos-infograma.csv
  format: null
  id: resource_8a072fb8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Base de datos infograma I Sem 2014.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Datos Infogramas 2014 (Base de datos infograma II Sem 2014.csv)
  download_url: https://data.humdata.org/dataset/4cd10b87-dc63-4f49-a21f-1109264069cf/resource/ed19892a-2765-4b45-a4fb-9076f125ec7e/download/base-de-datos-infograma-para-hdx.csv
  format: null
  id: resource_ed19892a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Base de datos infograma II Sem 2014.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_datosinfogramas2014_2014
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
  end: '2014-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: Colombia - Datos Infogramas 2014
version: null
vulnerability: null
---
