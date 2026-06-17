---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Hurricane Center
    url: https://data.humdata.org/dataset/recent-hurricanes
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Joint Typhoon Warning Center
    url: https://data.humdata.org/dataset/recent-hurricanes
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/recent-hurricanes
creator:
  affiliation: null
  email: null
  name: Esri
  url: https://data.humdata.org/dataset/recent-hurricanes
dataset_id: rdls_hzd-esri_recenthurricanes_20200505
description: 'Living Atlas live feed sources for hurricane path, observed path, forecast
  path, and intensity of tropical cyclone activity (hurricanes, typhoons, cyclones)
  from the National Hurricane Center and Joint Typhoon Warning Center. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/recent-hurricanes]'
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
      intensity_measure: PGWS:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC0-1.0
lineage:
  description: Live feed sources aggregating observed tropical cyclone tracks and
    intensity measurements from the National Hurricane Center (Atlantic/Eastern Pacific)
    and Joint Typhoon Warning Center (Western Pacific/Indian Ocean), providing real-time
    hazard monitoring of active hurricane, typhoon, and cyclone activity.
  sources:
  - id: source_1
    license: null
    name: National Hurricane Center
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Joint Typhoon Warning Center
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/recent-hurricanes
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: https://www.arcgis.com/home/item.html?id=c6da831d21d1468d8ec830773e5b0d7f
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This map contains live feed sources for hurricane path and forecast
    path of tropical activity from the National Hurricane Center and Joint Typhoon
    Warning Center.
  download_url: null
  format: null
  id: resource_5db4f414
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Hurricane and Cyclone App
- access_url: https://www.arcgis.com/home/item.html?id=248e7b5827a34b248647afb012c58787
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer describes the observed path, forecast track, and intensity
    of tropical cyclone activity (hurricanes, typhoons, cyclones) from the National
    Hurricane Center (NHC) and Joint Typhoon Warning Center (JTWC).
  download_url: null
  format: null
  id: resource_82f10e26
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Active Hurricanes, Cyclones and Typhoons
- access_url: https://www.arcgis.com/home/item.html?id=248e7b5827a34b248647afb012c58787
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This layer describes the observed path, forecast track, and intensity
    of tropical cyclone activity (hurricanes, typhoons, cyclones) from the National
    Hurricane Center (NHC) and Joint Typhoon Warning Center (JTWC).
  download_url: null
  format: null
  id: resource_e33ed170
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Recent Hurricanes, Cyclones and Typhoons
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-esri_recenthurricanes_20200505
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-05-05'
temporal_resolution: null
title: Recent Hurricanes
version: null
vulnerability: null
---
