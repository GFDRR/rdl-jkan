---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/colombia-desplazamiento-y-confinamiento-probabilidad-y-estimacion-i-sem-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-desplazamiento-y-confinamiento-probabilidad-y-estimacion-i-sem-2025
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-desplazamiento-y-confinamiento-probabilidad-y-estimacion-i-sem-2025
dataset_id: rdls_lss-col_3is_desplazamientoyconfinamie_2025
description: "Datos sobre estimaci\xF3n de personas que pueden ser v\xEDctima por\
  \ desplazamiento individual, masivo y confinamientos y probabilidad de presentarse\
  \ eventos de desplazamiento y confinamiento para el primer semestre del a\xF1o 2025.\
  \ El archivo de Excel incluye 3 hojas con informaci\xF3n sobre: - Estimaci\xF3n_Desplaza_individual:\
  \ Estimaci\xF3n de personas que pueden ser v\xEDctimas por eventos de desplazamiento\
  \ individual y probabilidad de presentarse eventos de desplazamiento individual\
  \ en el primer semestre del a\xF1o 2025. - Estimaci\xF3n_Desplaza_masivo: Estimaci\xF3\
  n de personas que pueden ser v\xEDctimas por eventos de desplazamiento masivo y\
  \ probabilidad de presentarse eventos de desplazamiento masivos en el primer semestre\
  \ del a\xF1o 2025. - Estimaci\xF3n_Confinamiento: Estimaci\xF3n de personas que\
  \ pueden ser v\xEDctimas por eventos de confinamiento y probabilidad de presentarse\
  \ eventos de confinamientos en el primer semestre del a\xF1o 2025.. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/colombia-desplazamiento-y-confinamiento-probabilidad-y-estimacion-i-sem-2025]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Historical displacement and confinement event data (2008-2022) were
    integrated with updated registries (2023-2025) to construct a unified baseline.
    Probabilistic forecasting models were applied to estimate the probability and
    number of persons affected by individual displacement, mass displacement, and
    confinement events at municipal level for the first semester of 2025.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-desplazamiento-y-confinamiento-probabilidad-y-estimacion-i-sem-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Estimated number of persons displaced by individual displacement
      events in first semester 2025
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Estimated number of persons displaced by mass displacement events
      in first semester 2025
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
  - asset_category: population
    asset_dimension: population
    description: Estimated number of persons affected by confinement events in first
      semester 2025
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Colombia: Desplazamiento y Confinamiento - Probabilidad y estimaci\xF3\
    n (Excel)"
  download_url: https://data.humdata.org/dataset/c11e8a42-060c-4c6e-8c46-85f8f2dda50d/resource/eea88dcf-a4d2-4629-a3b6-81df6263a952/download/datos_estimacion.xlsx
  format: null
  id: resource_eea88dcf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Datos_estimaci\xF3n.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_desplazamientoyconfinamie_2025
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
  start: '2025-01-01'
temporal_resolution: null
title: "Colombia: Desplazamiento y Confinamiento - Probabilidad y estimaci\xF3n"
version: null
vulnerability: null
---
