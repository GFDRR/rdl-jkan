---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/lebanon-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/lebanon-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/lebanon-acute-food-insecurity-country-data
dataset_id: rdls_lss-lbn_ipc_acuteinsecuritycountrydat_2022
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/lebanon-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The IPC Acute Food Insecurity classification system analyzes population
    food security status at national and sub-national levels using standardized protocols.
    National population figures are based on official country estimates, and IPC classifications
    are derived from technical working group assessments published in country IPC
    reports. Data is provided in multiple temporal formats (current and projected
    periods) and spatial aggregations (national, administrative level 1, and area-level).
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
- href: https://data.humdata.org/dataset/lebanon-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC Acute Food Insecurity phase, indicating
      food insecurity severity triggered by drought and crisis conditions
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
  description: 'Lebanon: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/8a2e7a6b-c276-4bfc-996b-e05bb0612b84/download/ipc_lbn.geojson
  format: null
  id: resource_8a2e7a6b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/d9c0246d-d2ac-47fd-9152-6d4c1706ee96/download/ipc_lbn_national_long_latest.csv
  format: null
  id: resource_d9c0246d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/45f4023e-07bb-48a0-8d8d-322002a5280c/download/ipc_lbn_level1_long_latest.csv
  format: null
  id: resource_45f4023e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/89d7f984-0e8d-42ae-9ff6-e01d77ea040b/download/ipc_lbn_level1_wide_latest.csv
  format: null
  id: resource_89d7f984
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (Latest IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/8ae7d40a-7f19-4538-89e5-35450b858b05/download/ipc_lbn_area_long_latest.csv
  format: null
  id: resource_8ae7d40a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (Latest IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/8407cb15-a189-43f7-868e-4500b8ace035/download/ipc_lbn_area_wide_latest.csv
  format: null
  id: resource_8407cb15
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/09e3bf96-8582-436d-9d2a-9b9064a1376d/download/ipc_lbn_national_long.csv
  format: null
  id: resource_09e3bf96
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/7fc882b6-342f-4804-ba1f-cf3c551f4605/download/ipc_lbn_national_wide.csv
  format: null
  id: resource_7fc882b6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (All IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/fb411f3a-c1ca-4cd4-8dec-162ef4d702d0/download/ipc_lbn_level1_long.csv
  format: null
  id: resource_fb411f3a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (All IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/94a0088e-58d2-47fb-8834-378a9ee9165a/download/ipc_lbn_level1_wide.csv
  format: null
  id: resource_94a0088e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (All IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/2ee870c6-f820-4477-a215-ea268ba5a294/download/ipc_lbn_area_long.csv
  format: null
  id: resource_2ee870c6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lebanon: Acute Food Insecurity Country Data (All IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/5e3a8ae5-52a4-408c-929f-689f09f5076e/resource/b044b737-60de-4a03-ac51-30f4f4fefe71/download/ipc_lbn_area_wide.csv
  format: null
  id: resource_b044b737
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_lbn_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lbn_ipc_acuteinsecuritycountrydat_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - LBN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-10-31'
  start: '2022-09-01'
temporal_resolution: null
title: 'Lebanon: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
