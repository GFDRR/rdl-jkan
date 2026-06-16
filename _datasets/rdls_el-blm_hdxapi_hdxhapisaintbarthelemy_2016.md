---
attributions:
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Location & Event Data Project (ACLED)
    url: https://data.humdata.org/dataset/hdx-hapi-blm
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Latin America and the Caribbean (ROLAC)
    url: https://data.humdata.org/dataset/hdx-hapi-blm
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-blm
creator:
  affiliation: null
  email: null
  name: HDX Humanitarian API Data
  url: https://data.humdata.org/dataset/hdx-hapi-blm
dataset_id: rdls_el-blm_hdxapi_hdxhapisaintbarthelemy_2016
description: 'This dataset contains data obtained from the HDX Humanitarian API (HDX
  HAPI), which provides standardized humanitarian indicators designed for seamless
  interoperability from multiple sources. The data facilitates automated workflows
  and visualizations to support humanitarian decision making. For more information,
  please see the HDX HAPI landing page and documentation .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/hdx-hapi-blm]'
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
hazard: null
license: CC-BY-4.0
lineage:
  description: The HDX HAPI aggregates standardized humanitarian indicators from multiple
    authoritative sources (ACLED for conflict events, OCHA ROLAC for population baselines)
    and provides them through a unified API interface. Data is organized by administrative
    level with reference periods and includes conflict-related fatalities and baseline
    population demographics to support humanitarian decision-making.
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
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hdx-hapi-blm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Fatalities from conflict and violence events
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
  description: 'Conflict Event data from HDX HAPI, please see the documentation for
    more information Source: Armed Conflict Location & Event Data Project (ACLED)
    License: By using ACLED data you agree to abide by the Terms of Use and Attribution
    Policy .'
  download_url: https://data.humdata.org/dataset/561d2c98-aa5b-4d33-8468-45ca6516ed04/resource/6d49267d-73ad-4c6d-9068-520fd583fdf9/download/hdx_hapi_conflict_event_blm.csv
  format: null
  id: resource_6d49267d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Coordination & Context: Conflict Events for Saint Barth\xE9lemy"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Baseline Population data from HDX HAPI, please see the documentation
    for more information Source: OCHA Latin America and the Caribbean (ROLAC) License:
    humanitarian use only'
  download_url: https://data.humdata.org/dataset/561d2c98-aa5b-4d33-8468-45ca6516ed04/resource/509821fc-8d66-4ca4-a8bc-15a9e07d4100/download/hdx_hapi_population_blm.csv
  format: null
  id: resource_509821fc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Geography & Infrastructure: Baseline Population for Saint Barth\xE9lemy"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Data Availability Data from HDX HAPI. Each row in this resource represents
    an administrative division for which data is available, by subcategory. Please
    see the documentation for more information Source: HDX HAPI License: Creative
    Commons Attribution for Intergovernmental Organisations'
  download_url: https://data.humdata.org/dataset/561d2c98-aa5b-4d33-8468-45ca6516ed04/resource/5dfb7859-06d8-415d-bf47-985b1f6b62f5/download/hdx_hapi_data_availability_blm.csv
  format: null
  id: resource_5dfb7859
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Metadata: Data Availability for Saint Barth\xE9lemy"
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-blm_hdxapi_hdxhapisaintbarthelemy_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - BLM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2016-01-01'
temporal_resolution: null
title: "HDX HAPI Data for Saint Barth\xE9lemy"
version: null
vulnerability: null
---
