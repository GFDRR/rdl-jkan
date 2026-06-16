---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/democratic-republic-of-the-congo-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/democratic-republic-of-the-congo-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/democratic-republic-of-the-congo-acute-food-insecurity-country-data
dataset_id: rdls_lss-cod_ipc_acuteinsecuritycountrydat_2017
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/democratic-republic-of-the-congo-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using the standardized IPC Manual methodology to assess
    food insecurity phases across national, provincial (Level 1), and area-level administrative
    units. Population figures are based on official country estimates and classified
    into IPC phases (1-5) with current and projected validity periods to inform humanitarian
    decision-making.
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
- href: https://data.humdata.org/dataset/democratic-republic-of-the-congo-acute-food-insecurity-country-data
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
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (IPC GeoJSON for latest analysis)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/46019466-93cc-406f-b2d9-43b37a1c0dab/download/ipc_cod.geojson
  format: null
  id: resource_46019466
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (Latest IPC national data in long form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/d631120c-fe5f-4453-a87f-ea30a6614acd/download/ipc_cod_national_long_latest.csv
  format: null
  id: resource_d631120c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (Latest IPC level 1 data in long form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/d4e5a156-dad0-436a-8bc2-35a0e983df4a/download/ipc_cod_level1_long_latest.csv
  format: null
  id: resource_d4e5a156
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (Latest IPC level 1 data in wide form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/a78d732e-fe79-49d0-82a2-9cc19a3a1a71/download/ipc_cod_level1_wide_latest.csv
  format: null
  id: resource_a78d732e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (Latest IPC area data in long form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/cc081488-52a5-41ab-8a21-798354b41ebf/download/ipc_cod_area_long_latest.csv
  format: null
  id: resource_cc081488
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (Latest IPC area data in wide form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/c70ab66e-c39e-4dcf-a20e-6267edc6a971/download/ipc_cod_area_wide_latest.csv
  format: null
  id: resource_c70ab66e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (All IPC national data in long form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/da295582-636e-4221-bdd2-ebf3d1899f51/download/ipc_cod_national_long.csv
  format: null
  id: resource_da295582
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (All IPC national data in wide form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/ad711884-c7ff-4ba8-8039-d26f16fb48d6/download/ipc_cod_national_wide.csv
  format: null
  id: resource_ad711884
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (All IPC level 1 data in long form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/99f433d6-1772-4278-a3ee-cc8edff6f5f4/download/ipc_cod_level1_long.csv
  format: null
  id: resource_99f433d6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (All IPC level 1 data in wide form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/ff71042d-bdb5-410a-b5d0-443d98c298cd/download/ipc_cod_level1_wide.csv
  format: null
  id: resource_ff71042d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (All IPC area data in long form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/8f883836-782f-4adc-bade-cf7dff9a1372/download/ipc_cod_area_long.csv
  format: null
  id: resource_8f883836
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data
    (All IPC area data in wide form)'
  download_url: https://data.humdata.org/dataset/1dfc7346-adc8-4dfc-b2ac-dc18549e9068/resource/736f72e0-2e28-4572-8a39-2944f392f079/download/ipc_cod_area_wide.csv
  format: null
  id: resource_736f72e0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_cod_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ipc_acuteinsecuritycountrydat_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-06-30'
  start: '2017-06-01'
temporal_resolution: null
title: 'Democratic Republic of the Congo: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
