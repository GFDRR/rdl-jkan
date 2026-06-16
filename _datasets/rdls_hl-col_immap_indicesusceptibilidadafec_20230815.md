---
attributions:
- entity:
    affiliation: null
    email: null
    name: DANE
    url: https://data.humdata.org/dataset/indice-susceptibilidad-afectaciones-fenomeno-de-el-nino-cluster-san
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: SIVIGILA
    url: https://data.humdata.org/dataset/indice-susceptibilidad-afectaciones-fenomeno-de-el-nino-cluster-san
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IDEAM
    url: https://data.humdata.org/dataset/indice-susceptibilidad-afectaciones-fenomeno-de-el-nino-cluster-san
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/indice-susceptibilidad-afectaciones-fenomeno-de-el-nino-cluster-san
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/indice-susceptibilidad-afectaciones-fenomeno-de-el-nino-cluster-san
dataset_id: rdls_hl-col_immap_indicesusceptibilidadafec_20230815
description: "Esta base contiene los datos utilizados en el c\xE1lculo del \xEDndice\
  \ de afectaci\xF3n y susceptibilidad en Inseguridad alimentaria y desnutrici\xF3\
  n aguda por el Fen\xF3meno de El Ni\xF1o a nivel municipal. Los c\xE1lculos se realizaron\
  \ a partir de fuentes oficiales como DANE, SIVIGILA, IDEAM y cumple con los criterios\
  \ estad\xEDsticos como temporalidad, representatividad y municipalizaci\xF3n de\
  \ la informaci\xF3n.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indice-susceptibilidad-afectaciones-fenomeno-de-el-nino-cluster-san]"
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: inferred
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Municipal-level susceptibility and impact index calculated from standardized\
    \ indicators of acute malnutrition, food insecurity, and climate conditions derived\
    \ from official Colombian sources (DANE, SIVIGILA, IDEAM). Data was standardized\
    \ and aggregated to municipal administrative units to assess population vulnerability\
    \ to El Ni\xF1o drought phenomenon impacts on food security and nutrition."
  sources:
  - id: source_1
    license: null
    name: DANE
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: SIVIGILA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: IDEAM
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/indice-susceptibilidad-afectaciones-fenomeno-de-el-nino-cluster-san
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: "Population susceptible to acute food insecurity and malnutrition\
      \ from El Ni\xF1o drought conditions"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  - asset_category: agriculture
    asset_dimension: product
    description: "Agricultural production affected by El Ni\xF1o-induced drought with\
      \ impacts on food security"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base contiene informaci\xF3n relevante sobre: i. prevalencia\
    \ desnutrici\xF3n estandarizado, ii. bajo peso estandarizado, iii. inflaci\xF3\
    n est\xE1ndar y iii. personas susceptibles al Fen\xF3meno del Ni\xF1o."
  download_url: https://data.humdata.org/dataset/fdb7dd18-008b-4787-850e-d97eecbd9528/resource/32013730-801a-4e21-8bab-fcdd26f24a73/download/indice-susceptibilidad-afectaciones-fenomeno-de-el-nino-cluster-san.xlsx
  format: null
  id: resource_32013730
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "\xCDndice susceptibilidad afectaciones Fen\xF3meno de El Ni\xF1o - Cl\xFA\
    ster SAN.xlsx"
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-col_immap_indicesusceptibilidadafec_20230815
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
  start: '2023-08-15'
temporal_resolution: null
title: "Colombia - \xCDndice susceptibilidad afectaciones Fen\xF3meno de El Ni\xF1\
  o - Cl\xFAster SAN"
version: null
vulnerability: null
---
