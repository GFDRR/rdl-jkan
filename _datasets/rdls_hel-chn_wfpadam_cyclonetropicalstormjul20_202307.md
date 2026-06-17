---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP ADAM
    url: https://data.humdata.org/dataset/china-cyclone-1000983
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-cyclone-1000983
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/china-cyclone-1000983
dataset_id: rdls_hel-chn_wfpadam_cyclonetropicalstormjul20_202307
description: 'ADAM ID: 1000983_8 Cyclone (tropical storm) during the period Jul 14
  2023-Jul 18 2023 in China. It impacted 20061341 people.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/china-cyclone-1000983]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone hazard
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
  type: strong_wind
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM collected and analyzed geospatial data on the tropical cyclone
    event occurring July 14-18, 2023 in China, mapping the storm track with wind speed
    measurements and overlaying population exposure data to quantify affected populations
    for humanitarian response dashboards.
  sources:
  - id: source_1
    license: null
    name: WFP ADAM
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/china-cyclone-1000983
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by tropical cyclone event
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
        type: total
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
  description: 'China: Cyclone - Tropical storm - Jul 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/11c01722-2d88-48b3-bb3a-ee54861bcd6f/resource/c3bbfc63-fa4d-4682-9efe-9901f6fe6e75/download/1000983-15-adam-ts-1000983-15-shp.zip
  format: null
  id: resource_c3bbfc63
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1000983-15-adam-ts-1000983-15-shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-chn_wfpadam_cyclonetropicalstormjul20_202307
spatial:
  bbox: null
  centroid: null
  countries:
  - CHN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-07-18'
  start: '2023-07-14'
temporal_resolution: null
title: 'China: Cyclone - Tropical storm - Jul 2023'
version: null
vulnerability: null
---
