---
attributions:
- entity:
    affiliation: null
    email: null
    name: IPC (Integrated Food Security Phase Classification)
    url: https://data.humdata.org/dataset/republique-centrafricaine-analyse-de-la-malnutrition-aigue-de-l-ipc
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/republique-centrafricaine-analyse-de-la-malnutrition-aigue-de-l-ipc
creator:
  affiliation: null
  email: null
  name: IPC
  url: https://data.humdata.org/dataset/republique-centrafricaine-analyse-de-la-malnutrition-aigue-de-l-ipc
dataset_id: rdls_lss-caf_hdx_republiquemalnutritionaig_2023
description: "Situation de la malnutrition aigu\xEB au niveau des sous-pr\xE9fecture\
  \ \xE0 partir de 2023.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/republique-centrafricaine-analyse-de-la-malnutrition-aigue-de-l-ipc]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC conducted multi-sectoral analysis across Central African Republic
    sub-prefectures to classify acute malnutrition phases and estimate affected populations
    (children 6-59 months, pregnant/lactating women) from September 2023 to August
    2024 and March 2025 to February 2026, producing prevalence rates and case counts
    disaggregated by age and gender.
  sources:
  - id: source_1
    license: null
    name: IPC (Integrated Food Security Phase Classification)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/republique-centrafricaine-analyse-de-la-malnutrition-aigue-de-l-ipc
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition prevalence and affected child population from
      drought-driven food insecurity
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.ipcinfo.org/ipc-country-analysis/details-map/en/c/1159671/?iso3=CAF
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Estimation des populations atteintes de malnutrition aigu\xEB ayant\
    \ besoin de traitement sur la p\xE9riode d'analyse de mars 2025 \xE0 f\xE9vrier\
    \ 2026 - 73 Sous-pr\xE9fectures et la ville de Bangui qui comprend quatre subdivisions,\
    \ dont chacune a \xE9t\xE9 consid\xE9r\xE9e comme une unit\xE9 d'analyse."
  download_url: https://data.humdata.org/dataset/8a686db7-2606-40cc-bdf5-29fc8235f2d4/resource/40da537f-d4ba-4eeb-b835-ec7df13ead71/download/ipc_car_amn_mar2025_feb2026.xlsx
  format: null
  id: resource_40da537f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IPC_CAR_AMN_Mar2025_Feb2026.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Estimation des populations atteintes de malnutrition aigu\xEB ayant\
    \ besoin de traitement sur la p\xE9riode d'analyse de septembre 2023 \xE0 ao\xFB\
    t 2024 - sur 69 sous-pr\xE9fectures, de la ville de Bangui et du camp de refugi\xE9\
    s de Birao."
  download_url: https://data.humdata.org/dataset/8a686db7-2606-40cc-bdf5-29fc8235f2d4/resource/184bb073-3c7c-4b1b-925e-c1af82c128d4/download/caf-ipc-estimation-populations-malnutrion-aigue-sep2023aout2024.xlsx
  format: null
  id: resource_184bb073
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "caf-ipc-estimation-populations-malnutrion-aigu\xEB-sep2023-ao\xFBt2024.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_hdx_republiquemalnutritionaig_2023
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
  end: '2026-02-28'
  start: '2023-09-01'
temporal_resolution: null
title: "Central African Republic - R\xE9publique Centrafricaine : Malnutrition Aigu\xEB"
version: null
vulnerability: null
---
