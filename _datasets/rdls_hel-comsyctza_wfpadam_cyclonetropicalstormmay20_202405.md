---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/comoros-cyclone-1001060
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/comoros-cyclone-1001060
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/comoros-cyclone-1001060
dataset_id: rdls_hel-comsyctza_wfpadam_cyclonetropicalstormmay20_202405
description: 'ADAM ID: 1001060_14 Cyclone (tropical storm) during the period May 01
  2024-May 04 2024 in Tanzania, Seychelles, Comoros. It impacted 0 people.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/comoros-cyclone-1001060]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speeds at 60 km/h and
      90 km/h thresholds
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM system collected and analyzed geospatial data from the May
    2024 tropical cyclone event affecting Comoros, Tanzania, and Seychelles. Population
    exposure was estimated at administrative levels (ADM0-ADM2) for wind speed thresholds
    of 60 km/h and 90 km/h, generating impact estimates aggregated by administrative
    boundaries.
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
- href: https://data.humdata.org/dataset/comoros-cyclone-1001060
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone winds during May 2024 event
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
  description: 'Comoros: Cyclone - Tropical storm - May 2024 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/3c283ec8-dc26-43cb-a25c-139a80b69daa/resource/9dc3a875-1714-4bba-a74e-9afe7252a4b7/download/1001060-15-adam-ts-1001060-15-pop-estimation.csv
  format: null
  id: resource_9dc3a875
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001060-15-adam-ts-1001060-15-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-comsyctza_wfpadam_cyclonetropicalstormmay20_202405
spatial:
  bbox: null
  centroid: null
  countries:
  - COM
  - TZA
  - SYC
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-05-04'
  start: '2024-05-01'
temporal_resolution: null
title: 'Comoros: Cyclone - Tropical storm - May 2024'
version: null
vulnerability: null
---
