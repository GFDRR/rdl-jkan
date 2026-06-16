---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/mozambique-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/mozambique-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/mozambique-acute-food-insecurity-country-data
dataset_id: rdls_lss-moz_ipc_acuteinsecuritycountrydat_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: The IPC Acute Food Insecurity classification system aggregates data
    from multiple sources (food security surveys, market monitoring, livelihood assessments)
    through national technical working groups to classify populations into five phases
    of food insecurity severity. Population estimates are stratified by administrative
    level and validity period, with current assessments and projections provided in
    both long and wide formats.
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
- href: https://data.humdata.org/dataset/mozambique-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC acute food insecurity phase, indicating
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
  description: 'Mozambique: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/b3ff6b2e-abfe-42c3-9731-45e75dd6e171/download/ipc_moz.geojson
  format: null
  id: resource_b3ff6b2e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/48c9921d-e978-4dea-b001-0355c3b11319/download/ipc_moz_national_long_latest.csv
  format: null
  id: resource_48c9921d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (Latest IPC level 1
    data in long form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/7158b7e7-0d87-43a6-b55c-fd1ff7b3aede/download/ipc_moz_level1_long_latest.csv
  format: null
  id: resource_7158b7e7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (Latest IPC level 1
    data in wide form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/80b4f218-8ffb-4ecd-a176-520848dbf25a/download/ipc_moz_level1_wide_latest.csv
  format: null
  id: resource_80b4f218
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/8b8193ad-9f61-416d-8c4b-45c64a5820f9/download/ipc_moz_area_long_latest.csv
  format: null
  id: resource_8b8193ad
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/cb79d18e-184b-484b-8cdc-66f0e9fb2cc8/download/ipc_moz_area_wide_latest.csv
  format: null
  id: resource_cb79d18e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/9ff54894-a1cc-41fb-8e6e-2f74f3ac0466/download/ipc_moz_national_long.csv
  format: null
  id: resource_9ff54894
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/0cf86f2a-9850-4165-939f-058e8ec65ad7/download/ipc_moz_national_wide.csv
  format: null
  id: resource_0cf86f2a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/6e900237-4993-420c-9c97-9955cdf491b0/download/ipc_moz_level1_long.csv
  format: null
  id: resource_6e900237
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/e4d0b370-9898-4d39-bfbd-0f6b848acea1/download/ipc_moz_level1_wide.csv
  format: null
  id: resource_e4d0b370
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/6bad6f06-02bd-4ced-9a80-81ff95133fda/download/ipc_moz_area_long.csv
  format: null
  id: resource_6bad6f06
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/6ec3aca3-7aa0-49b4-83d8-3df88fa7ae0d/resource/1f0e258f-8a90-4390-9ff7-a18b343865e3/download/ipc_moz_area_wide.csv
  format: null
  id: resource_1f0e258f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_moz_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_ipc_acuteinsecuritycountrydat_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2017-03-01'
temporal_resolution: null
title: 'Mozambique: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
