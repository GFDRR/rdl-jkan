---
attributions:
- entity:
    affiliation: null
    email: null
    name: CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data)
    url: https://data.humdata.org/dataset/colombia-precipitaciones-y-eventos-de-inundaciones-1990-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-precipitaciones-y-eventos-de-inundaciones-1990-2020
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/colombia-precipitaciones-y-eventos-de-inundaciones-1990-2020
dataset_id: rdls_hel-col_3is_precipitacionesyeventosde_2014
description: "Esta base de datos compila informaci\xF3n detallada sobre los eventos\
  \ de inundaciones ocurridos en Colombia entre 1990 y 2020, enriquecida con datos\
  \ de precipitaci\xF3n asociados a cada evento. La precipitaci\xF3n diaria se ha\
  \ obtenido de la fuente CHIRPS (Climate Hazards Group InfraRed Precipitation with\
  \ Station data), una de las referencias m\xE1s confiables para datos clim\xE1ticos\
  \ a nivel global. La integraci\xF3n de datos de inundaciones con informaci\xF3n\
  \ precisa de precipitaci\xF3n permite un an\xE1lisis profundo de los patrones asociados\
  \ al fen\xF3meno de La Ni\xF1a, un evento clim\xE1tico que ha tenido un impacto\
  \ significativo en la regi\xF3n. Esta base de datos es una herramienta invaluable\
  \ para quienes est\xE1n involucrados en la investigaci\xF3n y modelado de fen\xF3\
  menos clim\xE1ticos, as\xED como en la planificaci\xF3n y prevenci\xF3n de desastres.\
  \ Adem\xE1s de su utilidad para estudios hist\xF3ricos, esta base de datos puede\
  \ servir como insumo en modelos predictivos para anticipar futuros eventos relacionados\
  \ con La Ni\xF1a, contribuyendo a la toma de decisiones informadas y a la implementaci\xF3\
  n de medidas de mitigaci\xF3n en sectores vulnerables.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/colombia-precipitaciones-y-eventos-de-inundaciones-1990-2020]"
details: null
exposure:
- asset_type:
    description: Residential and community buildings affected by flood events
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Roads, bridges, water supply and sanitation infrastructure damaged
      by floods
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
- asset_type:
    description: Population exposed to flood events in Colombian municipalities
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_3
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
      intensity_measure: Precip:mm
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Post-event flood occurrence data from Colombian administrative records\
    \ (1990-2020) was integrated with daily precipitation measurements from CHIRPS\
    \ to create a comprehensive database linking rainfall patterns to documented flood\
    \ events. The dataset enables analysis of precipitation-flood associations and\
    \ La Ni\xF1a climate phenomenon impacts on Colombian flood hazards."
  sources:
  - id: source_1
    license: null
    name: CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/colombia-precipitaciones-y-eventos-de-inundaciones-1990-2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct fatalities from flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: Precip:mm
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Direct injuries from flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: Precip:mm
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displaced by flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: Precip:mm
      process: null
      trigger: null
      type: flood
    id: loss_3
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
  - asset_category: buildings
    asset_dimension: structure
    description: Residential buildings destroyed or damaged by floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: Precip:mm
      process: null
      trigger: null
      type: flood
    id: loss_4
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
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural land area affected by flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: Precip:mm
      process: null
      trigger: null
      type: flood
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Esta base de datos compila informaci\xF3n detallada sobre los eventos\
    \ de inundaciones ocurridos en Colombia entre 1990 y 2020, enriquecida con datos\
    \ de precipitaci\xF3n asociados a cada evento. La precipitaci\xF3n diaria se ha\
    \ obtenido de la fuente CHIRPS (Climate Hazards Group InfraRed Precipitation with\
    \ Station data), una de las referencias m\xE1s confiables para datos clim\xE1\
    ticos a nivel global. La integraci\xF3n de datos de inundaciones con informaci\xF3\
    n precisa de precipitaci\xF3n permite un an\xE1lisis profundo de los patrones\
    \ asociados al fen\xF3meno de La Ni\xF1a, un evento clim\xE1tico que ha tenido\
    \ un impacto significativo en la regi\xF3n. Esta base de datos es una herramienta\
    \ invaluable para quienes est\xE1n involucrados en la investigaci\xF3n y modelado\
    \ de fen\xF3menos clim\xE1ticos, as\xED como en la planificaci\xF3n y prevenci\xF3\
    n de desastres. Adem\xE1s de su utilidad para estudios hist\xF3ricos, esta base\
    \ de datos puede servir como insumo en modelos predictivos para anticipar futuros\
    \ eventos relacionados con La Ni\xF1a, contribuyendo a la toma de decisiones informadas\
    \ y a la implementaci\xF3n de medidas de mitigaci\xF3n en sectores vulnerables."
  download_url: https://data.humdata.org/dataset/5501ca60-ece4-4dd1-8063-aadcf9895377/resource/8b550712-79ef-4ef7-aff2-cf2aa3bab83a/download/datos_precipitaciones_inundaciones_1990_2020_colombia.xlsx
  format: null
  id: resource_8b550712
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Datos_Precipitaciones_Inundaciones_1990_2020_Colombia.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-col_3is_precipitacionesyeventosde_2014
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
  end: '2020-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: Colombia - Precipitaciones y Eventos de Inundaciones - 1990 - 2020
version: null
vulnerability: null
---
