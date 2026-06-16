---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/liberia-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/liberia-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/liberia-acute-food-insecurity-country-data
dataset_id: rdls_lss-lbr_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/liberia-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification was produced by the National
    IPC Technical Working Group using the standardized IPC Manual methodology to classify
    populations into five phases of food insecurity severity. Population estimates
    are based on official country census figures, with classifications conducted at
    national and sub-national (area) levels across multiple validity periods and projections.
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
- href: https://data.humdata.org/dataset/liberia-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified into IPC acute food insecurity phases (1-5)
      indicating severity of food insecurity
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
  description: 'Liberia: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/cc327626-72bb-4221-a916-baa0a674fc55/resource/9f0f5cbe-35c0-4bcd-bf44-1a9d53f29504/download/ipc_lbr.geojson
  format: null
  id: resource_9f0f5cbe
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbr.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/cc327626-72bb-4221-a916-baa0a674fc55/resource/25c7800b-8182-46cc-8f8a-2ad48ad8b17f/download/ipc_lbr_national_long_latest.csv
  format: null
  id: resource_25c7800b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbr_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/cc327626-72bb-4221-a916-baa0a674fc55/resource/4dfeb544-15fc-459d-93df-d6e459cec6b9/download/ipc_lbr_area_long_latest.csv
  format: null
  id: resource_4dfeb544
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbr_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/cc327626-72bb-4221-a916-baa0a674fc55/resource/0b876946-36b2-4ef1-9661-c63a5d8a3a1f/download/ipc_lbr_area_wide_latest.csv
  format: null
  id: resource_0b876946
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbr_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/cc327626-72bb-4221-a916-baa0a674fc55/resource/268b2c1e-83dd-4f2f-922c-f68b1efa8039/download/ipc_lbr_national_long.csv
  format: null
  id: resource_268b2c1e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbr_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/cc327626-72bb-4221-a916-baa0a674fc55/resource/3fb2ff81-f712-41db-9cdc-3a5819e9d7d3/download/ipc_lbr_national_wide.csv
  format: null
  id: resource_3fb2ff81
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbr_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Acute Food Insecurity Country Data (All IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/cc327626-72bb-4221-a916-baa0a674fc55/resource/b3e47e00-4699-4750-8f65-3b83255e9c1a/download/ipc_lbr_area_long.csv
  format: null
  id: resource_b3e47e00
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbr_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Liberia: Acute Food Insecurity Country Data (All IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/cc327626-72bb-4221-a916-baa0a674fc55/resource/c9b47950-3b5f-4830-9b8c-9c1e37c76fd0/download/ipc_lbr_area_wide.csv
  format: null
  id: resource_c9b47950
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbr_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lbr_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - LBR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Liberia: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
