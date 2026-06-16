---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/rdc-stock-de-personnes-retournees-au-31-mai-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/rdc-stock-de-personnes-retournees-au-31-mai-2025
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/rdc-stock-de-personnes-retournees-au-31-mai-2025
dataset_id: rdls_lss-cod_ochacod_rdcstockdepersonnesretour_2023
description: "Ce fichier contient le stock de personnes retourn\xE9es au 31 mai 2025.\
  \ A noter que seuls les personnes retourn\xE9es au cours de la p\xE9riode de d\xE9\
  cembre 2023 et mai 2025 (18 derniers mois) sont concern\xE9es.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/rdc-stock-de-personnes-retournees-au-31-mai-2025]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM conducted sample surveys to track population movements and returns
    in the DRC over an 18-month period (December 2023 to May 2025). Data was compiled
    into a registry of returnees with household and individual-level records, including
    movement dates, origin/destination locations, and accommodation status, to document
    post-displacement population recovery.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/rdc-stock-de-personnes-retournees-au-31-mai-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population returns following displacement, tracked by movement date
      and origin/destination locations
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "DR Congo - RDC stock de personnes retourn\xE9es au 31 mai 2025 (Excel)"
  download_url: https://data.humdata.org/dataset/68cd0f9e-fa8e-4db6-bda1-6990514fcdf7/resource/081499aa-8cb0-428c-9509-1c19be2bf791/download/rdc_mouvement_de_population_retourne_mai_2025.xlsx
  format: null
  id: resource_081499aa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rdc_mouvement_de_population_retourne_mai_2025.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ochacod_rdcstockdepersonnesretour_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-05-31'
  start: '2023-12-01'
temporal_resolution: null
title: "DR Congo - RDC stock de personnes retourn\xE9es au 31 mai 2025"
version: null
vulnerability: null
---
