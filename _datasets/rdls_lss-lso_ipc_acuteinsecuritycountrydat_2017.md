---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/lesotho-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/lesotho-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/lesotho-acute-food-insecurity-country-data
dataset_id: rdls_lss-lso_ipc_acuteinsecuritycountrydat_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/lesotho-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using standardized methodology to assess short-term
    food insecurity severity. Population figures are based on official country estimates
    and classified into IPC phases (1-5) representing increasing severity of food
    insecurity. Data includes current assessments and projections across national
    and sub-national administrative levels.
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
- href: https://data.humdata.org/dataset/lesotho-acute-food-insecurity-country-data
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
  description: 'Lesotho: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/1cdf5b2e-9da1-48b1-925c-5ed3628806b5/resource/ab671adc-b8d1-483f-8f6b-e42a78ab952c/download/ipc_lso.geojson
  format: null
  id: resource_ab671adc
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lso.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/1cdf5b2e-9da1-48b1-925c-5ed3628806b5/resource/913cfd11-fe4c-4c7b-b4b0-b09e9b68329a/download/ipc_lso_national_long_latest.csv
  format: null
  id: resource_913cfd11
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lso_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/1cdf5b2e-9da1-48b1-925c-5ed3628806b5/resource/e25aadbc-4d43-4dff-9be2-d1a05af0eda9/download/ipc_lso_area_long_latest.csv
  format: null
  id: resource_e25aadbc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lso_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/1cdf5b2e-9da1-48b1-925c-5ed3628806b5/resource/b0715e13-e458-409a-8084-8223f6474b87/download/ipc_lso_area_wide_latest.csv
  format: null
  id: resource_b0715e13
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lso_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/1cdf5b2e-9da1-48b1-925c-5ed3628806b5/resource/57869933-3355-4fa3-ac80-0cea1eabbdba/download/ipc_lso_national_long.csv
  format: null
  id: resource_57869933
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lso_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/1cdf5b2e-9da1-48b1-925c-5ed3628806b5/resource/13767236-7302-4b35-aa67-11c29491a97f/download/ipc_lso_national_wide.csv
  format: null
  id: resource_13767236
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lso_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Acute Food Insecurity Country Data (All IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/1cdf5b2e-9da1-48b1-925c-5ed3628806b5/resource/6664511b-d42e-4f61-a19d-af2c9e1ce33d/download/ipc_lso_area_long.csv
  format: null
  id: resource_6664511b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lso_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lesotho: Acute Food Insecurity Country Data (All IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/1cdf5b2e-9da1-48b1-925c-5ed3628806b5/resource/9c0720d9-c690-4c3d-9e70-d7f7e36c074a/download/ipc_lso_area_wide.csv
  format: null
  id: resource_9c0720d9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lso_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lso_ipc_acuteinsecuritycountrydat_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - LSO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2017-07-01'
temporal_resolution: null
title: 'Lesotho: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
