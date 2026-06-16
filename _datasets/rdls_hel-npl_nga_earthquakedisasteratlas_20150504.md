---
attributions:
- entity:
    affiliation: null
    email: null
    name: US National Geospatial-Intelligence Agency (NGA)
    url: https://data.humdata.org/dataset/disaster-atlas
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap (OSM)
    url: https://data.humdata.org/dataset/disaster-atlas
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: US National Geospatial-Intelligence Agency (inactive)
  url: https://data.humdata.org/dataset/disaster-atlas
creator:
  affiliation: null
  email: null
  name: US National Geospatial-Intelligence Agency (inactive)
  url: https://data.humdata.org/dataset/disaster-atlas
dataset_id: rdls_hel-npl_nga_earthquakedisasteratlas_20150504
description: 'Web Map for access and download of MGRS based Disaster Atlases in support
  of ongoing Nepal Earthquake operations. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/disaster-atlas]'
details: null
exposure:
- asset_type:
    description: Building stock and structures affected by earthquake in Nepal
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
- asset_type:
    description: Infrastructure assets including roads and utilities affected by earthquake
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population distribution and settlements in earthquake-affected areas
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_3
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC0-1.0
lineage:
  description: Post-event disaster atlas compiled from NGA geospatial intelligence
    and OSM exposure data to support Nepal earthquake response operations, integrating
    observed earthquake impacts with spatial asset inventories for disaster management.
  sources:
  - id: source_1
    license: null
    name: US National Geospatial-Intelligence Agency (NGA)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: OpenStreetMap (OSM)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-atlas
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage and destruction from earthquake ground motion
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake disaster
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: http://ngamaps.geointapps.org/arcgis/rest/services/NEPAL/Nepal_DisasterMappingAtlas/MapServer/0
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Web Map URL: http://nga.maps.arcgis.com/apps/MapJournal/index.html?appid=bbbb3a2d7d8d42969f6ddeeb5d8c0e73'
  download_url: null
  format: null
  id: resource_6a655070
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Nepal Earthquake Disaster Atlas Web-Service
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_nga_earthquakedisasteratlas_20150504
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-05-04'
temporal_resolution: null
title: Nepal Earthquake Disaster Atlas
version: null
vulnerability: null
---
