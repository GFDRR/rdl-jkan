---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/honduras-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/honduras-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/honduras-acute-food-insecurity-country-data
dataset_id: rdls_lss-hnd_ipc_acuteinsecuritycountrydat_2018
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/honduras-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates data
    from multiple sources (surveys, market monitoring, livelihood assessments) through
    the National IPC Technical Working Group to produce population estimates classified
    into five phases of food insecurity severity. These estimates are validated against
    official national population figures and published in country IPC reports, providing
    strategically relevant impact data for humanitarian decision-making.
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
- href: https://data.humdata.org/dataset/honduras-acute-food-insecurity-country-data
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
  description: 'Honduras: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/00a29d88-012a-414b-8d48-1813b824fb28/download/ipc_hnd.geojson
  format: null
  id: resource_00a29d88
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/7ce0a294-0406-4abc-993e-d21c85c3a73a/download/ipc_hnd_national_long_latest.csv
  format: null
  id: resource_7ce0a294
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/7f96725d-1d70-4d47-b78e-116e0c8cd5a4/download/ipc_hnd_area_long_latest.csv
  format: null
  id: resource_7f96725d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/da9ca3df-fe8d-4057-85b7-1fecd62df67b/download/ipc_hnd_area_wide_latest.csv
  format: null
  id: resource_da9ca3df
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/973d19b5-09b5-47b5-802f-4d7eb2803d53/download/ipc_hnd_national_long.csv
  format: null
  id: resource_973d19b5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/a94b6592-7ea7-4466-943c-ddda9382d572/download/ipc_hnd_national_wide.csv
  format: null
  id: resource_a94b6592
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/7766d830-3ae5-4ff1-8557-5c749b6a1a2f/download/ipc_hnd_level1_long.csv
  format: null
  id: resource_7766d830
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/ee3f15ff-d828-46d5-93fa-1e2d6c16d8f9/download/ipc_hnd_level1_wide.csv
  format: null
  id: resource_ee3f15ff
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Acute Food Insecurity Country Data (All IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/bd539d2a-8b8d-453e-a5a9-9e60703d1025/download/ipc_hnd_area_long.csv
  format: null
  id: resource_bd539d2a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Honduras: Acute Food Insecurity Country Data (All IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/41d20a32-ed74-4d67-87fa-1ea249b9ac23/resource/c51f2499-4929-4ba4-ba66-1d7d25cf9b98/download/ipc_hnd_area_wide.csv
  format: null
  id: resource_c51f2499
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_hnd_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hnd_ipc_acuteinsecuritycountrydat_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-30'
  start: '2018-12-01'
temporal_resolution: null
title: 'Honduras: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
