---
attributions:
- entity:
    affiliation: null
    email: null
    name: Maxar and Planet satellite imagery
    url: https://data.humdata.org/dataset/hotosm_mmr_damaged_buildings
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_mmr_damaged_buildings
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/hotosm_mmr_damaged_buildings
dataset_id: rdls_hl-mmr_hotosm_damagedbuildingsexport_20251026
description: 'Humanitarian OpenStreetMap Team (HOT) conducted a pilot of Crowdsourced
  Damage Assessment (CDA) with local mappers from the Myanmar OpenStreetMap Community
  (myOSM) to identify and map damaged buildings in priority affected townships from
  the March 2025 Myanmar earthquake. Through the CDA, mappers will review damaged
  buildings by comparing pre- and post-disaster satellite imageries (from Maxar and
  Planet) to identify signs of damages. These were reviewed, mapped, and validated
  with open-source tools MapSwipe, HOT Tasking Manager, and MapRoulette. Damage assessments
  were conducted in 20 townships, including: Bago, Magway, Aungmyaythazan, Chanayethazan,
  Mahaaungmyay, Chanmyathazi, Pyigyitagon, Amarapura, Sintgaing, Kyaukse, Meiktila,
  Thazi, Patheingyi, Za Bu Thi Ri, Det Khi Na Thi Ri, Pyinmana, Poke Ba Thi Ri, Oke
  Ta Ra Thi Ri, Lewe, and Sagaing. This dataset includes all OpenStreetMap features
  (nodes, ways, and relations) within Myanmar that contain any tag key related to
  ''damage''. ) Features may have these attributes: name building damage damage:event
  source:damage source:damage:date addr:street addr:city source This dataset is one
  of many OpenStreetMap exports on HDX . See the Humanitarian OpenStreetMap Team website
  for more information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hotosm_mmr_damaged_buildings]'
details: OpenStreetMap data is crowd sourced and cannot be considered to be exhaustive
exposure: []
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Local OpenStreetMap mappers conducted crowdsourced damage assessment
    by comparing pre- and post-disaster satellite imagery (Maxar and Planet) to identify
    damaged buildings in 20 priority townships affected by the March 2025 Myanmar
    earthquake. Damage observations were validated using open-source mapping tools
    (MapSwipe, HOT Tasking Manager, MapRoulette) and compiled into geospatial datasets
    documenting direct building damage from the earthquake event.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap Team (HOT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Maxar and Planet satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hotosm_mmr_damaged_buildings
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from March 2025 Myanmar earthquake assessed
      through pre- and post-event satellite imagery comparison
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Myanmar Damaged Buildings (OpenStreetMap Export) (GeoJSON)
  download_url: https://data.humdata.org/dataset/dfca769f-f305-4106-afcc-c4f78d399d6c/resource/52f23b1e-1835-4df7-94e3-f085a9d8bf28/download/hotosm_mmr_damaged_buildings.geojson
  format: null
  id: resource_52f23b1e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mmr_damaged_buildings.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Myanmar Damaged Buildings (OpenStreetMap Export) (KML)
  download_url: https://data.humdata.org/dataset/dfca769f-f305-4106-afcc-c4f78d399d6c/resource/17d4d4da-6163-471b-a35f-f296d6383b39/download/hotosm_mmr_damaged_buildings.kml
  format: null
  id: resource_17d4d4da
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hotosm_mmr_damaged_buildings.kml
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mmr_hotosm_damagedbuildingsexport_20251026
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-10-26'
temporal_resolution: null
title: Myanmar Damaged Buildings (OpenStreetMap Export)
version: null
vulnerability: null
---
