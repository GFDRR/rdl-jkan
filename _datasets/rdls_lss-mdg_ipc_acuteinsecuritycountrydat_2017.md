---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/madagascar-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/madagascar-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/madagascar-acute-food-insecurity-country-data
dataset_id: rdls_lss-mdg_ipc_acuteinsecuritycountrydat_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/madagascar-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates data
    from the National IPC Technical Working Group to produce phase-based population
    estimates at national, regional (Level 1), and area levels. Population figures
    are classified into IPC phases (1-5) representing severity of food insecurity,
    with current assessments and projections provided at multiple temporal intervals.
    Data is spatially referenced to administrative boundaries and includes confidence
    levels and justifications for classifications.
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
- href: https://data.humdata.org/dataset/madagascar-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC Acute Food Insecurity phase, indicating
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
  description: 'Madagascar: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/78120a74-b435-46a0-91d7-eced8d797f33/download/ipc_mdg.geojson
  format: null
  id: resource_78120a74
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/b46a76f4-d42c-4db1-bd03-59e3e85580ae/download/ipc_mdg_national_long_latest.csv
  format: null
  id: resource_b46a76f4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (Latest IPC level 1
    data in long form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/248ea335-b4cd-43c6-af5e-4c757df6f67d/download/ipc_mdg_level1_long_latest.csv
  format: null
  id: resource_248ea335
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (Latest IPC level 1
    data in wide form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/84e0300e-77d2-4a64-95fe-9c165fdb30b2/download/ipc_mdg_level1_wide_latest.csv
  format: null
  id: resource_84e0300e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/c02a479f-e9df-46ee-b6c6-e7bbd17495a4/download/ipc_mdg_area_long_latest.csv
  format: null
  id: resource_c02a479f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/e941f98d-d937-4f68-bccc-437be4cc82ce/download/ipc_mdg_area_wide_latest.csv
  format: null
  id: resource_e941f98d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/6bd4b40d-a504-4b37-95cd-522cf08dd493/download/ipc_mdg_national_long.csv
  format: null
  id: resource_6bd4b40d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/f36f0b69-14ee-44d3-ac61-c15b732e663e/download/ipc_mdg_national_wide.csv
  format: null
  id: resource_f36f0b69
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/b300d3dc-d06d-43aa-9695-e7fc589db3c6/download/ipc_mdg_level1_long.csv
  format: null
  id: resource_b300d3dc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/96361d66-e6e7-49f2-982e-f52262f729d9/download/ipc_mdg_level1_wide.csv
  format: null
  id: resource_96361d66
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/3298cd4e-0e5a-4a83-8cd5-4b4e95ed49dd/download/ipc_mdg_area_long.csv
  format: null
  id: resource_3298cd4e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Madagascar: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/42562e26-c618-4b63-abbe-5e6261e2a112/resource/289ef71e-0c17-482e-9f5e-fbe30e6f6236/download/ipc_mdg_area_wide.csv
  format: null
  id: resource_289ef71e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mdg_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mdg_ipc_acuteinsecuritycountrydat_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-04-30'
  start: '2017-03-01'
temporal_resolution: null
title: 'Madagascar: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
