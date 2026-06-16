---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNISDR
    url: https://data.humdata.org/dataset/climate-change-impact-in-togo
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Togo Government Agencies
    url: https://data.humdata.org/dataset/climate-change-impact-in-togo
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/climate-change-impact-in-togo
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/climate-change-impact-in-togo
dataset_id: rdls_lss-tgo_undrr_lossdata_20131231
description: 'Number of Deaths, Injured, Missing, Houses Destroyed, Houses Damaged,
  Victims Affected, Relocated, Evacuated, Losses and Damages in crops by climate change
  event. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/climate-change-impact-in-togo]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event disaster loss data compiled from UNISDR and Togo Government
    Agencies through direct observational and anecdotal reporting. The dataset aggregates
    recorded impacts from climate-related hazard events including deaths, injuries,
    displacement, building damage, and crop losses across Togo at the national scale.
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
    name: Togo Government Agencies
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/climate-change-impact-in-togo
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flood events in Togo
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
  - asset_category: buildings
    asset_dimension: structure
    description: Houses destroyed by flood events in Togo
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Deaths from flood events in Togo
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
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Injured persons from flood events in Togo
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
    description: Displaced and evacuated persons from flood events in Togo
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_5
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
  - asset_category: agriculture
    asset_dimension: product
    description: Crop losses and damages from drought events in Togo
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
          quantity_kind: area
          unit: null
        metric: loss
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
  download_url: https://data.humdata.org/dataset/463af9ac-a311-4d10-9ab9-cdb0ef4ed22a/resource/2d0ac135-1e71-4d2d-a2b5-e025406a5c08/download/togo.xlsx
  format: null
  id: resource_2d0ac135
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Togo.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Disaster Loss Data for Togo (Shapefile)
  download_url: https://data.humdata.org/dataset/463af9ac-a311-4d10-9ab9-cdb0ef4ed22a/resource/d6b85b8c-0b19-45e8-a6d8-9133b33c9be0/download/togo.zip
  format: null
  id: resource_d6b85b8c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Togo.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tgo_undrr_lossdata_20131231
spatial:
  bbox: null
  centroid: null
  countries:
  - TGO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2013-12-31'
temporal_resolution: null
title: Disaster Loss Data for Togo
version: null
vulnerability: null
---
