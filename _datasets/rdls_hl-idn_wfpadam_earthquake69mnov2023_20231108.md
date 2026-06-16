---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9h2
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9h2
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9h2
dataset_id: rdls_hl-idn_wfpadam_earthquake69mnov2023_20231108
description: 'ADAM ID: eq_us7000l9h2 Magnitude 6.9 earthquake at 10.0 depth occurred
  on Nov 08 2023 in Banda Sea. It impacted 736 people. The epicentre was at latitude
  -6.3878 longitude 129.7638.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9h2]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: 'Post-event earthquake impact assessment derived from USGS ShakeMaps
    (ADAM ID: eq_us7000l9h2) intersected with gridded population data to estimate
    affected population by Modified Mercalli Intensity (MMI) zones across administrative
    divisions in Indonesia.'
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
- href: https://data.humdata.org/dataset/indonesia-earthquake-eq-us7000l9h2
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking across MMI intensity
      zones
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
  description: 'Indonesia: Earthquake - 6.9M - Nov 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/e88abf6d-a797-470d-8d3e-ce3fd888f9bd/resource/7101edb1-22f7-4999-85b0-328b482eea09/download/sm-us7000l9h2-sm-us7000l9h2-pop-estimation.csv
  format: null
  id: resource_7101edb1
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000l9h2-sm-us7000l9h2-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-idn_wfpadam_earthquake69mnov2023_20231108
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-08'
temporal_resolution: null
title: 'Indonesia: Earthquake - 6.9M - Nov 2023'
version: null
vulnerability: null
---
