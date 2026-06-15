---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/mauritania-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/mauritania-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/mauritania-acute-food-insecurity-country-data
dataset_id: rdls_lss-mrt_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mauritania-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The IPC Acute Food Insecurity classification was produced by the National
    IPC Technical Working Group using the standardized IPC Manual methodology to assess
    food security phases across national and sub-national administrative levels. Population
    estimates are based on official country census figures, with classifications stratified
    by IPC phase (1-5) and geographic area, providing both current assessments and
    projections.
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
- href: https://data.humdata.org/dataset/mauritania-acute-food-insecurity-country-data
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
  description: 'Mauritania: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/918c9f1c-c8f4-4600-88f1-57ec904771ad/download/ipc_mrt.geojson
  format: null
  id: resource_918c9f1c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/2b25fdcd-7b42-4e49-92c8-9b012b8affe3/download/ipc_mrt_national_long_latest.csv
  format: null
  id: resource_2b25fdcd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (Latest IPC level 1
    data in long form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/076a6ec8-c888-47f3-8421-abe7bfabdb3a/download/ipc_mrt_level1_long_latest.csv
  format: null
  id: resource_076a6ec8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (Latest IPC level 1
    data in wide form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/7b0766d5-5a43-4b4e-a2d0-c0f611d8df9b/download/ipc_mrt_level1_wide_latest.csv
  format: null
  id: resource_7b0766d5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/7380116c-cedc-4218-ade2-f858a588ea1b/download/ipc_mrt_area_long_latest.csv
  format: null
  id: resource_7380116c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/0f4edd41-bd73-48aa-8b23-4ec7947f1f4b/download/ipc_mrt_area_wide_latest.csv
  format: null
  id: resource_0f4edd41
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/229ccdac-f6f0-4e4a-9d35-447f0c400c90/download/ipc_mrt_national_long.csv
  format: null
  id: resource_229ccdac
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/fa10aab0-7f54-4057-b6ea-0cf8dc94dda0/download/ipc_mrt_national_wide.csv
  format: null
  id: resource_fa10aab0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/00a0ec26-db27-46b9-ade3-5da207fc7eff/download/ipc_mrt_level1_long.csv
  format: null
  id: resource_00a0ec26
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/be424378-ce3d-493f-945b-32060ead3f6f/download/ipc_mrt_level1_wide.csv
  format: null
  id: resource_be424378
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/4c59755e-736e-448a-a201-332510dd7ffb/download/ipc_mrt_area_long.csv
  format: null
  id: resource_4c59755e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mauritania: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/c7ea0241-4f73-4ea6-bb43-9b14b78b6bba/resource/1bb79112-d93e-43c0-aaa1-60d707028c0a/download/ipc_mrt_area_wide.csv
  format: null
  id: resource_1bb79112
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_mrt_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mrt_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - MRT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Mauritania: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
