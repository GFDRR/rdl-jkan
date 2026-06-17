---
attributions:
- entity:
    affiliation: null
    email: null
    name: INFORM
    url: https://data.humdata.org/dataset/hdx-hapi-alb
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-alb
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNFPA
    url: https://data.humdata.org/dataset/hdx-hapi-alb
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-alb
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-alb
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Oxford Poverty & Human Development Initiative
    url: https://data.humdata.org/dataset/hdx-hapi-alb
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-alb
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-alb
dataset_id: rdls_hel-alb_hdxapi_hdxhapi_2001
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-alb]'
details: HDX HAPI is refreshed daily, but the source datasets may have different update
  schedules. Please refer to the source datasets for each subcategory to verify their
  specific update frequency.
exposure:
- asset_type:
    description: Baseline population distribution across Albania by location and administrative
      divisions
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
    UN agencies and research organizations (ACLED, INFORM, UNFPA, UNHCR, WFP, Oxford
    PHDI) into a unified registry for Albania. Source data are collected through administrative
    reporting, conflict event monitoring, and poverty surveys, then harmonized into
    common indicators with consistent spatial and temporal references to support humanitarian
    decision-making workflows.
  sources:
  - id: source_1
    license: null
    name: INFORM
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
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
    name: UNFPA
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
  - id: source_6
    license: null
    name: Oxford Poverty & Human Development Initiative
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-alb
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from conflict events in Albania
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
          quantity_kind: count
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
  download_url: https://data.humdata.org/dataset/f3fb71c4-1484-4c9d-a337-532336813ce5/resource/9a54abf1-04cc-4b0b-9eec-de507e6d8735/download/hdx_hapi_refugees_alb.csv
  format: null
  id: resource_9a54abf1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Albania'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Returnees data from HDX HAPI, please see the documentation for more
    information Source: UNHCR - The UN Refugee Agency License: Creative Commons Attribution
    for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/f3fb71c4-1484-4c9d-a337-532336813ce5/resource/9882696b-228e-421f-8aa9-deb1d78fe62d/download/hdx_hapi_returnees_alb.csv
  format: null
  id: resource_9882696b
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Returnees for Albania'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/f3fb71c4-1484-4c9d-a337-532336813ce5/resource/cf56bc00-bb50-4f2d-963f-0b6c4ac23208/download/hdx_hapi_conflict_event_alb.csv
  format: null
  id: resource_cf56bc00
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Albania'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'National Risk data from HDX HAPI, please see the documentation for
    more information Source: INFORM License: Creative Commons Attribution International
    (CC BY)'
  download_url: https://data.humdata.org/dataset/f3fb71c4-1484-4c9d-a337-532336813ce5/resource/b1bbcd32-477f-4ba4-9fff-1be4ab10e806/download/hdx_hapi_national_risk_alb.csv
  format: null
  id: resource_b1bbcd32
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: National Risk for Albania'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Poverty Rate data from HDX HAPI, please see the documentation for
    more information Source: Oxford Poverty & Human Development Initiative License:
    Public Domain / No restrictions (CC0)'
  download_url: https://data.humdata.org/dataset/f3fb71c4-1484-4c9d-a337-532336813ce5/resource/8b56923a-ed67-47ae-a11a-27e3a71a201d/download/hdx_hapi_poverty_rate_alb.csv
  format: null
  id: resource_8b56923a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Food Security, Nutrition & Poverty: Poverty Rate for Albania'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: UNFPA License: Creative Commons Attribution for Intergovernmental
    Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/f3fb71c4-1484-4c9d-a337-532336813ce5/resource/9d9b25b8-a07f-4347-bd82-4f71a1055aae/download/hdx_hapi_population_alb.csv
  format: null
  id: resource_9d9b25b8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Albania'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/f3fb71c4-1484-4c9d-a337-532336813ce5/resource/aaf46c5d-810a-487e-8617-11d3851c5d59/download/hdx_hapi_rainfall_alb.csv
  format: null
  id: resource_aaf46c5d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Albania'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/f3fb71c4-1484-4c9d-a337-532336813ce5/resource/68887e93-7efd-4fba-aaf8-a5051427c488/download/hdx_hapi_data_availability_alb.csv
  format: null
  id: resource_68887e93
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Albania'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-alb_hdxapi_hdxhapi_2001
spatial:
  bbox: null
  centroid: null
  countries:
  - ALB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2001-01-01'
temporal_resolution: null
title: HDX HAPI Data for Albania
version: null
vulnerability: null
---
