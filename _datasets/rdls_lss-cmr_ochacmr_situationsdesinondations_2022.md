---
attributions:
- entity:
    affiliation: null
    email: null
    name: Government of Cameroon
    url: https://data.humdata.org/dataset/cameroun-situations-des-inondations
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Croix-Rouge Camerounaise
    url: https://data.humdata.org/dataset/cameroun-situations-des-inondations
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Cameroon
  url: https://data.humdata.org/dataset/cameroun-situations-des-inondations
creator:
  affiliation: null
  email: null
  name: OCHA Cameroon
  url: https://data.humdata.org/dataset/cameroun-situations-des-inondations
dataset_id: rdls_lss-cmr_ochacmr_situationsdesinondations_2022
description: "Ce jeu de donn\xE9es porte sur les inondations au Cameroun et leurs\
  \ impacts sur la population.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cameroun-situations-des-inondations]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood impact data for Cameroon was collected through direct observational
    and anecdotal methods by the Government of Cameroon and the Croix-Rouge Camerounaise,
    compiled and disseminated by OCHA Cameroon. The dataset records post-event flood
    impacts at the commune and department level, including number of villages touched,
    affected households, affected persons, and fatalities, aggregated across multiple
    flood events over several years.
  sources:
  - id: source_1
    license: null
    name: Government of Cameroon
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Croix-Rouge Camerounaise
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cameroun-situations-des-inondations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Number of people and households affected by flooding across communes
      and departments in Cameroon
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
  - asset_category: population
    asset_dimension: population
    description: Loss of human lives (Perte en vies humaines) due to flooding events
      in Cameroon
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
        metric: casualty_count
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
  description: Cameroon - Cameroun - Situations des Inondations (Situation des inondations
    au 3 Octobre 2025)
  download_url: https://data.humdata.org/dataset/02d4dd29-2ded-4d2a-adeb-2f7f6dd0d69c/resource/86094846-15d0-49db-8ec8-fc67fa0a0646/download/cmr_floods_data_251003.xlsx
  format: null
  id: resource_86094846
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CMR_floods_data_251003.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cameroon - Cameroun - Situations des Inondations (Situation des inondations
    au 4 Novembre 2024)
  download_url: https://data.humdata.org/dataset/02d4dd29-2ded-4d2a-adeb-2f7f6dd0d69c/resource/e3960cd9-45b3-4577-b539-c664fa16e22f/download/cmr_floodsdata_20241104.xlsx
  format: null
  id: resource_e3960cd9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CMR_floodsData_20241104.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cameroon - Cameroun - Situations des Inondations (Situation des inondations\
    \ au 6 D\xE9cembre 2024)"
  download_url: https://data.humdata.org/dataset/02d4dd29-2ded-4d2a-adeb-2f7f6dd0d69c/resource/60ec36f5-59d9-40b6-983d-195b2e660276/download/cmr_exno_data_inondationlc_md_mt_v1.0_20221206.xlsx
  format: null
  id: resource_60ec36f5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CMR_EXNO_Data_InondationLC_MD_MT_V1.0_20221206.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cmr_ochacmr_situationsdesinondations_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - CMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-10-03'
  start: '2022-12-06'
temporal_resolution: null
title: Cameroon - Cameroun - Situations des Inondations
version: null
vulnerability: null
---
