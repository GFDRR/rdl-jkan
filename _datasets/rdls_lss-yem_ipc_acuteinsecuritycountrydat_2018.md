---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/yemen-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/yemen-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/yemen-acute-food-insecurity-country-data
dataset_id: rdls_lss-yem_ipc_acuteinsecuritycountrydat_2018
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yemen-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using the standardized IPC Manual methodology to assess
    food insecurity phases across Yemen's administrative levels. Population estimates
    are derived from official country census data and classified into IPC phases (1-5)
    representing severity of acute food insecurity, with temporal projections provided
    for decision-making on humanitarian response.
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
- href: https://data.humdata.org/dataset/yemen-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by IPC Acute Food Insecurity phase, indicating
      food insecurity severity triggered by drought and conflict-related disruptions
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
  description: 'Yemen: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/408b8ffa-ed54-41bb-9d0f-7e0e09872b54/download/ipc_yem.geojson
  format: null
  id: resource_408b8ffa
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/09be3148-921d-4253-bc93-5c094eeec6b8/download/ipc_yem_national_long_latest.csv
  format: null
  id: resource_09be3148
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/a8064ed0-82b8-453c-b238-5b7053619e4a/download/ipc_yem_level1_long_latest.csv
  format: null
  id: resource_a8064ed0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/4f732363-07df-44b6-942b-6e5c375325d8/download/ipc_yem_level1_wide_latest.csv
  format: null
  id: resource_4f732363
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (Latest IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/f0301af3-ab5f-478d-800d-739bc5fe4b32/download/ipc_yem_area_long_latest.csv
  format: null
  id: resource_f0301af3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (Latest IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/eafba251-0502-4622-886b-0a82d4439310/download/ipc_yem_area_wide_latest.csv
  format: null
  id: resource_eafba251
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (All IPC national data in
    long form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/f6e9594a-279a-4c98-a517-d3d421900cdf/download/ipc_yem_national_long.csv
  format: null
  id: resource_f6e9594a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (All IPC national data in
    wide form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/80e5d127-fbc4-4943-bc4b-13fca2784444/download/ipc_yem_national_wide.csv
  format: null
  id: resource_80e5d127
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (All IPC level 1 data in
    long form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/d6d844d4-a642-4933-a605-2eb236651eb2/download/ipc_yem_level1_long.csv
  format: null
  id: resource_d6d844d4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (All IPC level 1 data in
    wide form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/096661ba-eb8f-43d3-8084-792b31264fca/download/ipc_yem_level1_wide.csv
  format: null
  id: resource_096661ba
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/be2e99a9-f089-42a7-b47d-b358f2ddacca/download/ipc_yem_area_long.csv
  format: null
  id: resource_be2e99a9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/b70c2734-2339-4a4d-a69d-fa2bd3225156/resource/32741746-f267-4751-a27a-fa53ab80bbff/download/ipc_yem_area_wide.csv
  format: null
  id: resource_32741746
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_yem_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_ipc_acuteinsecuritycountrydat_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-02-28'
  start: '2018-12-01'
temporal_resolution: null
title: 'Yemen: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
