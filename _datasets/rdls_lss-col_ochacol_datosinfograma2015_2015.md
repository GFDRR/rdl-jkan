---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a Victimas (UARIV)"
    url: https://data.humdata.org/dataset/datos-infograma-2015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Unidad Nacional para La Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    url: https://data.humdata.org/dataset/datos-infograma-2015
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Instituto Nacional de Medicina Legal (INML)
    url: https://data.humdata.org/dataset/datos-infograma-2015
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Direcci\xF3n para la Acci\xF3n integral contra minas Antipersonal (DAICMA)"
    url: https://data.humdata.org/dataset/datos-infograma-2015
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Oficina para la coordinaci\xF3n de asuntos humanitarios (OCHA)"
    url: https://data.humdata.org/dataset/datos-infograma-2015
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/datos-infograma-2015
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/datos-infograma-2015
dataset_id: rdls_lss-col_ochacol_datosinfograma2015_2015
description: "El infograma es producido semestralmente desde 2006, usando informaci\xF3\
  n proveniente de la Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a Victimas\
  \ (UARIV), Direcci\xF3n para la Acci\xF3n integral contra minas Antipersonal (DAICMA),\
  \ la Unidad Nacional para La Gesti\xF3n del Riesgo de Desastres UNGRD, la Direcci\xF3\
  n de Polic\xEDa Judicial (DIJIN), el Instituto Nacional de Medicina Legal (INML),\
  \ Oficina para la coordinaci\xF3n de asuntos humanitarios (OCHA) y la Unidad de\
  \ manejo y analisis de informaci\xF3n Colombia (UMAIC). Analizar tendencias en las\
  \ diferentes situaciones humanitarias hace parte del principal objetivo del Infograma\
  \ de Situaci\xF3n Humanitaria. Este documento presenta mapas, gr\xE1ficas y estad\xED\
  sticas que reflejan la situaci\xF3n humanitaria en Colombia. Permite al usuario\
  \ analizar nacionalmente las tendencias de fen\xF3menos como el desplazamiento interno,\
  \ Minas anti personal y munici\xF3n sin explotar, desastres naturales, homicidios\
  \ y desaparecidos. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/datos-infograma-2015]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The Infograma dataset aggregates semi-annual humanitarian impact data
    from multiple Colombian government agencies (UARIV, UNGRD, INML, DAICMA, DIJIN,
    OCHA, UMAIC) covering natural disasters, conflict-related violence, and displacement.
    Data are compiled from direct observational records and administrative sources
    to track trends in humanitarian situations across Colombia.
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
    name: "Direcci\xF3n para la Acci\xF3n integral contra minas Antipersonal (DAICMA)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: "Oficina para la coordinaci\xF3n de asuntos humanitarios (OCHA)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/datos-infograma-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by natural disasters including earthquakes
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Population displaced by natural disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Fatalities from natural disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Colombia - Datos Infograma 2015 (Base de datos Infograma 2015.csv)
  download_url: https://data.humdata.org/dataset/9d416b86-454e-48d6-bdba-3bd755321d60/resource/d2cb83b5-3dde-4170-9b1b-6b512e8bfce6/download/base-de-datos-infograma-2015.csv
  format: null
  id: resource_d2cb83b5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Base de datos Infograma 2015.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia - Datos Infograma 2015 (Infograma(2015) 16-03-10.xlsx)
  download_url: https://data.humdata.org/dataset/9d416b86-454e-48d6-bdba-3bd755321d60/resource/c4ee3a1a-518e-4137-b829-3a4638a94166/download/infograma2015-16-03-10.xlsx
  format: null
  id: resource_c4ee3a1a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Infograma(2015) 16-03-10.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_datosinfograma2015_2015
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
  end: '2015-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: Colombia - Datos Infograma 2015
version: null
vulnerability: null
---
