---
attributions:
- entity:
    affiliation: null
    email: null
    name: ACLED (Armed Conflict Location & Event Data Project)
    url: https://data.humdata.org/dataset/hdx-hapi-eri
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-eri
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-eri
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-eri
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
    url: https://data.humdata.org/dataset/hdx-hapi-eri
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Financial Tracking System (FTS)
    url: https://data.humdata.org/dataset/hdx-hapi-eri
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-eri
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-eri
dataset_id: rdls_hel-eri_hdxapi_hdxhapi_1997
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-eri]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population by location, gender, and age range
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
    UN and international organizations (ACLED, INFORM, UNHCR, WFP, OCHA) into a unified
    API for Eritrea. Source data includes observed rainfall measurements, conflict
    event records, refugee population registries, and risk assessment models. Data
    is processed into normalized CSV tables with consistent temporal and geographic
    references to enable interoperable humanitarian decision-making workflows.
  sources:
  - id: source_1
    license: null
    name: ACLED (Armed Conflict Location & Event Data Project)
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
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: WFP - World Food Programme
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: OCHA Regional Office for Southern and Eastern Africa (ROSEA)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_6
    license: null
    name: OCHA Financial Tracking System (FTS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-eri
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Fatalities from conflict events in Eritrea
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
    description: Affected refugees and persons of concern due to displacement and
      humanitarian crises
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
  description: 'Refugees and Persons of Concern data from HDX HAPI, please see the
    documentation for more information Source: UNHCR - The UN Refugee Agency License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/92d5b9d9-d150-4c4b-8156-eb723da52b17/resource/b8311699-2bb8-4418-b707-61b5ee817992/download/hdx_hapi_refugees_eri.csv
  format: null
  id: resource_b8311699
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Eritrea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Returnees data from HDX HAPI, please see the documentation for more
    information Source: UNHCR - The UN Refugee Agency License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/92d5b9d9-d150-4c4b-8156-eb723da52b17/resource/5e13fdd0-c88e-4dd3-8f01-2e0780dae117/download/hdx_hapi_returnees_eri.csv
  format: null
  id: resource_5e13fdd0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Returnees for Eritrea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Funding data from HDX HAPI, please see the documentation for more
    information Source: OCHA Financial Tracking System (FTS) License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/92d5b9d9-d150-4c4b-8156-eb723da52b17/resource/a94cb591-1c6f-4e79-a0ce-3e20ed080089/download/hdx_hapi_funding_eri.csv
  format: null
  id: resource_a94cb591
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Funding for Eritrea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/92d5b9d9-d150-4c4b-8156-eb723da52b17/resource/db173f5f-3cb9-4173-8532-9a900529617a/download/hdx_hapi_conflict_event_eri.csv
  format: null
  id: resource_db173f5f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Eritrea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/92d5b9d9-d150-4c4b-8156-eb723da52b17/resource/8cdc121e-0386-484e-b45d-f9288768fa73/download/hdx_hapi_national_risk_eri.csv
  format: null
  id: resource_8cdc121e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Eritrea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: OCHA Regional Office for Southern and Eastern Africa
    (ROSEA) License: Creative Commons Attribution for Intergovernmental Organisations
    (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/92d5b9d9-d150-4c4b-8156-eb723da52b17/resource/7fbf84e2-d908-4ca3-aa20-856c88743778/download/hdx_hapi_population_eri.csv
  format: null
  id: resource_7fbf84e2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Eritrea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/92d5b9d9-d150-4c4b-8156-eb723da52b17/resource/6d53f0b3-f732-44b8-b657-04d3a7bff70f/download/hdx_hapi_rainfall_eri.csv
  format: null
  id: resource_6d53f0b3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Eritrea'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/92d5b9d9-d150-4c4b-8156-eb723da52b17/resource/473a41e6-5eb3-444c-8100-5a6e8dbe0c9d/download/hdx_hapi_data_availability_eri.csv
  format: null
  id: resource_473a41e6
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Eritrea'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-eri_hdxapi_hdxhapi_1997
spatial:
  bbox: null
  centroid: null
  countries:
  - ERI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '1997-01-01'
temporal_resolution: null
title: HDX HAPI Data for Eritrea
version: null
vulnerability: null
---
