---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-population-data-for-ton
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-population-data-for-ton
dataset_id: rdls_lss-ton_unhcr_dataforciblydisplacedpopu_1996
description: 'Data collated by UNHCR, containing information about forcibly displaced
  populations and stateless persons, spanning across more than 70 years of statistical
  activities. The data includes the countries / territories of asylum and origin.
  Specific resources are available for end-year population totals, demographics, asylum
  applications, decisions, and solutions availed by refugees and IDPs (resettlement,
  naturalisation or returns).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-population-data-for-ton]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: UNHCR compiled forcibly displaced population statistics from Tonga
    through biannual collection from host governments and UNHCR registration systems.
    Data includes end-year stock figures, demographic breakdowns by age and gender,
    asylum applications, decisions, and durable solutions (resettlement, naturalization,
    returns) for refugees and IDPs originating from Tonga.
  sources:
  - id: source_1
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-population-data-for-ton
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from Tonga recorded in UNHCR statistics
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Refugees and asylum seekers from Tonga in host countries
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing end-year stock population figures
    for forcibly displaced persons originating from Tonga. Data is available since
    1951.
  download_url: https://data.humdata.org/dataset/7a3fb7a3-7b23-4ef2-81cd-80834afa2fe8/resource/8c98dfb7-54d4-4e37-9b6a-dc26c3e43b5b/download/end_year_population_totals_originating_ton.csv
  format: null
  id: resource_8c98dfb7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: End-year stock population figures for forcibly displaced persons originating
    from Tonga
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about forcibly displaced
    populations originating from Tonga. It includes data on their demographics as
    well as sub-national locations. The demographic data is only collected annually
    and data is available from 2001.
  download_url: https://data.humdata.org/dataset/7a3fb7a3-7b23-4ef2-81cd-80834afa2fe8/resource/66d3b17e-9af2-4436-bef4-bddd6c8b64d2/download/demographics_originating_ton.csv
  format: null
  id: resource_66d3b17e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Demographics and locations of forcibly displaced people originating from
    Tonga
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about the number of
    applications for asylum originating from Tonga. Data is available since 2000.
  download_url: https://data.humdata.org/dataset/7a3fb7a3-7b23-4ef2-81cd-80834afa2fe8/resource/880eb612-91e6-447c-8511-ea7c0d076bca/download/asylum_applications_originating_ton.csv
  format: null
  id: resource_880eb612
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum applications by asylum seekers originating from Tonga
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR about asylum decisions taken on asylum claims
    of asylum seekers originating from Tonga. Data is available since 2000.
  download_url: https://data.humdata.org/dataset/7a3fb7a3-7b23-4ef2-81cd-80834afa2fe8/resource/1fd9ce9f-ad2a-48c8-b3d4-32183709bb08/download/asylum_decisions_originating_ton.csv
  format: null
  id: resource_1fd9ce9f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum decisions taken on asylum claims of asylum seekers originating from
    Tonga
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset collated by UNHCR, containing information about the number
    of forcibly displaced originating from Tonga availing different types of solutions
    for refugees and IDPs such as repatriation or resettlement. Data is available
    since 1983.
  download_url: https://data.humdata.org/dataset/7a3fb7a3-7b23-4ef2-81cd-80834afa2fe8/resource/6c02866d-1fb1-4bdb-87cf-4dedc3a2b79d/download/solutions_originating_ton.csv
  format: null
  id: resource_6c02866d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Solutions for refugees and IDPs originating from Tonga
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tonga - Data on forcibly displaced populations and stateless persons
    (QuickCharts data for Tonga)
  download_url: https://data.humdata.org/dataset/7a3fb7a3-7b23-4ef2-81cd-80834afa2fe8/resource/d563a9a2-3cdb-4690-bdf3-3b0b7f339c24/download/qc_data.csv
  format: null
  id: resource_d563a9a2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: qc_data.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ton_unhcr_dataforciblydisplacedpopu_1996
spatial:
  bbox: null
  centroid: null
  countries:
  - TON
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-06-30'
  start: '1996-01-01'
temporal_resolution: null
title: Tonga - Data on forcibly displaced populations and stateless persons
version: null
vulnerability: null
---
