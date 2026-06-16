---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM-DTM (International Organization for Migration - Displacement Tracking
      Matrix)
    url: https://data.humdata.org/dataset/ethiopia-drought-induced-displacement
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-drought-induced-displacement
creator:
  affiliation: null
  email: null
  name: OCHA Ethiopia
  url: https://data.humdata.org/dataset/ethiopia-drought-induced-displacement
dataset_id: rdls_hl-eth_ochaeth_droughtinduceddisplacemen_20230531
description: 'The dataset contains the number of newly displaced persons by Woreda
  due to the current drought in Ethiopia. It does not include protracted IDPs (people
  displaced due to previous droughts).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-drought-induced-displacement]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Displacement estimates derived from IOM-DTM site assessment data collected
    over 12 months, calculating net increments between successive assessment rounds
    for sites where drought was identified as the primary displacement cause by the
    majority of IDPs.
  sources:
  - id: source_1
    license: null
    name: IOM-DTM (International Organization for Migration - Displacement Tracking
      Matrix)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-drought-induced-displacement
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Newly displaced persons due to drought-induced displacement by Woreda
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia - Drought Induced Displacement Estimates (Drought Induced
    Displacement)
  download_url: https://docs.google.com/spreadsheets/d/e/2PACX-1vRppQx8JTKkKRCKmzfnCMmTFEcvCpkbP9PdHs1sQTUyacmbsx8tlAXpgBLFce-lcehukreGGuXjA_4S/pub?gid=961087049&single=true&output=csv
  format: null
  id: resource_e7c868d3
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Drought Induced Displacement
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-eth_ochaeth_droughtinduceddisplacemen_20230531
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-31'
temporal_resolution: null
title: Ethiopia - Drought Induced Displacement Estimates
version: null
vulnerability: null
---
