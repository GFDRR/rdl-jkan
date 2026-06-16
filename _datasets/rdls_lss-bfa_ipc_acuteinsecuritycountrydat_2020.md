---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/burkina-faso-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/burkina-faso-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/burkina-faso-acute-food-insecurity-country-data
dataset_id: rdls_lss-bfa_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burkina-faso-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates multi-sectoral
    evidence (food availability, access, utilization, stability) collected by the
    National IPC Technical Working Group to classify populations into five phases
    of food insecurity severity. Population figures are cross-referenced with official
    country census estimates and published in periodic IPC country reports, providing
    strategically relevant impact assessments for humanitarian decision-making.
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
- href: https://data.humdata.org/dataset/burkina-faso-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC acute food insecurity phase, indicating
      drought-driven food insecurity severity
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
  description: 'Burkina Faso: Acute Food Insecurity Country Data (IPC GeoJSON for
    latest analysis)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/105a74e4-47f6-4d84-a47a-f15323985e54/download/ipc_bfa.geojson
  format: null
  id: resource_105a74e4
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/5acad95f-52dc-4028-b50d-d952d17f4a66/download/ipc_bfa_national_long_latest.csv
  format: null
  id: resource_5acad95f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (Latest IPC level
    1 data in long form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/14570e57-dd36-4e31-bbb8-4d43006034f3/download/ipc_bfa_level1_long_latest.csv
  format: null
  id: resource_14570e57
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (Latest IPC level
    1 data in wide form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/2973d85a-5a9c-4b7b-889d-764853ddcb2f/download/ipc_bfa_level1_wide_latest.csv
  format: null
  id: resource_2973d85a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (Latest IPC area
    data in long form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/1fb2f594-b927-414d-a99e-24b37b7172cb/download/ipc_bfa_area_long_latest.csv
  format: null
  id: resource_1fb2f594
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (Latest IPC area
    data in wide form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/983c1dd8-ef81-4df8-8093-d93609a2aa30/download/ipc_bfa_area_wide_latest.csv
  format: null
  id: resource_983c1dd8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (All IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/068cadd2-92f0-4906-bbb2-54ad91394aff/download/ipc_bfa_national_long.csv
  format: null
  id: resource_068cadd2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (All IPC national
    data in wide form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/b7815955-9e0f-42be-b2cb-39f5c0f99537/download/ipc_bfa_national_wide.csv
  format: null
  id: resource_b7815955
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (All IPC level 1
    data in long form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/8fad52e3-480e-4c62-85fe-32dc73eec0bc/download/ipc_bfa_level1_long.csv
  format: null
  id: resource_8fad52e3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (All IPC level 1
    data in wide form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/4eedc208-2e90-40f5-8ff0-1b3457727256/download/ipc_bfa_level1_wide.csv
  format: null
  id: resource_4eedc208
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/127ee2f2-2d66-4a25-a0e8-d24e9c5b10e0/download/ipc_bfa_area_long.csv
  format: null
  id: resource_127ee2f2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Burkina Faso: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/17bcb527-9b05-48e8-b4cf-e25180f13e8c/resource/72a37603-3f20-4ddf-ad5e-2d35c229e4d2/download/ipc_bfa_area_wide.csv
  format: null
  id: resource_72a37603
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_bfa_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bfa_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Burkina Faso: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
