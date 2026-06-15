---
attributions:
- entity:
    affiliation: null
    email: null
    name: USGS
    url: https://data.humdata.org/dataset/png-earthquake-7-5-affected-villages
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NSO (National Statistics Office)
    url: https://data.humdata.org/dataset/png-earthquake-7-5-affected-villages
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: NDC (National Disaster Centre)
    url: https://data.humdata.org/dataset/png-earthquake-7-5-affected-villages
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UN in Papua New Guinea
  url: https://data.humdata.org/dataset/png-earthquake-7-5-affected-villages
creator:
  affiliation: null
  email: null
  name: UN in Papua New Guinea
  url: https://data.humdata.org/dataset/png-earthquake-7-5-affected-villages
dataset_id: rdls_hel-png_unpng_highlandsearthquake75affe_20180330
description: 'Affected Villages based on 2011 Population. Intensity - USGS Villages
  - NSO Affected Village - NDC. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/png-earthquake-7-5-affected-villages]'
details: Intensity - USGS Villages - NSO Affected Village - NDC
exposure:
- asset_type:
    description: Residential population in villages based on 2011 census data
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Village-level affected population data derived by integrating USGS
    earthquake intensity measurements with 2011 census population counts and NDC disaster
    impact assessments for the 2011 Papua New Guinea Highlands 7.5 magnitude earthquake.
  sources:
  - id: source_1
    license: null
    name: USGS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: NSO (National Statistics Office)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: NDC (National Disaster Centre)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/png-earthquake-7-5-affected-villages
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake ground shaking in villages
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Papua New Guinea Highlands Earthquake 7.5 Affected Villages (Affected
    Villages geocoded_SADD.xlsx)
  download_url: https://data.humdata.org/dataset/e2aa4dba-1e72-4100-a4fa-da91994130ef/resource/25f74986-6d15-4452-882a-d67f31919b75/download/affected-villages-geocoded_sadd.xlsx
  format: null
  id: resource_25f74986
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Affected Villages geocoded_SADD.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-png_unpng_highlandsearthquake75affe_20180330
spatial:
  bbox: null
  centroid: null
  countries:
  - PNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-03-30'
temporal_resolution: null
title: Papua New Guinea Highlands Earthquake 7.5 Affected Villages
version: null
vulnerability: null
---
