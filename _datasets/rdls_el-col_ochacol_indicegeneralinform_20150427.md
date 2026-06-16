---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM Index Methodology
    url: https://data.humdata.org/dataset/indice-inform
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/indice-inform
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/indice-inform
dataset_id: rdls_el-col_ochacol_indicegeneralinform_20150427
description: "\xCDndice compuesto para la gesti\xF3n del riesgo (INFORM) es una herramienta\
  \ para el an\xE1lisis del riesgo humanitario, permite cuantificar el riesgo de tener\
  \ una crisis o desastre en cada pa\xEDs. Identifica municipios en riesgo y factores\
  \ asociados con crisis humanitaria. Analiza como el riesgo cambia con el tiempo.\
  \ Riesgo = amenaza x vulnerabilidad x falta de capacidad de respuesta.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/indice-inform]"
details: "Ver \xCDndice INFORM NNA - Colombia : https://data.hdx.rwlabs.org/dataset/indice-inform-nna-colombia"
exposure:
- asset_type:
    description: Population exposure to humanitarian crises and disasters at municipal
      level
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
hazard: null
license: CC-BY-4.0
lineage:
  description: "INFORM Colombia aggregates multiple datasets from various sources\
    \ to calculate a composite humanitarian risk index at municipal level using the\
    \ formula Risk = Hazard \xD7 Vulnerability \xD7 Lack of Coping Capacity. The dataset\
    \ includes separate components for hazard (AMENAZA), vulnerability (VULNERABILIDAD),\
    \ and response capacity (FALTA DE CAPACIDAD DE RESPUESTA), integrated into overall\
    \ risk scores that track temporal changes in crisis probability."
  sources:
  - id: source_1
    license: null
    name: INFORM Index Methodology
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/indice-inform
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Humanitarian crisis risk from conflict and violence
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
    description: Humanitarian crisis risk from natural disasters including floods
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
  description: "\xCDndice General INFORM- Colombia (Variables INFORM)"
  download_url: https://data.humdata.org/dataset/5278ac8c-75a7-4ee8-a79e-f8ea7d186c0e/resource/7a7b1374-ebee-497b-9719-23f77c116ec6/download/base-original-inform.xlsx
  format: null
  id: resource_7a7b1374
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Variables INFORM
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice General INFORM- Colombia (Variables INFORM.csv)"
  download_url: https://data.humdata.org/dataset/5278ac8c-75a7-4ee8-a79e-f8ea7d186c0e/resource/d629704f-29c5-4e8d-808a-7b6f76586d6f/download/variables-inform.csv
  format: null
  id: resource_d629704f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Variables INFORM.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice General INFORM- Colombia (RESULTADOS INFORM.csv)"
  download_url: https://data.humdata.org/dataset/5278ac8c-75a7-4ee8-a79e-f8ea7d186c0e/resource/534c4862-1f4a-4458-84ff-794fe67116c1/download/resultados-inform.csv
  format: null
  id: resource_534c4862
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RESULTADOS INFORM.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice General INFORM- Colombia (CSV)"
  download_url: https://data.humdata.org/dataset/5278ac8c-75a7-4ee8-a79e-f8ea7d186c0e/resource/5a9f1d1e-ed47-432a-9fd8-43c03d162dce/download/amenaza.csv
  format: null
  id: resource_5a9f1d1e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AMENAZA.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice General INFORM- Colombia (CSV)"
  download_url: https://data.humdata.org/dataset/5278ac8c-75a7-4ee8-a79e-f8ea7d186c0e/resource/f224c71c-fac3-40cb-acd3-5228281d65ff/download/vulnerabilidad.csv
  format: null
  id: resource_f224c71c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VULNERABILIDAD.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice General INFORM- Colombia (FALTA DE CAPACIDAD DE RESPUESTA.csv)"
  download_url: https://data.humdata.org/dataset/5278ac8c-75a7-4ee8-a79e-f8ea7d186c0e/resource/4553e311-5837-4511-a6c1-3291c49a5143/download/falta-de-capacidad-de-respuesta.csv
  format: null
  id: resource_4553e311
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FALTA DE CAPACIDAD DE RESPUESTA.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice General INFORM- Colombia (20151005 RESULTADOS INFORM (1).xlsx)"
  download_url: https://data.humdata.org/dataset/5278ac8c-75a7-4ee8-a79e-f8ea7d186c0e/resource/272f0339-9538-41a7-9422-52ca182c95d9/download/20151005-resultados-inform-1.xlsx
  format: null
  id: resource_272f0339
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20151005 RESULTADOS INFORM (1).xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-col_ochacol_indicegeneralinform_20150427
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
  start: '2015-04-27'
temporal_resolution: null
title: "\xCDndice General INFORM- Colombia"
version: null
vulnerability: null
---
