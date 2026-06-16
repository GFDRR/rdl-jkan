---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/kingdom-of-eswatini-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/kingdom-of-eswatini-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/kingdom-of-eswatini-acute-food-insecurity-country-data
dataset_id: rdls_lss-swz_ipc_kingdomacuteinsecuritycou_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/kingdom-of-eswatini-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The IPC Acute Food Insecurity classification was produced by the National
    IPC Technical Working Group using standardized IPC methodology to assess food
    insecurity phases across the population. Population figures are based on official
    country estimates, and results are disaggregated by administrative area and time
    period (current and projection phases).
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
- href: https://data.humdata.org/dataset/kingdom-of-eswatini-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC Acute Food Insecurity phase (Phase 1-5)
      indicating food insecurity severity and affected counts
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
  description: 'Kingdom of Eswatini: Acute Food Insecurity Country Data (Latest IPC
    national data in long form with HXL tags)'
  download_url: https://data.humdata.org/dataset/735adb1e-add8-4542-aae5-c4783fdc5b40/resource/b3a089dd-b4ed-48ba-8f86-aff2a499e8d3/download/ipc_swz_national_long_latest.csv
  format: null
  id: resource_b3a089dd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_swz_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: Acute Food Insecurity Country Data (Latest IPC
    area data in long form with HXL tags)'
  download_url: https://data.humdata.org/dataset/735adb1e-add8-4542-aae5-c4783fdc5b40/resource/4345b645-2b86-4ea6-b0c1-1962e9103b26/download/ipc_swz_area_long_latest.csv
  format: null
  id: resource_4345b645
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_swz_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: Acute Food Insecurity Country Data (Latest IPC
    area data in wide form with HXL tags)'
  download_url: https://data.humdata.org/dataset/735adb1e-add8-4542-aae5-c4783fdc5b40/resource/1c24ebb2-5a50-4f48-be45-8a4169d7c9d1/download/ipc_swz_area_wide_latest.csv
  format: null
  id: resource_1c24ebb2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_swz_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: Acute Food Insecurity Country Data (All IPC national
    data in long form with HXL tags)'
  download_url: https://data.humdata.org/dataset/735adb1e-add8-4542-aae5-c4783fdc5b40/resource/10690981-d3c1-42cc-bb04-1fba9d5fbef2/download/ipc_swz_national_long.csv
  format: null
  id: resource_10690981
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_swz_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: Acute Food Insecurity Country Data (All IPC national
    data in wide form with HXL tags)'
  download_url: https://data.humdata.org/dataset/735adb1e-add8-4542-aae5-c4783fdc5b40/resource/94be9f88-8cba-4984-bafd-495a8513ac7c/download/ipc_swz_national_wide.csv
  format: null
  id: resource_94be9f88
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_swz_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: Acute Food Insecurity Country Data (All IPC area
    data in long form with HXL tags)'
  download_url: https://data.humdata.org/dataset/735adb1e-add8-4542-aae5-c4783fdc5b40/resource/12062099-63ff-480a-949e-490f91cb3a0e/download/ipc_swz_area_long.csv
  format: null
  id: resource_12062099
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_swz_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kingdom of Eswatini: Acute Food Insecurity Country Data (All IPC area
    data in wide form with HXL tags)'
  download_url: https://data.humdata.org/dataset/735adb1e-add8-4542-aae5-c4783fdc5b40/resource/2fbb0d5c-08e5-450a-858a-b1189b75c606/download/ipc_swz_area_wide.csv
  format: null
  id: resource_2fbb0d5c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_swz_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-swz_ipc_kingdomacuteinsecuritycou_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - SWZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-03-31'
  start: '2017-07-01'
temporal_resolution: null
title: 'Kingdom of Eswatini: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
