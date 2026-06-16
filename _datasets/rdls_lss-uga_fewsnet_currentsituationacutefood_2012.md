---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/uganda_current_situation_fewsnet_ipc_shapefile_for_2012
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/uganda_current_situation_fewsnet_ipc_shapefile_for_2012
dataset_id: rdls_lss-uga_fewsnet_currentsituationacutefood_2012
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Uganda Current Situation FEWS
  NET Acute Food Insecurity Classifications Geographic data for 2012. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/uganda_current_situation_fewsnet_ipc_shapefile_for_2012]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators collected IPC classification data on a monthly
    basis throughout 2012 across Uganda, classifying geographic areas into food insecurity
    phases. The data represents post-assessment impact classifications of populations
    experiencing acute food insecurity, with temporal snapshots captured in January,
    April, July, and October 2012.
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
- href: https://data.humdata.org/dataset/uganda_current_situation_fewsnet_ipc_shapefile_for_2012
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
  description: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (January - 2012 Uganda Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2012-01-01&format=geojson
  format: null
  id: resource_69add66e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2012 Uganda Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (January - 2012 Uganda Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2012-01-01&format=kml
  format: null
  id: resource_e99cf61b
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2012 Uganda Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (April - 2012 Uganda Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2012-04-01&format=kml
  format: null
  id: resource_69158bf1
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2012 Uganda Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (July - 2012 Uganda Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2012-07-01&format=kml
  format: null
  id: resource_29e22d35
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2012 Uganda Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (October - 2012 Uganda Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2012-10-01&format=kml
  format: null
  id: resource_ae2a5a1b
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2012 Uganda Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-uga_fewsnet_currentsituationacutefood_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - UGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2012-12-31'
  start: '2012-01-01'
temporal_resolution: null
title: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2012
version: null
vulnerability: null
---
