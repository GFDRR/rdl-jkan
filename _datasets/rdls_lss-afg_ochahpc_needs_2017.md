---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/afghanistan-humanitarian-needs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/afghanistan-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/afghanistan-humanitarian-needs
dataset_id: rdls_lss-afg_ochahpc_needs_2017
description: 'This dataset was compiled by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. It provides the Humanitarian Country Team''s shared understanding of the
  crisis, including the most pressing humanitarian need and the estimated number of
  people who need assistance, and represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: This dataset aggregates humanitarian needs assessments compiled by
    UNOCHA from multiple cluster partners and humanitarian organizations operating
    in Afghanistan. The data represents consolidated analysis of crisis impacts and
    population needs across multiple hazard types, derived from field assessments
    and cluster-level analysis to inform joint strategic humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need of humanitarian assistance due to flood-related crises
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
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People in need of humanitarian assistance due to drought-related
      crises
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
    description: People in need of humanitarian assistance due to earthquake-related
      crises
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
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
  description: This resource contains standardised national 2026 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/87fe9b59-4f82-44be-8b91-ec271a92ee68/download/afg_hpc_needs_api_2026.csv
  format: null
  id: resource_87fe9b59
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_api_2026.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2025 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/0b833380-f45a-445d-8690-08aed0a2ba76/download/afg_hpc_needs_api_2025.csv
  format: null
  id: resource_0b833380
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_api_2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2024 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/7fa84d35-6fe5-4e39-9ebc-46fb9e1ec9fd/download/afg_hpc_needs_api_2024.csv
  format: null
  id: resource_7fa84d35
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_api_2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset was compiled by the United Nations Office for the Coordination
    of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
    partners. It provides the Humanitarian Country Team's shared understanding of
    the crisis, including the most pressing humanitarian need and the estimated number
    of people who need assistance, and represents a consolidated evidence base and
    helps inform joint strategic response planning.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/9e82ad7e-470a-468a-a1fa-ab1bbc5ba80e/download/afg_hno_pin_2024.xlsx
  format: null
  id: resource_9e82ad7e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset was compiled by the United Nations Office for the Coordination
    of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
    partners. It provides the Humanitarian Country Team's shared understanding of
    the crisis, including the most pressing humanitarian need and the estimated number
    of people who need assistance, and represents a consolidated evidence base and
    helps inform joint strategic response planning.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/d90998a4-c72f-439d-b9bc-60225be31de0/download/afg_hno_pin_2023.xlsx
  format: null
  id: resource_d90998a4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset was compiled by the United Nations Office for the Coordination
    of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
    partners. It provides the Humanitarian Country Team's shared understanding of
    the crisis, including the most pressing humanitarian need and the estimated number
    of people who need assistance, and represents a consolidated evidence base and
    helps inform joint strategic response planning.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/4cf80a8c-ea53-469a-a56b-68f958aef323/download/afg_hno_pin_2022.xlsx
  format: null
  id: resource_4cf80a8c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset was compiled by the United Nations Office for the Coordination
    of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
    partners. It provides the Humanitarian Country Team's shared understanding of
    the crisis, including the most pressing humanitarian need and the estimated number
    of people who need assistance, and represents a consolidated evidence base and
    helps inform joint strategic response planning.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/e57f516a-d402-4c2b-b2c9-fee0767d4d34/download/afg_hno_pin_2021.xlsx
  format: null
  id: resource_e57f516a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset was compiled by the United Nations Office for the Coordination
    of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
    partners. It provides the Humanitarian Country Team's shared understanding of
    the crisis, including the most pressing humanitarian need and the estimated number
    of people who need assistance, and represents a consolidated evidence base and
    helps inform joint strategic response planning.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/d66174a3-0d8c-4580-88c5-c44874398656/download/afg_hrp_2020_revision_pin_jun_2020.xlsx
  format: null
  id: resource_d66174a3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset was compiled by the United Nations Office for the Coordination
    of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
    partners. It provides the Humanitarian Country Team's shared understanding of
    the crisis, including the most pressing humanitarian need and the estimated number
    of people who need assistance, and represents a consolidated evidence base and
    helps inform joint strategic response planning.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/608954bf-0373-4986-97f0-ef109a8b4ae7/download/afghanistan-humanitarian-needs-overview-2019.xlsx
  format: null
  id: resource_608954bf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_2019.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset was compiled by the United Nations Office for the Coordination
    of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
    partners. It provides the Humanitarian Country Team's shared understanding of
    the crisis, including the most pressing humanitarian need and the estimated number
    of people who need assistance, and represents a consolidated evidence base and
    helps inform joint strategic response planning.
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vT7_9za6UFTrdPESMJLMkoasZ3w4I3DVg2qqyqNvdUbg0Klh3rmeQTXYXJJezEzzrrieAzaIEo4i4LP/pub?output=xlsx
  format: null
  id: resource_9bbedfca
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_2018.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset was compiled by the United Nations Office for the Coordination
    of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
    partners. It provides the Humanitarian Country Team's shared understanding of
    the crisis, including the most pressing humanitarian need and the estimated number
    of people who need assistance, and represents a consolidated evidence base and
    helps inform joint strategic response planning. This dataset covers existing needs
    as of October 2016 as well as projected needs for 2017. It includes a breakdown
    of people in need (PIN) by cluster and population types (with SADD) and documentation
    of analysis method used for the estimation of needs.
  download_url: https://data.humdata.org/dataset/f06dad13-b38b-4659-ab9f-75c0d5152b33/resource/46acd096-04fd-4e26-9595-3ac2ba66e351/download/afg_hno_pin_2017.xlsx
  format: null
  id: resource_46acd096
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afg_hpc_needs_2017.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochahpc_needs_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Afghanistan: Humanitarian Needs'
version: null
vulnerability: null
---
