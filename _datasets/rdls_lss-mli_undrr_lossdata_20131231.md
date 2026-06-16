---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNISDR
    url: https://data.humdata.org/dataset/climate-change-impact-in-mali
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Mali Government Agencies
    url: https://data.humdata.org/dataset/climate-change-impact-in-mali
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/climate-change-impact-in-mali
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/climate-change-impact-in-mali
dataset_id: rdls_lss-mli_undrr_lossdata_20131231
description: 'Number of Deaths, Injured, Missing, Houses Destroyed, Houses Damaged,
  Victims Affected, Relocated, Evacuated, Losses and Damages in crops by climate change
  event. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/climate-change-impact-in-mali]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event disaster loss data compiled from Mali Government Agencies
    and UNISDR documenting direct impacts from climate change events including fatalities,
    injuries, housing damage, displacement, and crop losses. Data collected through
    direct observation and anecdotal reporting mechanisms at the national level.
  sources:
  - id: source_1
    license: null
    name: UNISDR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Mali Government Agencies
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/climate-change-impact-in-mali
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct crop losses and damages from climate change events (drought)
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
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Houses destroyed and damaged from climate change events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
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
    description: Deaths from climate change events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Injured persons from climate change events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Victims affected by climate change events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_5
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
    description: Persons relocated and evacuated from climate change events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_6
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
  description: Number of Deaths, Injured, Missing, Houses Destroyed, Houses Damaged,
    Victims Affected, Relocated, Evacuated, Losses and Damages in crops by climate
    change event
  download_url: https://data.humdata.org/dataset/19ed73b5-9f91-4568-a0f3-48b7fa8c1796/resource/b9e494bf-b6e6-4777-8745-9d55d86744f9/download/mali.xlsx
  format: null
  id: resource_b9e494bf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mali.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster Loss Data for Mali (Shapefile)
  download_url: https://data.humdata.org/dataset/19ed73b5-9f91-4568-a0f3-48b7fa8c1796/resource/2aac7c1d-8d30-41e1-b6d3-42a8cbcb0594/download/mali.zip
  format: null
  id: resource_2aac7c1d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Mali.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_undrr_lossdata_20131231
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2013-12-31'
temporal_resolution: null
title: Disaster Loss Data for Mali
version: null
vulnerability: null
---
