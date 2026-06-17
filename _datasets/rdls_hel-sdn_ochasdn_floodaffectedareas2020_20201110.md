---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sudan Humanitarian Aid Commission, Flood Task Force
    url: https://data.humdata.org/dataset/sudan-flood-affected-areas-2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-flood-affected-areas-2020
creator:
  affiliation: null
  email: null
  name: OCHA Sudan
  url: https://data.humdata.org/dataset/sudan-flood-affected-areas-2020
dataset_id: rdls_hel-sdn_ochasdn_floodaffectedareas2020_20201110
description: 'Sudan - Flood affected Areas 2020, Destroyed Houses completely/ partially
  and affected people and Deaths.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sudan-flood-affected-areas-2020]'
details: null
exposure:
- asset_type:
    description: Residential building stock affected by 2020 floods, classified by
      damage state
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population affected by 2020 flood event
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Post-event observational data collected by Sudan Humanitarian Aid Commission's
    Flood Task Force documenting flood-affected areas, building damage (complete and
    partial destruction), affected population counts, and fatalities from the 2020
    Sudan flood event. Data compiled from direct field observations and anecdotal
    reports at the locality level.
  sources:
  - id: source_1
    license: null
    name: Sudan Humanitarian Aid Commission, Flood Task Force
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sudan-flood-affected-areas-2020
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings completely or partially destroyed by 2020 floods
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People affected by 2020 floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
    description: Deaths caused by 2020 floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sudan - Flood Affected Areas 2020 (Excel)
  download_url: https://data.humdata.org/dataset/ecefeef1-73e8-4d26-be77-8161c9c05db5/resource/28732ce4-3100-4ebb-b353-3eb8fed9a56b/download/sudan_floods_affected_localities_10nov2020.xlsx
  format: null
  id: resource_28732ce4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sudan_Floods_Affected_Localities_10Nov2020
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-sdn_ochasdn_floodaffectedareas2020_20201110
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-11-10'
temporal_resolution: null
title: Sudan - Flood Affected Areas 2020
version: null
vulnerability: null
---
