---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/ecuador-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/ecuador-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/ecuador-acute-food-insecurity-country-data
dataset_id: rdls_lss-ecu_ipc_acuteinsecuritycountrydat_2024
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ecuador-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification was produced by Ecuador's
    National IPC Technical Working Group using the standardized IPC methodology to
    classify populations into five phases of food insecurity severity. Population
    estimates are based on official country census data and IPC technical assessments,
    with results disaggregated at national and sub-national (area/region) levels with
    validity periods and projections.
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
- href: https://data.humdata.org/dataset/ecuador-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified into IPC Acute Food Insecurity phases (1-5)
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
  description: 'Ecuador: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/63592c11-5812-4b99-b5ef-50f526bc0b17/resource/1f0bc4c8-9dfe-4c9e-8c28-6942b3916e1c/download/ipc_ecu.geojson
  format: null
  id: resource_1f0bc4c8
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ecu.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ecuador: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/63592c11-5812-4b99-b5ef-50f526bc0b17/resource/e6d8c15e-66b2-4e1c-ba8a-6a5f91c0e840/download/ipc_ecu_national_long_latest.csv
  format: null
  id: resource_e6d8c15e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ecu_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ecuador: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/63592c11-5812-4b99-b5ef-50f526bc0b17/resource/2879721e-0844-49fa-817d-e4d437ce7782/download/ipc_ecu_area_long_latest.csv
  format: null
  id: resource_2879721e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ecu_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ecuador: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/63592c11-5812-4b99-b5ef-50f526bc0b17/resource/2b7f3f94-eb33-4845-9163-fb3eb5cbf817/download/ipc_ecu_area_wide_latest.csv
  format: null
  id: resource_2b7f3f94
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ecu_area_wide_latest.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ecu_ipc_acuteinsecuritycountrydat_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-03-31'
  start: '2024-06-01'
temporal_resolution: null
title: 'Ecuador: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
