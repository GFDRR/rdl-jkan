---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/population-au-tchad-et-total-idps-retournes-refugies-sadd
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/population-au-tchad-et-total-idps-retournes-refugies-sadd
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/population-au-tchad-et-total-idps-retournes-refugies-sadd
creator:
  affiliation: null
  email: null
  name: OCHA Chad
  url: https://data.humdata.org/dataset/population-au-tchad-et-total-idps-retournes-refugies-sadd
dataset_id: rdls_lss-tcd_ochatcd_numberinternallydisplaced_2019
description: 'The data is about Internally Displaced Persons, Refugees, and Returnees,
  disaggregated by administrative level 2.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/population-au-tchad-et-total-idps-retournes-refugies-sadd]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Registry-based administrative data compiled by UNHCR and IOM documenting
    internally displaced persons, refugees, and returnees in Chad disaggregated by
    administrative level 2 (provinces and departments). Monthly updates track population
    movements and displacement status across the country.
  sources:
  - id: source_1
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-au-tchad-et-total-idps-retournes-refugies-sadd
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from flood and conflict-related displacement
      in Chad
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
    description: Refugees and returnees affected by displacement events in Chad
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
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Refugees as of September 2025)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/dbc0e171-dad9-4e8a-9cf5-6d5a970ecca0/download/tcd__refugie_septembre__20250930.xlsx
  format: null
  id: resource_dbc0e171
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Refugi\xE9_Septembre__20250930.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Refugees as of August 2025)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/f959c199-459a-40de-95d3-93270108d615/download/tcd__refugie_aout__20250831.xlsx
  format: null
  id: resource_f959c199
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Refugi\xE9_Aout__20250831.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Returnees as of July 2025)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/1a1054f9-3fc7-4b73-a96b-72e394e1e7ae/download/tcd__data_retourne_est_juillet__20250730.xlsx
  format: null
  id: resource_1a1054f9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Data_Retourn\xE9_EST_Juillet__20250730"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Returnees as of June 2025)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/f745cad7-9ab9-46c4-b1b0-ec0ba9b41491/download/tcd__data_retourne_est_juin__20250630.xlsx
  format: null
  id: resource_f745cad7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Data_Retourn\xE9_EST_Juin__20250630"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Returnees as of May 2024)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/ac5645cd-7da0-4a02-9504-ec8fb1da23ad/download/tcd__data_retourne_est_mai__20250430.xlsx
  format: null
  id: resource_ac5645cd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Data_Retourn\xE9_EST_Mai__20250430"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Returnees as of April 2025)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/29718f47-ed9b-4c50-b797-9668b3e39690/download/tcd__data_retourne_est_avril__20250430.xlsx
  format: null
  id: resource_29718f47
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Data_Retourn\xE9_EST_Avril__20250430"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Returnees as of March 2025)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/ac4dab72-bdb2-4722-8504-a56395efc195/download/tcd__data_retourne_est_mars__20250330.xlsx
  format: null
  id: resource_ac4dab72
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Data_Retourn\xE9_EST_Mars__20250330"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Returnees as of February 2025)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/ab0d734b-9da4-409d-b40b-f8ac55fbbf76/download/tcd__data_retourne_est_fevrier__20250230.xlsx
  format: null
  id: resource_ab0d734b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Data_Retourn\xE9_EST_F\xE9vrier__20250230"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Returnees as of November 2024)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/f4411533-da64-417f-bf94-60770be5ce0f/download/tcd__data_retourne__20241119.xlsx
  format: null
  id: resource_f4411533
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Data_Retourn\xE9__20241119.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Refugees and Returnees as of July 2024)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/9c39e4bd-594c-473d-a803-94384bf85d55/download/tcd__refugie_retourne__20240702.xlsx
  format: null
  id: resource_9c39e4bd
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD__Refugi\xE9s_Retourn\xE9s_20240702"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Returnees as of May 2024)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/3081047c-f882-429e-a42c-4430eb5874a7/download/tcd_viz_nombre_retournes_niveau_admin2_20240524.xlsx
  format: null
  id: resource_3081047c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD_Nombre_Retourn\xE9s_Niveau_Admin2_20240524.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Returnees as of November 2023)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/88eda02e-bdf0-4fa8-b914-f6113d22b206/download/tcd_viz_nombre_retournes_niveau_admin2_20231217.xlsx
  format: null
  id: resource_88eda02e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD_VIZ_Nombre_Retourn\xE9s_Niveau_Admin2_20231217.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Refugees as of November 2023)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/262439d0-6914-4392-8b3c-adb25287434f/download/tcd_viz_nombre_refugies_niveau_admin2_20231107.xlsx
  format: null
  id: resource_262439d0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD_VIZ_Nombre_R\xE9fugi\xE9s_Niveau_Admin2_20231107"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of IDPs by Admin 2)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/1913eb90-12e1-4324-9c39-d29c145e6162/download/tcd_pdi_20231006.xlsx
  format: null
  id: resource_1913eb90
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_PDI_20231006
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Number of Refugees and Returnees by Admin 2)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/41d8ec9a-836d-4620-b452-b197ff25ed92/download/tcd_viz_nombre_refugies_retournes_niveau_admin2_20230817.xlsx
  format: null
  id: resource_41d8ec9a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_refugees_returnees_admin2_20230817
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (IDPs, Returnees and Refugees by admin 2)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/04bd8392-525b-4e7b-b8e3-1654043956ae/download/tcd_viz_nombre_refugies_retournes_niveau_admin2_20230713.xlsx
  format: null
  id: resource_04bd8392
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "TCD_Nombre_R\xE9fugi\xE9s_Retourn\xE9s_Niveau_Admin2_20230713"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Reference data for HNO 2023)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/70ee2861-3add-476b-9c99-980914d3b706/download/tcd_hpc2023_donneesbase_20221205.xlsx
  format: null
  id: resource_70ee2861
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_HPC2023_DonneesBase_20221205
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Population Displacement data - November 2021)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/40dca1cb-ee4a-4f62-b6ef-b0a9546474d5/download/tcd_data_popdisplacement_20211126.xlsx
  format: null
  id: resource_40dca1cb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_DATA_PopDisplacement_20211126
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Reference data for HNO 2021)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/e944a4d5-b006-4e48-ab9b-17626b565a52/download/tcd_data_cod_ps_idp_rt_rf_20201130.xlsx
  format: null
  id: resource_e944a4d5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_DATA_COD_PS_IDP_RT_RF_20201130
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Population Displacement data - November 2020)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/4f9781f9-0ba4-4235-a0d7-d7124ce769f1/download/tcd_data_cod_ps_idp_rt_rf_20201031.xlsx
  format: null
  id: resource_4f9781f9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_DATA_COD_PS_IDP_RT_RF_20201031
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad - Number of Internally Displaced Persons, Refugees and Returnees
    (Reference data for HNO 2020)
  download_url: https://data.humdata.org/dataset/f09205c1-7102-407d-96bc-608b8803cd91/resource/3e47d8c4-1269-4a13-bb86-0b6a10b5811f/download/tcd_data_cod_ps_idp_rt_rf_20190930.xlsx
  format: null
  id: resource_3e47d8c4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TCD_DATA_COD_PS_IDP_RT_RF_20190930
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tcd_ochatcd_numberinternallydisplaced_2019
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
  end: '2025-09-30'
  start: '2019-09-30'
temporal_resolution: null
title: Chad - Number of Internally Displaced Persons, Refugees and Returnees
version: null
vulnerability: null
---
