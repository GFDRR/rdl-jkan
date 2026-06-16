---
attributions:
- entity:
    affiliation: null
    email: null
    name: Government of Chad
    url: https://data.humdata.org/dataset/tchad-suivi-des-inondations
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/tchad-suivi-des-inondations
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/tchad-suivi-des-inondations
creator:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/tchad-suivi-des-inondations
dataset_id: rdls_lss-tcd_ochatcd_suividesinondations_2022
description: "Ce jeu de donn\xE9es est un suivi des inondations au Tchad. Il donne\
  \ \xE9galement la capacit\xE9 des partenaires \xE0 r\xE9pondre aux besoins des sinistr\xE9\
  s.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/tchad-suivi-des-inondations]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event flood impact data compiled from direct observations by government
    and humanitarian partners across Chad's administrative divisions. Data includes
    affected households, casualties, building damage, livestock losses, and crop destruction
    recorded at provincial and departmental levels from 2022-2024.
  sources:
  - id: source_1
    license: null
    name: Government of Chad
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
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
- href: https://data.humdata.org/dataset/tchad-suivi-des-inondations
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage (collapsed houses) from flooding in Chad
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
  - asset_category: population
    asset_dimension: population
    description: Affected population (households and individuals) from flooding
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
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Deaths and injuries from flooding events
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural losses including destroyed crops and livestock
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tchad : Suivi des Inondations (Suivi des inondations - Octobre 2024)'
  download_url: https://data.humdata.org/dataset/25aa07d7-7c78-4754-bbc1-4eb9633714be/resource/d1cdabd6-2a75-4fb7-b371-0829a0d0a660/download/tcd_data_inondationsp_20241001.xlsx
  format: null
  id: resource_d1cdabd6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_Data_Inondations_20241001
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Tchad : Suivi des Inondations (Suivi des inondations - 25 Ao\xFBt\
    \ 2024)"
  download_url: https://data.humdata.org/dataset/25aa07d7-7c78-4754-bbc1-4eb9633714be/resource/6e05b7f4-3b99-4ae2-8672-4da9264201e8/download/tcd_viz_chiffres_cles_situation-des-inondations_20240825-1.xlsx
  format: null
  id: resource_6e05b7f4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tableau de suivi des inondations_25.08.2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Tchad : Suivi des Inondations (Suivi des inondations - 22 Ao\xFBt\
    \ 2024)"
  download_url: https://data.humdata.org/dataset/25aa07d7-7c78-4754-bbc1-4eb9633714be/resource/ff5f37b2-f8d7-4674-9b64-52b7404c6e24/download/data_share_ocha.xlsx
  format: null
  id: resource_ff5f37b2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tableau de suivi des inondations_Ndjamena_22.08.2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tchad : Suivi des Inondations (Tableau de suivi des inondations -
    23 Novembre 2022)'
  download_url: https://data.humdata.org/dataset/25aa07d7-7c78-4754-bbc1-4eb9633714be/resource/d10d4999-2267-4795-9a9b-b1e513067416/download/tcd_suiviinondation_20221123.xlsx
  format: null
  id: resource_d10d4999
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tableau de suivi des inondations_23.11.2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tchad : Suivi des Inondations (Tableau de suivi des inondations -13
    Octobre 2022)'
  download_url: https://data.humdata.org/dataset/25aa07d7-7c78-4754-bbc1-4eb9633714be/resource/d623aad3-af06-47bf-b60f-5057d7ccc4b3/download/analyse-de-gap-_-16.13.10.2022.xlsx
  format: null
  id: resource_d623aad3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tableau de suivi inondations_13.10.2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Tchad : Suivi des Inondations (Tableau de suivi des inondations -\
    \ 22 Ao\xFBt 2022)"
  download_url: https://data.humdata.org/dataset/25aa07d7-7c78-4754-bbc1-4eb9633714be/resource/c3090ba9-b171-4d2f-9117-c97c65ec268c/download/6_tableau-de-suivi-innondations_22.08.2022.xlsx
  format: null
  id: resource_c3090ba9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Tableau de suivi inondations_22.08.2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tchad : Suivi des Inondations (Tableau de suivi des inondations -
    15 Juillet 2022)'
  download_url: https://data.humdata.org/dataset/25aa07d7-7c78-4754-bbc1-4eb9633714be/resource/b3b4c073-760b-4bd8-8eb8-12131a2458e8/download/2.tableau-de-suivi-innondations_15.07.2022.xlsx
  format: null
  id: resource_b3b4c073
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2.tableau-de-suivi-inondations_15.07.2022.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tcd_ochatcd_suividesinondations_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-10-01'
  start: '2022-07-15'
temporal_resolution: null
title: 'Tchad : Suivi des Inondations'
version: null
vulnerability: null
---
