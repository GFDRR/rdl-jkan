---
attributions:
- entity:
    affiliation: null
    email: null
    name: GDACS
    url: https://data.humdata.org/dataset/population-affected-in-the-nepal-earthquake-estimate
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: USGS
    url: https://data.humdata.org/dataset/population-affected-in-the-nepal-earthquake-estimate
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Nepal (inactive)
  url: https://data.humdata.org/dataset/population-affected-in-the-nepal-earthquake-estimate
creator:
  affiliation: null
  email: null
  name: OCHA Nepal (inactive)
  url: https://data.humdata.org/dataset/population-affected-in-the-nepal-earthquake-estimate
dataset_id: rdls_hel-npl_ochanpl_populationaffectedearthqu_20150425
description: 'Population affected as calculated by GDACS .. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/population-affected-in-the-nepal-earthquake-estimate]'
details: null
exposure:
- asset_type:
    description: Population distribution derived from population density data overlaid
      with earthquake shake map
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
  - analysis_type: deterministic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: USGS shake map data from the Nepal earthquake event was overlaid with
    population density data through the GDACS automatic calculation system to estimate
    the total population affected by ground shaking, producing a deterministic post-event
    impact assessment.
  sources:
  - id: source_1
    license: null
    name: GDACS
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: USGS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/population-affected-in-the-nepal-earthquake-estimate
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking calculated from
      shake map and population density
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: Population Affected in the Nepal Earthquake (Estimate) (Population
    Affected (estimate).csv)
  download_url: https://data.humdata.org/dataset/0c8f38b4-6d30-42e3-bc27-6a5a5cf7c505/resource/73e3b456-e0fb-4e98-afe5-f7c61dd151d8/download/population-affected-estimate.csv
  format: null
  id: resource_73e3b456
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Population Affected (estimate).csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_ochanpl_populationaffectedearthqu_20150425
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-04-25'
temporal_resolution: null
title: Population Affected in the Nepal Earthquake (Estimate)
version: null
vulnerability: null
---
