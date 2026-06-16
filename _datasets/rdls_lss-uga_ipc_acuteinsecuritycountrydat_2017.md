---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/uganda-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/uganda-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/uganda-acute-food-insecurity-country-data
dataset_id: rdls_lss-uga_ipc_acuteinsecuritycountrydat_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/uganda-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system integrates multi-sectoral
    data on food availability, access, and utilization to classify populations into
    five phases of food insecurity severity. National population figures are derived
    from official country estimates, and IPC phase classifications are produced by
    the National IPC Technical Working Group following the IPC Manual methodology,
    with data published at national and sub-national administrative levels.
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
- href: https://data.humdata.org/dataset/uganda-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified into IPC acute food insecurity phases (1-5)
      as a consequence of drought and other livelihood shocks
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
  description: 'Uganda: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/77b77180-ab55-43a1-8b61-07ee13eb4181/download/ipc_uga.geojson
  format: null
  id: resource_77b77180
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uganda: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/a45b0e9f-3599-4a97-aa21-c6ea3e292d91/download/ipc_uga_national_long_latest.csv
  format: null
  id: resource_a45b0e9f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uganda: Acute Food Insecurity Country Data (Latest IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/f277ec57-5948-4e99-a58b-98f3d94adb70/download/ipc_uga_area_long_latest.csv
  format: null
  id: resource_f277ec57
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uganda: Acute Food Insecurity Country Data (Latest IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/8bcd6281-a053-4253-a213-03995f531a06/download/ipc_uga_area_wide_latest.csv
  format: null
  id: resource_8bcd6281
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uganda: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/e4116f02-376a-4d8c-b62c-b15baba6438a/download/ipc_uga_national_long.csv
  format: null
  id: resource_e4116f02
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uganda: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/0caac83b-b3ea-475c-a9a0-a632b52f2d1f/download/ipc_uga_national_wide.csv
  format: null
  id: resource_0caac83b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uganda: Acute Food Insecurity Country Data (All IPC level 1 data in
    long form)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/478b4c50-df38-434f-b038-a4b727894a8b/download/ipc_uga_level1_long.csv
  format: null
  id: resource_478b4c50
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uganda: Acute Food Insecurity Country Data (All IPC level 1 data in
    wide form)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/e5f65f81-3233-4c92-a68b-c95f2df2288f/download/ipc_uga_level1_wide.csv
  format: null
  id: resource_e5f65f81
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uganda: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/debc9316-f727-409f-a85b-1a20374c26d3/download/ipc_uga_area_long.csv
  format: null
  id: resource_debc9316
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Uganda: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/7c530c85-7478-49a3-a60c-e3af9427cb01/resource/c335c454-ce1c-46f2-9612-7a12201b25d8/download/ipc_uga_area_wide.csv
  format: null
  id: resource_c335c454
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_uga_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-uga_ipc_acuteinsecuritycountrydat_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-02-28'
  start: '2017-01-01'
temporal_resolution: null
title: 'Uganda: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
