---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/benin-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/benin-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/benin-acute-food-insecurity-country-data
dataset_id: rdls_lss-ben_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/benin-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates data
    from the National IPC Technical Working Group to produce standardized food insecurity
    phase classifications (Phase 1-5) for Benin's population at national, administrative
    level 1, and area levels. Population figures are based on official country estimates
    and IPC reports, with validity periods and projections included.
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
- href: https://data.humdata.org/dataset/benin-acute-food-insecurity-country-data
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
  description: 'Benin: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/e991b9ef-3e99-42fd-8fe9-d1d801d85056/download/ipc_ben.geojson
  format: null
  id: resource_e991b9ef
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/f40114f0-f02b-4343-b1e1-80ddd04e9964/download/ipc_ben_national_long_latest.csv
  format: null
  id: resource_f40114f0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/e835150e-6078-4a38-b4b9-cb0ada5a0698/download/ipc_ben_level1_long_latest.csv
  format: null
  id: resource_e835150e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/f8964c29-f0e7-49c9-8b3a-3da0a9027316/download/ipc_ben_level1_wide_latest.csv
  format: null
  id: resource_f8964c29
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (Latest IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/af8c5248-c9c2-41b0-ae75-aa227d258784/download/ipc_ben_area_long_latest.csv
  format: null
  id: resource_af8c5248
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (Latest IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/3a6b87c0-d7c7-4888-8dcf-4b2f66ab733a/download/ipc_ben_area_wide_latest.csv
  format: null
  id: resource_3a6b87c0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (All IPC national data in
    long form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/568549c5-b999-4bfb-a48b-befa64ceec4f/download/ipc_ben_national_long.csv
  format: null
  id: resource_568549c5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (All IPC national data in
    wide form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/0d8a8286-c02d-41ac-baae-382fecd15d42/download/ipc_ben_national_wide.csv
  format: null
  id: resource_0d8a8286
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (All IPC level 1 data in
    long form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/e05d1901-1148-41d1-9da9-93ff584b0043/download/ipc_ben_level1_long.csv
  format: null
  id: resource_e05d1901
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (All IPC level 1 data in
    wide form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/c7525eef-8e97-484d-ae0c-cfe6d8c999d4/download/ipc_ben_level1_wide.csv
  format: null
  id: resource_c7525eef
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/dcedfa7a-b612-4cf5-a4f3-1248e7a065ac/download/ipc_ben_area_long.csv
  format: null
  id: resource_dcedfa7a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Benin: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/251bc56c-f558-4030-9082-f6105561dee9/resource/acb5fa7f-8ce5-4a9d-a87e-9025eaa66fd6/download/ipc_ben_area_wide.csv
  format: null
  id: resource_acb5fa7f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ben_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ben_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - BEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Benin: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
