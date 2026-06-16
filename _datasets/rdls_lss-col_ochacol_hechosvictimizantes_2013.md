---
attributions:
- entity:
    affiliation: null
    email: null
    name: "UARIV (Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a las V\xED\
      ctimas)"
    url: https://data.humdata.org/dataset/colombia-hechos-victimizantes-uariv
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/colombia-hechos-victimizantes-uariv
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/colombia-hechos-victimizantes-uariv
dataset_id: rdls_lss-col_ochacol_hechosvictimizantes_2013
description: "Tabla con todos los hechos victimizantes reportados por UARIV por a\xF1\
  o, mes, departamento y municipio. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/colombia-hechos-victimizantes-uariv]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Registry data compiled by UARIV documenting all reported victimization
    events in Colombia disaggregated by type of event, department, municipality, year,
    month, age group, gender identity, and ethnic pertinence. Data represents administrative
    records of conflict-related violence impacts on the Colombian population.
  sources:
  - id: source_1
    license: null
    name: "UARIV (Unidad para la Atenci\xF3n y Reparaci\xF3n Integral a las V\xED\
      ctimas)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-hechos-victimizantes-uariv
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Victimization events (conflict-related violence) affecting population
      by age, gender, ethnicity, and geographic location
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
  - asset_category: population
    asset_dimension: population
    description: Internal displacement resulting from victimization events, classified
      by displacement type
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
  description: "Tabla con todos los hechos victimizantes reportados por UARIV hasta\
    \ junio del 2025 con desagregaci\xF3n por edad, grupo \xE9tnico, g\xE9nero, departamento\
    \ y municipio. Es importante tener en cuenta que por el hecho de que puede existir\
    \ alguna duplicidad de datos no se recomienda sumar la informaci\xF3n de hechos\
    \ victimizantes o dar esta informaci\xF3n como resultados de personas."
  download_url: https://data.humdata.org/dataset/7a82edf4-a7e2-4492-9801-5622767a2949/resource/4ca10ae9-edc0-4c82-9c43-a27a3e416992/download/pivot_uariv_data.xlsx
  format: null
  id: resource_4ca10ae9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Hechos victimizantes hasta 2025 UARIV.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Tabla con todos los hechos victimizantes reportados por UARIV hasta\
    \ abril del 2023 con desagregaci\xF3n por edad, g\xE9nero, etnia, departamento\
    \ y municipio. Es importante tener en cuenta que por el hecho de que puede existir\
    \ alguna duplicidad de datos no se recomienda sumar la informaci\xF3n de hechos\
    \ victimizantes o dar esta informaci\xF3n como resultados de personas."
  download_url: https://data.humdata.org/dataset/7a82edf4-a7e2-4492-9801-5622767a2949/resource/1c03eea7-1227-42ae-a1be-e9f08fe1392f/download/hechos_victimizantes_agosto_2023.csv
  format: null
  id: resource_1c03eea7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hechos_victimizantes_agosto_2023.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_hechosvictimizantes_2013
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
  end: '2025-06-30'
  start: '2013-01-01'
temporal_resolution: null
title: 'Colombia: Hechos Victimizantes'
version: null
vulnerability: null
---
