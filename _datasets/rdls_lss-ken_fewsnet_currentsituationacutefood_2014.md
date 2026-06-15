---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2014
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2014
dataset_id: rdls_lss-ken_fewsnet_currentsituationacutefood_2014
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Kenya Current Situation FEWS
  NET Acute Food Insecurity Classifications Geographic data for 2014. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2014]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC classification data were collected by FEWS NET enumerators on a
    monthly schedule throughout 2014 across Kenya. The classifications represent spatial
    assessments of acute food insecurity phases, which are indirect impacts of underlying
    drought hazards. Data were compiled into geographic datasets (GeoJSON/KML) with
    temporal snapshots at January, April, July, and October 2014.
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
- href: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classification of population affected by drought
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
    Geographic Data for 2014 (January - 2014 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2014-01-01&format=geojson
  format: null
  id: resource_96599e76
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2014 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2014 (January - 2014 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2014-01-01&format=kml
  format: null
  id: resource_f6935412
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2014 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2014 (April - 2014 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2014-04-01&format=geojson
  format: null
  id: resource_5e42a70d
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2014 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2014 (April - 2014 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2014-04-01&format=kml
  format: null
  id: resource_96065be2
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2014 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2014 (July - 2014 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2014-07-01&format=geojson
  format: null
  id: resource_22eb17c3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2014 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2014 (July - 2014 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2014-07-01&format=kml
  format: null
  id: resource_455bee95
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2014 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2014 (October - 2014 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2014-10-01&format=geojson
  format: null
  id: resource_da4ad90e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2014 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2014 (October - 2014 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2014-10-01&format=kml
  format: null
  id: resource_4e96617b
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2014 Kenya Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_fewsnet_currentsituationacutefood_2014
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
  end: '2014-12-31'
  start: '2014-01-01'
temporal_resolution: null
title: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2014
version: null
vulnerability: null
---
