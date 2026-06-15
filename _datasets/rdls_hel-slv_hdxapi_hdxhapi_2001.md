---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Integrated Food Security Phase Classification (IPC)
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Financial Tracking System (FTS)
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Oxford Poverty & Human Development Initiative
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_7
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNFPA
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_8
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_9
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-slv
  id: attribution_10
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-slv
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-slv
dataset_id: rdls_hel-slv_hdxapi_hdxhapi_2001
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-slv]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population distribution by administrative division
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
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    UN agencies and international organizations including ACLED, IOM, UNHCR, WFP,
    and OCHA. Data is collected through national assessments, administrative registries,
    and monitoring systems, then harmonized into common schemas with consistent spatial
    and temporal references. The dataset integrates displacement records, food security
    classifications, baseline population, and risk indicators to support humanitarian
    decision-making.
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
    name: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_7
    license: null
    name: Oxford Poverty & Human Development Initiative
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_8
    license: null
    name: UNFPA
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_9
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_10
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
- href: https://data.humdata.org/dataset/hdx-hapi-slv
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons from conflict and hazard events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
    description: Population affected by food insecurity classified by IPC phase
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
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/a6a426d4-8647-4400-9dd3-2a0626f1acbb/download/hdx_hapi_idps_slv.csv
  format: null
  id: resource_a6a426d4
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Internally-Displaced Persons for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Refugees and Persons of Concern data from HDX HAPI, please see the
    documentation for more information Source: UNHCR - The UN Refugee Agency License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/a91a5d27-ebee-4628-a8f5-11a94f0377a9/download/hdx_hapi_refugees_slv.csv
  format: null
  id: resource_a91a5d27
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Returnees data from HDX HAPI, please see the documentation for more
    information Source: UNHCR - The UN Refugee Agency License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/20ac0fcb-e7ea-4e8a-afea-38ed42bd846f/download/hdx_hapi_returnees_slv.csv
  format: null
  id: resource_20ac0fcb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Returnees for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Humanitarian needs data from HDX HAPI, please see the documentation
    for more information Source: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
    License: Creative Commons Attribution for Intergovernmental Organisations (CC
    BY-IGO)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/91a09d01-86aa-4014-a042-94f4fddf35e0/download/hdx_hapi_humanitarian_needs_slv.csv
  format: null
  id: resource_91a09d01
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Humanitarian Needs for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Funding data from HDX HAPI, please see the documentation for more
    information Source: OCHA Financial Tracking System (FTS) License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/f8f0f074-8d16-40fe-9300-1f38ab55026a/download/hdx_hapi_funding_slv.csv
  format: null
  id: resource_f8f0f074
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Funding for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/bae71c82-9c87-4c71-86f9-5e718cb60763/download/hdx_hapi_conflict_event_slv.csv
  format: null
  id: resource_bae71c82
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/8cecb3b3-b859-4441-9ae1-93335adfd1d6/download/hdx_hapi_national_risk_slv.csv
  format: null
  id: resource_8cecb3b3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Security data from HDX HAPI, please see the documentation for
    more information Source: Integrated Food Security Phase Classification (IPC) License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/805cd70c-ceee-44ac-be9e-01650f66b68e/download/hdx_hapi_food_security_slv.csv
  format: null
  id: resource_805cd70c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Security for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Prices & Market Monitor data from HDX HAPI, please see the documentation
    for more information Source: WFP - World Food Programme License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/74956918-6927-4e72-aad0-a003a7297bf4/download/hdx_hapi_food_price_slv.csv
  format: null
  id: resource_74956918
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Prices & Market Monitor for El
    Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Poverty Rate data from HDX HAPI, please see the documentation for
    more information Source: Oxford Poverty & Human Development Initiative License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/2dde1054-27a4-4102-9dd8-e7226e8cc3a9/download/hdx_hapi_poverty_rate_slv.csv
  format: null
  id: resource_2dde1054
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Poverty Rate for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: UNFPA License: Creative Commons Attribution for Intergovernmental
    Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/ffda9d3f-0e69-4d48-8e50-a611fd97b2c9/download/hdx_hapi_population_slv.csv
  format: null
  id: resource_ffda9d3f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/d703c4d3-a0b3-4c73-88a5-0a3cced08734/download/hdx_hapi_rainfall_slv.csv
  format: null
  id: resource_d703c4d3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for El Salvador'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/14ee5047-c768-4ade-9acd-dfef7884aabf/resource/a5a0dd67-7d49-4566-a261-363554224e1d/download/hdx_hapi_data_availability_slv.csv
  format: null
  id: resource_a5a0dd67
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for El Salvador'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-slv_hdxapi_hdxhapi_2001
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2028-12-31'
  start: '2001-01-01'
temporal_resolution: null
title: HDX HAPI Data for El Salvador
version: null
vulnerability: null
---
