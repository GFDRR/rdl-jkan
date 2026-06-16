---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/united-republic-of-tanzania-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/united-republic-of-tanzania-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/united-republic-of-tanzania-acute-food-insecurity-country-data
dataset_id: rdls_lss-tza_ipc_unitedrepublicacuteinsecu_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/united-republic-of-tanzania-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification was produced by Tanzania's
    National IPC Technical Working Group using the standardized IPC methodology to
    assess and classify population food security status into phases (1-5). Population
    figures are based on official country estimates and IPC reports, with data available
    at national and sub-national (area/district) levels with current and projected
    assessments.
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
- href: https://data.humdata.org/dataset/united-republic-of-tanzania-acute-food-insecurity-country-data
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
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (IPC
    GeoJSON for latest analysis)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/5d3e176d-0d4a-4328-a5a5-5e9a0ad8e708/download/ipc_tza.geojson
  format: null
  id: resource_5d3e176d
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (Latest
    IPC national data in long form)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/f17cbdbc-7bda-4614-80c2-85e73647fe25/download/ipc_tza_national_long_latest.csv
  format: null
  id: resource_f17cbdbc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (Latest
    IPC area data in long form)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/a0bd71ef-be58-49b9-82bc-7b6098faa9ae/download/ipc_tza_area_long_latest.csv
  format: null
  id: resource_a0bd71ef
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (Latest
    IPC area data in wide form)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/85829c2a-467b-42d1-98de-7b5d4c84341a/download/ipc_tza_area_wide_latest.csv
  format: null
  id: resource_85829c2a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (All
    IPC national data in long form)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/1b87654a-4a24-484d-88e7-450c3f0f3bb2/download/ipc_tza_national_long.csv
  format: null
  id: resource_1b87654a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (All
    IPC national data in wide form)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/70b619b0-54c6-426a-ba08-f5c648872d08/download/ipc_tza_national_wide.csv
  format: null
  id: resource_70b619b0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (All
    IPC level 1 data in long form)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/c5d7c650-4b01-4fa2-91ff-f02bbd7e691a/download/ipc_tza_level1_long.csv
  format: null
  id: resource_c5d7c650
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (All
    IPC level 1 data in wide form)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/85667c1c-f3ef-4cb2-bcba-f8d69a524097/download/ipc_tza_level1_wide.csv
  format: null
  id: resource_85667c1c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (All
    IPC area data in long form)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/3af28c5d-c76a-4ce9-a70b-64bed473c018/download/ipc_tza_area_long.csv
  format: null
  id: resource_3af28c5d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Republic of Tanzania: Acute Food Insecurity Country Data (All
    IPC area data in wide form)'
  download_url: https://data.humdata.org/dataset/eab07f34-57a9-4c46-9876-ed00825cb217/resource/c5a9f682-a71b-4621-bbfc-8571615d1384/download/ipc_tza_area_wide.csv
  format: null
  id: resource_c5a9f682
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_tza_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tza_ipc_unitedrepublicacuteinsecu_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-10-31'
  start: '2017-07-01'
temporal_resolution: null
title: 'United Republic of Tanzania: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
