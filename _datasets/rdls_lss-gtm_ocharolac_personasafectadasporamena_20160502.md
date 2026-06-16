---
attributions:
- entity:
    affiliation: null
    email: null
    name: "CONRED (Coordinadora Nacional Para la Reducci\xF3n de Desastres de Guatemala)"
    url: https://data.humdata.org/dataset/guatemala-personas-afectadas-por-amenazas-naturales-2015
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNICEF
    url: https://data.humdata.org/dataset/guatemala-personas-afectadas-por-amenazas-naturales-2015
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "G\xE1ndara & Asociados"
    url: https://data.humdata.org/dataset/guatemala-personas-afectadas-por-amenazas-naturales-2015
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/guatemala-personas-afectadas-por-amenazas-naturales-2015
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/guatemala-personas-afectadas-por-amenazas-naturales-2015
dataset_id: rdls_lss-gtm_ocharolac_personasafectadasporamena_20160502
description: 'Personas que han sido afectada por cualquier evento natural, ocurrido
  a nivel municipal.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/guatemala-personas-afectadas-por-amenazas-naturales-2015]'
details: "* [INFORM Guatemala.](http://www.inform-index.org/Subnational/Guatemala)\
  \ * Componente: Poblaci\xF3n Desprotegida * Categor\xEDa: Grupos Vulnerables * Dimensi\xF3\
  n: Vulnerabilidad"
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Municipal-level registry of people affected by natural hazard events
    in Guatemala compiled from CONRED records and partner organizations. Data aggregates
    impact counts across multiple hazard types (flood, strong wind, earthquake, landslide,
    volcanic) at the municipal administrative level for baseline risk assessment purposes.
  sources:
  - id: source_1
    license: null
    name: "CONRED (Coordinadora Nacional Para la Reducci\xF3n de Desastres de Guatemala)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: UNICEF
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: "G\xE1ndara & Asociados"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/guatemala-personas-afectadas-por-amenazas-naturales-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood events at municipal level in Guatemala
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
    description: Population affected by strong wind events at municipal level in Guatemala
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake events at municipal level in Guatemala
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
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
    description: Population affected by landslide events at municipal level in Guatemala
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
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by volcanic events at municipal level in Guatemala
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
    id: loss_5
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
  description: "Guatemala Personas Afectadas por Amenazas Naturales 2015 (Personas\
    \ afectadas por amenazas naturales a\xF1o 2015)"
  download_url: https://data.humdata.org/dataset/32fe6c3e-b5b8-46b1-b4e9-2d62d813cebf/resource/27e276e1-cee6-47f6-8778-db4898ad4ade/download/2.2.1.b-personas-afectadas-por-amenazas-naturales.xlsx
  format: null
  id: resource_27e276e1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2.2.1.B Personas afectadas por amenazas naturales.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_ocharolac_personasafectadasporamena_20160502
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-05-02'
temporal_resolution: null
title: Guatemala Personas Afectadas por Amenazas Naturales 2015
version: null
vulnerability: null
---
