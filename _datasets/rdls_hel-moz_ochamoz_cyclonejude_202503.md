---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/mira-tool-cyclone-jude-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/mira-tool-cyclone-jude-2025
creator:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/mira-tool-cyclone-jude-2025
dataset_id: rdls_hel-moz_ochamoz_cyclonejude_202503
description: 'This dataset will help the humanitarian community to understand the
  Needs after the cyclone Jude.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mira-tool-cyclone-jude-2025]'
details: null
exposure:
- asset_type:
    description: Residential population before and after Cyclone Jude by village and
      displacement status
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
- asset_type:
    description: Household structures classified by shelter conditions and displacement
      status
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC0-1.0
lineage:
  description: Post-event Multi-Indicator Rapid Assessment (MIRA) survey conducted
    by humanitarian partners across Mozambique following Cyclone Jude. Village-level
    data collected via sample survey methodology documenting pre- and post-disaster
    population counts, household displacement status, shelter conditions, and exposure
    to multiple hazard types (cyclone, flood, heavy rains, drought, violence). Data
    aggregated by province, district, and sub-district administrative levels to support
    humanitarian needs analysis.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mira-tool-cyclone-jude-2025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement and shelter conditions resulting from Cyclone
      Jude
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood hazard triggered by Cyclone Jude
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
        metric: exposure
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
  description: Mozambique - Cyclone Jude (Excel)
  download_url: https://data.humdata.org/dataset/e120e4a2-18f8-41b3-8ed2-f70a4214dec1/resource/e7676caf-fe1e-4380-8946-4c37388c7c1d/download/mira_-_ciclone_jude_2025_en.xlsx
  format: null
  id: resource_e7676caf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MIRA_-_Ciclone_JUDE_2025_EN.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-moz_ochamoz_cyclonejude_202503
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
  end: '2025-03-17'
  start: '2025-03-13'
temporal_resolution: null
title: Mozambique - Cyclone Jude
version: null
vulnerability: null
---
