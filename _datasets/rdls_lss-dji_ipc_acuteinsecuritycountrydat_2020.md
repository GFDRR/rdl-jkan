---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/djibouti-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/djibouti-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/djibouti-acute-food-insecurity-country-data
dataset_id: rdls_lss-dji_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/djibouti-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates national
    population estimates from official country sources and classifies them into five
    phases of food insecurity severity (Phase 1-5) based on standardized technical
    criteria. Data has been produced by the National IPC Technical Working Group for
    Djibouti since 2017, with estimates disaggregated by administrative level and
    time period (current and projected).
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
- href: https://data.humdata.org/dataset/djibouti-acute-food-insecurity-country-data
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
  description: 'Djibouti: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/fc6a6c1c-d84a-48f0-bed8-d33b0dc4a296/download/ipc_dji.geojson
  format: null
  id: resource_fc6a6c1c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/51383561-0a0a-4b9e-8717-631bd304ac8e/download/ipc_dji_national_long_latest.csv
  format: null
  id: resource_51383561
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/b348b442-5fbc-4cd5-84e5-36fa7cc99d74/download/ipc_dji_level1_long_latest.csv
  format: null
  id: resource_b348b442
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/29c4caa7-4fba-4534-b89a-f463cf88c82a/download/ipc_dji_level1_wide_latest.csv
  format: null
  id: resource_29c4caa7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/a42b9777-0425-43a7-ba46-33e955bd2341/download/ipc_dji_area_long_latest.csv
  format: null
  id: resource_a42b9777
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/6e5fafa8-a0cc-40ed-9da2-2a90d13f2fcf/download/ipc_dji_area_wide_latest.csv
  format: null
  id: resource_6e5fafa8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/15d6b14a-ed30-4dac-aa29-40a1de5be0f2/download/ipc_dji_national_long.csv
  format: null
  id: resource_15d6b14a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/7a336b65-daee-4c6b-a479-0d0fdece0ba4/download/ipc_dji_national_wide.csv
  format: null
  id: resource_7a336b65
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/e9764195-5501-455d-a8df-afde3b8b731d/download/ipc_dji_level1_long.csv
  format: null
  id: resource_e9764195
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/3285bc26-23ae-4a3a-9639-96d22b53ec6d/download/ipc_dji_level1_wide.csv
  format: null
  id: resource_3285bc26
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (All IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/aa8a5a70-f8a9-4140-b2c2-57c1c36b4291/download/ipc_dji_area_long.csv
  format: null
  id: resource_aa8a5a70
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Djibouti: Acute Food Insecurity Country Data (All IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/49fbd08a-2b4f-4fc6-af3c-eb94e2c642a5/resource/659a0304-9dad-4a2f-9b68-c9ea9fcc240b/download/ipc_dji_area_wide.csv
  format: null
  id: resource_659a0304
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_dji_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-dji_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - DJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Djibouti: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
