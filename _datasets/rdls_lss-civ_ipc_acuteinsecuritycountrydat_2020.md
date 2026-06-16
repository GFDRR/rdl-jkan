---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/cote-d-ivoire-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/cote-d-ivoire-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/cote-d-ivoire-acute-food-insecurity-country-data
dataset_id: rdls_lss-civ_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cote-d-ivoire-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using standardized assessment methodology documented
    in the IPC Manual. Population figures are classified into five phases (1-5) representing
    severity of food insecurity, with estimates disaggregated by administrative area
    and temporal validity periods. Data includes current assessments and projections.
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
- href: https://data.humdata.org/dataset/cote-d-ivoire-acute-food-insecurity-country-data
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
  description: "C\xF4te d'Ivoire: Acute Food Insecurity Country Data (IPC GeoJSON\
    \ for latest analysis)"
  download_url: https://data.humdata.org/dataset/e47d86cd-d0ec-4cae-9d93-9385b9175478/resource/5af2e909-1092-4755-a4e6-67f7b0543da6/download/ipc_civ.geojson
  format: null
  id: resource_5af2e909
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_civ.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Acute Food Insecurity Country Data (Latest IPC national\
    \ data in long form)"
  download_url: https://data.humdata.org/dataset/e47d86cd-d0ec-4cae-9d93-9385b9175478/resource/48c443de-3ae6-442e-8a5d-e5a8a5f91698/download/ipc_civ_national_long_latest.csv
  format: null
  id: resource_48c443de
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_civ_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Acute Food Insecurity Country Data (Latest IPC area\
    \ data in long form)"
  download_url: https://data.humdata.org/dataset/e47d86cd-d0ec-4cae-9d93-9385b9175478/resource/44e080e1-68c3-4737-b8cc-8dc48455bd27/download/ipc_civ_area_long_latest.csv
  format: null
  id: resource_44e080e1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_civ_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Acute Food Insecurity Country Data (Latest IPC area\
    \ data in wide form)"
  download_url: https://data.humdata.org/dataset/e47d86cd-d0ec-4cae-9d93-9385b9175478/resource/d27a3a47-42dc-431f-988c-b1af79a7ac29/download/ipc_civ_area_wide_latest.csv
  format: null
  id: resource_d27a3a47
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_civ_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Acute Food Insecurity Country Data (All IPC national\
    \ data in long form)"
  download_url: https://data.humdata.org/dataset/e47d86cd-d0ec-4cae-9d93-9385b9175478/resource/bb1fc792-a693-4526-89df-22c25f193b5b/download/ipc_civ_national_long.csv
  format: null
  id: resource_bb1fc792
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_civ_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Acute Food Insecurity Country Data (All IPC national\
    \ data in wide form)"
  download_url: https://data.humdata.org/dataset/e47d86cd-d0ec-4cae-9d93-9385b9175478/resource/52f019c5-3e6d-493d-a8ef-b2d92902a5e0/download/ipc_civ_national_wide.csv
  format: null
  id: resource_52f019c5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_civ_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Acute Food Insecurity Country Data (All IPC area\
    \ data in long form)"
  download_url: https://data.humdata.org/dataset/e47d86cd-d0ec-4cae-9d93-9385b9175478/resource/6474665d-d7cd-4249-8442-db3f8298ad43/download/ipc_civ_area_long.csv
  format: null
  id: resource_6474665d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_civ_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Acute Food Insecurity Country Data (All IPC area\
    \ data in wide form)"
  download_url: https://data.humdata.org/dataset/e47d86cd-d0ec-4cae-9d93-9385b9175478/resource/abe9f6fe-f1a5-4ab7-b2c4-7835a726088d/download/ipc_civ_area_wide.csv
  format: null
  id: resource_abe9f6fe
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_civ_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-civ_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - CIV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: "C\xF4te d'Ivoire: Acute Food Insecurity Country Data"
version: null
vulnerability: null
---
