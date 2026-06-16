---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/rwanda_current_situation_fewsnet_ipc_shapefile_for_2022
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/rwanda_current_situation_fewsnet_ipc_shapefile_for_2022
dataset_id: rdls_lss-rwa_fewsnet_currentsituationacutefood_2022
description: 'Rwanda Current Situation FEWS NET Acute Food Insecurity Classifications
  Geographic data for 2022. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/rwanda_current_situation_fewsnet_ipc_shapefile_for_2022]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC classification data collected by FEWS NET enumerators on a monthly
    schedule across Rwanda, spatially coded to geographic units and classified into
    IPC phases to represent acute food insecurity severity as a loss impact metric
    from underlying drought hazard.
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
- href: https://data.humdata.org/dataset/rwanda_current_situation_fewsnet_ipc_shapefile_for_2022
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
  description: Rwanda Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2022 (January - 2022 Rwanda Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=RW&scenario=CS&collection_date=2022-01-01&format=geojson
  format: null
  id: resource_0f009e99
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2022 Rwanda Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-rwa_fewsnet_currentsituationacutefood_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-31'
  start: '2022-01-01'
temporal_resolution: null
title: Rwanda Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2022
version: null
vulnerability: null
---
