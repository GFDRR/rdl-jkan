---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/malawi-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/malawi-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/malawi-acute-food-insecurity-country-data
dataset_id: rdls_lss-mwi_ipc_acuteinsecuritycountrydat_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification was produced by the National
    IPC Technical Working Group using standardized IPC methodology applied to Malawi
    population data. Population estimates are stratified by IPC phase (1-5) at national
    and sub-national (district/area) levels, with current assessments and projections
    provided across multiple time periods.
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
- href: https://data.humdata.org/dataset/malawi-acute-food-insecurity-country-data
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
  description: 'Malawi: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/2a22e894-04e6-4831-b726-2b6e596df2af/resource/13a6ca39-eb5a-42f2-ac1b-b9826537e1d2/download/ipc_mwi.geojson
  format: null
  id: resource_13a6ca39
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mwi.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/2a22e894-04e6-4831-b726-2b6e596df2af/resource/cbada0f8-430c-4fed-a080-83844b09f388/download/ipc_mwi_national_long_latest.csv
  format: null
  id: resource_cbada0f8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mwi_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Acute Food Insecurity Country Data (Latest IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/2a22e894-04e6-4831-b726-2b6e596df2af/resource/f6616874-0176-4610-a9e5-10a4e38da66e/download/ipc_mwi_area_long_latest.csv
  format: null
  id: resource_f6616874
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mwi_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Acute Food Insecurity Country Data (Latest IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/2a22e894-04e6-4831-b726-2b6e596df2af/resource/3cc01128-8d2b-4c77-9e0b-6078d6938c18/download/ipc_mwi_area_wide_latest.csv
  format: null
  id: resource_3cc01128
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mwi_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/2a22e894-04e6-4831-b726-2b6e596df2af/resource/6b4f6da5-0842-4e97-b28c-54046bdded9d/download/ipc_mwi_national_long.csv
  format: null
  id: resource_6b4f6da5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mwi_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/2a22e894-04e6-4831-b726-2b6e596df2af/resource/bb60a5ec-c664-408a-9448-b6462293f6b9/download/ipc_mwi_national_wide.csv
  format: null
  id: resource_bb60a5ec
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mwi_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/2a22e894-04e6-4831-b726-2b6e596df2af/resource/54dfffdb-0112-43d9-81e7-8a089dbc90d2/download/ipc_mwi_area_long.csv
  format: null
  id: resource_54dfffdb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mwi_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Malawi: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/2a22e894-04e6-4831-b726-2b6e596df2af/resource/71d78077-af71-46a2-bfc8-15365038e456/download/ipc_mwi_area_wide.csv
  format: null
  id: resource_71d78077
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mwi_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mwi_ipc_acuteinsecuritycountrydat_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2017-07-01'
temporal_resolution: null
title: 'Malawi: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
