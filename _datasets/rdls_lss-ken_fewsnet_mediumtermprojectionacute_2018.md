---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_medium_term_projection__fewsnet_ipc_shapefile_for_2018
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_medium_term_projection__fewsnet_ipc_shapefile_for_2018
dataset_id: rdls_lss-ken_fewsnet_mediumtermprojectionacute_2018
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Kenya Medium Term Projection
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2018. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/kenya_medium_term_projection__fewsnet_ipc_shapefile_for_2018]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators collected IPC classification data on a monthly
    schedule across Kenya in 2018. Geographic data were compiled into spatial datasets
    (GeoJSON/KML) representing food insecurity phases and scenarios for February,
    June, and December projections, providing medium-term acute food insecurity assessments
    at the sub-national level.
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
- href: https://data.humdata.org/dataset/kenya_medium_term_projection__fewsnet_ipc_shapefile_for_2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classification for populations affected by
      drought conditions
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
  description: Kenya Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (February - 2018 Kenya Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML2&collection_date=2018-02-01&format=geojson
  format: null
  id: resource_17d036b9
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2018 Kenya Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (February - 2018 Kenya Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML2&collection_date=2018-02-01&format=kml
  format: null
  id: resource_036e176d
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2018 Kenya Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (June - 2018 Kenya Medium Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML2&collection_date=2018-06-01&format=geojson
  format: null
  id: resource_03c6f9cb
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2018 Kenya Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (June - 2018 Kenya Medium Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML2&collection_date=2018-06-01&format=kml
  format: null
  id: resource_05913562
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2018 Kenya Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (December - 2018 Kenya Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML2&collection_date=2018-12-01&format=kml
  format: null
  id: resource_8060ff2e
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: December - 2018 Kenya Medium Term Projection FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_fewsnet_mediumtermprojectionacute_2018
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
  end: '2018-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: Kenya Medium Term Projection FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2018
version: null
vulnerability: null
---
