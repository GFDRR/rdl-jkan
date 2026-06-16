---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/south-sudan-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/south-sudan-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/south-sudan-acute-food-insecurity-country-data
dataset_id: rdls_lss-ssd_ipc_acuteinsecuritycountrydat_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using the standardized IPC manual methodology to assess
    food insecurity phases across national and sub-national administrative levels.
    Population figures are based on official country estimates and classified into
    IPC phases (1-5) representing severity of acute food insecurity, with current
    assessments and projections provided at multiple temporal intervals.
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
- href: https://data.humdata.org/dataset/south-sudan-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC acute food insecurity phase, indicating
      food insecurity severity driven by drought and other shocks
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
  description: 'South Sudan: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/1ada1f60-5465-4aa2-a8e9-188ab5bd2f0a/download/ipc_ssd.geojson
  format: null
  id: resource_1ada1f60
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/5dc31009-611d-44d9-9d1b-00e51d6e8fa3/download/ipc_ssd_national_long_latest.csv
  format: null
  id: resource_5dc31009
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (Latest IPC level
    1 data in long form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/0b79be00-7c46-4784-934d-6c80fc9d46ae/download/ipc_ssd_level1_long_latest.csv
  format: null
  id: resource_0b79be00
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (Latest IPC level
    1 data in wide form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/70864418-b009-4850-8ebf-01e5534d16ee/download/ipc_ssd_level1_wide_latest.csv
  format: null
  id: resource_70864418
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/356161ff-673d-480f-a183-abe93a268450/download/ipc_ssd_area_long_latest.csv
  format: null
  id: resource_356161ff
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/e36a52ee-1aa6-4bd3-a4a8-b47ec5d3ee66/download/ipc_ssd_area_wide_latest.csv
  format: null
  id: resource_e36a52ee
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (All IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/5e88477c-9d87-4ab2-bfa5-0303e21d9cc2/download/ipc_ssd_national_long.csv
  format: null
  id: resource_5e88477c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (All IPC national
    data in wide form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/d0b0faa3-1cad-470c-9b72-16f83932398d/download/ipc_ssd_national_wide.csv
  format: null
  id: resource_d0b0faa3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/effff6b6-dcaa-400c-837b-5d98906a73cc/download/ipc_ssd_level1_long.csv
  format: null
  id: resource_effff6b6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/0e1c15b4-16e5-4bf9-8ebf-4b2849b5d702/download/ipc_ssd_level1_wide.csv
  format: null
  id: resource_0e1c15b4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/6c221834-d751-4de0-9150-462bf753d9e8/download/ipc_ssd_area_long.csv
  format: null
  id: resource_6c221834
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Sudan: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c81bb6db-0f1d-4c59-8bde-52d7edc562e9/resource/944af6ed-0fb9-4e3e-9c67-4d4bfb1fb55d/download/ipc_ssd_area_wide.csv
  format: null
  id: resource_944af6ed
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ssd_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_ipc_acuteinsecuritycountrydat_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-07-31'
  start: '2017-01-01'
temporal_resolution: null
title: 'South Sudan: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
