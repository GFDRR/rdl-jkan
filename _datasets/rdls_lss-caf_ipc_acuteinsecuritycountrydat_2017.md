---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/central-african-republic-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/central-african-republic-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/central-african-republic-acute-food-insecurity-country-data
dataset_id: rdls_lss-caf_ipc_acuteinsecuritycountrydat_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/central-african-republic-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using standardized methodology (IPC Manual) applied
    to population data. Population figures are based on official country estimates.
    Data is published at national, administrative level 1, and area levels with current
    and projected phases across multiple time periods.
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
- href: https://data.humdata.org/dataset/central-african-republic-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC acute food insecurity phase, indicating
      food security vulnerability and need
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
  description: 'Central African Republic: Acute Food Insecurity Country Data (IPC
    GeoJSON for latest analysis)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/57b2d6a4-801b-436b-a0a8-bf17632733f8/download/ipc_caf.geojson
  format: null
  id: resource_57b2d6a4
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (Latest
    IPC national data in long form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/5f046902-c01f-4803-8a2f-e0e5a1cd733f/download/ipc_caf_national_long_latest.csv
  format: null
  id: resource_5f046902
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (Latest
    IPC level 1 data in long form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/b657b6ca-66b1-49d6-a098-e61bc11a7c3d/download/ipc_caf_level1_long_latest.csv
  format: null
  id: resource_b657b6ca
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (Latest
    IPC level 1 data in wide form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/6ef15943-3e3c-408b-997c-22fddf0b5070/download/ipc_caf_level1_wide_latest.csv
  format: null
  id: resource_6ef15943
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (Latest
    IPC area data in long form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/caeaf630-df0f-428b-9b5b-47f8a20c8f45/download/ipc_caf_area_long_latest.csv
  format: null
  id: resource_caeaf630
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (Latest
    IPC area data in wide form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/183f43f1-cae9-414d-b37a-c88ae1b4986a/download/ipc_caf_area_wide_latest.csv
  format: null
  id: resource_183f43f1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (All
    IPC national data in long form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/46060518-7587-44b9-a386-39c1a11cbd92/download/ipc_caf_national_long.csv
  format: null
  id: resource_46060518
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (All
    IPC national data in wide form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/b56c79b6-ea65-4b44-8a65-eba46e103ade/download/ipc_caf_national_wide.csv
  format: null
  id: resource_b56c79b6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (All
    IPC level 1 data in long form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/b6c3da43-f0d7-4ba9-a0a3-3338b81f2c9c/download/ipc_caf_level1_long.csv
  format: null
  id: resource_b6c3da43
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (All
    IPC level 1 data in wide form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/92146201-9136-4413-9324-11771357a342/download/ipc_caf_level1_wide.csv
  format: null
  id: resource_92146201
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (All
    IPC area data in long form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/68a8224d-bef9-40b9-a4ad-990e19a70422/download/ipc_caf_area_long.csv
  format: null
  id: resource_68a8224d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Central African Republic: Acute Food Insecurity Country Data (All
    IPC area data in wide form)'
  download_url: https://data.humdata.org/dataset/0ce50ddb-17d5-447d-9c61-bd330c4457e9/resource/5d6fa783-3823-4583-86cf-25df67cda22b/download/ipc_caf_area_wide.csv
  format: null
  id: resource_5d6fa783
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_caf_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_ipc_acuteinsecuritycountrydat_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-08-31'
  start: '2017-02-01'
temporal_resolution: null
title: 'Central African Republic: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
