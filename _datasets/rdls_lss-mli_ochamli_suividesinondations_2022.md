---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Direction R\xE9gionale du D\xE9veloppement Social et de l'Economie Solidaire\
      \ (DRDSES)"
    url: https://data.humdata.org/dataset/mali-suivi-des-inondations
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: "Equipe de Recherche - Actions pour le D\xE9veloppement Durable (ERADD)"
    url: https://data.humdata.org/dataset/mali-suivi-des-inondations
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Save the Children (SCI)
    url: https://data.humdata.org/dataset/mali-suivi-des-inondations
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Action Contre la Faim (ACF)
    url: https://data.humdata.org/dataset/mali-suivi-des-inondations
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/mali-suivi-des-inondations
creator:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/mali-suivi-des-inondations
dataset_id: rdls_lss-mli_ochamli_suividesinondations_2022
description: "Les donn\xE9es contiennent les impacts caus\xE9s par les inondations\
  \ et les fortes pluies au Mali.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mali-suivi-des-inondations]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood impact data collected through evaluation forms and email reports
    submitted by DRDSES to OCHA Mali, compiled and maintained in a centralized database
    by IM OCHA Mali. Data includes post-event impact records at commune and village
    level across Mali's regions, covering affected populations, casualties, injuries,
    and building damage from flooding and heavy rainfall events.
  sources:
  - id: source_1
    license: null
    name: "Direction R\xE9gionale du D\xE9veloppement Social et de l'Economie Solidaire\
      \ (DRDSES)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: "Equipe de Recherche - Actions pour le D\xE9veloppement Durable (ERADD)"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Save the Children (SCI)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: Action Contre la Faim (ACF)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mali-suivi-des-inondations
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population from flooding and heavy rainfall events
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
    description: Buildings damaged and destroyed from flooding
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
    description: Injured persons from flooding events
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
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Deaths from flooding events
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Schools damaged from flooding
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Donn\xE9es sur les impacts caus\xE9s par les inondations et les fortes\
    \ pluies au Mali au 7 Novembre 2024"
  download_url: https://data.humdata.org/dataset/9828479f-bdcf-47af-8149-e984f7f312a6/resource/496f41e0-fb9b-4a23-82ce-ad68556839dc/download/mli-personnes-affectees-par-les-inondations.xlsx
  format: null
  id: resource_496f41e0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "mli-personnes-affect\xE9es-par-les-inondations"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Mali: Suivi des Inondations (Donn\xE9es sur les impacts caus\xE9s\
    \ par les inondations et les fortes pluies au Mali.)"
  download_url: https://data.humdata.org/dataset/9828479f-bdcf-47af-8149-e984f7f312a6/resource/1209b98e-ad70-4d86-ae7e-96c8b426bf6f/download/2022_ocha_mli_data_inondation_septembre-1-1.xlsx
  format: null
  id: resource_1209b98e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mali_suivi des inondations
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_ochamli_suividesinondations_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-11-07'
  start: '2022-05-25'
temporal_resolution: null
title: 'Mali: Suivi des Inondations'
version: null
vulnerability: null
---
