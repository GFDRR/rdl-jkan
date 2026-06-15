---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Instituto de Hidrolog\xEDa, Meteorolog\xEDa y Estudios Ambientales (IDEAM)"
    url: https://data.humdata.org/dataset/estimaciones-afectaciones-por-fenomenos-hidrometeorologicos_ii-sem_colombia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/estimaciones-afectaciones-por-fenomenos-hidrometeorologicos_ii-sem_colombia
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/estimaciones-afectaciones-por-fenomenos-hidrometeorologicos_ii-sem_colombia
dataset_id: rdls_hel-col_3is_estimacionesafectacionesp_2025
description: "Con base en los escenarios de predicci\xF3n del Instituto de Hidrolog\xED\
  a, Meteorolog\xEDa y Estudios Ambientales (IDEAM), se identificaron las zonas con\
  \ susceptibilidad a inundaciones y deslizamientos durante el segundo trimestre de\
  \ 2025. El archivo de Excel que acompa\xF1a esta publicaci\xF3n contiene ocho hojas\
  \ con informaci\xF3n desagregada sobre personas, hogares, viviendas, zonas de cultivos,\
  \ instituciones educativas y centros de salud localizados en zonas susceptibles.\
  \ Adem\xE1s, para cada municipio se incluye el nivel de riesgo estimado, calculado\
  \ mediante el \xCDndice Municipal de Riesgo Ajustado por Capacidades, desarrollado\
  \ por el Departamento Nacional de Planeaci\xF3n (DNP).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/estimaciones-afectaciones-por-fenomenos-hidrometeorologicos_ii-sem_colombia]"
details: This dataset is a forecast.
exposure:
- asset_type:
    description: Rural and urban population residing in flood-susceptible zones by
      municipality
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
    description: Residential dwellings and households in flood-susceptible zones,
      disaggregated by rural and urban areas
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Agricultural crop zones exposed to flood hazard
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_3
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Educational institutions and health facilities located in flood-susceptible
      zones
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_4
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IDEAM hydrometeorological prediction scenarios were used to identify
    flood and landslide susceptibility zones. Spatial analysis overlaid these hazard
    zones with administrative boundaries and asset inventories (population, dwellings,
    agricultural areas, educational and health facilities) to quantify exposure by
    municipality. Municipal risk indices (IMGRAC) were calculated to support disaster
    risk planning and management.
  sources:
  - id: source_1
    license: null
    name: "Instituto de Hidrolog\xEDa, Meteorolog\xEDa y Estudios Ambientales (IDEAM)"
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/estimaciones-afectaciones-por-fenomenos-hidrometeorologicos_ii-sem_colombia
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to flood hazard in susceptible zones for April-June
      2025
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Dwellings and households exposed to flood hazard in susceptible zones
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population exposed to landslide hazard in susceptible zones for April-June
      2025
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Dwellings and households exposed to landslide hazard in susceptible
      zones
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: "Colombia: Estimaciones afectaciones por fen\xF3menos hidrometeorol\xF3\
    gicos (Forecast data)"
  download_url: https://data.humdata.org/dataset/d85d0585-4122-4f3c-8df9-789659eb4cf4/resource/a0b94c74-ea90-4218-b81c-bcaa20db9580/download/elementos_expuestos_inundacion_amj_2025_hdx.xlsx
  format: null
  id: resource_a0b94c74
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Elementos_expuestos_inundaci\xF3n_AMJ_2025_HDX.xlsx"
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-col_3is_estimacionesafectacionesp_2025
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
  end: '2025-12-31'
  start: '2025-07-01'
temporal_resolution: null
title: "Colombia: Estimaciones afectaciones por fen\xF3menos hidrometeorol\xF3gicos"
version: null
vulnerability: null
---
