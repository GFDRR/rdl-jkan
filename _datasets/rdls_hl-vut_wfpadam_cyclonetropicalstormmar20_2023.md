---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/vanuatu-cyclone-1000965
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-cyclone-1000965
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/vanuatu-cyclone-1000965
dataset_id: rdls_hl-vut_wfpadam_cyclonetropicalstormmar20_2023
description: 'A cyclone (tropical storm) during the period Feb 27 2023-Mar 03 2023
  in Vanuatu. It impacted 190950 people.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/vanuatu-cyclone-1000965]'
details: null
exposure: []
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
  description: WFP ADAM collected and analyzed geospatial and socio-economic data
    following the tropical cyclone event in Vanuatu (Feb 27 - Mar 03, 2023). The system
    aggregated impact information to produce a response dashboard with affected population
    counts and event mapping.
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
- href: https://data.humdata.org/dataset/vanuatu-cyclone-1000965
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by tropical cyclone in Vanuatu, March 2023
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
  description: 'Vanuatu: Cyclone - Tropical storm - Mar 2023 (Shape File)'
  download_url: https://adam-project-prod.s3-eu-west-1.amazonaws.com/adam_ts/events/2023/03/1000965_18/ADAM_TS_1000965_18_shp.zip
  format: null
  id: resource_b4fdbef9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ADAM_TS_1000965_18_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vut_wfpadam_cyclonetropicalstormmar20_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-03-03'
  start: '2023-02-27'
temporal_resolution: null
title: 'Vanuatu: Cyclone - Tropical storm - Mar 2023'
version: null
vulnerability: null
---
