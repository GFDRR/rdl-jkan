---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/chad_current_situation_fewsnet_ipc_shapefile_for_2015
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/chad_current_situation_fewsnet_ipc_shapefile_for_2015
dataset_id: rdls_lss-tcd_fewsnet_currentsituationacutefood_2015
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Chad Current Situation FEWS
  NET Acute Food Insecurity Classifications Geographic data for 2015. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/chad_current_situation_fewsnet_ipc_shapefile_for_2015]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators collected IPC classification data across Chad
    on a monthly basis throughout 2015 (January, April, July, October). The classifications
    were spatially referenced and compiled into geographic datasets (GeoJSON/KML format)
    representing food insecurity phases at sub-national administrative units, providing
    temporal snapshots of acute food insecurity conditions.
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
- href: https://data.humdata.org/dataset/chad_current_situation_fewsnet_ipc_shapefile_for_2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications (IPC phases) for population
      affected by drought conditions
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
  description: Chad Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (January - 2015 Chad Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=TD&scenario=CS&collection_date=2015-01-01&format=geojson
  format: null
  id: resource_ac720cf3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2015 Chad Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (January - 2015 Chad Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=TD&scenario=CS&collection_date=2015-01-01&format=kml
  format: null
  id: resource_aaaaf5c6
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2015 Chad Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (April - 2015 Chad Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=TD&scenario=CS&collection_date=2015-04-01&format=geojson
  format: null
  id: resource_fc3012e8
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2015 Chad Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (April - 2015 Chad Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=TD&scenario=CS&collection_date=2015-04-01&format=kml
  format: null
  id: resource_bd97dd7b
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2015 Chad Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (July - 2015 Chad Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=TD&scenario=CS&collection_date=2015-07-01&format=kml
  format: null
  id: resource_059c01d0
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2015 Chad Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (October - 2015 Chad Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=TD&scenario=CS&collection_date=2015-10-01&format=geojson
  format: null
  id: resource_4c7346f5
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2015 Chad Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Chad Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (October - 2015 Chad Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=TD&scenario=CS&collection_date=2015-10-01&format=kml
  format: null
  id: resource_f208bfd9
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2015 Chad Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-tcd_fewsnet_currentsituationacutefood_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - TCD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: Chad Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2015
version: null
vulnerability: null
---
