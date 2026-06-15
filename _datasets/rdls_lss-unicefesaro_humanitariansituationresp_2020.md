---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNICEF ESARO
    url: https://data.humdata.org/dataset/eastern-southern-africa-humanitarian-situation-and-response-dec2019
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WHO
    url: https://data.humdata.org/dataset/eastern-southern-africa-humanitarian-situation-and-response-dec2019
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/eastern-southern-africa-humanitarian-situation-and-response-dec2019
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR
    url: https://data.humdata.org/dataset/eastern-southern-africa-humanitarian-situation-and-response-dec2019
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/eastern-southern-africa-humanitarian-situation-and-response-dec2019
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/eastern-southern-africa-humanitarian-situation-and-response-dec2019
creator:
  affiliation: null
  email: null
  name: UNICEF Eastern and Southern Africa Regional Office (ESARO) (inactive)
  url: https://data.humdata.org/dataset/eastern-southern-africa-humanitarian-situation-and-response-dec2019
dataset_id: rdls_lss-unicefesaro_humanitariansituationresp_2020
description: 'UNICEF Eastern and Southern Africa Risks and Hazards- situation and
  response. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/eastern-southern-africa-humanitarian-situation-and-response-dec2019]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Multi-agency humanitarian situation data aggregated from UNICEF, WHO,
    OCHA, UNHCR, IOM, and government sources for Eastern and Southern Africa in 2020.
    The dataset compiles displacement counts, food security impacts, education disruptions,
    and humanitarian needs across the region from various sitreps and assessments.
  sources:
  - id: source_1
    license: null
    name: UNICEF ESARO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: WHO
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: UNHCR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
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
- href: https://data.humdata.org/dataset/eastern-southern-africa-humanitarian-situation-and-response-dec2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by food insecurity and humanitarian needs in
      Eastern and Southern Africa
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and refugees from various hazards and
      conflicts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Eastern and Southern Africa Humanitarian Situation and Response (UNICEF
    Eastern and Southern Africa Risks and Hazards- situation and response)
  download_url: https://data.humdata.org/dataset/6af23552-38ee-4bd6-a4ac-e4ccf229bca5/resource/b060b8d8-f066-4e4d-9824-4a063a7a426a/download/unicef-esaro-regional-db-2020-10.2.2021-annual-2020.xlsx
  format: null
  id: resource_b060b8d8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNICEF ESARO Regional db 2020 10.2.2021 annual 2020.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-unicefesaro_humanitariansituationresp_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - AGO
  - BDI
  - COM
  - DZA
  - ERI
  - ETH
  - KEN
  - LSO
  - MDG
  - MWI
  - MOZ
  - MUS
  - NAM
  - RWA
  - SYC
  - SOM
  - ZAF
  - SSD
  - SWZ
  - TZA
  - UGA
  - ZMB
  - ZWE
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: Eastern and Southern Africa Humanitarian Situation and Response
version: null
vulnerability: null
---
