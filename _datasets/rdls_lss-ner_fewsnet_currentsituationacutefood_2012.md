---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/niger_current_situation_fewsnet_ipc_shapefile_for_2012
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/niger_current_situation_fewsnet_ipc_shapefile_for_2012
dataset_id: rdls_lss-ner_fewsnet_currentsituationacutefood_2012
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Niger Current Situation FEWS
  NET Acute Food Insecurity Classifications Geographic data for 2012. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/niger_current_situation_fewsnet_ipc_shapefile_for_2012]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators collected IPC classification data across Niger
    on a monthly basis throughout 2012, classifying geographic areas by acute food
    insecurity phase. The spatial data was compiled into GeoJSON and KML formats representing
    food insecurity classifications at four time points (January, April, July, October
    2012).
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
- href: https://data.humdata.org/dataset/niger_current_situation_fewsnet_ipc_shapefile_for_2012
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications for populations affected by
      drought conditions in Niger
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
  description: Niger Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (January - 2012 Niger Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=CS&collection_date=2012-01-01&format=geojson
  format: null
  id: resource_9e2d19f3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2012 Niger Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (January - 2012 Niger Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=CS&collection_date=2012-01-01&format=kml
  format: null
  id: resource_383a0963
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2012 Niger Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (April - 2012 Niger Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=CS&collection_date=2012-04-01&format=geojson
  format: null
  id: resource_ba077089
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2012 Niger Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (April - 2012 Niger Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=CS&collection_date=2012-04-01&format=kml
  format: null
  id: resource_1ce56ca8
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2012 Niger Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (July - 2012 Niger Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=CS&collection_date=2012-07-01&format=kml
  format: null
  id: resource_2cc15d53
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2012 Niger Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (October - 2012 Niger Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=CS&collection_date=2012-10-01&format=geojson
  format: null
  id: resource_88e9d257
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2012 Niger Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2012 (October - 2012 Niger Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=CS&collection_date=2012-10-01&format=kml
  format: null
  id: resource_9d25fbb3
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2012 Niger Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ner_fewsnet_currentsituationacutefood_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - NER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2012-12-31'
  start: '2012-01-01'
temporal_resolution: null
title: Niger Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2012
version: null
vulnerability: null
---
