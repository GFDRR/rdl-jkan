---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/zambia-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/zambia-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/zambia-acute-food-insecurity-country-data
dataset_id: rdls_lss-zmb_ipc_acuteinsecuritycountrydat_2018
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/zambia-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using the standardized IPC Manual methodology to assess
    food insecurity phases across administrative levels. Population estimates are
    based on official country census data and IPC field assessments, classified into
    phases 1-5 representing severity from minimal to catastrophic food insecurity.
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
- href: https://data.humdata.org/dataset/zambia-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC acute food insecurity phase, indicating
      drought-driven food insecurity severity
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
  description: 'Zambia: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/a6ab75f1-a7f6-4d90-b6f4-6effde0c977c/download/ipc_zmb.geojson
  format: null
  id: resource_a6ab75f1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/604ab745-e8c8-40a4-9a04-4d0862666fb7/download/ipc_zmb_national_long_latest.csv
  format: null
  id: resource_604ab745
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/99509c69-d66c-4c64-89a3-19285d54edd3/download/ipc_zmb_level1_long_latest.csv
  format: null
  id: resource_99509c69
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/d54effbc-205f-4f69-b74b-d6c21f387123/download/ipc_zmb_level1_wide_latest.csv
  format: null
  id: resource_d54effbc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (Latest IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/67f647b6-527c-47c4-a3bf-6108ccb7d31d/download/ipc_zmb_area_long_latest.csv
  format: null
  id: resource_67f647b6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (Latest IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/dafea40b-3388-4f60-b8a5-27f5d42c3706/download/ipc_zmb_area_wide_latest.csv
  format: null
  id: resource_dafea40b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (All IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/b3f92775-a804-4dba-be23-446c003e1e01/download/ipc_zmb_national_long.csv
  format: null
  id: resource_b3f92775
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (All IPC national data
    in wide form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/0abf1d61-b564-4322-8bbe-608ba9bc7fb2/download/ipc_zmb_national_wide.csv
  format: null
  id: resource_0abf1d61
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (All IPC level 1 data in
    long form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/34ad8cce-cc32-455a-8471-d39ebc3a6eb9/download/ipc_zmb_level1_long.csv
  format: null
  id: resource_34ad8cce
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (All IPC level 1 data in
    wide form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/0cd05f60-b6db-44ab-b45d-8a452df58b13/download/ipc_zmb_level1_wide.csv
  format: null
  id: resource_0cd05f60
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/6c8bd3d6-90e7-49c1-9f38-81cf1374485f/download/ipc_zmb_area_long.csv
  format: null
  id: resource_6c8bd3d6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Zambia: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/d5c9e615-6625-463a-a1a2-6c81e64f73fd/resource/146e4867-f408-4d4c-a899-13a0757f412b/download/ipc_zmb_area_wide.csv
  format: null
  id: resource_146e4867
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_zmb_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-zmb_ipc_acuteinsecuritycountrydat_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-03-31'
  start: '2018-05-01'
temporal_resolution: null
title: 'Zambia: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
