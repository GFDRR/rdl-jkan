---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2017
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2017
dataset_id: rdls_lss-ken_fewsnet_currentsituationacutefood_2017
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Kenya Current Situation FEWS
  NET Acute Food Insecurity Classifications Geographic data for 2017. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2017]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IPC classification data collected by FEWS NET enumerators across Kenya
    on a monthly basis (February, June, October 2017) through field assessments and
    integrated analysis of food security indicators. Geographic polygons represent
    administrative units classified into IPC phases indicating severity of acute food
    insecurity, with metadata on collection dates, scenarios, and assistance eligibility.
  sources:
  - id: source_1
    license: null
    name: FEWS NET
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classification of populations affected by drought
      conditions
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: IPC Classification spatial data in different IPC scenarios collected by FEWS
  NET enumerators on a regular schedule (typically monthly).
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (February - 2017 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2017-02-01&format=geojson
  format: null
  id: resource_4f8a4fbb
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2017 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (February - 2017 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2017-02-01&format=kml
  format: null
  id: resource_e236e6dd
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2017 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (June - 2017 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2017-06-01&format=geojson
  format: null
  id: resource_d722b6ca
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2017 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (June - 2017 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2017-06-01&format=kml
  format: null
  id: resource_e0f01807
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2017 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (October - 2017 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2017-10-01&format=kml
  format: null
  id: resource_e49885c3
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2017 Kenya Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_fewsnet_currentsituationacutefood_2017
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
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2017
version: null
vulnerability: null
---
