---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/mozambique_current_situation_fewsnet_ipc_shapefile_for_2015
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/mozambique_current_situation_fewsnet_ipc_shapefile_for_2015
dataset_id: rdls_lss-moz_fewsnet_currentsituationacutefood_2015
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Mozambique Current Situation
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2015. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mozambique_current_situation_fewsnet_ipc_shapefile_for_2015]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: FEWS NET enumerators collected IPC classification data across Mozambique
    on a monthly basis throughout 2015. The classifications represent spatial assessments
    of acute food insecurity phases, which are typically triggered by drought and
    other hazards affecting food availability and access. The data was compiled into
    geographic datasets (GeoJSON and KML formats) with temporal coverage for January,
    April, July, and October 2015.
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
- href: https://data.humdata.org/dataset/mozambique_current_situation_fewsnet_ipc_shapefile_for_2015
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications derived from drought and food
      security conditions affecting populations
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
  description: Mozambique Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (January - 2015 Mozambique Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=CS&collection_date=2015-01-01&format=geojson
  format: null
  id: resource_5b0bc1c0
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2015 Mozambique Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (January - 2015 Mozambique Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=CS&collection_date=2015-01-01&format=kml
  format: null
  id: resource_921c8e91
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2015 Mozambique Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (April - 2015 Mozambique Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=CS&collection_date=2015-04-01&format=geojson
  format: null
  id: resource_789ea446
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2015 Mozambique Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (April - 2015 Mozambique Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=CS&collection_date=2015-04-01&format=kml
  format: null
  id: resource_8e5286f1
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2015 Mozambique Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (July - 2015 Mozambique Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=CS&collection_date=2015-07-01&format=geojson
  format: null
  id: resource_42ac215e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2015 Mozambique Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (October - 2015 Mozambique Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=CS&collection_date=2015-10-01&format=geojson
  format: null
  id: resource_624436e1
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2015 Mozambique Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2015 (October - 2015 Mozambique Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=CS&collection_date=2015-10-01&format=kml
  format: null
  id: resource_54f01fdf
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2015 Mozambique Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_fewsnet_currentsituationacutefood_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: Mozambique Current Situation FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2015
version: null
vulnerability: null
---
