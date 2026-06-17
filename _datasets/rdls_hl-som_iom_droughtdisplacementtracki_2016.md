---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-drought-displacement-tracking
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/somalia-drought-displacement-tracking
dataset_id: rdls_hl-som_iom_droughtdisplacementtracki_2016
description: 'Drought displacement tracking for somalia. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/somalia-drought-displacement-tracking]'
details: Note that this dataset contains observational data and it does not follow
  the same guidelines and quality assurance of the regular DTMs methodologies. Please
  use this information with caution.
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
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: CC-BY-4.0
lineage:
  description: Displacement tracking data collected through direct observation and
    anecdotal reports by IOM field teams monitoring population movements triggered
    by drought conditions in Somalia. Data represents post-event impact records of
    drought-induced displacement.
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
- href: https://data.humdata.org/dataset/somalia-drought-displacement-tracking
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement caused by drought conditions
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Drought Displacement Tracking (Drought Displacement Tracking)
  download_url: https://docs.google.com/spreadsheets/d/1-sC4D34q5xeMhaCk-7Mkqh9oKLMcMTGYzJd6juhleX4/edit?usp=drive_web
  format: Google Sheet
  id: resource_7689902d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Drought Displacement Tracking
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-som_iom_droughtdisplacementtracki_2016
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
  end: '2017-01-31'
  start: '2016-12-01'
temporal_resolution: null
title: Somalia - Drought Displacement Tracking
version: null
vulnerability: null
---
