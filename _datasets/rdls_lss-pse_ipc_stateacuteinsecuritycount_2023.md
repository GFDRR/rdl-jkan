---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/state-of-palestine-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/state-of-palestine-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/state-of-palestine-acute-food-insecurity-country-data
dataset_id: rdls_lss-pse_ipc_stateacuteinsecuritycount_2023
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/state-of-palestine-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates food
    security assessments conducted by the National IPC Technical Working Group for
    Palestine, classifying populations into phases (1-5) based on standardized indicators
    of food insecurity severity. Population figures are derived from official country
    estimates and published in country IPC reports, with data available at national
    and sub-national (area) levels with current and projected phases.
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
- href: https://data.humdata.org/dataset/state-of-palestine-acute-food-insecurity-country-data
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
  description: 'State of Palestine: Acute Food Insecurity Country Data (IPC GeoJSON
    for latest analysis)'
  download_url: https://data.humdata.org/dataset/a7f087b6-13f9-4426-b8bc-f107397eb073/resource/45732a0a-5022-468a-9323-dbb52b6c0953/download/ipc_pse.geojson
  format: null
  id: resource_45732a0a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_pse.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'State of Palestine: Acute Food Insecurity Country Data (Latest IPC
    national data in long form)'
  download_url: https://data.humdata.org/dataset/a7f087b6-13f9-4426-b8bc-f107397eb073/resource/5936f606-a868-410d-b992-1c6c17d8f75c/download/ipc_pse_national_long_latest.csv
  format: null
  id: resource_5936f606
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_pse_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'State of Palestine: Acute Food Insecurity Country Data (Latest IPC
    area data in long form)'
  download_url: https://data.humdata.org/dataset/a7f087b6-13f9-4426-b8bc-f107397eb073/resource/43f741e2-9174-4f6b-bc28-eb08dacb6cbd/download/ipc_pse_area_long_latest.csv
  format: null
  id: resource_43f741e2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_pse_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'State of Palestine: Acute Food Insecurity Country Data (Latest IPC
    area data in wide form)'
  download_url: https://data.humdata.org/dataset/a7f087b6-13f9-4426-b8bc-f107397eb073/resource/f3bbb789-7a79-4be6-ba9d-11e3c7bd4114/download/ipc_pse_area_wide_latest.csv
  format: null
  id: resource_f3bbb789
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_pse_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'State of Palestine: Acute Food Insecurity Country Data (All IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/a7f087b6-13f9-4426-b8bc-f107397eb073/resource/943ce39d-8e06-4370-8ba0-040763482597/download/ipc_pse_national_long.csv
  format: null
  id: resource_943ce39d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_pse_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'State of Palestine: Acute Food Insecurity Country Data (All IPC national
    data in wide form)'
  download_url: https://data.humdata.org/dataset/a7f087b6-13f9-4426-b8bc-f107397eb073/resource/3f3aa8d8-b7fb-4409-9bd5-4079eae51015/download/ipc_pse_national_wide.csv
  format: null
  id: resource_3f3aa8d8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_pse_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'State of Palestine: Acute Food Insecurity Country Data (All IPC area
    data in long form)'
  download_url: https://data.humdata.org/dataset/a7f087b6-13f9-4426-b8bc-f107397eb073/resource/5c6c32d0-8a39-4d8f-bfef-45b46b17caea/download/ipc_pse_area_long.csv
  format: null
  id: resource_5c6c32d0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_pse_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'State of Palestine: Acute Food Insecurity Country Data (All IPC area
    data in wide form)'
  download_url: https://data.humdata.org/dataset/a7f087b6-13f9-4426-b8bc-f107397eb073/resource/3260abe3-6243-45b0-b0e3-ff7604c1feee/download/ipc_pse_area_wide.csv
  format: null
  id: resource_3260abe3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_pse_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_ipc_stateacuteinsecuritycount_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-04-30'
  start: '2023-11-01'
temporal_resolution: null
title: 'State of Palestine: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
