---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/south-africa-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/south-africa-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/south-africa-acute-food-insecurity-country-data
dataset_id: rdls_lss-zaf_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/south-africa-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using the standardized IPC Manual methodology to assess
    food insecurity phases across administrative levels. Population figures are based
    on official country estimates and classified into IPC phases (1-5) representing
    severity of food insecurity, with current and projected estimates provided at
    national, provincial, and area levels.
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
- href: https://data.humdata.org/dataset/south-africa-acute-food-insecurity-country-data
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
  description: 'South Africa: Acute Food Insecurity Country Data (IPC GeoJSON for
    latest analysis)'
  download_url: https://data.humdata.org/dataset/1d11c733-acd9-4183-9d97-d5f2e8570f99/resource/eec5a82b-2004-4b1a-8576-ff17e2af0faa/download/ipc_zaf.geojson
  format: null
  id: resource_eec5a82b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zaf.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/1d11c733-acd9-4183-9d97-d5f2e8570f99/resource/e24999cc-beb9-45f7-9ba7-4a56f02dca87/download/ipc_zaf_national_long_latest.csv
  format: null
  id: resource_e24999cc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zaf_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: Acute Food Insecurity Country Data (Latest IPC level
    1 data in long form)'
  download_url: https://data.humdata.org/dataset/1d11c733-acd9-4183-9d97-d5f2e8570f99/resource/5900de72-c2ee-4ec6-8975-0efce6a87627/download/ipc_zaf_level1_long_latest.csv
  format: null
  id: resource_5900de72
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zaf_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: Acute Food Insecurity Country Data (Latest IPC level
    1 data in wide form)'
  download_url: https://data.humdata.org/dataset/1d11c733-acd9-4183-9d97-d5f2e8570f99/resource/b423dbff-a665-42c4-a264-a28088f6c89d/download/ipc_zaf_level1_wide_latest.csv
  format: null
  id: resource_b423dbff
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zaf_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: Acute Food Insecurity Country Data (Latest IPC area
    data in long form)'
  download_url: https://data.humdata.org/dataset/1d11c733-acd9-4183-9d97-d5f2e8570f99/resource/f49a99ba-c831-462d-b2fd-943a878ea38a/download/ipc_zaf_area_long_latest.csv
  format: null
  id: resource_f49a99ba
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zaf_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'South Africa: Acute Food Insecurity Country Data (Latest IPC area
    data in wide form)'
  download_url: https://data.humdata.org/dataset/1d11c733-acd9-4183-9d97-d5f2e8570f99/resource/8c86666a-f532-4af4-bdbe-14cd1799aa42/download/ipc_zaf_area_wide_latest.csv
  format: null
  id: resource_8c86666a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zaf_area_wide_latest.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-zaf_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - ZAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-03-31'
  start: '2020-09-01'
temporal_resolution: null
title: 'South Africa: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
