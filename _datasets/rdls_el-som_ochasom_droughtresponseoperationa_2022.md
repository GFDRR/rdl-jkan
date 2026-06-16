---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Partners
    url: https://data.humdata.org/dataset/somalia-drought-response-operationalpresence2022
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-drought-response-operationalpresence2022
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-drought-response-operationalpresence2022
dataset_id: rdls_el-som_ochasom_droughtresponseoperationa_2022
description: 'This dataset organizes data on operational presence and response around
  the drought crisis in Somalia.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-drought-response-operationalpresence2022]'
details: This dataset is created to present together drought related datasets.
exposure:
- asset_type:
    description: Population in need (PIN) and internally displaced persons (IDPs)
      affected by drought in Somalia
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
  description: This dataset aggregates operational and impact data from multiple humanitarian
    partners responding to the Somalia drought crisis. Data sources include population
    assessments, IPC food insecurity classifications (October-December 2022 projections),
    and humanitarian access severity ratings, compiled into a registry format to support
    operational coordination and response prioritization.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-drought-response-operationalpresence2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by drought crisis in Somalia, including IPC5
      food insecurity classifications
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
- access_url: https://data.humdata.org/dataset/ocha-somalia-population-idp-pin-operational-priority-areas-access-ipc5
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Drought related data: Population, IDPs, Affected Population, Priority
    Areas, IPC 5 (Oct - Dec 2022 projection), Severity of Access'
  download_url: null
  format: null
  id: resource_ba355403
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Population, IDPs, PIN, Priority Areas, IPC5 (Oct-Dec 2022 proj.), Severity
    of Access
- access_url: https://data.humdata.org/dataset/ocha-somalia-drought-response-2022
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Drought Response and Operational Presence (Response to the
    drought crisis in Somalia)
  download_url: null
  format: null
  id: resource_9c49551b
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Drought Response
- access_url: https://data.humdata.org/dataset/ocha-somalia-operational-presence-2022
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia Drought Response and Operational Presence (Operational presence
    in Somalia for the drought crisis)
  download_url: null
  format: null
  id: resource_57cfa4da
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Operational Presence
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-som_ochasom_droughtresponseoperationa_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-11-30'
  start: '2022-01-01'
temporal_resolution: null
title: Somalia Drought Response and Operational Presence
version: null
vulnerability: null
---
