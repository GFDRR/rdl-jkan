---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/sierra-leone-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/sierra-leone-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/sierra-leone-acute-food-insecurity-country-data
dataset_id: rdls_lss-sle_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sierra-leone-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using the standardized IPC manual methodology to assess
    food insecurity phases across national and sub-national administrative levels.
    Population estimates are based on official country census data and IPC field assessments,
    with results published in country IPC reports and aggregated at national, level
    1 (provincial), and area levels.
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
- href: https://data.humdata.org/dataset/sierra-leone-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC acute food insecurity phase, indicating
      food security status and vulnerability to drought and livelihood shocks
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
  description: 'Sierra Leone: Acute Food Insecurity Country Data (IPC GeoJSON for
    latest analysis)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/4266a17c-ee8b-42f3-8668-2fbd7aa37126/download/ipc_sle.geojson
  format: null
  id: resource_4266a17c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/e0a7aed8-7b7c-4ecf-8587-c67ca178fb55/download/ipc_sle_national_long_latest.csv
  format: null
  id: resource_e0a7aed8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (Latest IPC level
    1 data in long form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/48e886f2-9be5-49e0-85bb-5066de5948b3/download/ipc_sle_level1_long_latest.csv
  format: null
  id: resource_48e886f2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (Latest IPC level
    1 data in wide form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/5374378e-5179-45d8-98a2-abda8fc55203/download/ipc_sle_level1_wide_latest.csv
  format: null
  id: resource_5374378e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (Latest IPC area
    data in long form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/13fe0b65-e9be-45e1-857f-b184c0c6bb2c/download/ipc_sle_area_long_latest.csv
  format: null
  id: resource_13fe0b65
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (Latest IPC area
    data in wide form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/02d44830-44a4-47d8-a35c-0b686b532388/download/ipc_sle_area_wide_latest.csv
  format: null
  id: resource_02d44830
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (All IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/dc61e82e-2e90-47b3-ba91-701ce3b39395/download/ipc_sle_national_long.csv
  format: null
  id: resource_dc61e82e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (All IPC national
    data in wide form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/9ab830ab-08ff-4c21-a72e-cd6e2e749019/download/ipc_sle_national_wide.csv
  format: null
  id: resource_9ab830ab
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (All IPC level 1
    data in long form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/0a1293c8-6ea9-463f-93e7-41c91f9097ab/download/ipc_sle_level1_long.csv
  format: null
  id: resource_0a1293c8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (All IPC level 1
    data in wide form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/767c3cb8-71c3-41ff-9c23-9354b493a04e/download/ipc_sle_level1_wide.csv
  format: null
  id: resource_767c3cb8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/7e0b9679-c7e3-460a-8541-ed4fdc1dcaf3/download/ipc_sle_area_long.csv
  format: null
  id: resource_7e0b9679
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sierra Leone: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/71797def-82f5-4664-89d4-68293167d5d4/resource/33fe6a01-26d7-48f3-9fc1-85b4ed6d3b23/download/ipc_sle_area_wide.csv
  format: null
  id: resource_33fe6a01
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sle_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sle_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - SLE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Sierra Leone: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
