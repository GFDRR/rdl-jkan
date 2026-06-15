---
attributions:
- entity:
    affiliation: null
    email: null
    name: FAO SWALIM
    url: https://data.humdata.org/dataset/somalia-shabelle-and-juba-riverine-basin-population-displacement-estimates-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FAO SWALIM (inactive)
  url: https://data.humdata.org/dataset/somalia-shabelle-and-juba-riverine-basin-population-displacement-estimates-2015
creator:
  affiliation: null
  email: null
  name: FAO SWALIM (inactive)
  url: https://data.humdata.org/dataset/somalia-shabelle-and-juba-riverine-basin-population-displacement-estimates-2015
dataset_id: rdls_lss-som_faoswalim_shabellejubariverinebasin_20151113
description: 'This dataset shows the Shabelle and Juba Riverine Basin Population Displacement
  Estimates - 2015. Working assumptions: - Displaced population defined as direct
  displacement through flood inundation - Displaced population calculated by multiplying
  the number of hh''s by hh size of 6 - If a range is provided to quantify displacement
  the upper figure is used. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-shabelle-and-juba-riverine-basin-population-displacement-estimates-2015]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Flood inundation extents along the Shabelle and Juba riverine basins\
    \ were used to identify directly inundated households. Displaced population was\
    \ estimated by multiplying the number of inundated households by an assumed household\
    \ size of 6, with upper-bound figures used where ranges were reported. The dataset\
    \ was compiled by FAO SWALIM to support humanitarian response planning during\
    \ the 2015 El Ni\u221A\xB1o-related flooding event."
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
- href: https://data.humdata.org/dataset/somalia-shabelle-and-juba-riverine-basin-population-displacement-estimates-2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement estimates from riverine flood inundation
      along Shabelle and Juba basins in Somalia, 2015, calculated by multiplying inundated
      household counts by household size of 6
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
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Shabelle and Juba Riverine Basin Population Displacement
    Estimates - 2015 (Flood Information Report.xls)
  download_url: https://data.humdata.org/dataset/051b208a-23c5-43c7-9733-9faafb0b9690/resource/a295952b-a8e7-4c64-aafb-26a10989a0a4/download/flood-information-report.xls
  format: null
  id: resource_a295952b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Flood Information Report.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_faoswalim_shabellejubariverinebasin_20151113
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
  start: '2015-11-13'
temporal_resolution: null
title: Somalia - Shabelle and Juba Riverine Basin Population Displacement Estimates
  - 2015
version: null
vulnerability: null
---
