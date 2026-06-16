---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/base-de-datos-infograma-primer-semestre-del-2016
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/base-de-datos-infograma-primer-semestre-del-2016
dataset_id: rdls_lss-col_ochacol_basededatosinfogramaprime_2016
description: 'Tasas departamentales, municipales y tasa nacional de variables como:
  desplazamiento, homicidios, Victimas de explosivos, desapariciones y personas afectadas
  por desastres naturales.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/base-de-datos-infograma-primer-semestre-del-2016]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: Administrative registry compiled by OCHA Colombia aggregating departmental
    and municipal-level impact data from conflict-violence and natural disaster events
    during the first semester of 2016, presented as rates and counts across multiple
    impact categories.
  sources:
  - id: source_1
    license: null
    name: OCHA Colombia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/base-de-datos-infograma-primer-semestre-del-2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People affected by natural disasters including floods at departmental
      and municipal levels
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
    description: Victims of explosives (interpreted as blast/explosive events) at
      departmental and municipal levels
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
  description: Datos oficiales tomados de UARIV, CODHES, DIJIN, INML, UNGRD y monitor
    de OCHA. Recopilado y organizado por UMAIC
  download_url: https://data.humdata.org/dataset/d0a48593-af8d-49b0-8d4f-39ce2f620108/resource/3fcb3189-97a2-4137-8ffb-f85219d0b3da/download/infograma-2016-i.xlsx
  format: null
  id: resource_3fcb3189
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: infograma 2016-I.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_basededatosinfogramaprime_2016
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
  end: '2016-06-30'
  start: '2016-01-01'
temporal_resolution: null
title: Colombia - Base de datos Infograma primer semestre del 2016
version: null
vulnerability: null
---
