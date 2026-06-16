---
attributions:
- entity:
    affiliation: null
    email: null
    name: IPC (Integrated Food Security Phase Classification)
    url: https://data.humdata.org/dataset/rdc-ipc-amn
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ENN (Emergency Nutrition Network)
    url: https://data.humdata.org/dataset/rdc-ipc-amn
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/rdc-ipc-amn
creator:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/rdc-ipc-amn
dataset_id: rdls_lss-cod_hdx_republiquedemocratiquedum_2024
description: "Ce jeu de donn\xE9es pr\xE9sente l'analyse de la malnutrition aigu\xEB\
  \ de l'IPC (AMN).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/rdc-ipc-amn]"
details: "Limites de l'analyse : Le niveau de d\xE9sagr\xE9gation de l'analyse n'a\
  \ pas pu syst\xE9matiquement se faire jusqu'au niveau Zone de Sant\xE9."
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IPC Acute Malnutrition analysis for Democratic Republic of Congo, classifying
    malnutrition severity (global and severe acute malnutrition) among children under
    5 and pregnant/lactating women by health zone. Data covers two annual periods
    (July 2024-June 2025 and July 2025-June 2026) with treatment need estimates derived
    from IPC standardized protocols.
  sources:
  - id: source_1
    license: null
    name: IPC (Integrated Food Security Phase Classification)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: ENN (Emergency Nutrition Network)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/rdc-ipc-amn
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition cases in children under 5 and pregnant/lactating
      women requiring treatment, classified by severity (global and severe acute malnutrition)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  description: "Analyse de la malnutrition aigu\xEB de l'IPC (AMN) pour la p\xE9riode\
    \ de Juillet 2025 \xE0 Juin 2026, au niveau des provinces, territoires et zones\
    \ de sant\xE9."
  download_url: https://data.humdata.org/dataset/163d1b22-52d4-4f26-80bf-d5da720dda8f/resource/869a29e1-a2b4-41fa-9838-49f10f882d87/download/rdc-ipc-amn-juillet2025-juin2026.xlsx
  format: null
  id: resource_869a29e1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rdc-ipc-amn-juillet2025-juin2026
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Analyse de la malnutrition aigu\xEB de l'IPC (AMN) pour la p\xE9riode\
    \ de Juillet 2024 \xE0 Juin 2025, au niveau des provinces, territoires et zones\
    \ de sant\xE9."
  download_url: https://data.humdata.org/dataset/163d1b22-52d4-4f26-80bf-d5da720dda8f/resource/9784c335-cba0-49d2-805d-c5e4e2281ee1/download/rdc-ipc-amn-july2024-june2025.xlsx
  format: null
  id: resource_9784c335
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rdc-ipc-amn-july2024-june2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Analyse de la malnutrition aigu\xEB de l'IPC (AMN) pour la p\xE9riode\
    \ de Juillet 2024 \xE0 Juin 2025, au niveau des provinces, territoires et zones\
    \ de sant\xE9."
  download_url: https://data.humdata.org/dataset/163d1b22-52d4-4f26-80bf-d5da720dda8f/resource/eba74ba3-f8d4-4fe9-a612-e1d2f170902b/download/rdc-ipc-amn-july2024-june2025.csv
  format: null
  id: resource_eba74ba3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rdc-ipc-amn-july2024-june2025
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_hdx_republiquedemocratiquedum_2024
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
  end: '2026-06-30'
  start: '2024-06-01'
temporal_resolution: null
title: "R\xE9publique D\xE9mocratique du Congo : Malnutrition Aigu\xEB"
version: null
vulnerability: null
---
