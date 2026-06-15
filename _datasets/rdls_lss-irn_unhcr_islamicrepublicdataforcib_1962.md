---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-population-data-for-irn
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-population-data-for-irn
dataset_id: rdls_lss-irn_unhcr_islamicrepublicdataforcib_1962
description: 'Data collated by UNHCR, containing information about forcibly displaced
  populations and stateless persons, spanning across more than 70 years of statistical
  activities. The data includes the countries / territories of asylum and origin.
  Specific resources are available for end-year population totals, demographics, asylum
  applications, decisions, and solutions availed by refugees and IDPs (resettlement,
  naturalisation or returns).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-population-data-for-irn]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNHCR collates forcibly displaced population statistics from government
    sources and its own registration systems, compiling end-year stock figures, demographic
    breakdowns by location and accommodation type, asylum applications, decisions,
    and durable solutions (resettlement, naturalization, returns) for populations
    originating from and residing in Iran.
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
- href: https://data.humdata.org/dataset/unhcr-population-data-for-irn
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from Iran across multiple countries
      and time periods
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
    description: Refugees and asylum seekers originating from Iran
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
    for forcibly displaced persons originating from Iran (Islamic Republic of). Data
    is available since 1951.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/a4c44445-5861-467a-aadd-37904259d916/download/end_year_population_totals_originating_irn.csv
  format: null
  id: resource_a4c44445
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: End-year stock population figures for forcibly displaced persons originating
    from Iran (Islamic Republic of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing end-year stock population figures
    for forcibly displaced and stateless persons residing in Iran (Islamic Republic
    of). Data is available since 1951.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/f347441a-551b-4ea0-9fed-d3318c0560c0/download/end_year_population_totals_residing_irn.csv
  format: null
  id: resource_f347441a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: End-year stock population figures for forcibly displaced and stateless persons
    residing in Iran (Islamic Republic of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about forcibly displaced
    populations originating from Iran (Islamic Republic of). It includes data on their
    demographics as well as sub-national locations. The demographic data is only collected
    annually and data is available from 2001.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/772ce561-bbee-4c8a-8b1d-44cb9af9eb52/download/demographics_originating_irn.csv
  format: null
  id: resource_772ce561
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Demographics and locations of forcibly displaced people originating from
    Iran (Islamic Republic of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about forcibly displaced
    populations and stateless people residing in Iran (Islamic Republic of). It includes
    data on their demographics as well as sub-national locations. The demographic
    data is only collected annually and data is available from 2001.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/1db48136-6283-4663-a377-5fca458e26d3/download/demographics_residing_irn.csv
  format: null
  id: resource_1db48136
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Demographics and locations of forcibly displaced and stateless people residing
    in Iran (Islamic Republic of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about the number of
    applications for asylum originating from Iran (Islamic Republic of). Data is available
    since 2000.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/54eec1a2-2d49-4b8d-9b03-41d08a1d7b81/download/asylum_applications_originating_irn.csv
  format: null
  id: resource_54eec1a2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum applications by asylum seekers originating from Iran (Islamic Republic
    of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset collated by UNHCR, containing information about the number
    of applications for asylum residing in Iran (Islamic Republic of). Data is available
    since 2000.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/2c0d1d96-9f11-4296-a57b-e10281d515c9/download/asylum_applications_residing_irn.csv
  format: null
  id: resource_2c0d1d96
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum applications by asylum seekers residing in Iran (Islamic Republic
    of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR about asylum decisions taken on asylum claims
    of asylum seekers originating from Iran (Islamic Republic of). Data is available
    since 2000.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/4cc33c7f-61b0-4015-9225-d30f3e6b1886/download/asylum_decisions_originating_irn.csv
  format: null
  id: resource_4cc33c7f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum decisions taken on asylum claims of asylum seekers originating from
    Iran (Islamic Republic of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR about asylum decisions taken on asylum claims
    of asylum seekers residing in Iran (Islamic Republic of). Data is available since
    2000.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/4c873f42-0f18-499e-bd60-88716378c241/download/asylum_decisions_residing_irn.csv
  format: null
  id: resource_4c873f42
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum decisions taken on asylum claims of asylum seekers residing in Iran
    (Islamic Republic of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset collated by UNHCR, containing information about the number
    of forcibly displaced originating from Iran (Islamic Republic of) availing different
    types of solutions for refugees and IDPs such as repatriation or resettlement.
    Data is available since 1983.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/1b3e079d-1798-4ffd-bfaa-99539db693a5/download/solutions_originating_irn.csv
  format: null
  id: resource_1b3e079d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Solutions for refugees and IDPs originating from Iran (Islamic Republic of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about the number of
    forcibly displaced residing in Iran (Islamic Republic of) availing different types
    of solutions for refugees and IDPs such as repatriation or resettlement. Data
    is available since 1983.
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/3335e916-e713-4083-9cd3-3badf30d1908/download/solutions_residing_irn.csv
  format: null
  id: resource_3335e916
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Solutions for refugees and IDPs residing in Iran (Islamic Republic of)
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iran (Islamic Republic of) - Data on forcibly displaced populations
    and stateless persons (QuickCharts data for Iran (Islamic Republic of))
  download_url: https://data.humdata.org/dataset/e17f17c7-a3f2-47c5-aa16-908aaf04eade/resource/6fed1543-36d1-430c-acbf-5a44838c52c4/download/qc_data.csv
  format: null
  id: resource_6fed1543
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
slug: rdls_lss-irn_unhcr_islamicrepublicdataforcib_1962
spatial:
  bbox: null
  centroid: null
  countries:
  - IRN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-06-30'
  start: '1962-01-01'
temporal_resolution: null
title: Iran (Islamic Republic of) - Data on forcibly displaced populations and stateless
  persons
version: null
vulnerability: null
---
