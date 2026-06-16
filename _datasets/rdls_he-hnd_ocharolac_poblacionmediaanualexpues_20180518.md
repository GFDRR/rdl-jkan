---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Instituto Hondure\xF1o de Ciencias de la Tierra (IHCIT)"
    url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-terremotos-2012
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "El Instituto Nacional de Estad\xEDstica (INE)"
    url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-terremotos-2012
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-terremotos-2012
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-terremotos-2012
dataset_id: rdls_he-hnd_ocharolac_poblacionmediaanualexpues_20180518
description: "El indicador estima la poblaci\xF3n anualmente expuesta que habita en\
  \ \xE1reas con amenaza s\xEDsmica en base al Mapa de Amenaza de Sismos resultado\
  \ del 'an\xE1lisis de m\xE1xima aceleraci\xF3n del suelo para un periodo de retorno\
  \ de 500 a\xF1os que representa la m\xE1xima aceleraci\xF3n horizontal del suelo\
  \ esperada para los pr\xF3ximos 50 a\xF1os- IHCIT,2012'. El resultado es la composici\xF3\
  n de capas de las zonas con una amenaza alta o muy alta y el total de la poblaci\xF3\
  n que habita sobre dicha \xE1rea.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-terremotos-2012]"
details: "* [INFORM Honduras.](http://www.inform-index.org/Subnational/Honduras) *\
  \ Dimensi\xF3n: Peligro y Exposici\xF3n * Categor\xEDa: Peligros Naturales * Componente:\
  \ Terremoto"
exposure:
- asset_type:
    description: Annual average population exposed to high and very high seismic hazard
      zones
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
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 1
    events:
    - calculation_method: simulated
      description: Probabilistic earthquake ground motion hazard model representing
        maximum horizontal soil acceleration for a 500-year return period
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_earthquake
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_500yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.002
          probability: null
          return_period: 500
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The dataset integrates a probabilistic seismic hazard map (maximum
    horizontal soil acceleration at 500-year return period from IHCIT) with national
    population data (INE) through spatial overlay analysis to estimate the annual
    average population exposed to high and very high earthquake hazard zones in Honduras.
  sources:
  - id: source_1
    license: null
    name: "Instituto Hondure\xF1o de Ciencias de la Tierra (IHCIT)"
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: "El Instituto Nacional de Estad\xEDstica (INE)"
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/honduras-poblacion-media-anual-expuesta-a-terremotos-2012
  rel: source
loss: null
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
  description: "Poblaci\xF3n promedio anual expuesta que habita en \xE1reas propensas\
    \ a amenaza s\xEDsmica."
  download_url: https://data.humdata.org/dataset/da4c0739-d6ee-47ae-bcc9-4fe99ce7748a/resource/1af8e6c2-0ef6-4a33-be97-8126040a794f/download/1-pe.nat.trm-abs-poblacion-media-anual-expuesta-a-terremotos-absoluto.xlsx
  format: null
  id: resource_1af8e6c2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "1-PE.NAT.TRM-ABS - Poblaci\xF3n Media Anual Expuesta a Terremotos (absoluto).xlsx"
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-hnd_ocharolac_poblacionmediaanualexpues_20180518
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
title: "Honduras Poblaci\xF3n Media Anual Expuesta a Terremotos 2012"
version: null
vulnerability: null
---
