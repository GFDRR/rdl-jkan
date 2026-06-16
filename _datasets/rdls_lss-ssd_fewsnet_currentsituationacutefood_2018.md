---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/south_sudan_current_situation_fewsnet_ipc_shapefile_for_2018
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/south_sudan_current_situation_fewsnet_ipc_shapefile_for_2018
dataset_id: rdls_lss-ssd_fewsnet_currentsituationacutefood_2018
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. South Sudan Current Situation
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2018. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/south_sudan_current_situation_fewsnet_ipc_shapefile_for_2018]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC classification data were collected by FEWS NET enumerators on a
    monthly basis across South Sudan administrative units. Geographic boundaries and
    IPC phase classifications (representing food insecurity severity) were compiled
    into GeoJSON and KML formats for multiple time periods in 2018, representing post-event
    or ongoing food security impact assessments.
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
- href: https://data.humdata.org/dataset/south_sudan_current_situation_fewsnet_ipc_shapefile_for_2018
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
  description: South Sudan Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (February - 2018 South Sudan Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=CS&collection_date=2018-02-01&format=geojson
  format: null
  id: resource_25f14835
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2018 South Sudan Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (June - 2018 South Sudan Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=CS&collection_date=2018-06-01&format=geojson
  format: null
  id: resource_25de5d6a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2018 South Sudan Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (June - 2018 South Sudan Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=CS&collection_date=2018-06-01&format=kml
  format: null
  id: resource_8cebabec
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2018 South Sudan Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (October - 2018 South Sudan Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=CS&collection_date=2018-10-01&format=geojson
  format: null
  id: resource_acca11f8
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2018 South Sudan Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2018 (October - 2018 South Sudan Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=CS&collection_date=2018-10-01&format=kml
  format: null
  id: resource_694fe47b
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2018 South Sudan Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_fewsnet_currentsituationacutefood_2018
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2018-12-31'
  start: '2018-01-01'
temporal_resolution: null
title: South Sudan Current Situation FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2018
version: null
vulnerability: null
---
