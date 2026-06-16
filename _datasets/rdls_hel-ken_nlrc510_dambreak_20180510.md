---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap Team (HOTOSM)
    url: https://data.humdata.org/dataset/kenya-dam-break
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Airbus Satellite Imagery
    url: https://data.humdata.org/dataset/kenya-dam-break
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/kenya-dam-break
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/kenya-dam-break
dataset_id: rdls_hel-ken_nlrc510_dambreak_20180510
description: 'Datasets and map of dam break near solai in Kenya on May 9th 2018..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/kenya-dam-break]'
details: null
exposure:
- asset_type:
    description: Building footprints and inventory in the study area derived from
      pre-disaster satellite imagery and OpenStreetMap
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Pre-disaster building inventory was extracted from satellite imagery
    using HOTOSM tools and OpenStreetMap data. Post-event flood extent was delineated
    from Airbus satellite imagery acquired after the May 9, 2018 dam break. Affected
    buildings were identified by spatial intersection of the building inventory with
    the mapped flood zone to quantify direct structural damage.
  sources:
  - id: source_1
    license: null
    name: Netherlands Red Cross - 510
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian OpenStreetMap Team (HOTOSM)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Airbus Satellite Imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kenya-dam-break
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the May 2018 dam break flood event, identified
      by intersection of affected buildings with flood extent
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: OpenStreetMap buildings. Some buildings where manually traced outside
    of OSM and added to this dataset.
  download_url: https://data.humdata.org/dataset/9eab8aec-ed8e-4478-aaa1-7a22f39f0481/resource/14e32456-40ae-43c6-be24-72c7b5d35a1b/download/kenya-dam-break_planet_osm_polygon_buildings.zip
  format: null
  id: resource_14e32456
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kenya-dam-break_planet_osm_polygon_buildings.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Openstreetmap affected buildings. Some buildings where manually traced
    outside of OSM and added to this dataset.
  download_url: https://data.humdata.org/dataset/9eab8aec-ed8e-4478-aaa1-7a22f39f0481/resource/60b5124e-aa14-468b-8784-de19efad45ac/download/kenya-dam-break_planet_osm_polygon_affected_buildings.zip
  format: null
  id: resource_60b5124e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kenya-dam-break_planet_osm_polygon_affected_buildings.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Dam Break (Floodzone derived from satellite imagery)
  download_url: https://data.humdata.org/dataset/9eab8aec-ed8e-4478-aaa1-7a22f39f0481/resource/7b11e9d7-437f-475a-98bb-f359eff4251f/download/flood_zone-1.zip
  format: null
  id: resource_7b11e9d7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: floodzone.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_nlrc510_dambreak_20180510
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-05-10'
temporal_resolution: null
title: Kenya Dam Break
version: null
vulnerability: null
---
