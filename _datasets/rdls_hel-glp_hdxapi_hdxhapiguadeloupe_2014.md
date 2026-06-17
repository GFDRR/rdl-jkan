---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-glp
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Latin America and the Caribbean (ROLAC)
    url: https://data.humdata.org/dataset/hdx-hapi-glp
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNHCR - The UN Refugee Agency
    url: https://data.humdata.org/dataset/hdx-hapi-glp
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WFP - World Food Programme
    url: https://data.humdata.org/dataset/hdx-hapi-glp
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-glp
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-glp
dataset_id: rdls_hel-glp_hdxapi_hdxhapiguadeloupe_2014
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-glp]'
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
- asset_type:
    description: Agricultural exposure inferred from rainfall anomaly monitoring across
      spatial pixels
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      intensity_measure: rainfall:mm
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
    UN and research organizations (ACLED, UNHCR, WFP, OCHA) into a unified API. Data
    includes observed rainfall measurements with anomaly calculations, baseline population
    counts by demographics, conflict event records with fatalities, and refugee statistics.
    The dataset integrates these sources through common administrative location codes
    and reference periods to enable interoperable humanitarian decision-making workflows.
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
    name: OCHA Latin America and the Caribbean (ROLAC)
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
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-glp
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct fatalities from conflict events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rainfall:mm
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
    description: Affected population from conflict events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rainfall:mm
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
  - asset_category: population
    asset_dimension: population
    description: Refugee and persons of concern populations affected by drought and
      climate stress
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: rainfall:mm
      process: null
      trigger: null
      type: drought
    id: loss_3
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
  download_url: https://data.humdata.org/dataset/fd281c81-75e4-48cd-8e52-a5bd841333d5/resource/8fe1fcb2-6db1-4c12-83da-cd5a6bcfcbb6/download/hdx_hapi_refugees_glp.csv
  format: null
  id: resource_8fe1fcb2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Affected People: Refugees & Persons of Concern for Guadeloupe'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/fd281c81-75e4-48cd-8e52-a5bd841333d5/resource/a18ba28e-d7b5-401f-9a9d-6949fd91a866/download/hdx_hapi_conflict_event_glp.csv
  format: null
  id: resource_a18ba28e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Coordination & Context: Conflict Events for Guadeloupe'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: OCHA Latin America and the Caribbean (ROLAC) License:
    Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)'
  download_url: https://data.humdata.org/dataset/fd281c81-75e4-48cd-8e52-a5bd841333d5/resource/d0251dc9-5684-4e65-a014-dbab16880397/download/hdx_hapi_population_glp.csv
  format: null
  id: resource_d0251dc9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Geography & Infrastructure: Baseline Population for Guadeloupe'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Rainfall data from HDX HAPI, please see the documentation for more
    information Source: WFP - World Food Programme License: Creative Commons Attribution
    International (CC BY)'
  download_url: https://data.humdata.org/dataset/fd281c81-75e4-48cd-8e52-a5bd841333d5/resource/f8fa91e9-1e44-4c61-87c6-1ad37f2e2903/download/hdx_hapi_rainfall_glp.csv
  format: null
  id: resource_f8fa91e9
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Climate: Rainfall for Guadeloupe'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/fd281c81-75e4-48cd-8e52-a5bd841333d5/resource/13fe7cbe-ff9d-4e3f-bee7-a174fb04dea3/download/hdx_hapi_data_availability_glp.csv
  format: null
  id: resource_13fe7cbe
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'Metadata: Data Availability for Guadeloupe'
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-glp_hdxapi_hdxhapiguadeloupe_2014
spatial:
  bbox: null
  centroid: null
  countries:
  - GLP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2014-01-01'
temporal_resolution: null
title: HDX HAPI Data for Guadeloupe
version: null
vulnerability: null
---
