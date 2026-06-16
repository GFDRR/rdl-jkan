---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/bangladesh-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/bangladesh-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/bangladesh-acute-food-insecurity-country-data
dataset_id: rdls_lss-bgd_ipc_acuteinsecuritycountrydat_2023
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/bangladesh-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates food
    security assessments across Bangladesh at national, administrative level 1, and
    area levels. Population estimates are classified into IPC phases (1-5) representing
    severity of food insecurity, with current and projected estimates. Data is produced
    by the National IPC Technical Working Group using official country population
    figures and published in country IPC reports.
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
- href: https://data.humdata.org/dataset/bangladesh-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC acute food insecurity phase, indicating
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
  description: 'Bangladesh: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/07c84599-834b-4140-a827-fde1dc509dc9/download/ipc_bgd.geojson
  format: null
  id: resource_07c84599
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/a134ad09-edba-4cb2-9d4c-356ade9e8a13/download/ipc_bgd_national_long_latest.csv
  format: null
  id: resource_a134ad09
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (Latest IPC level 1
    data in long form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/4bf86474-8038-4acb-82b6-1dbcf755b252/download/ipc_bgd_level1_long_latest.csv
  format: null
  id: resource_4bf86474
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (Latest IPC level 1
    data in wide form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/2b5e0e88-bc37-42b5-b1fc-39187f2a2155/download/ipc_bgd_level1_wide_latest.csv
  format: null
  id: resource_2b5e0e88
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/8350e2e8-4787-4f84-be00-792f5d2548db/download/ipc_bgd_area_long_latest.csv
  format: null
  id: resource_8350e2e8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/0a8d7080-8adb-4ed5-a478-389a81a3a931/download/ipc_bgd_area_wide_latest.csv
  format: null
  id: resource_0a8d7080
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/b27d9f56-fcea-4705-83c4-80fa43120444/download/ipc_bgd_national_long.csv
  format: null
  id: resource_b27d9f56
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/110abd12-24e2-40a1-bb81-8130eb52aa2d/download/ipc_bgd_national_wide.csv
  format: null
  id: resource_110abd12
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/95f6db9b-a74f-4b60-8cca-bf50325d2581/download/ipc_bgd_level1_long.csv
  format: null
  id: resource_95f6db9b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/e4d45729-08f2-4bfd-94f0-280f760e4120/download/ipc_bgd_level1_wide.csv
  format: null
  id: resource_e4d45729
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/7b79fda7-c4a1-4a3e-b2fc-228ce31dd3e3/download/ipc_bgd_area_long.csv
  format: null
  id: resource_7b79fda7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bangladesh: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/1194daac-6c0d-48a3-a3eb-00cdaaa7c581/resource/d127115b-20b8-48bc-97a1-ba1b25d72dfa/download/ipc_bgd_area_wide.csv
  format: null
  id: resource_d127115b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bgd_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bgd_ipc_acuteinsecuritycountrydat_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2023-03-01'
temporal_resolution: null
title: 'Bangladesh: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
