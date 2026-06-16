---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-global-trends-forced-displacement-in-2021-data
creator:
  affiliation: null
  email: null
  name: UNHCR - The UN Refugee Agency
  url: https://data.humdata.org/dataset/unhcr-global-trends-forced-displacement-in-2021-data
dataset_id: rdls_lss-unhcr_globaltrendsforceddisplac_2021
description: 'This dataset contains 23 data tables on global trends in forced displacement
  in 2021. The data provide trends, national level summaries and the demographic composition
  of refugees, asylum-seekers, Venezuelans displaced abroad, internally displaced
  persons (IDPs), returnees (refugees and IDPs), stateless persons, and other persons
  of concern to UNHCR.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unhcr-global-trends-forced-displacement-in-2021-data]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: UNHCR compiled national-level administrative data on forced displacement
    populations reported by governments according to their own definitions and methodologies.
    The dataset aggregates 23 tables of global trends covering demographic composition
    and population counts of refugees, asylum-seekers, IDPs, returnees, and stateless
    persons for 2021.
  sources:
  - id: source_1
    license: null
    name: UNHCR - The UN Refugee Agency
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unhcr-global-trends-forced-displacement-in-2021-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons and refugees displaced by various hazards
      and conflicts
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
        metric: displaced
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Asylum seekers, returnees, stateless persons and other persons of
      concern
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'UNHCR Global Trends: Forced Displacement in 2021 Data (Excel)'
  download_url: https://data.humdata.org/dataset/84e5b6b3-8d85-4755-a276-2662d3daa25c/resource/e12d5189-06e1-4a81-bd7a-0effb29d8e40/download/21-wrd-tables_final.xlsx
  format: null
  id: resource_e12d5189
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 21-WRD-tables_FINAL.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-unhcr_globaltrendsforceddisplac_2021
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021-12-31'
  start: '2021-01-01'
temporal_resolution: null
title: 'UNHCR Global Trends: Forced Displacement in 2021 Data'
version: null
vulnerability: null
---
