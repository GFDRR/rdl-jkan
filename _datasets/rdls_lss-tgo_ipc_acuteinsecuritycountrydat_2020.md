---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/togo-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/togo-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/togo-acute-food-insecurity-country-data
dataset_id: rdls_lss-tgo_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/togo-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification was produced by the National
    IPC Technical Working Group using the standardized IPC Manual methodology to assess
    food insecurity phases across national and sub-national administrative levels.
    Population estimates are based on official country census figures, with classifications
    stratified by IPC phase (1-5) and validity periods to support food security decision-making.
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
- href: https://data.humdata.org/dataset/togo-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC acute food insecurity phase, indicating
      food security status and severity
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
  description: 'Togo: Acute Food Insecurity Country Data (IPC GeoJSON for latest analysis)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/a1355557-c46c-41a8-b130-d5dd76c8af95/download/ipc_tgo.geojson
  format: null
  id: resource_a1355557
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/301faef1-d646-4757-823c-1457e2f95f3e/download/ipc_tgo_national_long_latest.csv
  format: null
  id: resource_301faef1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/22599535-07dc-4c38-a88c-6ecdf0f800d6/download/ipc_tgo_level1_long_latest.csv
  format: null
  id: resource_22599535
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/9f479cc4-d9d5-4d6d-81bc-710c9308bf0c/download/ipc_tgo_level1_wide_latest.csv
  format: null
  id: resource_9f479cc4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (Latest IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/9255ef3b-bf9f-4e6c-9dce-6423373198f0/download/ipc_tgo_area_long_latest.csv
  format: null
  id: resource_9255ef3b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (Latest IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/867553e2-f3e8-4318-ba41-b4aa1f8dea97/download/ipc_tgo_area_wide_latest.csv
  format: null
  id: resource_867553e2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (All IPC national data in
    long form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/d049d848-448d-4791-9a18-39c4707c56e4/download/ipc_tgo_national_long.csv
  format: null
  id: resource_d049d848
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (All IPC national data in
    wide form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/74a05b35-1cdc-488b-963e-4eacca38841d/download/ipc_tgo_national_wide.csv
  format: null
  id: resource_74a05b35
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (All IPC level 1 data in
    long form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/1bf93eb5-8af3-48d4-a817-4478112e51da/download/ipc_tgo_level1_long.csv
  format: null
  id: resource_1bf93eb5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (All IPC level 1 data in
    wide form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/ea4beafa-3ed7-46a9-ade6-85a7e32ad89e/download/ipc_tgo_level1_wide.csv
  format: null
  id: resource_ea4beafa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/d2cff3d3-e3ba-402e-b8a1-24926a13f0df/download/ipc_tgo_area_long.csv
  format: null
  id: resource_d2cff3d3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Togo: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/18a62cd8-2735-475d-add4-6a427618d4b2/resource/bc135224-2fa2-487b-96d9-9e62aac622da/download/ipc_tgo_area_wide.csv
  format: null
  id: resource_bc135224
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tgo_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tgo_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - TGO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Togo: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
