---
attributions:
- entity:
    affiliation: null
    email: null
    name: Palestinian Central Bureau of Statistics (PCBS)
    url: https://data.humdata.org/dataset/the-state-of-palestine-escalation-of-hostilities
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Palestinian Ministry of Health
    url: https://data.humdata.org/dataset/the-state-of-palestine-escalation-of-hostilities
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Palestinian Central Bureau of Statistics
  url: https://data.humdata.org/dataset/the-state-of-palestine-escalation-of-hostilities
creator:
  affiliation: null
  email: null
  name: Palestinian Central Bureau of Statistics
  url: https://data.humdata.org/dataset/the-state-of-palestine-escalation-of-hostilities
dataset_id: rdls_lss-pse_pcbs_stateimpactescalationhost_2023
description: 'This dataset shows key figures from the escalation of hostilities since
  7 October 2023.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/the-state-of-palestine-escalation-of-hostilities]'
details: PCBS will update the figures once it is received from different data sources.
  The data discrepancies between PCBS and Shireen website is due to the date and time
  of update.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Impact data compiled from official Palestinian Central Bureau of Statistics
    registry and Palestinian Ministry of Health records documenting key figures (affected
    population, casualties, injuries, displacement) resulting from the escalation
    of hostilities since 7 October 2023.
  sources:
  - id: source_1
    license: null
    name: Palestinian Central Bureau of Statistics (PCBS)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Palestinian Ministry of Health
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/the-state-of-palestine-escalation-of-hostilities
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Affected population from conflict-related hostilities escalation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from conflict-related hostilities escalation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
    description: Injured persons from conflict-related hostilities escalation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  - asset_category: population
    asset_dimension: population
    description: Displaced population from conflict-related hostilities escalation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_4
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'State of Palestine: Impact of the Escalation of Hostilities (Spreadsheet
    showing figures of the impact of hostilities.)'
  download_url: https://data.humdata.org/dataset/a02d750c-b2f7-4e22-b884-e9e495209a3a/resource/429619ed-8b50-4a01-a2b3-88601bc606ce/download/opt_-escalation-of-hostilities-impact.xlsx
  format: null
  id: resource_429619ed
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: opt_-escalation-of-hostilities-impact.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-pse_pcbs_stateimpactescalationhost_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-31'
  start: '2023-10-07'
temporal_resolution: null
title: 'State of Palestine: Impact of the Escalation of Hostilities'
version: null
vulnerability: null
---
