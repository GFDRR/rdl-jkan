---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-mex
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-mex
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-mex
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-mex
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNFPA
    url: https://data.humdata.org/dataset/hdx-hapi-mex
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Oxford Poverty & Human Development Initiative
    url: https://data.humdata.org/dataset/hdx-hapi-mex
  id: attribution_6
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Financial Tracking System (FTS)
    url: https://data.humdata.org/dataset/hdx-hapi-mex
  id: attribution_7
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-mex
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-mex
dataset_id: rdls_hel-mex_hdxapi_hdxhapi_2001
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-mex]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population counts by location and demographic characteristics
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
      intensity_measure: rfh:mm
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    UN agencies and research organizations including INFORM risk indices, ACLED conflict
    data, UNHCR refugee statistics, and WFP food security assessments. Data is processed
    through the HDX HAPI platform to provide harmonized baseline population, hazard
    exposure, conflict impacts, and affected population counts at national and sub-national
    scales for Mexico.
  sources:
  - id: source_1
    license: null
    name: INFORM
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
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
    name: UNFPA
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
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
    name: OCHA Financial Tracking System (FTS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-mex
  rel: source
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: index
    description: Affected population counts including refugees, persons of concern,
      and returnees
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rfh:mm
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: economic_indicator
    asset_dimension: index
    description: Fatalities from conflict events in Mexico
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: rfh:mm
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: death
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
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/e470ac5c-b30e-4127-a26d-c7d941512c7f/download/hdx_hapi_refugees_mex.csv
  format: null
  id: resource_e470ac5c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Mexico'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Returnees data from HDX HAPI, please see the documentation for more
    information Source: UNHCR - The UN Refugee Agency License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/eca56cf3-ba67-4395-a525-65c6cd6f7c35/download/hdx_hapi_returnees_mex.csv
  format: null
  id: resource_eca56cf3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Returnees for Mexico'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Funding data from HDX HAPI, please see the documentation for more
    information Source: OCHA Financial Tracking System (FTS) License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/15b84d53-25ca-4933-9006-6ee669f6c95c/download/hdx_hapi_funding_mex.csv
  format: null
  id: resource_15b84d53
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Funding for Mexico'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/376ae117-3673-4a6c-b53b-66c8742947b9/download/hdx_hapi_conflict_event_mex.csv
  format: null
  id: resource_376ae117
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Mexico'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/4c182b4e-0364-4ce3-a65a-b1971281043d/download/hdx_hapi_national_risk_mex.csv
  format: null
  id: resource_4c182b4e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Mexico'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Food Prices & Market Monitor data from HDX HAPI, please see the documentation
    for more information Source: WFP - World Food Programme License: Creative Commons
    Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/a3cb4424-e0eb-4bae-a2dc-97ce4a0c2f17/download/hdx_hapi_food_price_mex.csv
  format: null
  id: resource_a3cb4424
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Food Prices & Market Monitor for Mexico'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Poverty Rate data from HDX HAPI, please see the documentation for
    more information Source: Oxford Poverty & Human Development Initiative License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/8f610ae3-5166-4e5f-8416-e4e92815bd1c/download/hdx_hapi_poverty_rate_mex.csv
  format: null
  id: resource_8f610ae3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Poverty Rate for Mexico'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: UNFPA License: Creative Commons Attribution for Intergovernmental
    Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/96bf4e3e-a9cd-4d47-ba1f-430a46cde539/download/hdx_hapi_population_mex.csv
  format: null
  id: resource_96bf4e3e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Mexico'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/8d337267-4ba5-4813-b76e-4548bcc9a633/download/hdx_hapi_rainfall_mex.csv
  format: null
  id: resource_8d337267
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Mexico'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/c218a4ff-a0a5-4df3-ac7e-1d7aa0a2a96e/resource/37fef7e3-68da-49eb-884e-25a804420fff/download/hdx_hapi_data_availability_mex.csv
  format: null
  id: resource_37fef7e3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Mexico'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mex_hdxapi_hdxhapi_2001
spatial:
  bbox: null
  centroid: null
  countries:
  - MEX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2028-12-31'
  start: '2001-01-01'
temporal_resolution: null
title: HDX HAPI Data for Mexico
version: null
vulnerability: null
---
