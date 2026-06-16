---
attributions:
- entity:
    affiliation: null
    email: null
    name: "Comit\xE9 National de collecte de Donn\xE9es Personnes D\xE9plac\xE9es\
      \ Internes"
    url: https://data.humdata.org/dataset/niger-retour-des-personnes-deplacees-internes
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Niger
  url: https://data.humdata.org/dataset/niger-retour-des-personnes-deplacees-internes
creator:
  affiliation: null
  email: null
  name: OCHA Niger
  url: https://data.humdata.org/dataset/niger-retour-des-personnes-deplacees-internes
dataset_id: rdls_lss-ner_ochaner_retourdespersonnesdeplace_20220826
description: "Ce jeu de donn\xE9es donne la planification des retours des personnes\
  \ d\xE9plac\xE9es internes \xE0 Diffa.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/niger-retour-des-personnes-deplacees-internes]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Registry-based administrative data collected by the National IDP Data
    Collection Committee documenting the planned return of internally displaced persons
    from Diffa region, compiled as of phase 2 in August 2022.
  sources:
  - id: source_1
    license: null
    name: "Comit\xE9 National de collecte de Donn\xE9es Personnes D\xE9plac\xE9es\
      \ Internes"
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/niger-retour-des-personnes-deplacees-internes
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons returning to Diffa region, with displacement
      triggered by flood hazard
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
  description: "Niger : Retour des Personnes D\xE9plac\xE9es Internes (Retour des\
    \ PDIs par village - Ao\xFBt 2022)"
  download_url: https://data.humdata.org/dataset/c7cb4aa8-1d2d-4589-b266-5fb46d4df687/resource/ba3d2c05-d74c-40d3-95b9-864f2ed0dade/download/retours-pdi_au-phase-2_diffa-26082022.xlsx
  format: null
  id: resource_ba3d2c05
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Retours PDI_au phase 2_Diffa_26082022.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ner_ochaner_retourdespersonnesdeplace_20220826
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
  end: null
  start: '2022-08-26'
temporal_resolution: null
title: "Niger : Retour des Personnes D\xE9plac\xE9es Internes"
version: null
vulnerability: null
---
