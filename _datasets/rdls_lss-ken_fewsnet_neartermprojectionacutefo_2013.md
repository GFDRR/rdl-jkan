---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_near_term_projection__fewsnet_ipc_shapefile_for_2013
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/kenya_near_term_projection__fewsnet_ipc_shapefile_for_2013
dataset_id: rdls_lss-ken_fewsnet_neartermprojectionacutefo_2013
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Kenya Near Term Projection
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2013. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/kenya_near_term_projection__fewsnet_ipc_shapefile_for_2013]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: FEWS NET enumerators collected IPC classification data across Kenya
    on a regular monthly schedule (January, April, July, October 2013). The classifications
    were spatially mapped to administrative units and stored in GeoJSON/KML formats
    with metadata including classification scale, scenario projections, and assistance
    requirements. This dataset represents post-assessment food insecurity impact classifications
    derived from field assessments.
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
- href: https://data.humdata.org/dataset/kenya_near_term_projection__fewsnet_ipc_shapefile_for_2013
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications (IPC phases) for populations
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
  description: Kenya Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2013 (January - 2013 Kenya Near Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML1&collection_date=2013-01-01&format=geojson
  format: null
  id: resource_2c59753b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2013 Kenya Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2013 (January - 2013 Kenya Near Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML1&collection_date=2013-01-01&format=kml
  format: null
  id: resource_d6fead78
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2013 Kenya Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2013 (April - 2013 Kenya Near Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML1&collection_date=2013-04-01&format=geojson
  format: null
  id: resource_9d4ac44b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2013 Kenya Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2013 (April - 2013 Kenya Near Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML1&collection_date=2013-04-01&format=kml
  format: null
  id: resource_f2779bab
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2013 Kenya Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2013 (July - 2013 Kenya Near Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML1&collection_date=2013-07-01&format=geojson
  format: null
  id: resource_19ebf7ea
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2013 Kenya Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2013 (July - 2013 Kenya Near Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML1&collection_date=2013-07-01&format=kml
  format: null
  id: resource_e4e5ac2a
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2013 Kenya Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2013 (October - 2013 Kenya Near Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML1&collection_date=2013-10-01&format=geojson
  format: null
  id: resource_beef1086
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2013 Kenya Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2013 (October - 2013 Kenya Near Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=KE&scenario=ML1&collection_date=2013-10-01&format=kml
  format: null
  id: resource_f2800dc4
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2013 Kenya Near Term Projection FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_fewsnet_neartermprojectionacutefo_2013
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
  end: '2013-12-31'
  start: '2013-01-01'
temporal_resolution: null
title: Kenya Near Term Projection FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2013
version: null
vulnerability: null
---
