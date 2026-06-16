---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a Victimas (UARIV)"
    url: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Unidad Nacional para La Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    url: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Direcci\xF3n para la Acci\xF3n integral contra minas Antipersonal (DAICMA)"
    url: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Instituto Nacional de Medicina Legal (INML)
    url: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Oficina para la coordinaci\xF3n de asuntos humanitarios (OCHA)"
    url: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Fondo Internacional de Emergencia de las Naciones Unidas para la Infancia
      (UNICEF)
    url: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015
dataset_id: rdls_lss-col_ochacol_datosinfogramasisemestre2_2015
description: "El infograma es producido semestralmente desde 2006, usando informaci\xF3\
  n proveniente de la Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a Victimas\
  \ (UARIV), Direcci\xF3n para la Acci\xF3n integral contra minas Antipersonal (DAICMA),\
  \ la Unidad Nacional para La Gesti\xF3n del Riesgo de Desastres UNGRD, la Direcci\xF3\
  n de Polic\xEDa Judicial (DIJIN), el Instituto Nacional de Medicina Legal (INML),\
  \ Oficina para la coordinaci\xF3n de asuntos humanitarios (OCHA) y Fondo Internacional\
  \ de Emergencia de las Naciones Unidas para la Infancia (UNICEF). Analizar tendencias\
  \ en las diferentes situaciones humanitarias hace parte del principal objetivo del\
  \ Infograma de Situaci\xF3n Humanitaria. Este documento presenta mapas, gr\xE1ficas\
  \ y estad\xEDsticas que reflejan la situaci\xF3n humanitaria en Colombia. Permite\
  \ al usuario analizar nacionalmente las tendencias de fen\xF3menos como el desplazamiento\
  \ interno, Minas anti personal y munici\xF3n sin explotar, desastres naturales,\
  \ homicidios, desaparecidos y el \xCDndice de Riesgo de la Situaci\xF3n Humanitaria..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015]"
details: "\xCDndice INFORM esta compuesto para la gesti\xF3n del riesgo (INFORM) es\
  \ una herramienta para el an\xE1lisis del riesgo humanitario, permite cuantificar\
  \ el riesgo de tener una crisis o desastre en cada pa\xEDs. Identifica municipios\
  \ en riesgo y factores asociados con crisis humanitaria. Analiza como el riesgo\
  \ cambia con el tiempo. Riesgo = amenaza x vulnerabilidad x falta de capacidad de\
  \ respuesta."
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Semiannual infogram compiled from multiple Colombian government and
    UN agency administrative records (UARIV, UNGRD, DAICMA, INML, DIJIN, OCHA, UNICEF)
    documenting humanitarian impacts from natural disasters and conflict-related violence.
    Data aggregated to track trends in affected and displaced populations across humanitarian
    crises.
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
    name: "Direcci\xF3n para la Acci\xF3n integral contra minas Antipersonal (DAICMA)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: Instituto Nacional de Medicina Legal (INML)
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
  - id: source_6
    license: null
    name: Fondo Internacional de Emergencia de las Naciones Unidas para la Infancia
      (UNICEF)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/datos-infogramas-i-semestre-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by natural disasters and conflict-related violence
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
    description: Population displaced due to natural disasters and humanitarian crises
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
  description: Colombia - Datos Infogramas I- Semestre 2015 (Base de datos infograma
    I Sem 2015.csv)
  download_url: https://data.humdata.org/dataset/3df8842f-c5d8-48cc-93c0-685eecae5fbd/resource/1b720a87-52a2-4964-b731-9e7a796f3868/download/base-de-datos-infograma-i-sem-2015.csv
  format: null
  id: resource_1b720a87
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Base de datos infograma I Sem 2015.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_datosinfogramasisemestre2_2015
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
  start: '2015-01-01'
temporal_resolution: null
title: Colombia - Datos Infogramas I- Semestre 2015
version: null
vulnerability: null
---
