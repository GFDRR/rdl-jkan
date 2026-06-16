---
attributions:
- entity:
    affiliation: null
    email: null
    name: DesInventar
    url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-sequia-2000-2015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Comit\xE9 Interinstitucional de Gesti\xF3n de Riesgo por Sequ\xEDa"
    url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-sequia-2000-2015
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Instituto Nacional de Estad\xEDstica (INE)"
    url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-sequia-2000-2015
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-sequia-2000-2015
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-sequia-2000-2015
dataset_id: rdls_hl-hnd_ocharolac_poblacionmediaanualexpues_20180518
description: "El indicador presenta la poblaci\xF3n anual promedio afectada por sequ\xED\
  a, seg\xFAn registros hist\xF3ricos del 2000-2015, en la base de datos DesInventar\
  \ y para el evento del sequia del 2015 realizado por el Comit\xE9 Interinstitucional\
  \ de Gesti\xF3n de Riesgo por Sequ\xEDa.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-sequia-2000-2015]"
details: "* [INFORM Honduras.](http://www.inform-index.org/Subnational/Honduras) *\
  \ Dimensi\xF3n: Peligro y Exposici\xF3n * Categor\xEDa: Peligros Naturales * Componente:\
  \ Sequ\xEDa"
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
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
license: CC-BY-4.0
lineage:
  description: Annual average population affected by drought was calculated from historical
    drought event records in the DesInventar database (2000-2015) and supplemented
    with data from the Interinstitutional Drought Risk Management Committee for the
    2015 drought event, using population statistics from the National Statistics Institute
    to quantify exposure.
  sources:
  - id: source_1
    license: null
    name: DesInventar
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "Comit\xE9 Interinstitucional de Gesti\xF3n de Riesgo por Sequ\xEDa"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: "Instituto Nacional de Estad\xEDstica (INE)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-sequia-2000-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Annual average population affected by drought events from 2000-2015
      and 2015 drought event
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
  description: "Honduras Poblaci\xF3n Media Anual Expuesta a Sequ\xEDa 2000-2015 (Poblaci\xF3\
    n promedio anual afectada por sequ\xEDa.)"
  download_url: https://data.humdata.org/dataset/f47aac91-c94a-4e1d-a49a-bf1c24e00e13/resource/37e28bfa-e35a-4c78-a932-99ac9a6a750e/download/6-pe.nat.sqa-abs-poblacion-media-anual-afectada-por-sequia.xlsx
  format: null
  id: resource_37e28bfa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "6- PE.NAT.SQA-ABS - Poblaci\xF3n Media Anual Afectada por Sequ\xEDa.xlsx"
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-hnd_ocharolac_poblacionmediaanualexpues_20180518
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-18'
temporal_resolution: null
title: "Honduras Poblaci\xF3n Media Anual Expuesta a Sequ\xEDa 2000-2015"
version: null
vulnerability: null
---
