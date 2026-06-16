---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/reunion-cyclone-1001041
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/reunion-cyclone-1001041
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/reunion-cyclone-1001041
dataset_id: rdls_hel-reu_wfpadam_reunioncyclonecategory2ja_202401
description: 'ADAM ID: 1001041_8 Cyclone (category 2) during the period Jan 12 2024-Jan
  15 2024 in Miscellaneous (French) Indian Ocean Islands, Madagascar. It impacted
  871751 people.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/reunion-cyclone-1001041]'
details: null
exposure:
- asset_type:
    description: Population exposed to cyclone wind speeds at multiple thresholds
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
  event_sets_by_hazard_type:
    strong_wind:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "ADAM collected observed tropical cyclone track geometry and wind speed\
    \ measurements for the January 2024 Category 2 cyclone event in R\xE9union. Wind\
    \ speed thresholds (60, 90, 120 kph) were intersected with gridded population\
    \ data to estimate affected populations by administrative division, generating\
    \ both spatial hazard layers and impact summaries for operational response."
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
- href: https://data.humdata.org/dataset/reunion-cyclone-1001041
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by Category 2 cyclone event
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
  description: "R\xE9union: Cyclone - Category 2 - Jan 2024 (Shape File)"
  download_url: https://data.humdata.org/dataset/6ea0599b-a659-4ba5-9ff7-1062bfd266d0/resource/d3ae0dd0-9de1-4cc8-a806-13608ac6ecb8/download/1001041-12-adam-ts-1001041-12-shp.zip
  format: null
  id: resource_d3ae0dd0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001041-12-adam-ts-1001041-12-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Cyclone - Category 2 - Jan 2024 (Population Estimation)"
  download_url: https://data.humdata.org/dataset/6ea0599b-a659-4ba5-9ff7-1062bfd266d0/resource/73178a91-88c3-4e61-86da-a09045daf2cf/download/1001041-12-adam-ts-1001041-12-pop-estimation.csv
  format: null
  id: resource_73178a91
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001041-12-adam-ts-1001041-12-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-reu_wfpadam_reunioncyclonecategory2ja_202401
spatial:
  bbox: null
  centroid: null
  countries:
  - REU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-01-15'
  start: '2024-01-12'
temporal_resolution: null
title: "R\xE9union: Cyclone - Category 2 - Jan 2024"
version: null
vulnerability: null
---
