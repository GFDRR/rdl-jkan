---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/argentina-earthquake-eq-us7000kqbl
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/argentina-earthquake-eq-us7000kqbl
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/argentina-earthquake-eq-us7000kqbl
dataset_id: rdls_hl-arg_wfpadam_earthquake62maug2023_20230823
description: 'ADAM ID: eq_us7000kqbl Magnitude 6.2 earthquake at 568.794 depth occurred
  on Aug 23 2023 in Santiago del Estero, Argentina. It impacted 11956 people. The
  epicentre was at latitude -26.9212 longitude -63.3389.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/argentina-earthquake-eq-us7000kqbl]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: MMI:-
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: ADAM system processed observed earthquake parameters (magnitude 6.2,
    depth 568.794 km, epicenter coordinates) and derived MMI intensity values at administrative
    levels, then intersected with gridded population data to estimate affected population
    counts by intensity zone.
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
- href: https://data.humdata.org/dataset/argentina-earthquake-eq-us7000kqbl
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by ground motion from the 6.2 magnitude earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
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
  description: 'Argentina: Earthquake - 6.2M - Aug 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/120844ad-4a81-4eae-8176-4eb2cd47946a/resource/206574f8-c387-47cf-93c2-7f561babe161/download/sm-us7000kqbl-sm-us7000kqbl-pop-estimation.csv
  format: null
  id: resource_206574f8
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000kqbl-sm-us7000kqbl-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-arg_wfpadam_earthquake62maug2023_20230823
spatial:
  bbox: null
  centroid: null
  countries:
  - ARG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-08-23'
temporal_resolution: null
title: 'Argentina: Earthquake - 6.2M - Aug 2023'
version: null
vulnerability: null
---
