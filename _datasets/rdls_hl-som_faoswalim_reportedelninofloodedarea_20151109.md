---
attributions:
- entity:
    affiliation: null
    email: null
    name: FAO SWALIM
    url: https://data.humdata.org/dataset/somalia-reported-elnino-flooded-areas
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FAO SWALIM (inactive)
  url: https://data.humdata.org/dataset/somalia-reported-elnino-flooded-areas
creator:
  affiliation: null
  email: null
  name: FAO SWALIM (inactive)
  url: https://data.humdata.org/dataset/somalia-reported-elnino-flooded-areas
dataset_id: rdls_hl-som_faoswalim_reportedelninofloodedarea_20151109
description: 'This dataset shows the reported flooded areas in somalia. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/somalia-reported-elnino-flooded-areas]'
details: This dataset has been linked to HDX from the FAO SWALIM Online portal
exposure: []
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
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: "Direct observational and anecdotal field data collected by FAO SWALIM\
    \ on reported flooded extents in the Shabelle and Juba riverine basins during\
    \ the 2015 El Ni\xF1o event, with associated population displacement estimates\
    \ derived from affected communities."
  sources:
  - id: source_1
    license: null
    name: FAO SWALIM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-reported-elnino-flooded-areas
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: "Population displacement estimates from El Ni\xF1o-induced fluvial\
      \ flooding in riverine basins"
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
  description: Shabelle and Juba Riverine Basin El Nino Population Displacement Estimates
    - 2015.xlsx
  download_url: https://data.humdata.org/dataset/e996dde0-27d4-4544-b720-b6c07cbb8119/resource/5f000d45-c2e3-4f85-9d22-2c0096814e6f/download/shabelle-and-juba-riverine-basin-el-nino-population-displacement-estimates-2015.xlsx
  format: null
  id: resource_5f000d45
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Shabelle and Juba Riverine Basin El Nino Population Displacement Estimates
    - 2015.xlsx
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_faoswalim_reportedelninofloodedarea_20151109
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-09'
temporal_resolution: null
title: Somalia - Reported Elnino flooded areas
version: null
vulnerability: null
---
