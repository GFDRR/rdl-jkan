---
attributions:
- entity:
    affiliation: null
    email: null
    name: National IPC Technical Working Group
    url: https://data.humdata.org/dataset/sudan-acute-food-insecurity-country-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/sudan-acute-food-insecurity-country-data
creator:
  affiliation: null
  email: null
  name: Integrated Food Security Phase Classification (IPC)
  url: https://data.humdata.org/dataset/sudan-acute-food-insecurity-country-data
dataset_id: rdls_lss-sdn_ipc_acuteinsecuritycountrydat_2019
description: 'The IPC Acute Food Insecurity (IPC AFI) classification provides strategically
  relevant information to decision makers that focuses on short-term objectives to
  prevent, mitigate or decrease severe food insecurity that threatens lives or livelihoods.
  This data has been produced by the National IPC Technical Working Groups for IPC
  population estimates since 2017. All national population figures are based on official
  country population estimates. IPC estimates are those published in country IPC reports.
  There is also a global dataset .. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-acute-food-insecurity-country-data]'
details: null
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: IPC Acute Food Insecurity classifications are produced by the National
    IPC Technical Working Group using standardized IPC methodology to classify populations
    into food insecurity phases (1-5) based on livelihood vulnerability and food access
    indicators. Population estimates are based on official country census data and
    are disaggregated by administrative level and time period (current analysis and
    projections).
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
- href: https://data.humdata.org/dataset/sudan-acute-food-insecurity-country-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by acute food insecurity phase due to drought
      and livelihood stress
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
  description: 'Sudan: Acute Food Insecurity Country Data (IPC GeoJSON for latest
    analysis)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/34bc177a-344f-4894-837e-86fea689e3b5/download/ipc_sdn.geojson
  format: null
  id: resource_34bc177a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (Latest IPC national data
    in long form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/f92dcdf7-f5cb-4b7e-8ade-052a4379a24d/download/ipc_sdn_national_long_latest.csv
  format: null
  id: resource_f92dcdf7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_national_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in long form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/664f3b4b-8105-488c-ad96-371d02872c56/download/ipc_sdn_level1_long_latest.csv
  format: null
  id: resource_664f3b4b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_level1_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (Latest IPC level 1 data
    in wide form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/95c3c714-06b7-467e-97d8-4506148ae68e/download/ipc_sdn_level1_wide_latest.csv
  format: null
  id: resource_95c3c714
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_level1_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (Latest IPC area data in
    long form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/b74da561-cb54-4b76-a3b0-1b5483e803d5/download/ipc_sdn_area_long_latest.csv
  format: null
  id: resource_b74da561
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_area_long_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (Latest IPC area data in
    wide form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/532c4144-db3a-497d-bbd2-f8f90ccba9ef/download/ipc_sdn_area_wide_latest.csv
  format: null
  id: resource_532c4144
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_area_wide_latest.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (All IPC national data in
    long form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/794f1edc-5456-4247-a7e6-fc830733e53e/download/ipc_sdn_national_long.csv
  format: null
  id: resource_794f1edc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_national_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (All IPC national data in
    wide form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/ff9269bb-c458-40d5-8694-b0f45f60c69c/download/ipc_sdn_national_wide.csv
  format: null
  id: resource_ff9269bb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_national_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (All IPC level 1 data in
    long form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/fa5e4cae-fb61-48c7-aa7b-74fb10551f26/download/ipc_sdn_level1_long.csv
  format: null
  id: resource_fa5e4cae
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_level1_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (All IPC level 1 data in
    wide form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/d82a28a6-2ed6-4db9-8972-026551defc5f/download/ipc_sdn_level1_wide.csv
  format: null
  id: resource_d82a28a6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_level1_wide.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (All IPC area data in long
    form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/aa8cbcc4-0024-4016-91f6-dfe4ad8c9385/download/ipc_sdn_area_long.csv
  format: null
  id: resource_aa8cbcc4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_area_long.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Sudan: Acute Food Insecurity Country Data (All IPC area data in wide
    form)'
  download_url: https://data.humdata.org/dataset/d21ca2c3-6675-4463-bcb1-ff713c60fcb0/resource/017c9cfb-1247-41db-92f5-6a5de97ec402/download/ipc_sdn_area_wide.csv
  format: null
  id: resource_017c9cfb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ipc_sdn_area_wide.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sdn_ipc_acuteinsecuritycountrydat_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-05-31'
  start: '2019-06-01'
temporal_resolution: null
title: 'Sudan: Acute Food Insecurity Country Data'
version: null
vulnerability: null
---
