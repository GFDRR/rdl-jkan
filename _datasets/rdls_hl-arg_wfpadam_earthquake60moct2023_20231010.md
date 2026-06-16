---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/argentina-earthquake-eq-us6000legn
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/argentina-earthquake-eq-us6000legn
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/argentina-earthquake-eq-us6000legn
dataset_id: rdls_hl-arg_wfpadam_earthquake60moct2023_20231010
description: 'ADAM ID: eq_us6000legn Magnitude 6.0 earthquake at 247.255 depth occurred
  on Oct 10 2023 in 57 km WSW of Abra Pampa, Argentina. It impacted 3132 people. The
  epicentre was at latitude -22.8844 longitude -66.2242.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/argentina-earthquake-eq-us6000legn]'
details: null
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
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: 'ADAM system processed the October 10, 2023 magnitude 6.0 earthquake
    event (USGS ID: us6000legn) by calculating Modified Mercalli Intensity (MMI) distribution
    across administrative divisions in Argentina and estimating affected population
    counts at different intensity thresholds (MMI 2-3) to support emergency response
    operations.'
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
- href: https://data.humdata.org/dataset/argentina-earthquake-eq-us6000legn
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking at different MMI
      intensity levels
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
  description: 'Argentina: Earthquake - 6.0M - Oct 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/285ed3ff-278e-4a8a-8f47-cb9641d82b38/resource/48c81673-825c-4867-85f3-70dc99e19dfc/download/sm-us6000legn-sm-us6000legn-pop-estimation.csv
  format: null
  id: resource_48c81673
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us6000legn-sm-us6000legn-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-arg_wfpadam_earthquake60moct2023_20231010
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
  start: '2023-10-10'
temporal_resolution: null
title: 'Argentina: Earthquake - 6.0M - Oct 2023'
version: null
vulnerability: null
---
