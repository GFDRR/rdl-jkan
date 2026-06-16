---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-ecu
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-ecu
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Integrated Food Security Phase Classification (IPC)
    url: https://data.humdata.org/dataset/hdx-hapi-ecu
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/hdx-hapi-ecu
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Financial Tracking System (FTS)
    url: https://data.humdata.org/dataset/hdx-hapi-ecu
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Oxford Poverty & Human Development Initiative
    url: https://data.humdata.org/dataset/hdx-hapi-ecu
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNFPA
    url: https://data.humdata.org/dataset/hdx-hapi-ecu
  id: attribution_7
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-ecu
  id: attribution_8
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-ecu
  id: attribution_9
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-ecu
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-ecu
dataset_id: rdls_el-ecu_hdxapi_hdxhapi_2001
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-ecu]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population distribution across administrative divisions
      in Ecuador
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from nine
    contributing organizations including ACLED, IPC, IOM, UNHCR, and WFP. Data is
    collected through national assessments, administrative registries, and event monitoring
    systems, then harmonized into common administrative geographies and temporal periods.
    The dataset integrates conflict events, displacement records, food security classifications,
    and baseline population to support humanitarian decision-making in Ecuador.
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
    name: Integrated Food Security Phase Classification (IPC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: OCHA Financial Tracking System (FTS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
    license: null
    name: Oxford Poverty & Human Development Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_7
    license: null
    name: UNFPA
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_8
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_9
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
- href: https://data.humdata.org/dataset/hdx-hapi-ecu
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict-related events in Ecuador
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Food insecurity classifications from IPC assessments in Ecuador
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
        type: direct
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
  description: "IDPs data from HDX HAPI, please see the documentation for more information\
    \ Source: International Organization for Migration (IOM) License: Copyright \xC2\
    \xA9 International Organization for Migration 2018 IOM reserves the right to assert\
    \ ownership of the Materials collected on the https://data.humdata.org/ website.\
    \ The Materials may be viewed, downloaded, and printed for non-commercial use\
    \ only, without, inter alia, any right to sell, resell, redistribute or create\
    \ derivative works therefrom. At all times the User shall credit the DTM as the\
    \ source, unless otherwise stated. The user must include the URL of the Materials\
    \ from the HDX Website, as well as the following credit line: Source: 'International\
    \ Organization for Migration (IOM), Displacement Tracking Matrix (DTM)'."
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/9189bd9e-cf3a-4118-bc7e-0f8e1b8dc879/download/hdx_hapi_idps_ecu.csv
  format: null
  id: resource_9189bd9e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Internally-Displaced Persons for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Refugees and Persons of Concern data from HDX HAPI, please see the
    documentation for more information Source: UNHCR - The UN Refugee Agency License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/3563a1b0-0384-469a-8d3d-25dbc80c3b79/download/hdx_hapi_refugees_ecu.csv
  format: null
  id: resource_3563a1b0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Returnees data from HDX HAPI, please see the documentation for more
    information Source: UNHCR - The UN Refugee Agency License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/99df31f8-60b7-4115-a36f-c44a55994664/download/hdx_hapi_returnees_ecu.csv
  format: null
  id: resource_99df31f8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Returnees for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Funding data from HDX HAPI, please see the documentation for more
    information Source: OCHA Financial Tracking System (FTS) License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/79cdefe3-d6af-4d5d-94d1-a69c5fdc43fc/download/hdx_hapi_funding_ecu.csv
  format: null
  id: resource_79cdefe3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Funding for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/e93898c1-90b9-4cfc-9ef3-8d48a03955c6/download/hdx_hapi_conflict_event_ecu.csv
  format: null
  id: resource_e93898c1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/5e54fe61-d7a8-426d-8ea7-eed85d9617c6/download/hdx_hapi_national_risk_ecu.csv
  format: null
  id: resource_5e54fe61
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Security data from HDX HAPI, please see the documentation for
    more information Source: Integrated Food Security Phase Classification (IPC) License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/dc6bcc72-ef68-4be4-870a-591420ab4f2f/download/hdx_hapi_food_security_ecu.csv
  format: null
  id: resource_dc6bcc72
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Security for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Prices & Market Monitor data from HDX HAPI, please see the documentation
    for more information Source: WFP - World Food Programme License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/5d5a1370-c507-47bb-866c-a0cb69a905f2/download/hdx_hapi_food_price_ecu.csv
  format: null
  id: resource_5d5a1370
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Prices & Market Monitor for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Poverty Rate data from HDX HAPI, please see the documentation for
    more information Source: Oxford Poverty & Human Development Initiative License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/46bcf0db-b97c-42c7-9247-f433e41c81aa/download/hdx_hapi_poverty_rate_ecu.csv
  format: null
  id: resource_46bcf0db
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Poverty Rate for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: UNFPA License: Creative Commons Attribution for Intergovernmental
    Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/ea8396f6-1847-4c5c-8ae2-f37e305732d7/download/hdx_hapi_population_ecu.csv
  format: null
  id: resource_ea8396f6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/9e559dfe-b678-431a-80a2-8f3536b01f62/download/hdx_hapi_rainfall_ecu.csv
  format: null
  id: resource_9e559dfe
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Ecuador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/46cf296f-2bc3-4bc3-a44b-b87baa9798bb/resource/e6d354dd-d4d8-4f0b-af36-8531b9603991/download/hdx_hapi_data_availability_ecu.csv
  format: null
  id: resource_e6d354dd
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Ecuador'
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ecu_hdxapi_hdxhapi_2001
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2027-12-31'
  start: '2001-01-01'
temporal_resolution: null
title: HDX HAPI Data for Ecuador
version: null
vulnerability: null
---
