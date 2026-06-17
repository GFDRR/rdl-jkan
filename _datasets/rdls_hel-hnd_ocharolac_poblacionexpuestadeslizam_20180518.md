---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Instituto Hondure\xF1o de Ciencias de la Tierra (IHCIT)"
    url: https://data.humdata.org/dataset/honduras-poblacion-expuesta-a-deslizamientos-2012
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Instituto Nacional de Estad\xEDstica (INE)"
    url: https://data.humdata.org/dataset/honduras-poblacion-expuesta-a-deslizamientos-2012
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-expuesta-a-deslizamientos-2012
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-expuesta-a-deslizamientos-2012
dataset_id: rdls_hel-hnd_ocharolac_poblacionexpuestadeslizam_20180518
description: "El indicador estima la poblaci\xF3n expuesta que habita en zonas propensa\
  \ a deslizamientos, en base al Mapa de Susceptibilidad a Movimientos de Laderas.\
  \ El resultado es la composici\xF3n de capas de las zonas con una amenaza alta o\
  \ muy alta y el total de la poblaci\xF3n que habita sobre dicha \xE1rea.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/honduras-poblacion-expuesta-a-deslizamientos-2012]"
details: "* [INFORM Honduras.](http://www.inform-index.org/Subnational/Honduras) *\
  \ Dimensi\xF3n: Peligro y Exposici\xF3n * Categor\xEDa: Peligros Naturales * Componente:\
  \ Deslizamiento"
exposure:
- asset_type:
    description: Population residing in landslide-prone zones classified by susceptibility
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
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-4.0
lineage:
  description: Landslide susceptibility zones from IHCIT were overlaid with population
    distribution data from INE census to estimate the absolute number of people residing
    in areas classified as high or very high landslide hazard. The result is a spatial
    composition of susceptible zones and the total exposed population inhabiting those
    areas.
  sources:
  - id: source_1
    license: null
    name: "Instituto Hondure\xF1o de Ciencias de la Tierra (IHCIT)"
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: "Instituto Nacional de Estad\xEDstica (INE)"
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/honduras-poblacion-expuesta-a-deslizamientos-2012
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to landslide hazard in high and very high susceptibility
      zones
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: "Honduras Poblaci\xF3n Expuesta a Deslizamientos 2012 (Poblaci\xF3\
    n expuesta que habita en zonas susceptibles a movimientos de laderas.)"
  download_url: https://data.humdata.org/dataset/92a24a44-b37d-4afe-a493-5e2184e2a563/resource/717ca106-dd46-4ed9-8a3b-57d6ed55c8bf/download/5-pe.nat.dlz-abs-poblacion-expuesta-a-deslizamientos-absoluto.xlsx
  format: null
  id: resource_717ca106
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "5-PE.NAT.DLZ-ABS - Poblaci\xF3n Expuesta a Deslizamientos (absoluto).xlsx"
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-hnd_ocharolac_poblacionexpuestadeslizam_20180518
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
title: "Honduras Poblaci\xF3n Expuesta a Deslizamientos 2012"
version: null
vulnerability: null
---
