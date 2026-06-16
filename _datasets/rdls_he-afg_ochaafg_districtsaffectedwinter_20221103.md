---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/afghanistan-districts-affected-by-winter
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-districts-affected-by-winter
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-districts-affected-by-winter
dataset_id: rdls_he-afg_ochaafg_districtsaffectedwinter_20221103
description: 'The Winter affected districts mapping showcases the 2021 winter affected
  areas to aid planning and resource mobilization is critical to get ahead of winter
  2022-2023.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-districts-affected-by-winter]'
details: null
exposure:
- asset_type:
    description: Population in districts affected by winter conditions
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
      intensity_measure: AirTemp:C
      process: extreme_cold
      trigger: null
      type: extreme_temperature
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Winter-affected districts were identified through direct observational
    data and anecdotal reports from humanitarian partners operating in Afghanistan
    during the 2021 winter season. District-level administrative boundaries were mapped
    to indicate areas experiencing winter hazards to support planning and resource
    mobilization for the 2022-2023 winter season.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-districts-affected-by-winter
  rel: source
loss: null
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
  description: The Winter affected districts mapping showcases the 2021 winter affected
    areas to aid planning and resource mobilization is critical to get ahead of winter
    2022-2023.
  download_url: https://data.humdata.org/dataset/60d64723-cf9c-41c1-9f09-6967251ca161/resource/fce5688c-c019-4738-bf8e-4d1976fa4386/download/districts-affected-by-winter_.xlsx
  format: null
  id: resource_fce5688c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AFG-districts-affected-by-winter
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-afg_ochaafg_districtsaffectedwinter_20221103
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-03'
temporal_resolution: null
title: Afghanistan - Districts Affected by Winter
version: null
vulnerability: null
---
