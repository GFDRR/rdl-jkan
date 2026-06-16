---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/united-states-of-america-cyclone-1001000
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/united-states-of-america-cyclone-1001000
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/united-states-of-america-cyclone-1001000
dataset_id: rdls_hel-usa_wfpadam_americacyclonetropicalsto_2023
description: 'ADAM ID: 1001000_7 Cyclone (tropical storm) during the period Aug 26
  2023-Sep 02 2023 in United States. It impacted 494630 people.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/united-states-of-america-cyclone-1001000]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speeds at multiple thresholds
      (60, 90, 120 kph)
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
  - analysis_type: probabilistic
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
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system collected observed tropical cyclone track and wind
    speed data for the September 2023 event in the USA. Population exposure was estimated
    by intersecting wind speed fields with gridded population data at three wind speed
    thresholds (60, 90, 120 kph), producing affected population counts by administrative
    division and overall impact figures.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/united-states-of-america-cyclone-1001000
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone winds during September 2023
      event
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
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: 'United States of America: Cyclone - Tropical storm - Sep 2023 (Shape
    File)'
  download_url: https://data.humdata.org/dataset/206e6979-1bce-434c-9a7f-8e1994a856bc/resource/eeb33b15-389f-4df7-97fd-31c49bd74e30/download/1001000-29-adam-ts-1001000-29-shp.zip
  format: null
  id: resource_eeb33b15
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001000-29-adam-ts-1001000-29-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Cyclone - Tropical storm - Sep 2023 (Population
    Estimation)'
  download_url: https://data.humdata.org/dataset/206e6979-1bce-434c-9a7f-8e1994a856bc/resource/f4836c4d-b1d0-4367-ab60-f40c7154548b/download/1001000-29-adam-ts-1001000-29-pop-estimation.csv
  format: null
  id: resource_f4836c4d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001000-29-adam-ts-1001000-29-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-usa_wfpadam_americacyclonetropicalsto_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-09-02'
  start: '2023-08-26'
temporal_resolution: null
title: 'United States of America: Cyclone - Tropical storm - Sep 2023'
version: null
vulnerability: null
---
