---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/indice-inform-nna-colombia
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNICEF
    url: https://data.humdata.org/dataset/indice-inform-nna-colombia
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/indice-inform-nna-colombia
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/indice-inform-nna-colombia
dataset_id: rdls_el-col_ochacol_indiceinformnna_20150107
description: "INFORM ni\xF1os, ni\xF1as y adolescentes es un \xEDndice de gesti\xF3\
  n del riesgo con el objetivo de mitigar riesgos. Para tratar el tema del \xEDndice\
  \ INFORM de ni\xF1as, ni\xF1os y adolecentes al igual que INFORM general se trabajar\xE1\
  \ con las tres dimensiones - amenazas espec\xEDficas de NNA, vulnerabilidad y falta\
  \ de capacidad de respuesta-. La metodolog\xEDa est\xE1 enfocada en utilizar informaci\xF3\
  n desagregada de NNA dentro de los cuales se encuentra sismos, deslizamientos, inundaci\xF3\
  n, volc\xE1n, homicidios, ex\xE1menes m\xE9dicos por presunto delito sexual, desaparecidos,\
  \ violencia interpersonal, secuestros, expulsi\xF3n, recepci\xF3n, ex\xE1menes m\xE9\
  dicos por presunto delito sexual, violencia interpersonal, mortalidad por enfermedad\
  \ respiratoria aguda, mortalidad por enfermedad diarreica aguda, mortalidad materna,\
  \ alfabetismo y ni\xF1os en ruta de restablecimiento de derechos.. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/indice-inform-nna-colombia]"
details: "Ver \xCDndice General INFORM- Colombia: https://data.hdx.rwlabs.org/dataset/indice-inform"
exposure:
- asset_type:
    description: Children, adolescents and youth population disaggregated by age and
      gender in Colombia
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: INFORM NNA index integrates hazard exposure data (earthquakes, landslides,
    floods, volcanic activity), age and gender-disaggregated population exposure,
    and vulnerability/response capacity indicators for children, adolescents and youth
    in Colombia. Data compiled from OCHA and UNICEF sources using direct observational
    data and anecdotal information to produce a composite risk management index at
    sub-national administrative levels.
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
    name: UNICEF
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/indice-inform-nna-colombia
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population of children, adolescents and youth affected by earthquake
      hazard
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
    description: Population of children, adolescents and youth affected by landslide
      hazard
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  - asset_category: population
    asset_dimension: population
    description: Population of children, adolescents and youth affected by flood hazard
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population of children, adolescents and youth affected by volcanic
      hazard
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_4
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice INFORM NNA - Colombia (Excel)"
  download_url: https://data.humdata.org/dataset/5eaaadd3-c356-4479-bd7f-59993ad90a99/resource/0d22f513-8858-4684-95ff-fd2c44e469fc/download/150914resultados_finales.xlsx
  format: null
  id: resource_0d22f513
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 150914resultados_finales.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice INFORM NNA - Colombia (CSV)"
  download_url: https://data.humdata.org/dataset/5eaaadd3-c356-4479-bd7f-59993ad90a99/resource/c52e7601-e78a-4100-a444-52ddb22293b7/download/amenazas.csv
  format: null
  id: resource_c52e7601
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Amenazas.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice INFORM NNA - Colombia (Falta de Capacidad de Respuesta.csv)"
  download_url: https://data.humdata.org/dataset/5eaaadd3-c356-4479-bd7f-59993ad90a99/resource/c2dbfa01-d496-4773-bdd1-cd1658d25f93/download/falta-de-capacidad-de-respuesta.csv
  format: null
  id: resource_c2dbfa01
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Falta de Capacidad de Respuesta.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xCDndice INFORM NNA - Colombia (CSV)"
  download_url: https://data.humdata.org/dataset/5eaaadd3-c356-4479-bd7f-59993ad90a99/resource/5bd89096-45df-46cf-ad9f-b9430e4a6274/download/vulnerabilidad.csv
  format: null
  id: resource_5bd89096
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Vulnerabilidad.csv
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-col_ochacol_indiceinformnna_20150107
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
  start: '2015-01-07'
temporal_resolution: null
title: "\xCDndice INFORM NNA - Colombia"
version: null
vulnerability: null
---
