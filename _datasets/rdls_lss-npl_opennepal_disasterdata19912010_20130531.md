---
attributions:
- entity:
    affiliation: null
    email: null
    name: DesInventar
    url: https://data.humdata.org/dataset/disaster-data-from-1991-2010
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/disaster-data-from-1991-2010
creator:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/disaster-data-from-1991-2010
dataset_id: rdls_lss-npl_opennepal_disasterdata19912010_20130531
description: 'The dataset includes the disasters that occurred in Nepal from the year
  1971 to the year 1990.The data is obtained from http://www.desinventar.net/DesInventar/report.jsp..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/disaster-data-from-1991-2010]'
details: null
exposure: []
hazard: null
license: ODbL-1.0/
lineage:
  description: Historical disaster impact data compiled from DesInventar, a global
    disaster inventory system, documenting reported events in Nepal from 1971-1990
    with associated damage and affected population figures across multiple hazard
    types.
  sources:
  - id: source_1
    license: null
    name: DesInventar
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/disaster-data-from-1991-2010
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding events
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake events
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
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
    description: Population affected by flooding events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_4
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_5
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by landslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_6
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - Disaster data from 1991-2010 (CSV)
  download_url: http://data.opennepal.net/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://data.opennepal.net/sites/default/files/resources/disaster_data_1991_2010_0.csv&nid=123
  format: null
  id: resource_dc846257
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: disaster_data_1991_2010_0.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_opennepal_disasterdata19912010_20130531
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
  start: '2013-05-31'
temporal_resolution: null
title: Nepal - Disaster data from 1991-2010
version: null
vulnerability: null
---
