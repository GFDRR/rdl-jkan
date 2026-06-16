---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/sierra_leone_medium_term_projection__fewsnet_ipc_shapefile_for_2015
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/sierra_leone_medium_term_projection__fewsnet_ipc_shapefile_for_2015
dataset_id: rdls_lss-sle_fewsnet_mediumtermprojectionacute_2015
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Sierra Leone Medium Term Projection
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2015. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/sierra_leone_medium_term_projection__fewsnet_ipc_shapefile_for_2015]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators conducted regular (typically monthly) surveys
    to classify acute food insecurity conditions using the IPC framework. Geographic
    data for October 2015 medium-term projections were compiled into spatial datasets
    representing food insecurity classifications across Sierra Leone.
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
- href: https://data.humdata.org/dataset/sierra_leone_medium_term_projection__fewsnet_ipc_shapefile_for_2015
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
  description: Sierra Leone Medium Term Projection FEWS NET Acute Food Insecurity
    Classifications Geographic Data for 2015 (October - 2015 Sierra Leone Medium Term
    Projection FEWS NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SL&scenario=ML2&collection_date=2015-10-01&format=geojson
  format: null
  id: resource_19232fb8
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2015 Sierra Leone Medium Term Projection FEWS NET IPC Geographic
    Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-sle_fewsnet_mediumtermprojectionacute_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - SLE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2015-12-31'
  start: '2015-01-01'
temporal_resolution: null
title: Sierra Leone Medium Term Projection FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2015
version: null
vulnerability: null
---
