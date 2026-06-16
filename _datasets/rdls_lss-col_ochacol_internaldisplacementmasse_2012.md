---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/massdisplacementcolombia
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/massdisplacementcolombia
dataset_id: rdls_lss-col_ochacol_internaldisplacementmasse_2012
description: 'Afectados y eventos de desplazamientos Masivos 2012-2019. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/massdisplacementcolombia]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Registry-based compilation of internally displaced persons (IDPs) and
    mass displacement events in Colombia spanning 2012-2019. Data aggregates reported
    displacement incidents and affected population counts from humanitarian monitoring,
    providing post-event impact records of population displacement across multiple
    hazard types.
  sources:
  - id: source_1
    license: null
    name: OCHA Colombia
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/massdisplacementcolombia
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internal displacement of populations from mass events (convective
      storms, floods, and other hazards)
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
  description: Colombia - Internal displacement in mass events 2012-2019 (People-IDPs
    and events) - Afectados y eventos de desplazamientos Masivos 2012-2019 (Afectados
    y eventos de desplazamientos Masivos 2012-2019)
  download_url: https://docs.google.com/spreadsheets/d/19561PHl7VHCJ91_2J5eU_e2RbazFT0OcNf2BYCZ6_Vg/edit#gid=0
  format: null
  id: resource_09f4074b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Afectados y eventos de desplazamientos Masivos 2012-2019
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_internaldisplacementmasse_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-06-30'
  start: '2012-01-01'
temporal_resolution: null
title: Colombia - Internal displacement in mass events 2012-2019 (People-IDPs and
  events) - Afectados y eventos de desplazamientos Masivos 2012-2019
version: null
vulnerability: null
---
