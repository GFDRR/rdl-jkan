---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2012
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2012
dataset_id: rdls_lss-ken_fewsnet_currentsituationacutefood_2012
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Kenya Current Situation FEWS
  NET Acute Food Insecurity Classifications Geographic data for 2012. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2012]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: FEWS NET enumerators conducted regular (typically monthly) field assessments
    across Kenya to classify acute food insecurity conditions using the IPC framework.
    Geographic data representing IPC phase classifications were compiled into spatial
    datasets (GeoJSON/KML) for January, April, July, and October 2012, capturing temporal
    variation in food insecurity severity across administrative units.
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
- href: https://data.humdata.org/dataset/kenya_current_situation_fewsnet_ipc_shapefile_for_2012
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications (IPC phases) affecting populations
      in Kenya during drought conditions
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
    Geographic Data for 2012 (January - 2012 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2012-01-01&format=geojson
  format: null
  id: resource_77a0453c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2012 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (January - 2012 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2012-01-01&format=kml
  format: null
  id: resource_2e277851
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2012 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (April - 2012 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2012-04-01&format=geojson
  format: null
  id: resource_eaa742a5
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2012 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (April - 2012 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2012-04-01&format=kml
  format: null
  id: resource_7b1d6939
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2012 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (July - 2012 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2012-07-01&format=geojson
  format: null
  id: resource_2c3cc0d2
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2012 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (July - 2012 Kenya Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2012-07-01&format=kml
  format: null
  id: resource_ded6a361
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2012 Kenya Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (October - 2012 Kenya Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=CS&collection_date=2012-10-01&format=kml
  format: null
  id: resource_0872e227
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2012 Kenya Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_fewsnet_currentsituationacutefood_2012
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
  end: '2012-12-31'
  start: '2012-01-01'
temporal_resolution: null
title: Kenya Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2012
version: null
vulnerability: null
---
