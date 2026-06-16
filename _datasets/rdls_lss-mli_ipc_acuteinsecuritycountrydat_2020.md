---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/mali-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/mali-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/mali-acute-food-insecurity-country-data
dataset_id: rdls_lss-mli_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mali-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates data
    from multiple sources (surveys, market monitoring, livelihood assessments) through
    the National IPC Technical Working Group to classify populations into five phases
    of food insecurity severity. Population figures are based on official country
    estimates and published in country IPC reports, with data available at national,
    regional (Level 1), and area levels with current and projected validity periods.
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
- href: https://data.humdata.org/dataset/mali-acute-food-insecurity-country-data
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
  description: 'Mali: Acute Food Insecurity Country Data (IPC GeoJSON for latest analysis)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/306feb4a-4f08-4881-b095-701d1555184c/download/ipc_mli.geojson
  format: null
  id: resource_306feb4a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/507215fd-9b28-46d6-ad1d-f07033c84c77/download/ipc_mli_national_long_latest.csv
  format: null
  id: resource_507215fd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/304a914b-8a5a-4b15-a9f6-8dd4a68e5747/download/ipc_mli_level1_long_latest.csv
  format: null
  id: resource_304a914b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/f0552815-4863-49a0-85d8-0efc436fcc65/download/ipc_mli_level1_wide_latest.csv
  format: null
  id: resource_f0552815
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Acute Food Insecurity Country Data (All IPC national data in
    long form)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/ca5762ca-628f-4026-a904-cd4a320b55fb/download/ipc_mli_national_long.csv
  format: null
  id: resource_ca5762ca
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Acute Food Insecurity Country Data (All IPC national data in
    wide form)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/dce51ebb-4ed8-482b-8b51-76424332ca90/download/ipc_mli_national_wide.csv
  format: null
  id: resource_dce51ebb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Acute Food Insecurity Country Data (All IPC level 1 data in
    long form)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/ec0caf22-0e2e-4292-b157-0f0875d70fa6/download/ipc_mli_level1_long.csv
  format: null
  id: resource_ec0caf22
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Acute Food Insecurity Country Data (All IPC level 1 data in
    wide form)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/a3896bcd-c67d-4161-9d6d-f7ffbcdcb94e/download/ipc_mli_level1_wide.csv
  format: null
  id: resource_a3896bcd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/6cee01eb-dfa5-49ff-a2b9-9a07ad4feff3/download/ipc_mli_area_long.csv
  format: null
  id: resource_6cee01eb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/38958cd5-c20a-4f80-be2f-8cad061f04e9/resource/c73b954c-b8cf-4357-be8c-1f4d8aebe3d2/download/ipc_mli_area_wide.csv
  format: null
  id: resource_c73b954c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mli_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Mali: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
