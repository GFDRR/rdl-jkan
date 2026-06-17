---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-kir
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-kir
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-kir
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNFPA
    url: https://data.humdata.org/dataset/hdx-hapi-kir
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Oxford Poverty & Human Development Initiative
    url: https://data.humdata.org/dataset/hdx-hapi-kir
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ACLED
    url: https://data.humdata.org/dataset/hdx-hapi-kir
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-kir
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-kir
dataset_id: rdls_hel-kir_hdxapi_hdxhapi_2003
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-kir]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population by gender and age range at administrative levels
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
  type: drought
license: CC-BY-4.0
lineage:
  description: HDX HAPI aggregates standardized humanitarian indicators from multiple
    UN agencies and research organizations into a unified API. For Kiribati, rainfall
    observations are integrated with INFORM's national risk assessment model to characterize
    drought hazard exposure, while baseline population data and poverty metrics are
    combined with refugee/displacement records to quantify climate-related impacts
    and vulnerability.
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
    name: WFP - World Food Programme
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
    name: UNFPA
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_5
    license: null
    name: Oxford Poverty & Human Development Initiative
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
    license: null
    name: ACLED
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-kir
  rel: source
loss:
  losses:
  - asset_category: economic_indicator
    asset_dimension: index
    description: Affected refugees and persons of concern, potentially climate-displaced
      populations
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
    description: Poverty rates and vulnerability to poverty as indirect drought impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rfh:mm
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
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
  download_url: https://data.humdata.org/dataset/30e55df4-90bd-4a9f-b19a-70daa86ba908/resource/a6c717d0-7ca9-464d-a234-9164c8d996b4/download/hdx_hapi_refugees_kir.csv
  format: null
  id: resource_a6c717d0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Kiribati'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/30e55df4-90bd-4a9f-b19a-70daa86ba908/resource/1382a98e-8c06-4e38-9516-38894030ec4e/download/hdx_hapi_conflict_event_kir.csv
  format: null
  id: resource_1382a98e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Kiribati'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/30e55df4-90bd-4a9f-b19a-70daa86ba908/resource/2816b1e8-c82a-4c99-9f5a-ddbda58d884f/download/hdx_hapi_national_risk_kir.csv
  format: null
  id: resource_2816b1e8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Kiribati'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Poverty Rate data from HDX HAPI, please see the documentation for
    more information Source: Oxford Poverty & Human Development Initiative License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/30e55df4-90bd-4a9f-b19a-70daa86ba908/resource/9c0585e3-2e43-43f2-940e-5fd61c98aa6b/download/hdx_hapi_poverty_rate_kir.csv
  format: null
  id: resource_9c0585e3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Poverty Rate for Kiribati'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: UNFPA License: Creative Commons Attribution for Intergovernmental
    Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/30e55df4-90bd-4a9f-b19a-70daa86ba908/resource/4192526c-285d-4433-af54-ede752053fb9/download/hdx_hapi_population_kir.csv
  format: null
  id: resource_4192526c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Kiribati'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/30e55df4-90bd-4a9f-b19a-70daa86ba908/resource/c7a8550c-932e-467c-a206-42f36f480471/download/hdx_hapi_rainfall_kir.csv
  format: null
  id: resource_c7a8550c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Kiribati'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/30e55df4-90bd-4a9f-b19a-70daa86ba908/resource/c876d2ff-cd2f-472b-98f8-022787ba60d3/download/hdx_hapi_data_availability_kir.csv
  format: null
  id: resource_c876d2ff
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Kiribati'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-kir_hdxapi_hdxhapi_2003
spatial:
  bbox: null
  centroid: null
  countries:
  - KIR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2003-01-01'
temporal_resolution: null
title: HDX HAPI Data for Kiribati
version: null
vulnerability: null
---
