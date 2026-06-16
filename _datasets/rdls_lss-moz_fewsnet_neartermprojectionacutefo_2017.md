---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/mozambique_near_term_projection__fewsnet_ipc_shapefile_for_2017
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/mozambique_near_term_projection__fewsnet_ipc_shapefile_for_2017
dataset_id: rdls_lss-moz_fewsnet_neartermprojectionacutefo_2017
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Mozambique Near Term Projection
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2017. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mozambique_near_term_projection__fewsnet_ipc_shapefile_for_2017]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: FEWS NET enumerators collected IPC classification data on a monthly
    schedule across Mozambique in 2017. Geographic boundaries were classified into
    IPC phases (1-5) representing acute food insecurity severity levels. Data were
    compiled into near-term projection scenarios for February, June, and October 2017
    and distributed as geospatial features (GeoJSON/KML).
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
- href: https://data.humdata.org/dataset/mozambique_near_term_projection__fewsnet_ipc_shapefile_for_2017
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications for population affected by
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
  description: Mozambique Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (February - 2017 Mozambique Near Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=ML1&collection_date=2017-02-01&format=geojson
  format: null
  id: resource_7aaf3836
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2017 Mozambique Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (February - 2017 Mozambique Near Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=ML1&collection_date=2017-02-01&format=kml
  format: null
  id: resource_2285ba0f
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2017 Mozambique Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (June - 2017 Mozambique Near Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=ML1&collection_date=2017-06-01&format=geojson
  format: null
  id: resource_82d62239
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2017 Mozambique Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (October - 2017 Mozambique Near Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=ML1&collection_date=2017-10-01&format=geojson
  format: null
  id: resource_362b5549
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2017 Mozambique Near Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mozambique Near Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2017 (October - 2017 Mozambique Near Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MZ&scenario=ML1&collection_date=2017-10-01&format=kml
  format: null
  id: resource_6781f5d4
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2017 Mozambique Near Term Projection FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_fewsnet_neartermprojectionacutefo_2017
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
  end: '2017-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: Mozambique Near Term Projection FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2017
version: null
vulnerability: null
---
