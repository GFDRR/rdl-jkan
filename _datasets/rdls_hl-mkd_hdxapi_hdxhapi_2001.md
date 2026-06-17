---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-mkd
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-mkd
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Oxford Poverty & Human Development Initiative
    url: https://data.humdata.org/dataset/hdx-hapi-mkd
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-mkd
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-mkd
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-mkd
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-mkd
dataset_id: rdls_hl-mkd_hdxapi_hdxhapi_2001
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-mkd]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: CC-BY-4.0
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    authoritative sources (ACLED, INFORM, UNHCR, WFP, OPHI) into a unified API framework
    for North Macedonia. Data are collected through established monitoring systems
    and integrated into common administrative and temporal reference structures to
    enable interoperable humanitarian analysis and decision support.
  sources:
  - id: source_1
    license: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: INFORM
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: Oxford Poverty & Human Development Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: WFP - World Food Programme
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-mkd
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct fatalities from conflict events in North Macedonia
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by poverty and food insecurity in North Macedonia
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: indirect
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Refugees and Persons of Concern data from HDX HAPI, please see the
    documentation for more information Source: UNHCR - The UN Refugee Agency License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/e17e4e3d-055b-487e-b77c-095232f7f615/resource/efcfb7d1-93cb-467a-ad27-79d1ffccc2b2/download/hdx_hapi_refugees_mkd.csv
  format: null
  id: resource_efcfb7d1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for North Macedonia'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Returnees data from HDX HAPI, please see the documentation for more
    information Source: UNHCR - The UN Refugee Agency License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/e17e4e3d-055b-487e-b77c-095232f7f615/resource/9f65de32-6fa4-4617-895c-99cf456a3d3f/download/hdx_hapi_returnees_mkd.csv
  format: null
  id: resource_9f65de32
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Returnees for North Macedonia'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/e17e4e3d-055b-487e-b77c-095232f7f615/resource/2d1efc74-7601-4cea-9aca-e4aa13034c90/download/hdx_hapi_conflict_event_mkd.csv
  format: null
  id: resource_2d1efc74
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for North Macedonia'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/e17e4e3d-055b-487e-b77c-095232f7f615/resource/4d2450f8-91b9-48d5-90a3-34522c64fda0/download/hdx_hapi_national_risk_mkd.csv
  format: null
  id: resource_4d2450f8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for North Macedonia'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Poverty Rate data from HDX HAPI, please see the documentation for
    more information Source: Oxford Poverty & Human Development Initiative License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/e17e4e3d-055b-487e-b77c-095232f7f615/resource/1e21dbec-8fbc-4d3c-b36c-330e1c58dd83/download/hdx_hapi_poverty_rate_mkd.csv
  format: null
  id: resource_1e21dbec
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Poverty Rate for North Macedonia'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/e17e4e3d-055b-487e-b77c-095232f7f615/resource/fe7a52f7-b6ca-437d-918b-7de2ac065c10/download/hdx_hapi_rainfall_mkd.csv
  format: null
  id: resource_fe7a52f7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for North Macedonia'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/e17e4e3d-055b-487e-b77c-095232f7f615/resource/8be4a5eb-9c75-44da-9227-dfd0f386e6f2/download/hdx_hapi_data_availability_mkd.csv
  format: null
  id: resource_8be4a5eb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for North Macedonia'
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mkd_hdxapi_hdxhapi_2001
spatial:
  bbox: null
  centroid: null
  countries:
  - MKD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2001-01-01'
temporal_resolution: null
title: HDX HAPI Data for North Macedonia
version: null
vulnerability: null
---
