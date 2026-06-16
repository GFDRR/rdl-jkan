---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/afghanistan-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/afghanistan-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/afghanistan-acute-food-insecurity-country-data
dataset_id: rdls_lss-afg_ipc_acuteinsecuritycountrydat_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates evidence
    on food availability, access, and utilization to classify populations into five
    phases of acute food insecurity severity. National IPC Technical Working Groups
    synthesize data from multiple sources to produce population estimates by phase
    at national, provincial (Level 1), and area levels, with current assessments and
    future projections.
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
- href: https://data.humdata.org/dataset/afghanistan-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Population classified into IPC acute food insecurity phases (1-5)
      indicating severity of food insecurity and livelihood disruption
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
          quantity_kind: area
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
  description: 'Afghanistan: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/fc0655df-10a5-4894-a185-b04e0add9aa5/download/ipc_afg.geojson
  format: null
  id: resource_fc0655df
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/1286f8a6-bfa1-4171-8064-cc3c9619813e/download/ipc_afg_national_long_latest.csv
  format: null
  id: resource_1286f8a6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (Latest IPC level
    1 data in long form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/07996838-234f-458a-9bb3-df223389b08e/download/ipc_afg_level1_long_latest.csv
  format: null
  id: resource_07996838
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (Latest IPC level
    1 data in wide form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/f2d89579-e7bb-4037-aea4-56d0cbd2764c/download/ipc_afg_level1_wide_latest.csv
  format: null
  id: resource_f2d89579
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/4330440c-af78-484a-8d4d-1fb6b57adc9e/download/ipc_afg_area_long_latest.csv
  format: null
  id: resource_4330440c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/f111bc7a-6de8-4a36-9caf-1d302741a14c/download/ipc_afg_area_wide_latest.csv
  format: null
  id: resource_f111bc7a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (All IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/34d93f17-96db-40a8-a490-ec97990d9d45/download/ipc_afg_national_long.csv
  format: null
  id: resource_34d93f17
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (All IPC national
    data in wide form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/ff95315a-0ce5-420f-b0a3-0e09453cd212/download/ipc_afg_national_wide.csv
  format: null
  id: resource_ff95315a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/8494cb33-eaa7-46e1-9b0e-2ed0bd2052d1/download/ipc_afg_level1_long.csv
  format: null
  id: resource_8494cb33
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/33d3053e-ae1e-40e4-b8c7-56bfd66fc219/download/ipc_afg_level1_wide.csv
  format: null
  id: resource_33d3053e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/d54e6696-0280-49b4-b839-5e8399bc4651/download/ipc_afg_area_long.csv
  format: null
  id: resource_d54e6696
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Afghanistan: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c49d7959-1c24-4ef6-a975-12428461f292/resource/8ccab177-704c-4d32-b5d0-99e2946ec4cc/download/ipc_afg_area_wide.csv
  format: null
  id: resource_8ccab177
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_afg_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ipc_acuteinsecuritycountrydat_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-09-30'
  start: '2017-05-01'
temporal_resolution: null
title: 'Afghanistan: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
