---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    url: https://data.humdata.org/dataset/colombia-emergencias-por-desastres-naturales
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/colombia-emergencias-por-desastres-naturales
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/colombia-emergencias-por-desastres-naturales
dataset_id: rdls_lss-col_ochacol_emergenciaspordesastresna_2022
description: "Emergencias por desastres naturales seg\xFAn reporte de la UNGRD. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/colombia-emergencias-por-desastres-naturales]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event disaster impact registry compiled by UNGRD from emergency
    reports across Colombian departments and municipalities. Data includes standardized
    impact metrics (deaths, injuries, affected persons, damaged buildings, affected
    roads, destroyed dwellings, affected hectares) aggregated by event date, location,
    and hazard type for the period 2016-2024.
  sources:
  - id: source_1
    license: null
    name: "Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-emergencias-por-desastres-naturales
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: People affected by flood events
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
  - asset_category: buildings
    asset_dimension: structure
    description: Destroyed dwellings from flood events
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural land affected (hectares) by flood events
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
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: People affected by landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  - asset_category: buildings
    asset_dimension: structure
    description: Destroyed dwellings from landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: People affected by strong wind/storm events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_6
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
  - asset_category: buildings
    asset_dimension: structure
    description: Destroyed dwellings from strong wind/storm events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_7
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
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
  description: 'Colombia: Emergencias por Desastres Naturales (Colombia desastres
    naturales Enero 2016- 2 Julio 2024 fuente UNGRD)'
  download_url: https://data.humdata.org/dataset/8b4abbc2-a705-4eb7-8909-bdc7d9ed20ce/resource/239f7524-f5e1-49ca-ab2b-82cb15afa94b/download/ungrd_2016_2024_total.xlsx
  format: null
  id: resource_239f7524
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ungrd_2016_2024_total.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Colombia emergencias por desastres naturales, UNGRD. 1 enero a 11 de
    abril 2023
  download_url: https://data.humdata.org/dataset/8b4abbc2-a705-4eb7-8909-bdc7d9ed20ce/resource/6f4c8b32-1dfa-46d6-b16a-5cad8b25f0b0/download/emergencias-2023-martes-11-de-abril-7am.xlsx
  format: null
  id: resource_6f4c8b32
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Colombia emergencias por desastres naturales, UNGRD. 1 enero a 11 de abril
    2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Emergencias por desastres naturales reportadas UNGRD 1 de enero a 7
    de marzo 2023
  download_url: https://data.humdata.org/dataset/8b4abbc2-a705-4eb7-8909-bdc7d9ed20ce/resource/fb9cb227-035a-49a5-a311-a32295645afa/download/emergencias-2023-martes-07-de-marzo-7am.xlsx
  format: null
  id: resource_fb9cb227
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Colombia emergencias por desastres naturales, UNGRD. 1 enero a 7 de marzo
    2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Emergencias por desastres naturales 2022 seg\xFAn reporte de la Unidad\
    \ Nacional de Gesti\xF3n de Riesgos y Desastres"
  download_url: https://data.humdata.org/dataset/8b4abbc2-a705-4eb7-8909-bdc7d9ed20ce/resource/a3585673-c67e-4b29-82f5-bdcb6ead5711/download/emergencias-2022.xlsx
  format: null
  id: resource_a3585673
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Colombia emergencias por desastres naturales UNGRD 2022
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_emergenciaspordesastresna_2022
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
  end: '2024-07-02'
  start: '2022-01-01'
temporal_resolution: null
title: 'Colombia: Emergencias por Desastres Naturales'
version: null
vulnerability: null
---
