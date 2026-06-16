---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/ethiopia-humanitarian-needs
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian Country Team and partners
    url: https://data.humdata.org/dataset/ethiopia-humanitarian-needs
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/ethiopia-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/ethiopia-humanitarian-needs
dataset_id: rdls_lss-eth_ochahpc_needs_2018
description: 'This dataset was compiled by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. It provides the Humanitarian Country Team''s shared understanding of the
  crisis, including the most pressing humanitarian need and the estimated number of
  people who need assistance, and represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The Humanitarian Needs Overview (HNO) dataset was compiled by UNOCHA
    on behalf of the Humanitarian Country Team through aggregation of partner assessments
    and reports across multiple humanitarian clusters and administrative divisions.
    Data represents consolidated estimates of people in need, affected populations,
    and targeted assistance across multiple crisis drivers (conflict, drought, flooding)
    and humanitarian sectors, processed into standardized administrative hierarchies
    (Admin 1-3) for joint strategic response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian Country Team and partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need and affected by humanitarian crisis including flood-related
      displacement
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
    description: People in need and affected by humanitarian crisis including drought-related
      food insecurity
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
    description: Internally displaced persons and affected populations from conflict
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/sites/reliefweb.int/files/resources/ethiopia_2021_humanitarian_needs_overview_hno.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised national 2025 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/882d0746-ac2a-4471-b40d-a92dee832ee2/resource/5c049ef4-1dc0-4618-bb7f-a7be0b044137/download/eth_hpc_needs_api_2025.csv
  format: null
  id: resource_5c049ef4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eth_hpc_needs_api_2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2024 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/882d0746-ac2a-4471-b40d-a92dee832ee2/resource/79eb6301-add8-42de-95bc-6088ffba7731/download/eth_hpc_needs_api_2024.csv
  format: null
  id: resource_79eb6301
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eth_hpc_needs_api_2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Ethiopia Humanitarian Needs 2024 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/882d0746-ac2a-4471-b40d-a92dee832ee2/resource/31eec4ef-87d8-4278-9c29-4c80558eb39f/download/ethiopia-2024-humanitairan-needs-overview_hxl.xlsx
  format: null
  id: resource_31eec4ef
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eth_hpc_needs_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Ethiopia Humanitarian Needs 2021 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/882d0746-ac2a-4471-b40d-a92dee832ee2/resource/a43c1bb3-084a-422e-aa9c-16c310b76209/download/ethiopia-2021-humanitairan-needs-overview.xlsx
  format: null
  id: resource_a43c1bb3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eth_hpc_needs_2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Ethiopia Humanitarian Needs 2020 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/882d0746-ac2a-4471-b40d-a92dee832ee2/resource/04e357f9-9ab7-4d6b-8102-2503bf02c6be/download/ethiopia-2020-humanitarian-needs-overview.xlsx
  format: null
  id: resource_04e357f9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eth_hpc_needs_2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Ethiopia Humanitarian Needs 2019 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/882d0746-ac2a-4471-b40d-a92dee832ee2/resource/d3f41f1c-f110-40e0-b65f-4e05afcdb9cf/download/ethiopia-humanitarian-needs-overview_2019.xlsx
  format: null
  id: resource_d3f41f1c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eth_hpc_needs_2019.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Ethiopia Humanitarian Needs 2018 dataset was compiled by OCHA on
    behalf of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/882d0746-ac2a-4471-b40d-a92dee832ee2/resource/232be819-b3d2-4475-b954-c206cf430b01/download/ethiopia-hno-2018_hxl.xlsx
  format: null
  id: resource_232be819
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eth_hpc_needs_2018.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_ochahpc_needs_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-08'
  start: '2018-01-01'
temporal_resolution: null
title: 'Ethiopia: Humanitarian Needs'
version: null
vulnerability: null
---
