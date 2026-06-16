---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/china-cyclone-1001018
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-cyclone-1001018
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-cyclone-1001018
dataset_id: rdls_hel-chnjpnphl_wfpadam_cyclonetropicaldepression_2023
description: 'ADAM ID: 1001018_4 Cyclone (tropical depression) during the period Sep
  29 2023-Oct 10 2023 in China, Japan, Philippines. It impacted 3755569 people.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/china-cyclone-1001018]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM system collected observed tropical cyclone track geometry
    and wind speed measurements during the September 29 - October 10, 2023 event.
    Population exposure was estimated by intersecting wind speed thresholds (60, 90,
    120 kph) with gridded population data at administrative levels (ADM0, ADM1, ADM2),
    aggregating affected population counts by wind speed intensity zones.
  sources:
  - id: source_1
    license: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/china-cyclone-1001018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by tropical depression cyclone event across
      China, Japan, and Philippines
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
  description: 'China: Cyclone - Tropical depression - Oct 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/50bbe5b2-eb03-402c-9639-5e1ba1615125/resource/6f299345-b319-4939-8ff7-29038755946a/download/1001018-43-adam-ts-1001018-43-shp.zip
  format: null
  id: resource_6f299345
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001018-43-adam-ts-1001018-43-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China: Cyclone - Tropical depression - Oct 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/50bbe5b2-eb03-402c-9639-5e1ba1615125/resource/0ee22155-ff8d-4fe5-8519-0dbc12343a22/download/1001018-43-adam-ts-1001018-43-pop-estimation.csv
  format: null
  id: resource_0ee22155
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001018-43-adam-ts-1001018-43-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-chnjpnphl_wfpadam_cyclonetropicaldepression_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - CHN
  - JPN
  - PHL
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-10-10'
  start: '2023-09-29'
temporal_resolution: null
title: 'China: Cyclone - Tropical depression - Oct 2023'
version: null
vulnerability: null
---
