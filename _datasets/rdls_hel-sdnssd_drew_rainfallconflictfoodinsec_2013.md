---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA TRMM/TMPA 3P43
    url: https://data.humdata.org/dataset/rainfall-conflict-and-food-insecurity-measurement-in-post-succession-sudan-and-south-sudan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/rainfall-conflict-and-food-insecurity-measurement-in-post-succession-sudan-and-south-sudan
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Integrated Phase Classification (IPC) / Famine Early Warning Systems Network
      (FEWSNET)
    url: https://data.humdata.org/dataset/rainfall-conflict-and-food-insecurity-measurement-in-post-succession-sudan-and-south-sudan
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Armed Conflict Locations and Events Data Project (ACLED)
    url: https://data.humdata.org/dataset/rainfall-conflict-and-food-insecurity-measurement-in-post-succession-sudan-and-south-sudan
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/rainfall-conflict-and-food-insecurity-measurement-in-post-succession-sudan-and-south-sudan
creator:
  affiliation: null
  email: null
  name: Drew University (inactive)
  url: https://data.humdata.org/dataset/rainfall-conflict-and-food-insecurity-measurement-in-post-succession-sudan-and-south-sudan
dataset_id: rdls_hel-sdnssd_drew_rainfallconflictfoodinsec_2013
description: 'July precipitation anomalies from 2013-2016 for Sudan and South Sudan,
  which may have negatively affected agrarian populations during the lean season,
  are generated from NASA TRMM/TMPA 3P43 (Tropical Rainfall Measuring Mission/Multi-Satellite
  Precipitation Analysis). These anomalies are available to analyze in relation local
  population estimates (WorldPop), reported conflict events and fatalities (Armed
  Conflict Locations and Events Data Project), food security classification (Integrated
  Phase Classification, Famine Early Warning Systems Network), and other sources for
  measuring crop access to water (Climate Hazards Group InfraRed Precipitation with
  Station data). Data were compiled by Maimouna Kante and Lisa Jordan.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/rainfall-conflict-and-food-insecurity-measurement-in-post-succession-sudan-and-south-sudan]'
details: Data provided as is. NASA NEO TRMM Floating Point Raster files were used.
exposure:
- asset_type:
    description: Agrarian populations and crop production areas vulnerable to precipitation
      anomalies
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Local population estimates from WorldPop
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
      intensity_measure: precipitation_anomaly:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: July precipitation anomalies were derived from NASA TRMM/TMPA satellite
    observations for 2013-2016 and analyzed in relation to WorldPop population estimates,
    IPC food security classifications, and ACLED conflict data to measure drought
    impacts on food access during the lean season in Sudan and South Sudan.
  sources:
  - id: source_1
    license: null
    name: NASA TRMM/TMPA 3P43
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Integrated Phase Classification (IPC) / Famine Early Warning Systems Network
      (FEWSNET)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: Armed Conflict Locations and Events Data Project (ACLED)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/rainfall-conflict-and-food-insecurity-measurement-in-post-succession-sudan-and-south-sudan
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Food insecurity classification (IPC) linked to drought-affected agrarian
      populations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: precipitation_anomaly:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: July precipitation anomalies from 2013-2016 for Sudan and South Sudan,
    which may have negatively affected agrarian populations during the lean season,
    are generated from NASA TRMM/TMPA 3P43 (Tropical Rainfall Measuring Mission/Multi-Satellite
    Precipitation Analysis). These anomalies are available to analyze in relation
    local population estimates (WorldPop), reported conflict events and fatalities
    (Armed Conflict Locations and Events Data Project), food security classification
    (Integrated Phase Classification, Famine Early Warning Systems Network), and other
    sources for measuring crop access to water (Climate Hazards Group InfraRed Precipitation
    with Station data).
  download_url: https://data.humdata.org/dataset/c244053c-2a7c-4a2c-b83d-5355725474be/resource/84eac0c8-aff5-424f-a0e7-d2c12099da1d/download/sudan_climate-conflict_dataset.zip
  format: null
  id: resource_84eac0c8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sudan_Climate-Conflict_Dataset.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-sdnssd_drew_rainfallconflictfoodinsec_2013
spatial:
  bbox: null
  centroid: null
  countries:
  - SDN
  - SSD
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-07-31'
  start: '2013-07-31'
temporal_resolution: null
title: Rainfall, Conflict, and Food Insecurity Measurement in Post-Succession Sudan
  and South Sudan (July Months, 2013-2016)
version: null
vulnerability: null
---
