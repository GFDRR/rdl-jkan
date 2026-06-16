---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-population-data-for-vgb
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-population-data-for-vgb
dataset_id: rdls_lss-vgb_unhcr_britishvirginislandsdataf_2021
description: 'Data collated by UNHCR, containing information about forcibly displaced
  populations and stateless persons, spanning across more than 70 years of statistical
  activities. The data includes the countries / territories of asylum and origin.
  Specific resources are available for end-year population totals, demographics, asylum
  applications, decisions, and solutions availed by refugees and IDPs (resettlement,
  naturalisation or returns).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-population-data-for-vgb]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: UNHCR collects and compiles displacement statistics from government
    sources and its own registration systems, quality-assures the data through biannual
    cycles, and disseminates end-year population totals, demographics, asylum applications,
    and solutions (resettlement, naturalization, returns) for forcibly displaced and
    stateless populations in British Virgin Islands.
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
- href: https://data.humdata.org/dataset/unhcr-population-data-for-vgb
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Forcibly displaced populations including refugees, asylum seekers,
      and internally displaced persons
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
    description: Stateless persons and others of concern to UNHCR
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
    for forcibly displaced persons originating from British Virgin Islands. Data is
    available since 1951.
  download_url: https://data.humdata.org/dataset/42fa0f0d-e224-4449-ba02-bf1aa0f1d646/resource/80b39a0a-70b5-4b4a-8e2e-1b3408b81e60/download/end_year_population_totals_originating_vgb.csv
  format: null
  id: resource_80b39a0a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: End-year stock population figures for forcibly displaced persons originating
    from British Virgin Islands
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing end-year stock population figures
    for forcibly displaced and stateless persons residing in British Virgin Islands.
    Data is available since 1951.
  download_url: https://data.humdata.org/dataset/42fa0f0d-e224-4449-ba02-bf1aa0f1d646/resource/8f4114ad-0f4f-45fd-b3a5-a8eb1374607a/download/end_year_population_totals_residing_vgb.csv
  format: null
  id: resource_8f4114ad
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: End-year stock population figures for forcibly displaced and stateless persons
    residing in British Virgin Islands
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about forcibly displaced
    populations originating from British Virgin Islands. It includes data on their
    demographics as well as sub-national locations. The demographic data is only collected
    annually and data is available from 2001.
  download_url: https://data.humdata.org/dataset/42fa0f0d-e224-4449-ba02-bf1aa0f1d646/resource/0dc0e5f7-72a5-40fe-82d9-ff7a987cb49c/download/demographics_originating_vgb.csv
  format: null
  id: resource_0dc0e5f7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Demographics and locations of forcibly displaced people originating from
    British Virgin Islands
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about forcibly displaced
    populations and stateless people residing in British Virgin Islands. It includes
    data on their demographics as well as sub-national locations. The demographic
    data is only collected annually and data is available from 2001.
  download_url: https://data.humdata.org/dataset/42fa0f0d-e224-4449-ba02-bf1aa0f1d646/resource/eb68b086-bb29-4257-8b9e-95747b4103a0/download/demographics_residing_vgb.csv
  format: null
  id: resource_eb68b086
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Demographics and locations of forcibly displaced and stateless people residing
    in British Virgin Islands
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset collated by UNHCR, containing information about the number
    of applications for asylum residing in British Virgin Islands. Data is available
    since 2000.
  download_url: https://data.humdata.org/dataset/42fa0f0d-e224-4449-ba02-bf1aa0f1d646/resource/2d18abca-1387-498a-8c4a-06ebd15e627f/download/asylum_applications_residing_vgb.csv
  format: null
  id: resource_2d18abca
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum applications by asylum seekers residing in British Virgin Islands
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR about asylum decisions taken on asylum claims
    of asylum seekers residing in British Virgin Islands. Data is available since
    2000.
  download_url: https://data.humdata.org/dataset/42fa0f0d-e224-4449-ba02-bf1aa0f1d646/resource/6137e77f-7010-4cfb-8cf6-ab8642afbf39/download/asylum_decisions_residing_vgb.csv
  format: null
  id: resource_6137e77f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum decisions taken on asylum claims of asylum seekers residing in British
    Virgin Islands
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: British Virgin Islands - Data on forcibly displaced populations and
    stateless persons (QuickCharts data for British Virgin Islands)
  download_url: https://data.humdata.org/dataset/42fa0f0d-e224-4449-ba02-bf1aa0f1d646/resource/94da9162-e1d5-45b7-b178-c83511adf7ab/download/qc_data.csv
  format: null
  id: resource_94da9162
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
slug: rdls_lss-vgb_unhcr_britishvirginislandsdataf_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - VGB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-06-30'
  start: '2021-01-01'
temporal_resolution: null
title: British Virgin Islands - Data on forcibly displaced populations and stateless
  persons
version: null
vulnerability: null
---
