---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/uganda_current_situation_fewsnet_ipc_shapefile_for_2011
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/uganda_current_situation_fewsnet_ipc_shapefile_for_2011
dataset_id: rdls_lss-uga_fewsnet_currentsituationacutefood_2011
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Uganda Current Situation FEWS
  NET Acute Food Insecurity Classifications Geographic data for 2011. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/uganda_current_situation_fewsnet_ipc_shapefile_for_2011]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators collected Integrated Food Security Phase Classification
    (IPC) data on a monthly basis throughout 2011 across Uganda. The classifications
    were spatially mapped to geographic units and compiled into GeoJSON and KML formats
    for four observation periods (January, April, July, October). The dataset represents
    post-event or ongoing food insecurity assessments linked to underlying hazards
    such as drought.
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
- href: https://data.humdata.org/dataset/uganda_current_situation_fewsnet_ipc_shapefile_for_2011
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications (IPC phases) affecting populations
      in Uganda
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
    Geographic Data for 2011 (January - 2011 Uganda Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2011-01-01&format=geojson
  format: null
  id: resource_c3894fde
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2011 Uganda Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2011 (January - 2011 Uganda Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2011-01-01&format=kml
  format: null
  id: resource_ddfcaec4
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2011 Uganda Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2011 (April - 2011 Uganda Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2011-04-01&format=kml
  format: null
  id: resource_d511afd1
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2011 Uganda Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2011 (July - 2011 Uganda Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2011-07-01&format=kml
  format: null
  id: resource_ca16b075
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2011 Uganda Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2011 (October - 2011 Uganda Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=UG&scenario=CS&collection_date=2011-10-01&format=kml
  format: null
  id: resource_83dd83b1
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2011 Uganda Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-uga_fewsnet_currentsituationacutefood_2011
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
  end: '2011-12-31'
  start: '2011-01-01'
temporal_resolution: null
title: Uganda Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2011
version: null
vulnerability: null
---
