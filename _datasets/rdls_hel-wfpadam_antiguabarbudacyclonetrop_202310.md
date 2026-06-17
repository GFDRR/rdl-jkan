---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/antigua-and-barbuda-cyclone-1001025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/antigua-and-barbuda-cyclone-1001025
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/antigua-and-barbuda-cyclone-1001025
dataset_id: rdls_hel-wfpadam_antiguabarbudacyclonetrop_202310
description: 'ADAM ID: 1001025_12 Cyclone (tropical storm) during the period Oct 18
  2023-Oct 29 2023 in Virgin Islands British, Antigua and Barbuda, Montserrat, Guadeloupe,
  Bermuda, Barbados, Dominica. It impacted 35248 people.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/antigua-and-barbuda-cyclone-1001025]'
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
  type: strong_wind
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system collected observed tropical cyclone wind speed data
    and spatial boundaries for the October 2023 tropical storm event. Population exposure
    was estimated by intersecting wind speed zones with gridded population data at
    administrative levels, generating population counts at three wind speed thresholds
    (60, 90, 120 kph). Post-event impact figures aggregated affected population across
    seven affected countries.
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
- href: https://data.humdata.org/dataset/antigua-and-barbuda-cyclone-1001025
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by tropical storm event (35,248 people)
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
  description: 'Antigua and Barbuda: Cyclone - Tropical storm - Oct 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/8c4021ec-4661-4ed1-bf42-d8c730b801b8/resource/bcd0f951-ef26-44ee-b74d-1bb32be692b0/download/1001025-40-adam-ts-1001025-40-shp.zip
  format: null
  id: resource_bcd0f951
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001025-40-adam-ts-1001025-40-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Antigua and Barbuda: Cyclone - Tropical storm - Oct 2023 (Population
    Estimation)'
  download_url: https://data.humdata.org/dataset/8c4021ec-4661-4ed1-bf42-d8c730b801b8/resource/21a79af2-066e-4455-9af7-c1368331d58c/download/1001025-40-adam-ts-1001025-40-pop-estimation.csv
  format: null
  id: resource_21a79af2
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001025-40-adam-ts-1001025-40-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-wfpadam_antiguabarbudacyclonetrop_202310
spatial:
  bbox: null
  centroid: null
  countries:
  - ATG
  - BRB
  - BMU
  - DMA
  - GLP
  - MSR
  - VGB
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-10-29'
  start: '2023-10-18'
temporal_resolution: null
title: 'Antigua and Barbuda: Cyclone - Tropical storm - Oct 2023'
version: null
vulnerability: null
---
