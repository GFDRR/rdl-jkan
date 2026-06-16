---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Central African Republic
  url: https://data.humdata.org/dataset/republique-centrafricaine-situation-des-inondations
creator:
  affiliation: null
  email: null
  name: OCHA Central African Republic
  url: https://data.humdata.org/dataset/republique-centrafricaine-situation-des-inondations
dataset_id: rdls_el-caf_ochacaf_republiquesituationdesino_2021
description: "Le jeu de donn\xE9es porte sur les inondations en Centrafrique, leurs\
  \ impacts sur la population et les r\xE9ponses apport\xE9es.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/republique-centrafricaine-situation-des-inondations]"
details: null
exposure:
- asset_type:
    description: Residential population by administrative division (HNO 2022 baseline)
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
    description: Private and public infrastructure (residential, commercial, administrative,
      educational, health, religious facilities)
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
    description: Cultivable land affected by flooding measured in hectares
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
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event flood impact data compiled by OCHA from humanitarian partner
    reports across Central African Republic (2021-2024). Data collection methodology
    combines direct observational records and anecdotal reports from field sources,
    aggregated by administrative division (prefecture, sous-prefecture, commune) with
    geospatial coordinates. The dataset integrates impact assessments (affected populations,
    infrastructure damage, casualties, displacement) with sectoral needs identification
    and humanitarian response tracking.
  sources:
  - id: source_1
    license: null
    name: OCHA Central African Republic
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/republique-centrafricaine-situation-des-inondations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct count of individuals and households affected by flooding events
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
    description: Direct damage to private and public infrastructure from flooding
      (collapsed structures, roof damage, affected facilities)
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
    description: Deaths and injuries resulting from flooding
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
  - asset_category: population
    asset_dimension: population
    description: Population displacement and movement triggered by flooding
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
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural land loss measured in hectares of cultivable area affected
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Situation\
    \ des Inondations (Donn\xE9es sur les Inondations de 2021 \xE0 Octobre 2024)"
  download_url: https://data.humdata.org/dataset/3e230b3f-e0d7-4c7d-a788-0d4c82d8f814/resource/4f3da21e-fecf-4332-a536-fb9f1270e206/download/ocha-car_donnees-inondations_data_compil_2021-2024.xlsx
  format: null
  id: resource_4f3da21e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA CAR_DONNEES-INONDATIONS_DATA_COMPIL_2021-2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Situation\
    \ des Inondations (Donn\xE9es sur les Inondations de 2021 \xE0 Septembre 2024)"
  download_url: https://data.humdata.org/dataset/3e230b3f-e0d7-4c7d-a788-0d4c82d8f814/resource/fecb9374-c871-4502-bd6b-6b6352b0b465/download/ocha-car_donnees-inondations_data_compil_2021-2024.xlsx
  format: null
  id: resource_fecb9374
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA CAR_DONNEES-INONDATIONS_DATA_COMPIL_2021-2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Situation\
    \ des Inondations (Donn\xE9es sur les Inondations au 11 D\xE9cembre 2023)"
  download_url: https://data.humdata.org/dataset/3e230b3f-e0d7-4c7d-a788-0d4c82d8f814/resource/138a3a3e-11ce-42e1-8649-dc656eb10f43/download/synthese_besoins_reponse_gaps_dec2023.xlsx
  format: null
  id: resource_138a3a3e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Synthese_besoins_reponse_gaps_Dec2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Situation\
    \ des Inondations (Donn\xE9es sur les Inondations au 6 D\xE9cembre 2022)"
  download_url: https://data.humdata.org/dataset/3e230b3f-e0d7-4c7d-a788-0d4c82d8f814/resource/dff21492-ea0b-442d-9b79-3fd7c7ffb367/download/ocha-car_donnees-inondations_data_comppil_6122022.xlsx
  format: null
  id: resource_dff21492
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA CAR_DONNEES-INONDATIONS_DATA_COMPPIL_6122022
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-caf_ochacaf_republiquesituationdesino_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-10-31'
  start: '2021-04-23'
temporal_resolution: null
title: "Central African Republic - R\xE9publique Centrafricaine : Situation des Inondations"
version: null
vulnerability: null
---
