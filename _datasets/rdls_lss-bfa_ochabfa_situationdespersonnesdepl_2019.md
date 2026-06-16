---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Groupe de Coordination Op\xE9rationnelle de la R\xE9ponse Rapide (GCORR)"
    url: https://data.humdata.org/dataset/situation-des-personnes-deplacees-internes
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Secr\xE9tariat Permanent du Conseil National de Secours d'Urgence et de\
      \ R\xE9habilitation (SP/CONASUR)"
    url: https://data.humdata.org/dataset/situation-des-personnes-deplacees-internes
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Burkina Faso
  url: https://data.humdata.org/dataset/situation-des-personnes-deplacees-internes
creator:
  affiliation: null
  email: null
  name: OCHA Burkina Faso
  url: https://data.humdata.org/dataset/situation-des-personnes-deplacees-internes
dataset_id: rdls_lss-bfa_ochabfa_situationdespersonnesdepl_2019
description: "Situation des personnes d\xE9plac\xE9es internes au Burkina Faso. Les\
  \ derni\xE8res donn\xE9es ont \xE9t\xE9 fournies par le Groupe de Coordination Op\xE9\
  rationnelle de la R\xE9ponse Rapide (GCORR). Les donn\xE9es historiques proviennent\
  \ du Secr\xE9tariat Permanent du Conseil National de Secours d'Urgence et de R\xE9\
  habilitation (SP/CONASUR).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/situation-des-personnes-deplacees-internes]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: 'Displacement data compiled from two primary sources: current incident-based
    registry data from GCORR capturing shock type, displacement dates, and demographic
    composition (gender and age disaggregated), and historical administrative records
    from SP/CONASUR tracking cumulative IDP populations by administrative division.
    Data spans 2019-2025 with monthly updates documenting displacement flows and population
    concentrations across Burkina Faso.'
  sources:
  - id: source_1
    license: null
    name: "Groupe de Coordination Op\xE9rationnelle de la R\xE9ponse Rapide (GCORR)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
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
- href: https://data.humdata.org/dataset/situation-des-personnes-deplacees-internes
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from security incidents and armed conflict
      in Burkina Faso
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
  description: "Incidents de s\xE9curit\xE9 et alertes ayant donn\xE9 lieu au d\xE9\
    placement interne de personnes au Burkina par communes au 08 mai 2025. Le jeu\
    \ de donn\xE9es inclut les besoins prioritaires des populations d\xE9plac\xE9\
    es."
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/f00b3784-7b4d-4725-8bed-904712d31d19/download/pdi-gcorr-burkinafaso-may2025.xlsx
  format: null
  id: resource_f00b3784
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: PDI-GCORR-BurkinaFaso-May2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes au Burkina par communes au 31/03/2023)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/777d6429-8fbd-431c-9402-dc70b8603251/download/idps4.xlsx
  format: null
  id: resource_777d6429
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation des PDI_31_mars 2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes au Burkina par communes au 31/01/2023)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/33c0a1fe-85e0-428c-86b7-c90beb9f6314/download/situation-des-pdi-par-communes-31-janvier-2022pcodes.xlsx
  format: null
  id: resource_33c0a1fe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation des PDI par Communes 31 janvier
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes au Burkina par communes au 31/12/2022)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/44708287-ed0a-4a2e-98a3-1eeb221eae92/download/situation-des-pdi-par-communes-accueil-du-31-decembre-2022-1.xlsx
  format: null
  id: resource_44708287
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: situation_pdi_Jan2019_to_Dec2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes au Burkina par communes au 30/11/2022)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/6deef2ff-d3a6-4a21-827f-f494443feb81/download/situation-des-pdi-par-communes-30-novembre-2022-1.xlsx
  format: null
  id: resource_6deef2ff
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: situation_pdi_Jan2019_to_Nov2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes au Burkina par communes au 31/10/2022)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/b2d91a81-4233-44a6-9a9c-e1d96aa9f144/download/situation-des-pdi-par-communes-31-octobre-2022pcodes.xlsx
  format: null
  id: resource_b2d91a81
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: situation_pdi_Jan2019_to_Oct2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes au Burkina par communes au 30/09/2022)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/da8e0b29-e5c8-4816-adde-99c6d122df71/download/situation-des-pdi-par-communes-30-avril-2022-apres-nettoyage-conasur-pcodes-2.xlsx
  format: null
  id: resource_da8e0b29
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: situation_pdi_Jan2019_to_Sept2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes au Burkina par communes au 30/04/2022)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/b86b59c0-967b-4ee5-976f-36f498f69399/download/situation-des-pdi-par-communes-30-avril-2022-pcodes.xlsx
  format: null
  id: resource_b86b59c0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: situation_pdi_Jan2019_to_Avr2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes au Burkina par communes au 31/03/2022)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/92e62bdf-4d70-4bfb-bddf-b0b2e0cf7f55/download/situation-des-pdi-par-communes-31-mars-2022-pcodes.xlsx
  format: null
  id: resource_92e62bdf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: situation_pdi_Jan2019_to_Mar2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Excel)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/03893b1b-076f-4c31-847d-7f418f90d51b/download/situation_pdi_30112021.xlsx
  format: null
  id: resource_03893b1b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: situation_pdi_30112021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 31/07/2021)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/836b04c5-e2d9-40c1-a757-8049ede15feb/download/situation_pdi_31072021.xlsx
  format: null
  id: resource_836b04c5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: situation_pdi_31072021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 30/06/2021)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/3406a7ce-200b-4cd9-8672-01cd2ebb3c59/download/situation_pdi_30062021.xlsx
  format: null
  id: resource_3406a7ce
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation_pdi_30062021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 31/05/2021)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/3929e742-398f-4013-88d1-3bf43c4563c4/download/situation_pdi_31052021.xlsx
  format: null
  id: resource_3929e742
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation_pdi_31052021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 31/03/2021)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/d7cb51dc-ff5f-4b09-b1c7-737e38c3c2c3/download/situation_pdi_31032021.xlsx
  format: null
  id: resource_d7cb51dc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation_PDI_31032021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 31/12/2020)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/227a91a6-f174-467b-8dd2-d985dcc5d4e3/download/situation_pdi_31122020.xlsx
  format: null
  id: resource_227a91a6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: situation_pdi_31122020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 08/08/2020)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/9cad6117-8dc8-4004-9c32-78f0493cf2b9/download/situation_pdi_08082020.xlsx
  format: null
  id: resource_9cad6117
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation_PDI_08082020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 09/07/2020)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/020c7a8a-39a8-41ea-bef9-8e9977621101/download/situation_pdi_09072020.xlsx
  format: null
  id: resource_020c7a8a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation_PDI_09072020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 29/02/2020)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/a00a2e2c-fc75-4fc9-ba80-3d37c062409c/download/situation_pdi_20200229.xlsx
  format: null
  id: resource_a00a2e2c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation_PDI_20200229
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 12/02/2020)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/3c9b4d37-6aeb-425b-974e-70a87d83bcea/download/situation_pdis_14022020xlsx.xlsx
  format: null
  id: resource_3c9b4d37
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation_PDIs_14022020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes (Personnes\
    \ d\xE9plac\xE9es internes par communes au 27/01/2020)"
  download_url: https://data.humdata.org/dataset/5a0dfc28-6fb6-4719-bff7-71fa35b87588/resource/60de9b18-f0db-4d88-ac75-5df779998604/download/situation-pdis-27012020.xlsx
  format: null
  id: resource_60de9b18
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Situation_PDIs_27012020
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bfa_ochabfa_situationdespersonnesdepl_2019
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
  end: '2025-05-08'
  start: '2019-01-27'
temporal_resolution: null
title: "Burkina Faso: Situation des Personnes D\xE9plac\xE9es Internes"
version: null
vulnerability: null
---
