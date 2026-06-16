---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/elementos-_expuestos_efm_2025
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/elementos-_expuestos_efm_2025
dataset_id: rdls_exp-col_ochacol_elementosexpuestospredicc_2025
description: "Datos sobre los elementos expuestos en zonas susceptibles a inundaciones,\
  \ sequ\xEDas meteorol\xF3gicas y deslizamientos durante el primer trimestre de 2025.\
  \ El archivo de Excel incluye 12 hojas con informaci\xF3n detallada sobre: Personas,\
  \ hogares y viviendas. Zonas de cultivos. Instituciones educativas Centros de salud.\
  \ En zonas susceptibles de inundaci\xF3n, sequ\xEDa meteorol\xF3gica y deslizamientos\
  \ para el primer trimestre del a\xF1o, as\xED mismo se adiciono para cada resultado\
  \ el nivel de riesgo para cada municipio a partir del \xCDndice Municipal de Riesgo\
  \ Ajustado por Capacidades desarrollado por el DNP. Las fuentes de informaci\xF3\
  n utilizadas son el IDEAM, el DANE, DNP - Cl\xFAster de Salud y UNICEF Emergencias..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/elementos-_expuestos_efm_2025]"
details: The sources of information used are IDEAM, DANE, DNP - Health Cluster and
  UNICEF Emergencies.
exposure:
- asset_type:
    description: Urban and rural population exposed to hydrometeorological hazards
      by municipality
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Agricultural land use by crop type exposed to hydrometeorological
      hazards
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Educational institutions exposed to hydrometeorological hazards
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_3
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Multiple geospatial datasets representing exposed elements (population,
    agriculture, education facilities, health centers) were integrated into a unified
    framework and subjected to spatial join analysis (point-in-polygon) to determine
    exposure to hydrometeorological hazard zones (flooding, drought, landslides) at
    the municipal level for Q1 2025. Municipal risk indices (IMGRAC) were calculated
    and appended to characterize relative risk capacity.
  sources:
  - id: source_1
    license: null
    name: Multiple sources(see comments for full list)
    risk_data_type:
    - exposure
    type: null
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/elementos-_expuestos_efm_2025
  rel: source
loss: null
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
  description: "Datos sobre los elementos expuestos en zonas susceptibles a inundaciones,\
    \ sequ\xEDas meteorol\xF3gicas y deslizamientos durante el primer trimestre de\
    \ 2025. El n\xFAmero de personas y hogares expuestos se calculan a partir de la\
    \ superposici\xF3n de las capas de afectaci\xF3n con el Marco Geostadistico Nacional\
    \ del Censo 2018 DANE. El archivo de Excel incluye 12 hojas con informaci\xF3\
    n detallada sobre: Personas, hogares y viviendas. Zonas de cultivos. Instituciones\
    \ educativas Centros de salud. En zonas susceptibles de inundaci\xF3n, sequ\xED\
    a meteorol\xF3gica y deslizamientos para el primer trimestre del a\xF1o, as\xED\
    \ mismo se adiciono para cada resultado el nivel de riesgo para cada municipio\
    \ a partir del \xCDndice Municipal de Riesgo Ajustado por Capacidades desarrollado\
    \ por el DNP. Las fuentes de informaci\xF3n utilizadas son el IDEAM, el DANE,\
    \ DNP - Cl\xFAster de Salud y UNICEF Emergencias."
  download_url: https://data.humdata.org/dataset/23d428d2-1572-44e0-bee6-edf3df2ff481/resource/13d63255-c07f-494f-8fb8-7bb35f9cc500/download/elementos-_expuestos_efm_2025-1.xlsx
  format: null
  id: resource_13d63255
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Elementos _Expuestos_EFM_2025 1.xlsx
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-col_ochacol_elementosexpuestospredicc_2025
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
  end: '2025-03-31'
  start: '2025-01-01'
temporal_resolution: null
title: "Colombia - Elementos Expuestos-Predicci\xF3n Impactos por Fen\xF3menos Hidrometeorol\xF3\
  gicos"
version: null
vulnerability: null
---
