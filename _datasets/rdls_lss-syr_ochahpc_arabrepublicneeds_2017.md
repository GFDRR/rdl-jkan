---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/syrian-arab-republic-humanitarian-needs
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian Country Team and partners
    url: https://data.humdata.org/dataset/syrian-arab-republic-humanitarian-needs
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/syrian-arab-republic-humanitarian-needs
creator:
  affiliation: null
  email: null
  name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
  url: https://data.humdata.org/dataset/syrian-arab-republic-humanitarian-needs
dataset_id: rdls_lss-syr_ochahpc_arabrepublicneeds_2017
description: 'This dataset was compiled by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. It provides the Humanitarian Country Team''s shared understanding of the
  crisis, including the most pressing humanitarian need and the estimated number of
  people who need assistance, and represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/syrian-arab-republic-humanitarian-needs]'
details: Humanitarian needs data up to 2024 were provided manually from OCHA field
  offices on an annual basis. From 2024 onwards, Humanitarian needs data will be updated
  automatically through OCHA's HPC tools API.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: This dataset aggregates humanitarian needs assessments from multiple
    clusters and humanitarian partners in Syria, compiled by UNOCHA. Data was derived
    from cluster-level analysis and consolidated into inter-sector severity and people-in-need
    (PiN) estimates at administrative levels 1-3, with sector-specific breakdowns
    for response planning.
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
- href: https://data.humdata.org/dataset/syrian-arab-republic-humanitarian-needs
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need across multiple sectors due to Syrian humanitarian
      crisis
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
    description: Targeted and reached populations across humanitarian response sectors
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
  url: https://reliefweb.int/attachments/5eef8c1a-fe65-4961-9d6e-a8bec0578724/Syria%20HNO%202024_EN.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised national 2026 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/c58c2303-2071-496b-afdd-764a41faf70b/download/syr_hpc_needs_api_2026.csv
  format: null
  id: resource_c58c2303
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_api_2026.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised national 2025 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/ce08d74b-e3f5-4375-aed5-bf6faf88dced/download/syr_hpc_needs_api_2025.csv
  format: null
  id: resource_ce08d74b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_api_2025.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Syria Humanitarian Needs 2025 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/64b4ace4-f4bd-44ab-ad1e-fe6243a357e9/download/syria_hpc_needs_2025.xlsx
  format: null
  id: resource_64b4ace4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syria_hpc_needs_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This resource contains standardised subnational 2024 Humanitarian Needs
    Overview data taken from the OCHA HPC Tools system which is under active development.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/ce700599-5cab-4daf-82ac-4a9fbfb51b38/download/syr_hpc_needs_api_2024.csv
  format: null
  id: resource_ce700599
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_api_2024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Syria Humanitarian Needs 2024 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/0bc1b237-862c-47f9-b751-443d8ffa9bee/download/pin_severity_hno_2024_20240401.xlsx
  format: null
  id: resource_0bc1b237
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Syria Humanitarian Needs 2023 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/77b38c47-d802-4ae5-8445-73cd3132be22/download/pin_severity_hno_2023.xlsx
  format: null
  id: resource_77b38c47
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Syria Humanitarian Needs 2022 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/1db339d1-2ffe-498c-ada3-5731dffdff42/download/pin_severity_hno_2022.xlsx
  format: null
  id: resource_1db339d1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Syria Humanitarian Needs 2021 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/f2616997-c404-4aa9-9918-e33ac2cc7657/download/pin_severity_hno_2021.xlsx
  format: null
  id: resource_f2616997
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Syria Humanitarian Needs 2020 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/d2ccb4b7-7d43-42bd-8d4b-520e0bd766c1/download/pin_severity_hno_2020.xlsx
  format: null
  id: resource_d2ccb4b7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Syria Humanitarian Needs 2019 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/b93a3abb-ee2a-4cde-a1c2-53d00f610181/download/pin_severity_hno_2019.xlsx
  format: null
  id: resource_b93a3abb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_2019.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Syria Humanitarian Needs 2018 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/9bc31bb3-4752-4d61-83fb-903a3264d66b/download/pin_severity_pmr_2018.xlsx
  format: null
  id: resource_9bc31bb3
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_2018.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The Syria Humanitarian Needs 2017 dataset was compiled by OCHA on behalf
    of the Humanitarian Country Team and partners.
  download_url: https://data.humdata.org/dataset/cfd515f3-e45c-4c6b-a0f4-1a517f0b726f/resource/a2101ffc-4831-4b0d-bda6-86c9d183a568/download/pin_severity_hno_2017.xlsx
  format: null
  id: resource_a2101ffc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: syr_hpc_needs_2017.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_ochahpc_arabrepublicneeds_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'Syrian Arab Republic: Humanitarian Needs'
version: null
vulnerability: null
---
