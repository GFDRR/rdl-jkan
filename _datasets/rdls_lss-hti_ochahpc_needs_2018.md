---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Country Team and partners
    url: https://data.humdata.org/dataset/haiti-humanitarian-needs
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: JIAF (Joint Inter-Agency Analysis Framework)
    url: https://data.humdata.org/dataset/haiti-humanitarian-needs
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/haiti-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/haiti-humanitarian-needs
dataset_id: rdls_lss-hti_ochahpc_needs_2018
description: 'This data was consolidated by OCHA on behalf of the Humanitarian Country
  Team and partners. It provides a shared understanding of the crisis, including the
  most pressing humanitarian need and the estimated number of people who need assistance.
  It represents a consolidated evidence base and helps inform joint strategic response
  planning.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/haiti-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian needs data consolidated by OCHA on behalf of the Humanitarian
    Country Team through the HNO process, aggregating partner assessments of affected
    populations, people in need, and targeted assistance across sectors and administrative
    divisions. The JIAF methodology standardizes data collection and analysis across
    humanitarian clusters to produce a shared evidence base for strategic response
    planning.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Country Team and partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: JIAF (Joint Inter-Agency Analysis Framework)
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/haiti-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need across humanitarian clusters due to drought and insecurity
      crisis
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
  url: https://analysis.jiaf.info/
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised national 2026 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/72761082-d078-48d3-938b-b8cdb8b3d687/download/hti_hpc_needs_api_2026.csv
  format: null
  id: resource_72761082
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_api_2026.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2025 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/b5b9c773-5916-42d3-a349-30c898ca59db/download/hti_hpc_needs_api_2025.csv
  format: null
  id: resource_b5b9c773
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_api_2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2024 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/6e72866e-c976-4b08-9873-643b6e34c92d/download/hti_hpc_needs_api_2024.csv
  format: null
  id: resource_6e72866e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_api_2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Haiti Humanitarian Needs 2024 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/fae834e9-f3cc-42db-a964-7f4c127e5019/download/hti_hpc2024_pin_cible.xlsx
  format: null
  id: resource_fae834e9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Haiti Humanitarian Needs 2023 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/697c88b8-f57b-4fa0-b735-9fc13328626b/download/hti_pin_hno_2023_hdx.xlsx
  format: null
  id: resource_697c88b8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Haiti Humanitarian Needs 2022 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/9c1ceb75-ecb2-4cfa-8cf2-ebfe9fb1be88/download/hti-pin-hno-2022-2.xlsx
  format: null
  id: resource_9c1ceb75
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Haiti Humanitarian Needs 2021 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/a6ed08e6-91c0-4776-a0fd-61b3616a1a5f/download/hti-pin-hno-2021.xlsx
  format: null
  id: resource_a6ed08e6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Haiti Humanitarian Needs 2020 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/b0fb7301-8707-4a91-810a-fe414b26f93d/download/hti-pin-hno-2020.xlsx
  format: null
  id: resource_b0fb7301
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Haiti Humanitarian Needs 2019 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/0ea85277-7274-46cb-a116-36777b93ac98/download/haiti-pin-hno-2019.xlsx
  format: null
  id: resource_0ea85277
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_2019.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Haiti Humanitarian Needs 2018 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/780d9bc7-c2c9-4dd3-9458-887e35b44698/resource/d6517a68-928e-4274-94b0-20ddddc4fb00/download/2018-haiti-revised-hno.xlsx
  format: null
  id: resource_d6517a68
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_hpc_needs_2018.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_ochahpc_needs_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: 'Haiti: Humanitarian Needs'
version: null
vulnerability: null
---
