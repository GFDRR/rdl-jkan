---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ministry of Home Affairs, Nepal
    url: https://data.humdata.org/dataset/official-figures-for-casualties-and-damage
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Nepali Police
    url: https://data.humdata.org/dataset/official-figures-for-casualties-and-damage
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Nepal (inactive)
  url: https://data.humdata.org/dataset/official-figures-for-casualties-and-damage
creator:
  affiliation: null
  email: null
  name: OCHA Nepal (inactive)
  url: https://data.humdata.org/dataset/official-figures-for-casualties-and-damage
dataset_id: rdls_lss-npl_ochanpl_officialfigurescasualties_20150605
description: 'Contains frequently updated figures for deaths, injuries, and damaged
  government and public buildings, by district.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/official-figures-for-casualties-and-damage]'
details: Check for updates. Data will be updated as figures become available.
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Post-event impact data compiled from official reports by Nepal's Ministry
    of Home Affairs and Nepali Police, aggregating deaths, injuries, and building
    damage assessments by district following an earthquake event. Data is frequently
    updated as assessments progress.
  sources:
  - id: source_1
    license: null
    name: Ministry of Home Affairs, Nepal
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Nepali Police
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/official-figures-for-casualties-and-damage
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake affecting government and public
      buildings by district
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Earthquake-related deaths by district
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
    description: Earthquake-related injuries by district
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
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
  description: 'Nepal: Official figures for casualties and damage (MoHA/NEOC Official
    Figures)'
  download_url: https://docs.google.com/spreadsheets/d/1MCsMtcfN8jwGg4qdzYZCKyxpYp8cdqRSrEpF1WpR6ZE/edit#gid=1367273225
  format: Google Sheet
  id: resource_af078993
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MoHA/NEOC Official Figures
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_ochanpl_officialfigurescasualties_20150605
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
  start: '2015-06-05'
temporal_resolution: null
title: 'Nepal: Official figures for casualties and damage'
version: null
vulnerability: null
---
