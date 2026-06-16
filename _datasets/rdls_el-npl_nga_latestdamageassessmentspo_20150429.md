---
attributions:
- entity:
    affiliation: null
    email: null
    name: US National Geospatial-Intelligence Agency (NGA)
    url: https://data.humdata.org/dataset/http-nepal-nga-opendata-arcgis-com-datasets-eb0bba9bbb0d46c69b4bdf541ea2300e-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: US National Geospatial-Intelligence Agency (inactive)
  url: https://data.humdata.org/dataset/http-nepal-nga-opendata-arcgis-com-datasets-eb0bba9bbb0d46c69b4bdf541ea2300e-0
creator:
  affiliation: null
  email: null
  name: US National Geospatial-Intelligence Agency (inactive)
  url: https://data.humdata.org/dataset/http-nepal-nga-opendata-arcgis-com-datasets-eb0bba9bbb0d46c69b4bdf541ea2300e-0
dataset_id: rdls_el-npl_nga_latestdamageassessmentspo_20150429
description: 'NGA Damage Assessment Centroids, IDP Camps, Coverd Roads Nepal Earthquake.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/http-nepal-nga-opendata-arcgis-com-datasets-eb0bba9bbb0d46c69b4bdf541ea2300e-0]'
details: null
exposure:
- asset_type:
    description: Building structures assessed for damage from the Nepal earthquake
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
    description: Road network coverage assessed post-earthquake
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
      quantity_kind: length
      unit: null
- asset_type:
    description: Internally displaced persons in IDP camps
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
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: Post-event damage assessments conducted by NGA using direct observational
    and anecdotal data collection methods following the Nepal earthquake. Damage centroids,
    IDP camp locations, and affected road infrastructure were georeferenced and compiled
    into a centralized GeoJSON dataset for spatial analysis of earthquake impacts.
  sources:
  - id: source_1
    license: null
    name: US National Geospatial-Intelligence Agency (NGA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/http-nepal-nga-opendata-arcgis-com-datasets-eb0bba9bbb0d46c69b4bdf541ea2300e-0
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessments from the Nepal earthquake
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
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population displacement recorded in IDP camps following the earthquake
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
        metric: displaced
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Latest NGA Damage Assessments Points (NGA Damage Assessment
    Centroids, IDP Camps, Coverd Roads Nepal Earthquake)
  download_url: http://nepal.nga.opendata.arcgis.com/datasets/eb0bba9bbb0d46c69b4bdf541ea2300e_0.geojson
  format: null
  id: resource_5265b11a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Latest NGA Damage Assessments Points
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-npl_nga_latestdamageassessmentspo_20150429
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
  start: '2015-04-29'
temporal_resolution: null
title: Nepal - Latest NGA Damage Assessments Points
version: null
vulnerability: null
---
