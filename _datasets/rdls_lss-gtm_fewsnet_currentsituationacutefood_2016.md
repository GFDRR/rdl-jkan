---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/guatemala_current_situation_fewsnet_ipc_shapefile_for_2016
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/guatemala_current_situation_fewsnet_ipc_shapefile_for_2016
dataset_id: rdls_lss-gtm_fewsnet_currentsituationacutefood_2016
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Guatemala Current Situation
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2016. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/guatemala_current_situation_fewsnet_ipc_shapefile_for_2016]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: FEWS NET enumerators collected IPC classification data across Guatemala
    on a monthly basis (February, June, October 2016). Raw classifications were spatially
    referenced and compiled into geographic datasets (GeoJSON/KML) representing food
    insecurity phases by administrative unit. The IPC framework integrates multiple
    livelihood and food security indicators to classify populations into food insecurity
    phases, serving as a loss/impact dataset for humanitarian response planning.
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
- href: https://data.humdata.org/dataset/guatemala_current_situation_fewsnet_ipc_shapefile_for_2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications derived from drought and other
      livelihood shocks affecting populations
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
  description: Guatemala Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (February - 2016 Guatemala Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=GT&scenario=CS&collection_date=2016-02-01&format=geojson
  format: null
  id: resource_23855a3a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2016 Guatemala Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Guatemala Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (February - 2016 Guatemala Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=GT&scenario=CS&collection_date=2016-02-01&format=kml
  format: null
  id: resource_8815ede2
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2016 Guatemala Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Guatemala Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (June - 2016 Guatemala Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=GT&scenario=CS&collection_date=2016-06-01&format=geojson
  format: null
  id: resource_ad09b22e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2016 Guatemala Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Guatemala Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (June - 2016 Guatemala Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=GT&scenario=CS&collection_date=2016-06-01&format=kml
  format: null
  id: resource_5ad95dcd
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2016 Guatemala Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Guatemala Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (October - 2016 Guatemala Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=GT&scenario=CS&collection_date=2016-10-01&format=geojson
  format: null
  id: resource_aa08e8f6
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2016 Guatemala Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Guatemala Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (October - 2016 Guatemala Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=GT&scenario=CS&collection_date=2016-10-01&format=kml
  format: null
  id: resource_e35e7ce3
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2016 Guatemala Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_fewsnet_currentsituationacutefood_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Guatemala Current Situation FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2016
version: null
vulnerability: null
---
