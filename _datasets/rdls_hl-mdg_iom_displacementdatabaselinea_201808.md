---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/madagascar-baseline-assessment-data-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/madagascar-baseline-assessment-data-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/madagascar-baseline-assessment-data-iom-dtm
dataset_id: rdls_hl-mdg_iom_displacementdatabaselinea_201808
description: 'The dataset has displaced people at sub national level with cause of
  the displacement. IOM Madagascar is implementing its DTM program to better understand
  the movements of drought-affected populations and provide critical information to
  government and humanitarian actors on the subject.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/madagascar-baseline-assessment-data-iom-dtm]'
details: null
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
      intensity_measure: SPI:-
      process: agricultural_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: IOM DTM conducted repeated baseline assessment surveys (Rounds 1-5)
    across Madagascar communes to track drought-affected population displacement at
    sub-national administrative levels. Survey data captured household and individual
    displacement counts, migration timing, and destination locations, providing empirical
    loss records of population displacement caused by drought.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/madagascar-baseline-assessment-data-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population counts by administrative division caused by
      drought
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  description: Madagascar Displacement Data - Baseline Assessment [IOM DTM] (DTM Madagascar
    Baseline Assessment Round 5)
  download_url: https://data.humdata.org/dataset/ed13d55a-0b9a-4a9a-b1bb-9bc76475cc59/resource/b1e2a1f7-bd73-42a7-9cde-6227a78d4b77/download/bdd_dtm_bf2_evaluation_5_sud_madagascar_p-1.xlsx
  format: null
  id: resource_b1e2a1f7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Madagascar Baseline Assessment Round 5
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 847 displaced persons, at sub national level, were identified between
    January and April 2018 with cause of displacement.
  download_url: https://data.humdata.org/dataset/ed13d55a-0b9a-4a9a-b1bb-9bc76475cc59/resource/bd82be15-3eb0-4b4c-8680-5dfbebc9b980/download/dtm-madagascar-baseline-assessment-round-4.xlsx
  format: null
  id: resource_bd82be15
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Madagascar Baseline Assessment Round 4
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Madagascar Displacement Data - Baseline Assessment [IOM DTM] (DTM Madagascar
    Baseline Assessment Round 2)
  download_url: https://data.humdata.org/dataset/ed13d55a-0b9a-4a9a-b1bb-9bc76475cc59/resource/6e442163-7a20-4d25-a646-fb8cfe05103f/download/dtm-madagascar-baseline-assessment-round-2.xlsx
  format: null
  id: resource_6e442163
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Madagascar Baseline Assessment Round 2
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Madagascar Displacement Data - Baseline Assessment [IOM DTM] (DTM Madagascar
    Baseline Assessment Round 1)
  download_url: https://data.humdata.org/dataset/ed13d55a-0b9a-4a9a-b1bb-9bc76475cc59/resource/ac8ebecc-c6d9-4c7e-985f-c2f742ac012b/download/dtm-madagascar-baseline-assessment-round-1.xlsx
  format: null
  id: resource_ac8ebecc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: DTM Madagascar Baseline Assessment Round 1
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mdg_iom_displacementdatabaselinea_201808
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-08-31'
  start: '2018-08-01'
temporal_resolution: null
title: Madagascar Displacement Data - Baseline Assessment [IOM DTM]
version: null
vulnerability: null
---
