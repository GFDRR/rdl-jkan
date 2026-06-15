---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/ethiopia-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/ethiopia-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/ethiopia-acute-food-insecurity-country-data
dataset_id: rdls_lss-eth_ipc_acuteinsecuritycountrydat_2019
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates multi-sectoral
    evidence on food security conditions to assign populations to standardized phases
    (1-5) indicating severity of food insecurity. National population figures are
    based on official country estimates, and classifications are produced by the National
    IPC Technical Working Group following the IPC Manual methodology to provide decision-relevant
    information on acute food insecurity threats to lives and livelihoods.
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
- href: https://data.humdata.org/dataset/ethiopia-acute-food-insecurity-country-data
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
  description: 'Ethiopia: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/514d087e-fa33-4993-b2d5-c067403085ed/download/ipc_eth.geojson
  format: null
  id: resource_514d087e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/1203c8aa-40e5-4514-9b65-922fe1d51c11/download/ipc_eth_national_long_latest.csv
  format: null
  id: resource_1203c8aa
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/776e7733-51ca-430d-8eeb-7af9f7329f17/download/ipc_eth_level1_long_latest.csv
  format: null
  id: resource_776e7733
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/079f8e89-bbd0-458a-9461-99e209d369f5/download/ipc_eth_level1_wide_latest.csv
  format: null
  id: resource_079f8e89
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/2d129a42-fe07-42aa-818d-85f4d92bf479/download/ipc_eth_area_long_latest.csv
  format: null
  id: resource_2d129a42
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/63967f73-f86d-4c14-b0b6-18d346cd6b93/download/ipc_eth_area_wide_latest.csv
  format: null
  id: resource_63967f73
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/d7e09834-9e45-438d-ad11-cf27d1ec93af/download/ipc_eth_national_long.csv
  format: null
  id: resource_d7e09834
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/4e05acb2-95c8-48a3-94a5-34d5db0b2644/download/ipc_eth_national_wide.csv
  format: null
  id: resource_4e05acb2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/a09c3b82-1f03-4f6a-8a18-f6500cf479a8/download/ipc_eth_level1_long.csv
  format: null
  id: resource_a09c3b82
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/97848286-7d58-4490-87d3-b00daec1d64f/download/ipc_eth_level1_wide.csv
  format: null
  id: resource_97848286
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (All IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/92ddd9a7-b285-4aa9-b3d3-86b1b29ec8a9/download/ipc_eth_area_long.csv
  format: null
  id: resource_92ddd9a7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Acute Food Insecurity Country Data (All IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/4e035f60-be39-4c6d-bd60-5502082e3be9/resource/1561d5d2-e92c-4712-9adf-ad61580ed8b5/download/ipc_eth_area_wide.csv
  format: null
  id: resource_1561d5d2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_eth_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_ipc_acuteinsecuritycountrydat_2019
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
  end: '2021-09-30'
  start: '2019-07-01'
temporal_resolution: null
title: 'Ethiopia: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
