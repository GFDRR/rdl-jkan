---
attributions:
- entity:
    affiliation: null
    email: null
    name: 3iSolution
    url: https://data.humdata.org/dataset/pin-general-y-severidad-intersectorial-colombia-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/pin-general-y-severidad-intersectorial-colombia-2024
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/pin-general-y-severidad-intersectorial-colombia-2024
dataset_id: rdls_lss-col_3is_pingeneralyseveridadinter_20240219
description: "Para el a\xF1o 2024 la estimaci\xF3n de las Personas en Necesidad (PiN)\
  \ General y las Severidades intersectoriales para Colombia, se desarroll\xF3 siguiendo\
  \ la metodolog\xEDa global JIAF 2.0 (Joint Intersectoral Analysis Framework, por\
  \ sus siglas en ingl\xE9s). Esto se relaciona con el an\xE1lisis del documento del\
  \ Plan de Respuesta a Prioridades Comunitarias - PRPC- 2024.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/pin-general-y-severidad-intersectorial-colombia-2024]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The dataset was produced using the JIAF 2.0 global methodology, which
    integrates multi-sectoral humanitarian indicators across clusters (health, shelter,
    food security, etc.) to estimate People in Need (PiN) and intersectoral severity
    scores at sub-national level in Colombia for 2024. Expert judgment from regional
    HNO workshops was incorporated alongside disaggregation by vulnerable population
    groups and predictive modelling of mass displacement, confinement, and climate
    variability. The outputs inform the 2024 Community Response Priority Plan (PRPC).
  sources:
  - id: source_1
    license: null
    name: 3iSolution
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pin-general-y-severidad-intersectorial-colombia-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in Need (PiN) estimates and intersectoral severity classifications
      for Colombia 2024 using JIAF 2.0 methodology, including displacement and climate
      variability impacts
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial 2024 (C\xE1lculo\
    \ PiN General y severidad intersectorial, Colombia 2024.)"
  download_url: https://data.humdata.org/dataset/012fda67-d322-4450-bb0f-cfd6b1286c74/resource/b2f04bb7-748a-40d4-a842-7dffc351fc7b/download/matriz-jiaf-2.0-pin-general-y-severidad-intersectorial-colombia-2024.xlsx
  format: null
  id: resource_b2f04bb7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Matriz JIAF 2.0 PiN General y Severidad Intersectorial - Colombia 2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial 2024 (Desagregaci\xF3\
    n de los grupos vulnerables del PiN General, Colombia 2024.)"
  download_url: https://data.humdata.org/dataset/012fda67-d322-4450-bb0f-cfd6b1286c74/resource/fb2a46a6-8da3-4739-b2a2-0b3a4584cab2/download/desagregacion-grupos-vulnerables-pin-general-colombia-2024.xlsx
  format: null
  id: resource_fb2a46a6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Desagregaci\xF3n grupos vulnerables PiN General - Colombia 2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial 2024 (Resultados\
    \ del PiN General y PiN por cl\xFAster, Colombia 2024.)"
  download_url: https://data.humdata.org/dataset/012fda67-d322-4450-bb0f-cfd6b1286c74/resource/2e868464-d880-49a1-9e2a-ac01311481de/download/resultados-pin-general-y-pin-por-cluster-colombia-2024.xlsx
  format: null
  id: resource_2e868464
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Resultados PiN General y PiN por cl\xFAster - Colombia 2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Resumen de indicadores seleccionados por los cl\xFAster para la construcci\xF3\
    n de cada PiN, Colombia 2024."
  download_url: https://data.humdata.org/dataset/012fda67-d322-4450-bb0f-cfd6b1286c74/resource/c1441c5d-a255-40bc-84f2-248502e7007b/download/resumen-indicadores-seleccionados-por-cluster-colombia-2024.xlsx
  format: null
  id: resource_c1441c5d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Resumen indicadores seleccionados por cl\xFAster - Colombia 2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Resultados de los talleres regionales HNO 2023 . Nota: Estos datos\
    \ son importantes para el c\xE1lculo del de la severidad ya que se considera como\
    \ el 'Juicio de expertos'."
  download_url: https://data.humdata.org/dataset/012fda67-d322-4450-bb0f-cfd6b1286c74/resource/9ffa1468-96df-43a7-9d3c-439bd75d9ac5/download/resultados-votacion-juicio-de-expertos-talleres-regionales-hno-2023.xlsx
  format: null
  id: resource_9ffa1468
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Resultados votaci\xF3n juicio de expertos talleres regionales HNO 2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial 2024 (C\xE1lculo\
    \ de comunidades de acogida, Colombia 2024.)"
  download_url: https://data.humdata.org/dataset/012fda67-d322-4450-bb0f-cfd6b1286c74/resource/f5d609d8-87a9-4b51-a839-32e3974bc14e/download/comunidades-de-acogida-colombia-2024.xlsx
  format: null
  id: resource_f5d609d8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Comunidades de acogida - Colombia 2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial 2024 (Nota metodol\xF3\
    gica PiN General y Severidad Intersectorial - Colombia 2024.pdf)"
  download_url: https://data.humdata.org/dataset/012fda67-d322-4450-bb0f-cfd6b1286c74/resource/65fe42b0-d922-4a2d-9ff4-455b1b52f0b1/download/nota-metodologica-pin-general-y-severidad-intersectorial-colombia-2024.pdf
  format: null
  id: resource_65fe42b0
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Nota metodol\xF3gica PiN General y Severidad Intersectorial - Colombia 2024.pdf"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia - PiN General y Severidad Intersectorial 2024 (Nota metodol\xF3\
    gica desagregaci\xF3n de grupos vulnerables - Colombia 2024.pdf)"
  download_url: https://data.humdata.org/dataset/012fda67-d322-4450-bb0f-cfd6b1286c74/resource/f8b7a7ac-8043-4c43-9e06-ecf7826c2267/download/nota-metodologica-desagregacion-de-grupos-vulnerables-colombia-2024.pdf
  format: null
  id: resource_f8b7a7ac
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Nota metodol\xF3gica desagregaci\xF3n de grupos vulnerables - Colombia 2024.pdf"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Nota metodol\xF3gica predicciones des.masivo_confinamiento_var.climatica\
    \ - Colombia 2024.pdf"
  download_url: https://data.humdata.org/dataset/012fda67-d322-4450-bb0f-cfd6b1286c74/resource/e2469b48-f925-44eb-92c9-20206b0c9ad0/download/nota-metodologica-predicciones-des.masivo_confinamiento_var.climatica-colombia-2024.pdf
  format: null
  id: resource_e2469b48
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Nota metodol\xF3gica predicciones des.masivo_confinamiento_var.climatica\
    \ - Colombia 2024.pdf"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_pingeneralyseveridadinter_20240219
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
  end: null
  start: '2024-02-19'
temporal_resolution: null
title: Colombia - PiN General y Severidad Intersectorial 2024
version: null
vulnerability: null
---
