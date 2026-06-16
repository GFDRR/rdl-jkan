---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/chad-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/chad-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/chad-acute-food-insecurity-country-data
dataset_id: rdls_lss-tcd_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/chad-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates data
    from multiple sources (market prices, livelihood assessments, nutrition surveys)
    analyzed by the National IPC Technical Working Group to classify populations into
    five phases of food insecurity severity. Population estimates are based on official
    country census figures and IPC analysis periods, producing both current and projected
    food insecurity classifications at national and sub-national administrative levels.
  sources:
  - id: source_1
    license: null
    name: National IPC Technical Working Group
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/chad-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC Acute Food Insecurity phase, indicating
      food insecurity severity linked to drought and other shocks
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
  url: https://www.ipcinfo.org/ipc/technical/manual_en
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (IPC GeoJSON for latest analysis)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/b7c7cb79-ba72-4ebc-a98f-773e025a24de/download/ipc_tcd.geojson
  format: null
  id: resource_b7c7cb79
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/c52c7ed7-9f4b-4878-82ee-643385266b9a/download/ipc_tcd_national_long_latest.csv
  format: null
  id: resource_c52c7ed7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/de819621-e205-40a0-b37c-c8e88d47deb9/download/ipc_tcd_level1_long_latest.csv
  format: null
  id: resource_de819621
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/cf87a830-38db-4893-9152-a3423613215d/download/ipc_tcd_level1_wide_latest.csv
  format: null
  id: resource_cf87a830
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (Latest IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/10e0bad6-6b42-4bdc-9425-cc168dd7db3b/download/ipc_tcd_area_long_latest.csv
  format: null
  id: resource_10e0bad6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (Latest IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/e729c025-42f1-4145-b5a1-7ef8a5bdcf84/download/ipc_tcd_area_wide_latest.csv
  format: null
  id: resource_e729c025
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (All IPC national data in
    long form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/baabbe4b-13fa-4971-9269-25a0aba38c11/download/ipc_tcd_national_long.csv
  format: null
  id: resource_baabbe4b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (All IPC national data in
    wide form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/3730a41b-df8b-4ce0-a6ef-a7412d769172/download/ipc_tcd_national_wide.csv
  format: null
  id: resource_3730a41b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (All IPC level 1 data in
    long form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/87f11baa-01f6-4774-a074-abf43775d07b/download/ipc_tcd_level1_long.csv
  format: null
  id: resource_87f11baa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (All IPC level 1 data in
    wide form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/dddecf15-8de4-4654-9bd9-9d51cc08a189/download/ipc_tcd_level1_wide.csv
  format: null
  id: resource_dddecf15
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/b5cedaa7-6036-4de8-b71f-6238cab7ef3a/download/ipc_tcd_area_long.csv
  format: null
  id: resource_b5cedaa7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Chad: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/e7315ba9-c0c0-46c5-972f-6ab41201ebc1/resource/29affa08-52e4-4bf6-81d7-676380cbbbdc/download/ipc_tcd_area_wide.csv
  format: null
  id: resource_29affa08
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tcd_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tcd_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Chad: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
