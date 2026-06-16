---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-population-data-for-bih
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-population-data-for-bih
dataset_id: rdls_lss-bih_unhcr_dataforciblydisplacedpopu_1992
description: 'Data collated by UNHCR, containing information about forcibly displaced
  populations and stateless persons, spanning across more than 70 years of statistical
  activities. The data includes the countries / territories of asylum and origin.
  Specific resources are available for end-year population totals, demographics, asylum
  applications, decisions, and solutions availed by refugees and IDPs (resettlement,
  naturalisation or returns).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-population-data-for-bih]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: UNHCR collated statistics on forcibly displaced populations and stateless
    persons spanning over 70 years, sourced primarily from governments hosting these
    populations and UNHCR's own registration systems. Data includes end-year population
    stocks, demographics, locations, asylum applications, decisions, and durable solutions
    (resettlement, naturalization, returns) for refugees and IDPs originating from
    or residing in Bosnia and Herzegovina.
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
- href: https://data.humdata.org/dataset/unhcr-population-data-for-bih
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and refugees from Bosnia and Herzegovina,
      primarily resulting from conflict-related displacement
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
    description: Asylum seekers, stateless persons, and other populations of concern
      to UNHCR
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
    for forcibly displaced persons originating from Bosnia and Herzegovina. Data is
    available since 1951.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/e85ec0c4-7ea0-4c36-aca0-b72150fc8dee/download/end_year_population_totals_originating_bih.csv
  format: null
  id: resource_e85ec0c4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: End-year stock population figures for forcibly displaced persons originating
    from Bosnia and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing end-year stock population figures
    for forcibly displaced and stateless persons residing in Bosnia and Herzegovina.
    Data is available since 1951.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/0190c92b-e4fd-45da-b382-cf8414d0892d/download/end_year_population_totals_residing_bih.csv
  format: null
  id: resource_0190c92b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: End-year stock population figures for forcibly displaced and stateless persons
    residing in Bosnia and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about forcibly displaced
    populations originating from Bosnia and Herzegovina. It includes data on their
    demographics as well as sub-national locations. The demographic data is only collected
    annually and data is available from 2001.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/d3f3f5ff-84b3-4b3e-be0f-28a8acc99981/download/demographics_originating_bih.csv
  format: null
  id: resource_d3f3f5ff
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Demographics and locations of forcibly displaced people originating from
    Bosnia and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about forcibly displaced
    populations and stateless people residing in Bosnia and Herzegovina. It includes
    data on their demographics as well as sub-national locations. The demographic
    data is only collected annually and data is available from 2001.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/ab0bfe00-99a2-45c0-bb7a-e7a1ddbd9c74/download/demographics_residing_bih.csv
  format: null
  id: resource_ab0bfe00
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Demographics and locations of forcibly displaced and stateless people residing
    in Bosnia and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about the number of
    applications for asylum originating from Bosnia and Herzegovina. Data is available
    since 2000.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/ef47e16d-83e4-4f06-a722-928710e624ec/download/asylum_applications_originating_bih.csv
  format: null
  id: resource_ef47e16d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum applications by asylum seekers originating from Bosnia and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset collated by UNHCR, containing information about the number
    of applications for asylum residing in Bosnia and Herzegovina. Data is available
    since 2000.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/7f271220-fcdf-4c81-8cb2-c038aae7f431/download/asylum_applications_residing_bih.csv
  format: null
  id: resource_7f271220
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum applications by asylum seekers residing in Bosnia and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR about asylum decisions taken on asylum claims
    of asylum seekers originating from Bosnia and Herzegovina. Data is available since
    2000.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/cee4d6f5-e107-4504-9bd7-9c03609cecef/download/asylum_decisions_originating_bih.csv
  format: null
  id: resource_cee4d6f5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum decisions taken on asylum claims of asylum seekers originating from
    Bosnia and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR about asylum decisions taken on asylum claims
    of asylum seekers residing in Bosnia and Herzegovina. Data is available since
    2000.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/f0e0e2a8-787c-4ad4-86a7-ec5d5a4f3609/download/asylum_decisions_residing_bih.csv
  format: null
  id: resource_f0e0e2a8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Asylum decisions taken on asylum claims of asylum seekers residing in Bosnia
    and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Dataset collated by UNHCR, containing information about the number
    of forcibly displaced originating from Bosnia and Herzegovina availing different
    types of solutions for refugees and IDPs such as repatriation or resettlement.
    Data is available since 1983.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/dc8cc50a-668e-46ac-8c6e-92b5db28acef/download/solutions_originating_bih.csv
  format: null
  id: resource_dc8cc50a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Solutions for refugees and IDPs originating from Bosnia and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data collated by UNHCR, containing information about the number of
    forcibly displaced residing in Bosnia and Herzegovina availing different types
    of solutions for refugees and IDPs such as repatriation or resettlement. Data
    is available since 1983.
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/aeee89b1-9d8c-4544-a424-df0bb545352d/download/solutions_residing_bih.csv
  format: null
  id: resource_aeee89b1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Solutions for refugees and IDPs residing in Bosnia and Herzegovina
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bosnia and Herzegovina - Data on forcibly displaced populations and
    stateless persons (QuickCharts data for Bosnia and Herzegovina)
  download_url: https://data.humdata.org/dataset/aa274d18-79fa-4656-a103-ade17f20c8ae/resource/3b585074-0779-4ae7-bdf7-7f78f0b3b0f7/download/qc_data.csv
  format: null
  id: resource_3b585074
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
slug: rdls_lss-bih_unhcr_dataforciblydisplacedpopu_1992
spatial:
  bbox: null
  centroid: null
  countries:
  - BIH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-06-30'
  start: '1992-01-01'
temporal_resolution: null
title: Bosnia and Herzegovina - Data on forcibly displaced populations and stateless
  persons
version: null
vulnerability: null
---
