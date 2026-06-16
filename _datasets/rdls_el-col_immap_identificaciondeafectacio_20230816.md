---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    url: https://data.humdata.org/dataset/identificacion-de-afectacion-multiple-en-los-municipios-de-colombia
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Departamento Administrativo Nacional de Estad\xEDstica (DANE)"
    url: https://data.humdata.org/dataset/identificacion-de-afectacion-multiple-en-los-municipios-de-colombia
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/identificacion-de-afectacion-multiple-en-los-municipios-de-colombia
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/identificacion-de-afectacion-multiple-en-los-municipios-de-colombia
dataset_id: rdls_el-col_immap_identificaciondeafectacio_20230816
description: "Para identificar situaciones de afectaci\xF3n m\xFAltiple, se hizo la\
  \ b\xFAsqueda de indicadores o informaci\xF3n estad\xEDstica agregada en los diferentes\
  \ sistemas de informaci\xF3n de las entidades oficiales del pa\xEDs, en los registros\
  \ de inter\xE9s p\xFAblico. Se seleccionaron los siguientes indicadores: la tasa\
  \ de deserci\xF3n, la cobertura neta, la proporci\xF3n de estudiantes en extraedad,\
  \ matriculados provenientes de Venezuela, poblaci\xF3n afectada por emergencias\
  \ de origen natural reportados por la Unidad Nacional para la Gesti\xF3n del Riesgo\
  \ de Desastres (UNGRD), el n\xFAmero de sedes afectadas, y matriculados afectados\
  \ por ola invernal seg\xFAn el Ministerio de Educaci\xF3n (MEN); adicionalmente,\
  \ se utiliz\xF3 el \xCDndice de Riesgo de Victimizaci\xF3n (IRV), presencia de cultivos\
  \ de coca y el indicador personas en necesidad PiN del Cl\xFAster de Educaci\xF3\
  n en Emergencias para el a\xF1o 2023.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/identificacion-de-afectacion-multiple-en-los-municipios-de-colombia]"
details: null
exposure:
- asset_type:
    description: School-age population (students) by municipality, including Venezuelan
      migrants and vulnerable subgroups
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
    description: Educational facilities (school seats/establishments) by municipality
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC0-1.0
lineage:
  description: Municipal-level data aggregated from official Colombian government
    information systems (UNGRD disaster records, DANE census and education statistics)
    to identify multiple vulnerability indicators in education sector. Data compiled
    by iMMAP through systematic search of public registries to characterize affected
    populations and infrastructure in municipalities experiencing natural hazard impacts
    and education disruption.
  sources:
  - id: source_1
    license: null
    name: "Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres (UNGRD)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "Departamento Administrativo Nacional de Estad\xEDstica (DANE)"
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/identificacion-de-afectacion-multiple-en-los-municipios-de-colombia
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by natural hazard emergencies reported by UNGRD
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Educational facilities affected by natural hazard emergencies
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
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Documento metodol\xF3gico que evidencia como salieron los resultados\
    \ para el an\xE1lisis de la Afectaci\xF3n M\xFAltiple en el cl\xFAster de Educaci\xF3\
    n en Emergencias."
  download_url: https://data.humdata.org/dataset/584a6313-9edc-4360-9841-989d51735270/resource/7d06d511-12cf-4ab0-9766-f29080f5918b/download/documento_metodologico_eee_afectacionmultiple.pdf
  format: null
  id: resource_7d06d511
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Documento_metodol\xF3gico_EeE_Afectaci\xF3nM\xFAltiple.pdf"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene informaci\xF3n relevante que se utiliz\xF3 en la\
    \ identificaci\xF3n de afectaci\xF3n m\xFAltiple en los municipios de Colombia."
  download_url: https://data.humdata.org/dataset/584a6313-9edc-4360-9841-989d51735270/resource/a38f3183-9595-4f86-af6d-9491299c9251/download/datos-identificacion-multiple-afectacion-en-municipios-de-colombia.xlsx
  format: null
  id: resource_a38f3183
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Datos identificaci\xF3n m\xFAltiple afectaci\xF3n en municipios de Colombia.xlsx"
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-col_immap_identificaciondeafectacio_20230816
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
  start: '2023-08-16'
temporal_resolution: null
title: "Identificaci\xF3n de afectaci\xF3n m\xFAltiple en los municipios de Colombia,\
  \ Cl\xFAster Educaci\xF3n en Emergencias."
version: null
vulnerability: null
---
