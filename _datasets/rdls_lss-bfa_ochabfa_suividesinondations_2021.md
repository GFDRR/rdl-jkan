---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Secr\xE9tariat Permanent du Conseil National de Secours d'Urgence et de\
      \ R\xE9habilitation (SP/CONASUR)"
    url: https://data.humdata.org/dataset/burkina-faso-suivi-des-inondations
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Burkina Faso
  url: https://data.humdata.org/dataset/burkina-faso-suivi-des-inondations
creator:
  affiliation: null
  email: null
  name: OCHA Burkina Faso
  url: https://data.humdata.org/dataset/burkina-faso-suivi-des-inondations
dataset_id: rdls_lss-bfa_ochabfa_suividesinondations_2021
description: "Ces donn\xE9es du CONASUR contiennent les informations sur l'impacts\
  \ des inondations au Burkina Faso en 2021, 2022, 2023 et 2024. Il contient le numbre\
  \ de personnes ou foyers affect\xE9s.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burkina-faso-suivi-des-inondations]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event flood impact data collected directly by CONASUR through
    observational and anecdotal methods across Burkina Faso regions from 2021-2024.
    Data includes affected population counts, household impacts, casualty figures,
    building destruction, and agricultural damage aggregated by administrative region
    and commune.
  sources:
  - id: source_1
    license: null
    name: "Secr\xE9tariat Permanent du Conseil National de Secours d'Urgence et de\
      \ R\xE9habilitation (SP/CONASUR)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burkina-faso-suivi-des-inondations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct flood impact on affected population and households in Burkina
      Faso
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
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding including destroyed habitats
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
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural losses from flooded fields measured in hectares
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Situation des inondations au Burkina Faso entre 2021 et 2024 d\xE9\
    sagr\xE9ger au niveau administratif 1 (HXL)."
  download_url: https://data.humdata.org/dataset/18f28ed5-ea97-4e26-bbb0-c7bb2d8b1abc/resource/37ac6749-6813-4760-ad51-f6c1c99f5263/download/bfa_inondation_2021-2024.xlsx
  format: null
  id: resource_37ac6749
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA Inondations 2021 - 2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Suivi des Inondations (Situation des inondations au
    BFA en 2023)'
  download_url: https://data.humdata.org/dataset/18f28ed5-ea97-4e26-bbb0-c7bb2d8b1abc/resource/09cef61d-b5fc-42c6-9cf5-99371e938b40/download/bfa_flood_2023.xlsx
  format: null
  id: resource_09cef61d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA Inondations 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Suivi des Inondations (Situation des inondations au
    BFA en 2022)'
  download_url: https://data.humdata.org/dataset/18f28ed5-ea97-4e26-bbb0-c7bb2d8b1abc/resource/10c6c885-607d-44d6-999d-055930f0afd6/download/conasur_situation-catastrophes_2022-innodation1.xlsx
  format: null
  id: resource_10c6c885
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA Inondations 2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Suivi des Inondations (Situation des inondations au
    BFA en 2021)'
  download_url: https://data.humdata.org/dataset/18f28ed5-ea97-4e26-bbb0-c7bb2d8b1abc/resource/506d596f-3439-44ea-a9b7-67ec7053e2dd/download/donnees_cat_30092021-vf-inondations-et-incendies-2021.xlsx
  format: null
  id: resource_506d596f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA Inondations 2021
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bfa_ochabfa_suividesinondations_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: 'Burkina Faso: Suivi des Inondations'
version: null
vulnerability: null
---
