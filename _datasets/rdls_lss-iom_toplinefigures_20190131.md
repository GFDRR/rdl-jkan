---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-topline-figures
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-topline-figures
dataset_id: rdls_lss-iom_toplinefigures_20190131
description: 'Topline figures dataset for IOM organisation page. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/iom-topline-figures]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM compiles topline displacement figures from its global field presence
    and partner networks, aggregating internally displaced persons counts and related
    indicators to provide organization-wide summary statistics for monitoring and
    reporting purposes.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/iom-topline-figures
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons figures aggregated by IOM
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
        metric: displaced
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
  description: IOM Topline Figures
  download_url: https://docs.google.com/spreadsheets/d/1kPO1CmPvc42j9TouovP5tyiSdegRk1wISLpxMWDlfaQ/edit?usp=drive_web
  format: null
  id: resource_855e9fe2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IOM Topline Figures
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-iom_toplinefigures_20190131
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
  end: null
  start: '2019-01-31'
temporal_resolution: null
title: IOM Topline Figures
version: null
vulnerability: null
---
