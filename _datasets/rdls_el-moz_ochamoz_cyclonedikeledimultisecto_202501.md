---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/mozambique-cyclone-dikeledi-multi-sectoral-initial-rapid-assessment
creator:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/mozambique-cyclone-dikeledi-multi-sectoral-initial-rapid-assessment
dataset_id: rdls_el-moz_ochamoz_cyclonedikeledimultisecto_202501
description: 'Cyclone Dikeledi Multi-Sectoral Initial Rapid Assessment (MIRA) analysis
  dataset of Nampula, Mozambique.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mozambique-cyclone-dikeledi-multi-sectoral-initial-rapid-assessment]'
details: null
exposure:
- asset_type:
    description: Residential population before and after Cyclone Dikeledi, including
      displaced persons, returnees, and vulnerable groups
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Multi-Sectoral Initial Rapid Assessment (MIRA) survey data collected
    through sample surveys by humanitarian partners in Nampula Province, Mozambique
    following Cyclone Dikeledi in 2025. The dataset captures village-level post-event
    population counts, household displacement status, shelter conditions, and vulnerable
    population groups through structured questionnaires administered by trained enumerators.
  sources:
  - id: source_1
    license: null
    name: OCHA Mozambique
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mozambique-cyclone-dikeledi-multi-sectoral-initial-rapid-assessment
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement and shelter conditions resulting from Cyclone
      Dikeledi
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
    description: Total affected population and household counts from Cyclone Dikeledi
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
  description: 'Mozambique: Cyclone Dikeledi Multi-Sectoral Initial Rapid Assessment
    (Cyclone Dikeledi Multi-Sectoral Initial Rapid Assessment)'
  download_url: https://data.humdata.org/dataset/3238d15d-f1af-4ff1-a0ee-a4cef3e23978/resource/b19e7dfc-33e1-443e-aafb-8fd530fae65b/download/mira_-_ciclone_dikeledi_2025_-_all_versions.xlsx
  format: null
  id: resource_b19e7dfc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MIRA_-_Ciclone_DIKELEDI_2025_-_all_versions.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-moz_ochamoz_cyclonedikeledimultisecto_202501
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
  end: '2025-01-25'
  start: '2025-01-23'
temporal_resolution: null
title: 'Mozambique: Cyclone Dikeledi Multi-Sectoral Initial Rapid Assessment'
version: null
vulnerability: null
---
