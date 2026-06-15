---
attributions:
- entity:
    affiliation: null
    email: null
    name: Commission des Mouvements de Population (CMP)
    url: https://data.humdata.org/dataset/statistiques-detaillees-des-sites-pdis-en-republique-centrafricaine
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Central African Republic
  url: https://data.humdata.org/dataset/statistiques-detaillees-des-sites-pdis-en-republique-centrafricaine
creator:
  affiliation: null
  email: null
  name: OCHA Central African Republic
  url: https://data.humdata.org/dataset/statistiques-detaillees-des-sites-pdis-en-republique-centrafricaine
dataset_id: rdls_lss-caf_ochacaf_republiquecompilationdesp_2020
description: "Ce jeu de donn\xE9es, valid\xE9 par la commission des mouvements de\
  \ population, donne l'historique des Personnes D\xE9plac\xE9es Internes (PDIs),\
  \ R\xE9fugi\xE9s et Retourn\xE9s par sous-pr\xE9fecture.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/statistiques-detaillees-des-sites-pdis-en-republique-centrafricaine]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Population movement data collected and maintained by the Commission
    des Mouvements de Population (CMP) in Central African Republic, compiled monthly
    by OCHA into time-series registries tracking internally displaced persons, refugees,
    and returnees at sub-prefecture administrative level from 2021 onwards.
  sources:
  - id: source_1
    license: null
    name: Commission des Mouvements de Population (CMP)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/statistiques-detaillees-des-sites-pdis-en-republique-centrafricaine
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict and insecurity in Central
      African Republic
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Refugee populations from Central African Republic
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
    description: Returnee populations to Central African Republic
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
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs, retourn\xE9s - ao\xFBt 2025)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/aed281e4-0548-42f0-8fd6-58e3fea26ecc/download/ocha_car_compil_pdi_refugies_retournes_aout_2025.xlsx
  format: null
  id: resource_aed281e4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_AOUT_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - F\xE9vrier 2025)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/52a3b189-20af-414c-8a0e-abcda73f27ad/download/ocha-car_compil_pdi_refugies_retournes_fev-2025.xlsx
  format: null
  id: resource_52a3b189
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA CAR_COMPIL_PDI_REFUGIES_RETOURNES_FEV 2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Decembre 2024)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/0d20359e-2aca-44c4-8f71-acd0a3aeef73/download/ocha_car_compil_pdi_refugies_retournes_dec_2024.xlsx
  format: null
  id: resource_0d20359e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_DEC_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Novembre 2024)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/107f74f9-32c2-4ca3-8e52-67ad2964a5db/download/ocha_car_compil_pdi_refugies_retournes_nov_2024.xlsx
  format: null
  id: resource_107f74f9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_NOV_2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Octobre 2024)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/72114cc7-6ecc-4017-8bf1-a4afb3d040ff/download/ocha_car_compil_pdi_refugies_retournes_octobre_2024.xlsx
  format: null
  id: resource_72114cc7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_OCTOBRE_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Juin 2024)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/108f564d-faaf-4ea4-b4ed-94c64e458668/download/ocha-car_compil_pdi_refugies_retournes_juin-2024.xlsx
  format: null
  id: resource_108f564d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA CAR_COMPIL_PDI_REFUGIES_RETOURNES_JUIN 2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Mars 2024)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/4ce543b3-31f4-4a30-a516-e03fdae4d6cc/download/ocha_car_compil_pdi_refugies_retournes_mars_2024.xlsx
  format: null
  id: resource_4ce543b3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_MARS_2024.
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - D\xE9cembre 2023)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/304148cf-9cd3-4ba9-971c-4beaa95f61e3/download/ocha_car_compil_pdi_refugies_retournes_decembre_2023-copie.xlsx
  format: null
  id: resource_304148cf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_DECEMBRE_2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Novembre 2023)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/2e4d2cff-5f64-4bc8-a417-f3e96a659def/download/compile_cmp_car.xlsx
  format: null
  id: resource_2e4d2cff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_Novembre_2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Octobre 2023)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/cdb64ba3-b7e0-4372-81b8-b0c571226edf/download/ocha_car_compil_pdi_refugies_retournes_octobre_2023.xlsx
  format: null
  id: resource_cdb64ba3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_OCTOBRE_2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Ao\xFBt 2023)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/39fa99df-31b0-4b4f-aba4-3baa8469ff98/download/ocha_car_compil_pdi_refugies_retournes_aout_2023.xlsx
  format: null
  id: resource_39fa99df
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_AOUT_2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Juillet 2023)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/e5716a51-62eb-4181-a313-f34945fa453a/download/ocha_car_compil_pdi_refugies_retournes_juillet_2023.xlsx
  format: null
  id: resource_e5716a51
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REFUGIES_RETOURNES_JUILLET_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Mars 2023)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/67b211fa-9742-4f84-9017-91da1541fd50/download/ocha_car_compil_pdi_ref_mars_2023.xlsx
  format: null
  id: resource_67b211fa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_MARS_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Janvier 2023)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/853e1b2c-16d2-4aaf-9f34-6566ea11480d/download/ocha_car_compil_pdi_ref_jan_2023.xlsx
  format: null
  id: resource_853e1b2c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_JAN_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Octobre 2022)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/99a1c9a3-98e0-427c-8e4b-e7c70889ba97/download/car_mouvement_population_octobre-2022.xlsx
  format: null
  id: resource_99a1c9a3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_OCTOBRE_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Juillet 2022)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/ccfb0390-b78b-4838-9533-08b28e6acdf4/download/ocha_car_compil_pdi_ref_juillet_2022.xlsx
  format: null
  id: resource_ccfb0390
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_JUILLET_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Avril 2022)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/72393b83-56db-4b07-aec0-b30b301afc97/download/ocha_car_compil_pdi_ref_avril_2022.xlsx
  format: null
  id: resource_72393b83
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_AVRIL_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - F\xE9vrier 2022)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/1d861732-b457-43fe-b912-8d671178b78e/download/ocha_car_compil_pdi_ref_fev_2022_v0-1.xlsx
  format: null
  id: resource_1d861732
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_FEV_2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - D\xE9cembre 2021)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/c4df8eda-1692-4bdf-8435-4cd8dadbc3e1/download/ocha_car_compil_pdi_ref_dec_2021.xlsx
  format: null
  id: resource_c4df8eda
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_DEC_2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Octobre 2021)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/20bd1993-76eb-4f96-9142-611503bb0bee/download/ocha_car_compil_pdi_ref_oct_2021_vf.xlsx
  format: null
  id: resource_20bd1993
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_OCT_2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Juillet 2021)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/63719253-7b93-4b7a-b496-0fe460648bf1/download/ocha_car_compil_pdi_ref_juillet_2021_vf.xlsx
  format: null
  id: resource_63719253
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_JUL_2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Juin 2021)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/0e0dbafd-3617-4aac-88c2-a488cd7993b2/download/ocha_car_compil_pdi_ref_juin_2021_vf.xlsx
  format: null
  id: resource_0e0dbafd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_JUN_2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Mars 2021)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/0f4f2219-f981-4e6f-94a0-91c320006d60/download/ocha_car_compil_pdi_ref_mars_2021_vf.xlsx
  format: null
  id: resource_0f4f2219
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_MAR_2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Janvier 2021)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/c984a3a0-f4be-4aba-b4f5-9a35e1ee4782/download/ocha_car_compil_pdi_ref_jan_2021.xlsx
  format: null
  id: resource_c984a3a0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_JAN_2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Octobre 2020)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/80f1a531-51fc-4c96-b803-6aeca288c1d5/download/ocha_car_compil_pdi_ref_oct_2020_vf.xlsx
  format: null
  id: resource_80f1a531
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_OCT_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/c8ef3acf-e928-43a1-8502-5cef5ac1b944/download/car_compilation_donnees_statistiques_pdis.xlsx
  format: null
  id: resource_c8ef3acf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_Compilation_Donnees_statistiques_PDIs
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Juin 2019)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/88f7dbfe-2064-469d-b047-8531241be3a9/download/ochar_car_idp_refugees_june2019.xlsx
  format: null
  id: resource_88f7dbfe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_IDP_Refugees_June2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Central African Republic - R\xE9publique Centrafricaine : Compilation\
    \ des Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9\
    s (Statistiques des PDIs - Octobre 2019)"
  download_url: https://data.humdata.org/dataset/c0ab1fef-323a-4f50-9fbb-a70462b3e644/resource/d8ad5480-d81a-4eff-bbcf-f8a9a0a2d7c0/download/ocha_car_compil_pdi_ref_oct_2020_vf.xlsx
  format: null
  id: resource_d8ad5480
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: OCHA_CAR_COMPIL_PDI_REF_OCT_2020
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_ochacaf_republiquecompilationdesp_2020
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
  end: '2025-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: "Central African Republic - R\xE9publique Centrafricaine : Compilation des\
  \ Personnes D\xE9plac\xE9es Internes, des R\xE9fugi\xE9s et des Retourn\xE9s"
version: null
vulnerability: null
---
