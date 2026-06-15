---
attributions:
- entity:
    affiliation: null
    email: null
    name: Information Management Working Group
    url: https://data.humdata.org/dataset/moz-idai-sitreps
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/moz-idai-sitreps
creator:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/moz-idai-sitreps
dataset_id: rdls_lss-moz_ochamoz_cycloneidaikeyfiguressitu_20190412
description: 'This dataset contains key figures and other data pertaining to the evolving
  humanitarian situation in during the Tropical Cyclone Idai response in Mozambique..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/moz-idai-sitreps]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Situation reports and key figures from the Information Management Working
    Group documenting post-event impacts of Tropical Cyclone Idai in Mozambique. Data
    compiled from direct observations and anecdotal reports during the humanitarian
    response, aggregating casualty, displacement, and damage figures across affected
    areas.
  sources:
  - id: source_1
    license: null
    name: Information Management Working Group
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/moz-idai-sitreps
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by Tropical Cyclone Idai in Mozambique
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
  - asset_category: buildings
    asset_dimension: structure
    description: Building damage from Tropical Cyclone Idai
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: 'Mozambique: Cyclone Idai Key Figures and Situation Reports Data (Tropical
    Cyclone Idai response situation report data)'
  download_url: https://docs.google.com/spreadsheets/d/1o99KTZke1sAGwCC2QOPHfDdaGSNarycUeH7mnJvTQqI/export?format=xlsx
  format: null
  id: resource_97d04e88
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ Idai Sitreps
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_ochamoz_cycloneidaikeyfiguressitu_20190412
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-04-12'
temporal_resolution: null
title: 'Mozambique: Cyclone Idai Key Figures and Situation Reports Data'
version: null
vulnerability: null
---
