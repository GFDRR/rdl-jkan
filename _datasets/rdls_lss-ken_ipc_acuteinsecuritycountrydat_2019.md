---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/kenya-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/kenya-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/kenya-acute-food-insecurity-country-data
dataset_id: rdls_lss-ken_ipc_acuteinsecuritycountrydat_2019
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/kenya-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The IPC Acute Food Insecurity classification integrates data from national
    technical working groups to classify populations into five phases of food insecurity
    severity. Population estimates are based on official country census figures and
    IPC assessments, producing spatially-disaggregated impact classifications at national,
    regional, and area levels with validity periods and phase projections.
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
- href: https://data.humdata.org/dataset/kenya-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC acute food insecurity phase due to drought
      and other livelihood shocks
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
  description: 'Kenya: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/1cead27a-1a9b-40c0-a65c-f42b21bf1a6f/download/ipc_ken.geojson
  format: null
  id: resource_1cead27a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/72116c3d-26a0-4598-af92-63d7f86bcf79/download/ipc_ken_national_long_latest.csv
  format: null
  id: resource_72116c3d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/15a9d265-5c16-436e-a165-d0e80ad6e045/download/ipc_ken_level1_long_latest.csv
  format: null
  id: resource_15a9d265
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/4ca20321-4d3d-45a1-97b7-1cfdf92e77c6/download/ipc_ken_level1_wide_latest.csv
  format: null
  id: resource_4ca20321
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (Latest IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/ff4d480a-67b6-4cfa-aa12-ac0b1ba7ef01/download/ipc_ken_area_long_latest.csv
  format: null
  id: resource_ff4d480a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (Latest IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/e757548e-091c-4579-8648-7a9d33b7ee9c/download/ipc_ken_area_wide_latest.csv
  format: null
  id: resource_e757548e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (All IPC national data in
    long form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/2ab9a771-4fbd-4581-ba00-5fc03aef6902/download/ipc_ken_national_long.csv
  format: null
  id: resource_2ab9a771
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (All IPC national data in
    wide form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/5ff21b34-bbf8-44e2-b571-329603ca6651/download/ipc_ken_national_wide.csv
  format: null
  id: resource_5ff21b34
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (All IPC level 1 data in
    long form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/41e6ead9-b98d-4e36-bb35-233c2f1f4e71/download/ipc_ken_level1_long.csv
  format: null
  id: resource_41e6ead9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (All IPC level 1 data in
    wide form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/967c531f-0822-41ef-90f9-f128cc914350/download/ipc_ken_level1_wide.csv
  format: null
  id: resource_967c531f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/e0fb3f12-e096-41f2-a943-3ce94e7f8e3e/download/ipc_ken_area_long.csv
  format: null
  id: resource_e0fb3f12
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kenya: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/f12e4f52-a55f-4f77-8dec-1b60d03fcca8/resource/5f0267d1-4c5c-4f12-8e57-f8f7640ec636/download/ipc_ken_area_wide.csv
  format: null
  id: resource_5f0267d1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_ken_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_ipc_acuteinsecuritycountrydat_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2019-07-01'
temporal_resolution: null
title: 'Kenya: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
