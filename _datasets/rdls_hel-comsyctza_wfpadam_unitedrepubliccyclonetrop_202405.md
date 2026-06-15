---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/united-republic-of-tanzania-cyclone-1001060
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/united-republic-of-tanzania-cyclone-1001060
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/united-republic-of-tanzania-cyclone-1001060
dataset_id: rdls_hel-comsyctza_wfpadam_unitedrepubliccyclonetrop_202405
description: 'ADAM ID: 1001060_10 Cyclone (tropical storm) during the period May 01
  2024-May 04 2024 in Tanzania, Seychelles, Comoros. It impacted 8846 people.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/united-republic-of-tanzania-cyclone-1001060]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speed thresholds at 60,
      90, and 120 km/h
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WFP ADAM system collected observed tropical cyclone wind speed data
    and integrated it with gridded population estimates to quantify population exposure
    at three wind speed thresholds (60, 90, 120 km/h) during the May 2024 cyclone
    event in Tanzania, Seychelles, and Comoros, producing administrative-level impact
    summaries.
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/united-republic-of-tanzania-cyclone-1001060
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone with 8,846 people impacted
      during May 2024 event
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
  description: 'United Republic of Tanzania: Cyclone - Tropical storm - May 2024 (Population
    Estimation)'
  download_url: https://data.humdata.org/dataset/d94b7874-8dd0-416f-ad78-476ac36ceb64/resource/92a407a0-630b-42a3-a798-cb357c738b26/download/1001060-14-adam-ts-1001060-14-pop-estimation.csv
  format: null
  id: resource_92a407a0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001060-14-adam-ts-1001060-14-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-comsyctza_wfpadam_unitedrepubliccyclonetrop_202405
spatial:
  bbox: null
  centroid: null
  countries:
  - TZA
  - SYC
  - COM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-05-04'
  start: '2024-05-01'
temporal_resolution: null
title: 'United Republic of Tanzania: Cyclone - Tropical storm - May 2024'
version: null
vulnerability: null
---
