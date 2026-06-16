---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/timor-leste-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/timor-leste-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/timor-leste-acute-food-insecurity-country-data
dataset_id: rdls_lss-tls_ipc_acuteinsecuritycountrydat_2022
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/timor-leste-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using standardized IPC methodology to assess food
    insecurity phases across population groups. Population figures are based on official
    country estimates and classified into IPC phases (1-5) representing severity of
    food insecurity, with current and projected estimates provided at national and
    sub-national administrative levels.
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
- href: https://data.humdata.org/dataset/timor-leste-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: index
    description: Population classified in acute food insecurity phases (IPC Phase
      1-5) due to drought and livelihood stress
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
          quantity_kind: currency
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
  description: 'Timor-Leste: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/9bc4d8bc-0de4-40e4-94c5-a9a6fa3ecf54/resource/512efb69-957a-45f7-8e45-b751fa76b2d7/download/ipc_tls.geojson
  format: null
  id: resource_512efb69
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tls.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Timor-Leste: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/9bc4d8bc-0de4-40e4-94c5-a9a6fa3ecf54/resource/e967c034-daf9-4d80-b8da-5ab18070ee1e/download/ipc_tls_national_long_latest.csv
  format: null
  id: resource_e967c034
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tls_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Timor-Leste: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/9bc4d8bc-0de4-40e4-94c5-a9a6fa3ecf54/resource/7db95059-290d-4ff3-b2bd-9846f2c3e4cb/download/ipc_tls_area_long_latest.csv
  format: null
  id: resource_7db95059
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tls_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Timor-Leste: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/9bc4d8bc-0de4-40e4-94c5-a9a6fa3ecf54/resource/0efb04fb-0f0b-45f8-9a40-d96403865e0e/download/ipc_tls_area_wide_latest.csv
  format: null
  id: resource_0efb04fb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tls_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Timor-Leste: Acute Food Insecurity Country Data (All IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/9bc4d8bc-0de4-40e4-94c5-a9a6fa3ecf54/resource/457017e5-c279-4840-9030-9bf3c8fe70ec/download/ipc_tls_national_long.csv
  format: null
  id: resource_457017e5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tls_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Timor-Leste: Acute Food Insecurity Country Data (All IPC national
    data in wide form)'
  download_url: https://data.humdata.org/dataset/9bc4d8bc-0de4-40e4-94c5-a9a6fa3ecf54/resource/716cef75-f657-41c7-a10a-ab16c04ff456/download/ipc_tls_national_wide.csv
  format: null
  id: resource_716cef75
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tls_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Timor-Leste: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/9bc4d8bc-0de4-40e4-94c5-a9a6fa3ecf54/resource/e28f86b7-6c3b-4ae0-8dd0-e92513ec4c15/download/ipc_tls_area_long.csv
  format: null
  id: resource_e28f86b7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tls_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Timor-Leste: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/9bc4d8bc-0de4-40e4-94c5-a9a6fa3ecf54/resource/6a238528-ff85-4ba8-9a77-43e2a8336275/download/ipc_tls_area_wide.csv
  format: null
  id: resource_6a238528
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tls_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tls_ipc_acuteinsecuritycountrydat_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - TLS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-09-30'
  start: '2022-11-01'
temporal_resolution: null
title: 'Timor-Leste: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
