---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/colombia-pin-general-y-severidad-intersectorial-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: JIAF 2.0 (Joint Intersectoral Analysis Framework)
    url: https://data.humdata.org/dataset/colombia-pin-general-y-severidad-intersectorial-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-general-y-severidad-intersectorial-2025
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-pin-general-y-severidad-intersectorial-2025
dataset_id: rdls_lss-col_3is_pingeneralyseveridadinter_2025
description: "Para el a\xF1o 2025 la estimaci\xF3n de las Personas en Necesidad (PiN)\
  \ General y las Severidades intersectoriales para Colombia, se desarroll\xF3 siguiendo\
  \ la metodolog\xEDa global JIAF 2.0 (Joint Intersectoral Analysis Framework, por\
  \ sus siglas en ingl\xE9s). Esto se relaciona con el an\xE1lisis del documento del\
  \ Plan de Respuesta a Prioridades Comunitarias - PRPC- 2025.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/colombia-pin-general-y-severidad-intersectorial-2025]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: PiN and intersectoral severity estimates for Colombia in 2025 were
    generated using the JIAF 2.0 global methodology, which integrates multi-sectoral
    humanitarian indicators to classify affected populations by severity levels. The
    analysis supports the Community Response Priorities Plan (PRPC) 2025 and includes
    disaggregation by vulnerable groups and host communities.
  sources:
  - id: source_1
    license: null
    name: OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: JIAF 2.0 (Joint Intersectoral Analysis Framework)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-pin-general-y-severidad-intersectorial-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in Need (PiN) estimates and intersectoral severity classifications
      for affected populations in Colombia
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial (C\xE1lculo PiN\
    \ General y severidad intersectorial, Colombia 2025.)"
  download_url: https://data.humdata.org/dataset/90846cf3-d748-468f-bb97-f8da3d586512/resource/aecc9d8b-6977-4374-8102-5e0f046e0092/download/matriz-jiaf-2.0-pin_severidad-intersectorial-colombia-2025.xlsx
  format: null
  id: resource_aecc9d8b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Matriz JIAF 2.0 PiN_Severidad Intersectorial - Colombia 2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Resumen de indicadores seleccionados por los cl\xFAster para la construcci\xF3\
    n de cada PiN, Colombia 2025."
  download_url: https://data.humdata.org/dataset/90846cf3-d748-468f-bb97-f8da3d586512/resource/6eb562ad-a20e-4157-84f2-78f4ec23d5e2/download/indicadores-seleccionados-por-cluster-colombia-2025.xlsx
  format: null
  id: resource_6eb562ad
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Indicadores seleccionados por cl\xFAster - Colombia 2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial (Desagregaci\xF3\
    n de los grupos vulnerables del PiN General, Colombia 2025.)"
  download_url: https://data.humdata.org/dataset/90846cf3-d748-468f-bb97-f8da3d586512/resource/acf4e6c4-975a-4383-b321-81d258382338/download/desagregacion-grupos-vulnerables-pin-general-colombia-2025.xlsx
  format: null
  id: resource_acf4e6c4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Desagregaci\xF3n grupos vulnerables PiN General - Colombia 2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial (C\xE1lculo de comunidades\
    \ de acogida, Colombia 2025.)"
  download_url: https://data.humdata.org/dataset/90846cf3-d748-468f-bb97-f8da3d586512/resource/bb618e78-4c9b-4ea9-99eb-38711737945d/download/comunidades-de-acogida-colombia-2025.xlsx
  format: null
  id: resource_bb618e78
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Comunidades de acogida - Colombia 2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial (Nota metodol\xF3\
    gica desagregaci\xF3n de grupos vulnerables - Colombia 2025.pdf)"
  download_url: https://data.humdata.org/dataset/90846cf3-d748-468f-bb97-f8da3d586512/resource/0ee2798c-267b-4d81-8b4d-8aacbf5dd3ed/download/desagregacion-de-grupos-vulnerables-colombia-2025.pdf
  format: null
  id: resource_0ee2798c
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Nota metodol\xF3gica desagregaci\xF3n de grupos vulnerables - Colombia 2025.pdf"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_pingeneralyseveridadinter_2025
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
  end: '2025-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: Colombia - PiN General y Severidad Intersectorial
version: null
vulnerability: null
---
