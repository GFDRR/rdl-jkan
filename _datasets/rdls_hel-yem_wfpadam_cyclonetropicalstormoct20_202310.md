---
attributions:
- entity:
    affiliation: null
    email: null
    name: WFP Advanced Disaster Analysis & Mapping (ADAM)
    url: https://data.humdata.org/dataset/yemen-cyclone-1001026
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/yemen-cyclone-1001026
creator:
  affiliation: null
  email: null
  name: WFP Advanced Disaster Analysis & Mapping
  url: https://data.humdata.org/dataset/yemen-cyclone-1001026
dataset_id: rdls_hel-yem_wfpadam_cyclonetropicalstormoct20_202310
description: 'ADAM ID: 1001026_9 Cyclone (tropical storm) during the period Oct 20
  2023-Oct 24 2023 in Yemen. It impacted 41258 people.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/yemen-cyclone-1001026]'
details: null
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind speeds at multiple thresholds
      (60, 90, 120 km/h)
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
  description: WFP ADAM system processed observed tropical cyclone track and wind
    field data from October 20-24, 2023 to generate wind speed polygons at multiple
    thresholds (60, 90, 120 km/h). Population exposure was estimated by intersecting
    wind speed zones with gridded population data at administrative levels (ADM0-ADM2),
    producing both spatial (shapefile) and tabular (CSV) outputs of affected population
    counts.
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
- href: https://data.humdata.org/dataset/yemen-cyclone-1001026
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total population affected by tropical cyclone event (41,258 people
      impacted)
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
  description: 'Yemen: Cyclone - Tropical storm - Oct 2023 (Shape File)'
  download_url: https://data.humdata.org/dataset/1ce1fd01-ac2b-4704-9ebe-4637d123fcd9/resource/7e7866f0-2f5e-46cd-bfca-f933830935a8/download/1001026-16-adam-ts-1001026-16-shp.zip
  format: null
  id: resource_7e7866f0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001026-16-adam-ts-1001026-16-shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: Cyclone - Tropical storm - Oct 2023 (Population Estimation)'
  download_url: https://data.humdata.org/dataset/1ce1fd01-ac2b-4704-9ebe-4637d123fcd9/resource/1d0b7351-4d55-4584-94de-d37b3ba81b63/download/1001026-16-adam-ts-1001026-16-pop-estimation.csv
  format: null
  id: resource_1d0b7351
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 1001026-16-adam-ts-1001026-16-pop-estimation.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-yem_wfpadam_cyclonetropicalstormoct20_202310
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-10-24'
  start: '2023-10-20'
temporal_resolution: null
title: 'Yemen: Cyclone - Tropical storm - Oct 2023'
version: null
vulnerability: null
---
