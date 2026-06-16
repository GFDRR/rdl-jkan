---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/vanuatu-cyclone-1001027
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-cyclone-1001027
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-cyclone-1001027
dataset_id: rdls_hel-slbvut_wfpadam_cyclonetropicaldepression_202310
description: 'ADAM ID: 1001027_8 Cyclone (tropical depression) during the period Oct
  21 2023-Oct 26 2023 in Vanuatu, Solomon Islands. It impacted 49248 people.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/vanuatu-cyclone-1001027]'
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
license: CC-BY-SA-4.0
lineage:
  description: WFP ADAM system collected observed tropical cyclone track geometry
    and wind speed measurements during the October 21-26, 2023 tropical depression
    event. Population exposure was estimated by intersecting wind speed thresholds
    (60, 90, 120 kph) with gridded population data at administrative levels, producing
    population counts exposed to each wind intensity band.
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
- href: https://data.humdata.org/dataset/vanuatu-cyclone-1001027
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by tropical depression cyclone event
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
  description: 'Vanuatu: Cyclone - Tropical depression - Oct 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/8e420560-3066-4c0f-9d94-4e4a188e5e4a/resource/4155ffba-041b-4392-b01d-024e1837f4b5/download/1001027-18-adam-ts-1001027-18-shp.zip
  format: null
  id: resource_4155ffba
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001027-18-adam-ts-1001027-18-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Vanuatu: Cyclone - Tropical depression - Oct 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/8e420560-3066-4c0f-9d94-4e4a188e5e4a/resource/05abe257-62ec-4092-adfd-9860f79464eb/download/1001027-18-adam-ts-1001027-18-pop-estimation.csv
  format: null
  id: resource_05abe257
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001027-18-adam-ts-1001027-18-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-slbvut_wfpadam_cyclonetropicaldepression_202310
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  - SLB
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-10-26'
  start: '2023-10-21'
temporal_resolution: null
title: 'Vanuatu: Cyclone - Tropical depression - Oct 2023'
version: null
vulnerability: null
---
