---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/guinea-bissau-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/guinea-bissau-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/guinea-bissau-acute-food-insecurity-country-data
dataset_id: rdls_lss-gnb_ipc_acuteinsecuritycountrydat_2020
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/guinea-bissau-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group through standardized assessment methodology (IPC Manual)
    applied to population data. Population figures are classified into IPC phases
    (1-5) representing severity of food insecurity, with estimates disaggregated by
    administrative area and time period (current and projections). This represents
    post-assessment impact classification of food insecurity outcomes.
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
- href: https://data.humdata.org/dataset/guinea-bissau-acute-food-insecurity-country-data
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
  description: 'Guinea-Bissau: Acute Food Insecurity Country Data (IPC GeoJSON for
    latest analysis)'
  download_url: https://data.humdata.org/dataset/3f6ee45d-fdb2-4705-9e56-6ca143c2c33a/resource/e112c667-b47f-46b3-9945-1d86e005434c/download/ipc_gnb.geojson
  format: null
  id: resource_e112c667
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_gnb.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Acute Food Insecurity Country Data (Latest IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/3f6ee45d-fdb2-4705-9e56-6ca143c2c33a/resource/61c58074-727e-4a16-b070-fe599b64eb3c/download/ipc_gnb_national_long_latest.csv
  format: null
  id: resource_61c58074
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_gnb_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Acute Food Insecurity Country Data (Latest IPC area
    data in long form)'
  download_url: https://data.humdata.org/dataset/3f6ee45d-fdb2-4705-9e56-6ca143c2c33a/resource/a40ca269-a075-49c0-a344-6f845dd8f16f/download/ipc_gnb_area_long_latest.csv
  format: null
  id: resource_a40ca269
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_gnb_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Acute Food Insecurity Country Data (Latest IPC area
    data in wide form)'
  download_url: https://data.humdata.org/dataset/3f6ee45d-fdb2-4705-9e56-6ca143c2c33a/resource/4a084a6d-e56c-4c92-985d-c7ce63267d16/download/ipc_gnb_area_wide_latest.csv
  format: null
  id: resource_4a084a6d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_gnb_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Acute Food Insecurity Country Data (All IPC national
    data in long form)'
  download_url: https://data.humdata.org/dataset/3f6ee45d-fdb2-4705-9e56-6ca143c2c33a/resource/d88d1392-6121-49ec-9b10-e86f9f843dc0/download/ipc_gnb_national_long.csv
  format: null
  id: resource_d88d1392
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_gnb_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Acute Food Insecurity Country Data (All IPC national
    data in wide form)'
  download_url: https://data.humdata.org/dataset/3f6ee45d-fdb2-4705-9e56-6ca143c2c33a/resource/1b7947fc-0903-4688-ae99-3e93e73953b3/download/ipc_gnb_national_wide.csv
  format: null
  id: resource_1b7947fc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_gnb_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Acute Food Insecurity Country Data (All IPC area data
    in long form)'
  download_url: https://data.humdata.org/dataset/3f6ee45d-fdb2-4705-9e56-6ca143c2c33a/resource/faac5126-6253-4ded-b7c0-a14100f22a71/download/ipc_gnb_area_long.csv
  format: null
  id: resource_faac5126
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_gnb_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Acute Food Insecurity Country Data (All IPC area data
    in wide form)'
  download_url: https://data.humdata.org/dataset/3f6ee45d-fdb2-4705-9e56-6ca143c2c33a/resource/0c3c2108-17e0-4bea-b96d-3e486a83664a/download/ipc_gnb_area_wide.csv
  format: null
  id: resource_0c3c2108
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_gnb_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gnb_ipc_acuteinsecuritycountrydat_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - GNB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-08-31'
  start: '2020-10-01'
temporal_resolution: null
title: 'Guinea-Bissau: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
