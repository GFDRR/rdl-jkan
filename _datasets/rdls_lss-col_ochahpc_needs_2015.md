---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/colombia-humanitarian-needs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/colombia-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/colombia-humanitarian-needs
dataset_id: rdls_lss-col_ochahpc_needs_2015
description: 'This dataset was compiled by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. It provides the Humanitarian Country Team''s shared understanding of the
  crisis, including the most pressing humanitarian need and the estimated number of
  people who need assistance, and represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/colombia-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian needs data compiled by UNOCHA from multiple cluster sources
    and humanitarian partners through the Humanitarian Country Team assessment process.
    Data aggregated at administrative level 1 (departments) with annual updates from
    2015-2026, capturing people in need, affected populations, and displacement figures
    to inform joint strategic response planning.
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
- href: https://data.humdata.org/dataset/colombia-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People affected by flooding requiring humanitarian assistance
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
    description: Internally displaced persons from flood-related crises
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
  description: This resource contains standardised national 2026 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/2ee27d72-8e6f-4aee-83fd-2bddeaad6428/download/col_hpc_needs_api_2026.csv
  format: null
  id: resource_2ee27d72
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_api_2026.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2025 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/a9ee2367-1563-4a00-8f16-4c0568f44003/download/col_hpc_needs_api_2025.csv
  format: null
  id: resource_a9ee2367
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_api_2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2024 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/d98afd76-55a9-451e-80ba-4e5c81602f99/download/col_hpc_needs_api_2024.csv
  format: null
  id: resource_d98afd76
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_api_2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Colombia Humanitarian Needs 2024 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/771034b7-d89a-485c-8655-8d4a52172277/download/matriz-jiaf-2.0-colombia-2024_v4_vf.xlsx
  format: null
  id: resource_771034b7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_2024
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Colombia Humanitarian Needs 2023 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/c17c6020-a670-4ca7-8d73-6f32a737c292/download/pin-intersectorial-con-indicadores-clave-2023-colombia.xlsx
  format: null
  id: resource_c17c6020
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Colombia Humanitarian Needs 2021 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/9cc357a8-c2db-415a-8c80-948316041a85/download/pin-intersectorial-2021-con-indicadores-clave.xlsx
  format: null
  id: resource_9cc357a8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Colombia Humanitarian Needs 2020 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/ce6993e4-3aca-42d4-b90a-fa98780e9458/download/colombia-pin-2020-sectoriales-por-ch.xlsx
  format: null
  id: resource_ce6993e4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Colombia Humanitarian Needs 2019 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/c0eee459-0a60-4e8f-9613-7e7f0b8c67a5/download/hno_2019_final.xlsx
  format: null
  id: resource_c0eee459
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Colombia Humanitarian Needs 2017 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/e9fb98c6-ccae-49a4-b6fa-392da7698eba/download/hno-2017-priorizacion-necesidades-v4.xlsx
  format: null
  id: resource_e9fb98c6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Colombia Humanitarian Needs 2015 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/56fb6a8c-bf86-4678-ac4e-99873fa05f42/resource/973d9b9e-690d-4bbe-9275-c791a5f634b9/download/141007-hno-2015-necesidades.xlsx
  format: null
  id: resource_973d9b9e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: col_hpc_needs_2015
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochahpc_needs_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: 'Colombia: Humanitarian Needs'
version: null
vulnerability: null
---
