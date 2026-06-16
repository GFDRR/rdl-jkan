---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Minist\xE8re de l'Action Humanitaire et de la Gestion des Catastrophes\
      \ du Niger"
    url: https://data.humdata.org/dataset/niger-situation-des-inondations
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Niger
  url: https://data.humdata.org/dataset/niger-situation-des-inondations
creator:
  affiliation: null
  email: null
  name: OCHA Niger
  url: https://data.humdata.org/dataset/niger-situation-des-inondations
dataset_id: rdls_lss-ner_ochaner_situationdesinondations_2022
description: "Ce jeu donne donn\xE9es donne la situation des inondations au Niger..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/niger-situation-des-inondations]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event flood impact data collected through direct observation and
    anecdotal reports by Niger's Ministry of Humanitarian Action and Disaster Management.
    Data aggregated by locality and administrative division with temporal coverage
    from 2022 to 2025, documenting affected households, displaced persons, and infrastructure
    damage across multiple flood events.
  sources:
  - id: source_1
    license: null
    name: "Minist\xE8re de l'Action Humanitaire et de la Gestion des Catastrophes\
      \ du Niger"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/niger-situation-des-inondations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct impact on affected population from flood events in Niger
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
    description: Direct building damage from flood events in Niger
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
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - Novembre 2025)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/48950455-b863-4a5e-b721-102c8c80da8c/download/ner-situation-desagregee-au-29-septembre-2025.csv
  format: null
  id: resource_48950455
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "NER Situation de\u0301sagre\u0301ge\u0301e au 29 Septembre 2025.csv"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - Novembre 2024)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/14c35c87-8819-4aaa-a881-a959c963ab6f/download/situation_des_inondations_expression_des_besoins_et_reponses-au-11-novembre-2024.xlsx
  format: null
  id: resource_14c35c87
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Situation_des_inondations,_expression_des_besoins_et_Re\u0301ponses au 11\
    \ Novembre 2024"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - Septembre 2024)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/8b40cc5b-3952-4d06-9db8-42e29996217e/download/situation_des_inondations_expression_des_besoins_et_reponses-du-18-au-23_septembre_2024.xlsx
  format: null
  id: resource_8b40cc5b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Situation_des_inondations,_expression_des_besoins_et_R\xE9ponses du 18 au\
    \ 23_Septembre_2024"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - Juillet 2024)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/08e28fa0-58c5-462f-abd5-3572f34fd061/download/situation_des_inondations_et_expression_des_besoins-a-la-date-du-01-07-2024.xlsx
  format: null
  id: resource_08e28fa0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SITUATION_DES_INONDATIONS_ET_EXPRESSION_DES_BESOINS a la date du 01-07-2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - 9 Octobre 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/29c2a3cf-2ad3-4841-b41d-b1c82c8be7c2/download/ner_situation-des-inondations-au-09-octobre-2023-dshu-mahgc.xlsx
  format: null
  id: resource_29c2a3cf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NER_SITUATION DES INONDATIONS AU 09 OCTOBRE 2023 DSHU MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Donn\xE9es d\xE9sagr\xE9g\xE9es\
    \ sur la situation des inondations au Niger - 09 Octobre 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/36a9ea1b-737a-4b65-b4b6-b106fda5558e/download/donnees_desagregee_-9_10_2023_mahgc.xlsx
  format: null
  id: resource_36a9ea1b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DONNEES_DESAGREGEE_ 9_10_2023_MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Donn\xE9es d\xE9sagr\xE9g\xE9es\
    \ sur la situation des inondations au Niger - 02 Octobre 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/62ff7a60-ac12-4ab8-8714-bedb77b9a813/download/donnees_desagregee_inondations_2_10_2023.xlsx
  format: null
  id: resource_62ff7a60
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DONNEES_DESAGREGEE_INONDATIONS_2_10_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - 25 Septembre 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/48d5da7d-fc8d-4233-afd1-2023c4ae32ef/download/ner_situation-des-inondations-au-25-septembre-2023-dshu-mahgc.xlsx
  format: null
  id: resource_48d5da7d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NER_SITUATION DES INONDATIONS AU 25 SEPTEMBRE 2023 DSHU MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - 18 Septembre 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/52b2be0a-3ad1-470f-9d0e-cb5c680c9e6f/download/ner_situation-des-inondations-au-18-septembre-2023-dshu-mahgc.xlsx
  format: null
  id: resource_52b2be0a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NER_SITUATION DES INONDATIONS AU 18 SEPTEMBRE 2023 DSHU MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - 11 Septembre 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/b5f97774-76ab-4513-a953-90fe6e5dc6f3/download/situation-des-inondations-au-11-septembre-2023-dshu-mahgc-1.xlsx
  format: null
  id: resource_b5f97774
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SITUATION DES INONDATIONS AU 11 SEPTEMBRE 2023 DSHU MAHGC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Donn\xE9es d\xE9sagr\xE9g\xE9es sur la situation des inondations au\
    \ Niger - 11 Septembre 2023"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/9427a40b-62fc-476f-92ba-7934acd9d13f/download/donnees_desagregee_11-09-2023_mahgc.xlsx
  format: null
  id: resource_9427a40b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DONNEES_DESAGREGEE_11 09 2023_MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - 4 Septembre 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/fa13e9bc-5c55-421f-a1ed-b7b9ea67cd87/download/situation-des-inondations-au-04septembre-2023-dshu-mahgc.xlsx
  format: null
  id: resource_fa13e9bc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SITUATION DES INONDATIONS AU 04 SEPTEMBRE 2023 DSHU MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Donn\xE9es d\xE9sagr\xE9g\xE9es\
    \ sur la situation des inondations au Niger - 4 Septembre 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/a0804293-ea8d-4e19-b07a-ce5bf07bfe05/download/donnees_desagregee_04-09-2023_mahgc.xlsx
  format: null
  id: resource_a0804293
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DONNEES_DESAGREGEE_04 09 2023_MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - 14 Ao\xFBt 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/0559042a-7c63-4e02-adb3-5915504f9515/download/situation-des-inondations-14-aout-2023-dshu-mahgc.xlsx
  format: null
  id: resource_0559042a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SITUATION DES INONDATIONS 14 AOUT 2023 DSHU MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Donn\xE9es d\xE9sagr\xE9g\xE9es\
    \ sur la situation des inondations au Niger - 14 Ao\xFBt 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/d5085894-20c5-4f9d-aea4-4e11842087a4/download/donnees_desagregee-14-08-23-mahgc.xlsx
  format: null
  id: resource_d5085894
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DONNEES_DESAGREGEE 14 08 23 MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ - 7 Ao\xFBt 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/e36fac86-fcee-4b44-b122-03176344a2ab/download/situation-des-inondations-au-7-aout-2023-mahgc-dshu.xlsx
  format: null
  id: resource_e36fac86
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SITUATION DES INONDATIONS AU 7 AOUT 2023 MAHGC DSHU.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Donn\xE9es d\xE9sagr\xE9g\xE9es\
    \ sur la situation des inondations au Niger - 7 Ao\xFBt 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/5fc6fd26-d58f-46fc-84fd-e87fca394233/download/donnee_desagreg_07-08-2023-mahgc-ds.xlsx
  format: null
  id: resource_5fc6fd26
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DONNEE_DESAGREGEE_07-08 2023 MAHGC DS.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Donn\xE9es d\xE9sagr\xE9g\xE9es\
    \ sur la situation des inondations au Niger - 21 Ao\xFBt 2023)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/034c8c9f-6d04-4270-81d7-1fe67c786a15/download/donnees_desagregee_-21-08-2023_mahgc.xlsx
  format: null
  id: resource_034c8c9f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DONNEES_DESAGREGEE_ 21 08 2023_MAHGC.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger : Situation des inondations (Situation des inondations 2022
    au Niger - Janvier 2023)'
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/090aa35c-4ba7-4bfc-b85a-c79692383005/download/ner_situations_des_inondations_2022_au-18-janvier-2023.xlsx
  format: null
  id: resource_090aa35c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ner_situations_des_inondations_2022_au 18 janvier 2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niger : Situation des inondations (Situation des inondations au Niger
    - Octobre 2022)'
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/d39a8ccf-577e-47e7-93a6-95970f5fe26e/download/situation-des-inondations-au-24-10-2022-dshu-mahgc.xlsx
  format: null
  id: resource_d39a8ccf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ner_situations_des_inondations_Oct2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ de Juin \xE0 Ao\xFBt 2022)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/b12bf485-073f-459e-a3f5-c6b31778684b/download/ner_situation-des-inondations_juin_aout_2022_au_21082022.xlsx
  format: null
  id: resource_b12bf485
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "ner_situation_des_inondations_juin_ao\xFBt_2022"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Niger : Situation des inondations (Situation des inondations au Niger\
    \ et r\xE9ponses apport\xE9es - Novembre 2024)"
  download_url: https://data.humdata.org/dataset/cfb9413f-1c52-4f22-9f21-297ef01ea3b0/resource/b5f66ee8-d677-49a3-9546-ca8aa655e77a/download/situation_des_inondations_expression_des_besoins_et_reponses-au-11-novembre-2024.xlsx
  format: null
  id: resource_b5f66ee8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Situation_des_inondations,_expression_des_besoins_et_Re\u0301ponses au 11\
    \ Novembre 2024.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ner_ochaner_situationdesinondations_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-11'
  start: '2022-06-06'
temporal_resolution: null
title: 'Niger : Situation des inondations'
version: null
vulnerability: null
---
