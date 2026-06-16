---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Unidad para la Atenci\xF3n Integral y Reparaci\xF3n a las V\xEDctimas (UARIV)"
    url: https://data.humdata.org/dataset/victimas-del-conflicto-armado-colombiano-por-hechos-registrados-entre-2017-y-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/victimas-del-conflicto-armado-colombiano-por-hechos-registrados-entre-2017-y-2021
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/victimas-del-conflicto-armado-colombiano-por-hechos-registrados-entre-2017-y-2021
dataset_id: rdls_lss-col_immap_victimasdelconflictoarmad_2017
description: "Esta base de datos, extra\xEDda del portal de datos abiertos de la Unidad\
  \ para la Atenci\xF3n Integral y Reparaci\xF3n a las V\xEDctimas, contiene el n\xFA\
  mero de v\xEDctimas por hechos del conflicto armado en Colombia entre 2017-2021\
  \ desagregado por hecho victimizante, departamento de ocurrencia, sexo, etnia y\
  \ condici\xF3n de discapacidad. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/victimas-del-conflicto-armado-colombiano-por-hechos-registrados-entre-2017-y-2021]"
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: Administrative registry data extracted from the Colombian government's
    UARIV open data portal, documenting individual victimization events from armed
    conflict between 2017-2021, disaggregated by victimization type, department, sex,
    ethnicity, and disability status to enable impact assessment and reparations planning.
  sources:
  - id: source_1
    license: null
    name: "Unidad para la Atenci\xF3n Integral y Reparaci\xF3n a las V\xEDctimas (UARIV)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/victimas-del-conflicto-armado-colombiano-por-hechos-registrados-entre-2017-y-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population from armed conflict violence events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Internally displaced persons from armed conflict events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  - asset_category: population
    asset_dimension: population
    description: Deaths from armed conflict violence
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
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
  description: "V\xEDctimas del conflicto armado colombiano por hechos registrados\
    \ entre 2017 y 2021 (Excel)"
  download_url: https://data.humdata.org/dataset/1b2b2d17-c66a-4f67-bdbd-9bc7d32c2c04/resource/d14adc69-7ce2-43b1-91f5-c0ea2e973055/download/victimas_hecho_dpto_2017_2021.xlsx
  format: null
  id: resource_d14adc69
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: victimas_hecho_dpto_2017_2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_immap_victimasdelconflictoarmad_2017
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
  end: '2021-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: "V\xEDctimas del conflicto armado colombiano por hechos registrados entre 2017\
  \ y 2021"
version: null
vulnerability: null
---
