---
attributions:
- entity:
    affiliation: null
    email: null
    name: Census 2000
    url: https://data.humdata.org/dataset/typhoon-maysak-response-priority-index
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Census 2010
    url: https://data.humdata.org/dataset/typhoon-maysak-response-priority-index
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UCL
    url: https://data.humdata.org/dataset/typhoon-maysak-response-priority-index
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/typhoon-maysak-response-priority-index
creator:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/typhoon-maysak-response-priority-index
dataset_id: rdls_hel-fsmphl_brc_typhoonmaysakresponseprio_20150408
description: 'A priority index created for use in the response to Typhoon Maysak using
  a combination of pre-disaster and disaster data. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/typhoon-maysak-response-priority-index]'
details: null
exposure:
- asset_type:
    description: Residential population distribution from Census 2000 and 2010 data
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Pre-disaster population exposure data from Census 2000 and 2010 were
    combined with observed Typhoon Maysak event data and UCL analysis to create a
    composite priority index for humanitarian response allocation, integrating baseline
    vulnerability with event-specific impact assessment.
  sources:
  - id: source_1
    license: null
    name: Census 2000
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Census 2010
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: UCL
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/typhoon-maysak-response-priority-index
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Typhoon Maysak used to prioritize response
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Micronesia, Philippines - Typhoon Maysak Response Priority Index (Excel)
  download_url: https://data.humdata.org/dataset/ba4f8543-3639-4a2b-9271-6f07f9954462/resource/14fe9ef4-a0dd-4fc9-88b1-928a6169ba60/download/typhoon-maysak-priority-index-v2.xlsx
  format: null
  id: resource_14fe9ef4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Typhoon_Maysak_priority_index_v2.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-fsmphl_brc_typhoonmaysakresponseprio_20150408
spatial:
  bbox: null
  centroid: null
  countries:
  - FSM
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-04-08'
temporal_resolution: null
title: Micronesia, Philippines - Typhoon Maysak Response Priority Index
version: null
vulnerability: null
---
