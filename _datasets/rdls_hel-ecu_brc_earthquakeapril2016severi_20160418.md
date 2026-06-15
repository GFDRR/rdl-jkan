---
attributions:
- entity:
    affiliation: null
    email: null
    name: USGS Earthquake Hazards Program
    url: https://data.humdata.org/dataset/ecuador-earthquake-april-2016-severity-index
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: HDX Poverty and Population Dataset
    url: https://data.humdata.org/dataset/ecuador-earthquake-april-2016-severity-index
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/ecuador-earthquake-april-2016-severity-index
creator:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/ecuador-earthquake-april-2016-severity-index
dataset_id: rdls_hel-ecu_brc_earthquakeapril2016severi_20160418
description: 'A predictive severity index created using population * poverty * MMI
  Population and Poverty from: https://data.hdx.rwlabs.org/dataset/poverty-and-population
  MMI from: http://earthquake.usgs.gov/earthquakes/eventpage/us20005j32#shakemap.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ecuador-earthquake-april-2016-severity-index]'
details: null
exposure:
- asset_type:
    description: Census population distribution across Ecuador
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
- asset_type:
    description: Poverty index by geographic area
    id: economic_indicator
    scheme: null
    title: null
    uri: null
  category: economic_indicator
  id: exposure_2
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: index
      unit: null
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
  description: A predictive severity index was calculated by multiplying gridded population
    data from census sources, poverty indices, and observed Modified Mercalli Intensity
    values from the USGS shakemap of the April 2016 Ecuador earthquake. This composite
    index identifies areas of highest humanitarian concern by combining hazard intensity
    with population vulnerability and economic deprivation.
  sources:
  - id: source_1
    license: null
    name: USGS Earthquake Hazards Program
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: HDX Poverty and Population Dataset
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ecuador-earthquake-april-2016-severity-index
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Predictive severity index combining population exposure, poverty
      vulnerability, and earthquake ground motion intensity
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
  description: 'A predictive severity index created using population * poverty * Mw
    Population and Poverty from: https://data.hdx.rwlabs.org/dataset/poverty-and-population
    Mw from: http://earthquake.usgs.gov/earthquakes/eventpage/us20005j32#shakemap
    Please note data was missing for 4 Cantons: Las Golondrinas Manga Del Cura El
    Piedrero La Concordia'
  download_url: https://docs.google.com/spreadsheets/d/1OlxhQ_ejRKNvohbnfJ7yJPKD6U6pXcPPfsFnwBbP2nc/edit?usp=drive_web
  format: Google Sheet
  id: resource_58069fa8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ecuador Earthquake - April 2016 - Severity index
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ecu_brc_earthquakeapril2016severi_20160418
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-04-18'
temporal_resolution: null
title: Ecuador Earthquake - April 2016 - Severity index
version: null
vulnerability: null
---
