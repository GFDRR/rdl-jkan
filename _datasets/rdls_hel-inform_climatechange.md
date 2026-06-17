---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-climate-change
creator:
  affiliation: null
  email: null
  name: INFORM
  url: https://data.humdata.org/dataset/inform-climate-change
dataset_id: rdls_hel-inform_climatechange
description: 'INFORM Climate Change analyses how the risk of humanitarian crises will
  change as a result of climate change under different emission and population scenarios..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/inform-climate-change]'
details: null
exposure:
- asset_type:
    description: Population exposed to changing climate hazards under future scenarios
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
    description: Agricultural land and livelihoods vulnerable to climate change impacts
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
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
  description: INFORM Climate Change integrates climate projections, population scenarios,
    and socioeconomic vulnerability indicators to model future humanitarian crisis
    risk under different emission pathways. The composite indicator combines hazard
    exposure and vulnerability dimensions to produce forward-looking risk assessments
    at global scale.
  sources:
  - id: source_1
    license: null
    name: INFORM
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-climate-change
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Humanitarian crisis risk to population from climate-driven drought
      and resource scarcity
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
        metric: exposure
        modelling: simulated
        type: indirect
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Climate Change (INFORM CC Brochure data.xlsx)
  download_url: https://data.humdata.org/dataset/10900f21-fd42-489a-a1e2-be1d066bce44/resource/1ffdeab7-4901-477e-a821-a198b53e4c15/download/inform-cc-brochure-data.xlsx
  format: null
  id: resource_1ffdeab7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM CC Brochure data.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: INFORM Climate Change Brochure.pdf
  download_url: https://data.humdata.org/dataset/10900f21-fd42-489a-a1e2-be1d066bce44/resource/7b54062c-05ea-425d-8e07-929efb82195e/download/inform-climate-change-brochure-4.pdf
  format: null
  id: resource_7b54062c
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM Climate Change Brochure.pdf
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-inform_climatechange
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: INFORM Climate Change
version: null
vulnerability: null
---
