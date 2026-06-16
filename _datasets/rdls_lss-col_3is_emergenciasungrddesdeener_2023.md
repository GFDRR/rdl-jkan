---
attributions:
- entity:
    affiliation: null
    email: null
    name: "UNGRD (Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres)"
    url: https://data.humdata.org/dataset/emergencias-ungrd-desde-enero-2023-a-agosto-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/emergencias-ungrd-desde-enero-2023-a-agosto-2024
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/emergencias-ungrd-desde-enero-2023-a-agosto-2024
dataset_id: rdls_lss-col_3is_emergenciasungrddesdeener_2023
description: 'Datos de emergencias de la UNGRD desde Enero 2023 a Agosto 2024 a nivel
  municipal mes a mes y con total de afectaciones reportadas. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/emergencias-ungrd-desde-enero-2023-a-agosto-2024]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Post-event emergency impact data compiled by UNGRD from January 2023
    to August 2024, aggregated monthly at municipal level across Colombian departments.
    Records include direct impacts on population, buildings, and infrastructure from
    various hazard events, primarily flooding based on column structure.
  sources:
  - id: source_1
    license: null
    name: "UNGRD (Unidad Nacional para la Gesti\xF3n del Riesgo de Desastres)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/emergencias-ungrd-desde-enero-2023-a-agosto-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings destroyed and affected by flood events
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Infrastructure damage including roads, bridges, water and sanitation
      systems
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected, injured, and deceased from flood events
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
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural land affected by flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_4
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Datos de emergencias de la UNGRD desde Enero 2023 a Agosto 2024 a nivel
    municipal
  download_url: https://data.humdata.org/dataset/dda7291b-3e0a-406c-9c44-3fe89949f7cd/resource/8fef3a20-87fd-4fa4-913c-b7d4103e1347/download/ungrd_2023_a_2024_agosto.xlsx
  format: null
  id: resource_8fef3a20
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNGRD_2023_A_2024_AGOSTO.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_3is_emergenciasungrddesdeener_2023
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
  end: '2024-08-31'
  start: '2023-01-01'
temporal_resolution: null
title: Colombia - Emergencias UNGRD desde Enero 2023 a Agosto 2024
version: null
vulnerability: null
---
