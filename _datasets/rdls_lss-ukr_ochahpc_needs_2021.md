---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA Humanitarian Programme Cycle Tools
    url: https://data.humdata.org/dataset/ukraine-humanitarian-needs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/ukraine-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/ukraine-humanitarian-needs
dataset_id: rdls_lss-ukr_ochahpc_needs_2021
description: 'This dataset was compiled by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. It provides the Humanitarian Country Team''s shared understanding of the
  crisis, including the most pressing humanitarian need and the estimated number of
  people who need assistance, and represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ukraine-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian needs data compiled by UNOCHA from humanitarian partners
    through the Humanitarian Programme Cycle, aggregating observational and anecdotal
    data on affected populations, people in need (PIN), and displacement across administrative
    units in Ukraine.
  sources:
  - id: source_1
    license: null
    name: OCHA Humanitarian Programme Cycle Tools
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ukraine-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by conflict and humanitarian crisis requiring
      assistance
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Internally displaced persons (IDPs) due to conflict
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised national 2026 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/019de7ad-8043-4755-b1fb-f84ce4b961a5/resource/7c36dd7b-e5d9-45d2-ae45-f4838bcef91c/download/ukr_hpc_needs_api_2026.csv
  format: null
  id: resource_7c36dd7b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_hpc_needs_api_2026.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2025 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/019de7ad-8043-4755-b1fb-f84ce4b961a5/resource/4d9edbf8-fd51-414a-8eca-eb9b3c670116/download/ukr_hpc_needs_api_2025.csv
  format: null
  id: resource_4d9edbf8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_hpc_needs_api_2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2024 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/019de7ad-8043-4755-b1fb-f84ce4b961a5/resource/e6ae7b20-f690-4596-85c0-fff53bede24d/download/ukr_hpc_needs_api_2024.csv
  format: null
  id: resource_e6ae7b20
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_hpc_needs_api_2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Ukraine Humanitarian Needs 2024 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/019de7ad-8043-4755-b1fb-f84ce4b961a5/resource/a10ae1ac-533f-4b0a-bc5a-d04bad3ef132/download/ukr-2024-hnrp-pin-severity-targets-activities-20240119.xlsx
  format: null
  id: resource_a10ae1ac
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_hpc_needs_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Ukraine Humanitarian Needs 2023 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/019de7ad-8043-4755-b1fb-f84ce4b961a5/resource/9865aa90-d0a4-4d78-845d-3fffa67be0be/download/ukraine-2023-hno-pin-and-severity-for-hdx-20230215.xlsx
  format: null
  id: resource_9865aa90
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_hpc_needs_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Ukraine Humanitarian Needs 2022 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/019de7ad-8043-4755-b1fb-f84ce4b961a5/resource/e710eac9-5e02-4cfd-8588-69afcb870af8/download/ukr_-2022-hno_pin-sadd.xlsx
  format: null
  id: resource_e710eac9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_hpc_needs_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Ukraine Humanitarian Needs 2021 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/019de7ad-8043-4755-b1fb-f84ce4b961a5/resource/c446cddf-6f80-4c48-bd3f-9bb9f845a478/download/ukr_hno_pin_sadd_201014_final.xlsx
  format: null
  id: resource_c446cddf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukr_hpc_needs_2021.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ukr_ochahpc_needs_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: 'Ukraine: Humanitarian Needs'
version: null
vulnerability: null
---
