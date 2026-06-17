---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-mli
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-mli
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Integrated Food Security Phase Classification (IPC)
    url: https://data.humdata.org/dataset/hdx-hapi-mli
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/hdx-hapi-mli
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-mli
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-mli
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-mli
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-mli
dataset_id: rdls_hel-mli_hdxapi_hdxhapi_1997
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-mli]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population statistics for Mali at administrative levels
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
    authoritative sources including IOM displacement tracking, IPC food security classifications,
    and INFORM risk indices. Data is harmonized to common administrative boundaries
    and temporal reference periods to enable interoperability across humanitarian
    datasets for Mali.
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
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Integrated Food Security Phase Classification (IPC)
    risk_data_type:
    - loss
    type: model
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
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
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
- href: https://data.humdata.org/dataset/hdx-hapi-mli
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons due to various hazards including flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
    description: Food insecurity phase classifications indicating population affected
      by drought-related food crises
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
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/25edc35c-c4f8-4677-812c-0df1ca161dcc/download/hdx_hapi_idps_mli.csv
  format: null
  id: resource_25edc35c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Internally-Displaced Persons for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Refugees and Persons of Concern data from HDX HAPI, please see the
    documentation for more information Source: UNHCR - The UN Refugee Agency License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/51cf2867-3adc-48cf-9a36-123112589b73/download/hdx_hapi_refugees_mli.csv
  format: null
  id: resource_51cf2867
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Returnees data from HDX HAPI, please see the documentation for more
    information Source: UNHCR - The UN Refugee Agency License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/281703de-b9b0-4cfd-8b04-db9e3d732787/download/hdx_hapi_returnees_mli.csv
  format: null
  id: resource_281703de
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Returnees for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Humanitarian needs data from HDX HAPI, please see the documentation
    for more information Source: OCHA Humanitarian Programme Cycle Tools (HPC Tools)
    License: Creative Commons Attribution for Intergovernmental Organisations (CC
    BY-IGO)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/a39d238a-2ab5-4053-a585-a82d836413d7/download/hdx_hapi_humanitarian_needs_mli.csv
  format: null
  id: resource_a39d238a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Humanitarian Needs for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Operational Presence data from HDX HAPI, please see the documentation
    for more information Source: OCHA Mali License: Creative Commons Attribution for
    Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/e4dbde74-5363-4cc6-9f27-81f76af0140c/download/hdx_hapi_operational_presence_mli.csv
  format: null
  id: resource_e4dbde74
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Operational Presence for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Funding data from HDX HAPI, please see the documentation for more
    information Source: OCHA Financial Tracking System (FTS) License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/877f9bcb-7713-4fb3-8813-c15554c67154/download/hdx_hapi_funding_mli.csv
  format: null
  id: resource_877f9bcb
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Funding for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/acfbc8e8-102c-48e8-9638-c025e44d05d4/download/hdx_hapi_conflict_event_mli.csv
  format: null
  id: resource_acfbc8e8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/023d5200-1881-4303-a2fd-26cb57c5600e/download/hdx_hapi_national_risk_mli.csv
  format: null
  id: resource_023d5200
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Security data from HDX HAPI, please see the documentation for
    more information Source: Integrated Food Security Phase Classification (IPC) License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/981ebb34-f958-405e-87f6-e5273cfc8d66/download/hdx_hapi_food_security_mli.csv
  format: null
  id: resource_981ebb34
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Security for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Prices & Market Monitor data from HDX HAPI, please see the documentation
    for more information Source: WFP - World Food Programme License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/47806e1b-8863-4243-a00b-ebd6665a2c16/download/hdx_hapi_food_price_mli.csv
  format: null
  id: resource_47806e1b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Prices & Market Monitor for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Poverty Rate data from HDX HAPI, please see the documentation for
    more information Source: Oxford Poverty & Human Development Initiative License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/64d44092-4b65-47c7-9daa-0ad964fafaa8/download/hdx_hapi_poverty_rate_mli.csv
  format: null
  id: resource_64d44092
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Poverty Rate for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: OCHA Mali License: Creative Commons Attribution for
    Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/4e7a0656-7d96-465f-bbf8-d4ce51780f65/download/hdx_hapi_population_mli.csv
  format: null
  id: resource_4e7a0656
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/450d5321-1538-4357-9543-e6eee30153b5/download/hdx_hapi_rainfall_mli.csv
  format: null
  id: resource_450d5321
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Mali'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/6c093977-569e-47b5-a91f-018ce3089fa5/resource/7b92d097-04fc-49d4-b15c-5ac1056926bd/download/hdx_hapi_data_availability_mli.csv
  format: null
  id: resource_7b92d097
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Mali'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mli_hdxapi_hdxhapi_1997
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2028-12-31'
  start: '1997-01-01'
temporal_resolution: null
title: HDX HAPI Data for Mali
version: null
vulnerability: null
---
