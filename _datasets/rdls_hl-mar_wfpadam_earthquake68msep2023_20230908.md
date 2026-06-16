---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/morocco-earthquake-eq-us7000kufc
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/morocco-earthquake-eq-us7000kufc
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/morocco-earthquake-eq-us7000kufc
dataset_id: rdls_hl-mar_wfpadam_earthquake68msep2023_20230908
description: 'ADAM ID: eq_us7000kufc Magnitude 6.8 earthquake at 18.535 depth occurred
  on Sep 08 2023 in 26km SW of Amizmiz. It impacted 380662 people. The epicentre was
  at latitude 31.1095 longitude -8.4404.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/morocco-earthquake-eq-us7000kufc]'
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
  description: WFP ADAM system processed the USGS earthquake event (us7000kufc) and
    derived population exposure to ground shaking by intersecting MMI intensity zones
    with gridded population data, stratifying affected counts by administrative boundaries
    and Modified Mercalli Intensity levels (3-7).
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
- href: https://data.humdata.org/dataset/morocco-earthquake-eq-us7000kufc
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking across MMI intensity
      levels 3-7
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
  description: 'Morocco: Earthquake - 6.8M - Sep 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/62467e35-c0ee-4ec0-82ce-35eed21a4e6c/resource/022c1662-f8be-43a9-b921-82f89dc4ec62/download/sm-us7000kufc-sm-us7000kufc-pop-estimation.csv
  format: null
  id: resource_022c1662
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sm-us7000kufc-sm-us7000kufc-pop-estimation.csv
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mar_wfpadam_earthquake68msep2023_20230908
spatial:
  bbox: null
  centroid: null
  countries:
  - MAR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-08'
temporal_resolution: null
title: 'Morocco: Earthquake - 6.8M - Sep 2023'
version: null
vulnerability: null
---
