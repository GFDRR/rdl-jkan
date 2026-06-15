---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/ethiopia_current_situation_fewsnet_ipc_shapefile_for_2022
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/ethiopia_current_situation_fewsnet_ipc_shapefile_for_2022
dataset_id: rdls_lss-eth_fewsnet_currentsituationacutefood_2022
description: 'Ethiopia Current Situation FEWS NET Acute Food Insecurity Classifications
  Geographic data for 2022. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia_current_situation_fewsnet_ipc_shapefile_for_2022]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators collected IPC classification data on a regular
    monthly schedule across Ethiopia in 2022. The spatial data represents acute food
    insecurity phases classified according to IPC standards, which serve as impact
    indicators of underlying drought hazards affecting food security.
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
- href: https://data.humdata.org/dataset/ethiopia_current_situation_fewsnet_ipc_shapefile_for_2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classification of population affected by drought
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
  description: Ethiopia Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2022 (January - 2022 Ethiopia Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=ET&scenario=CS&collection_date=2022-01-01&format=geojson
  format: null
  id: resource_2d649e91
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2022 Ethiopia Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2022 (January - 2022 Ethiopia Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=ET&scenario=CS&collection_date=2022-01-01&format=kml
  format: null
  id: resource_6f39c25e
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2022 Ethiopia Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2022 (February - 2022 Ethiopia Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=ET&scenario=CS&collection_date=2022-02-01&format=geojson
  format: null
  id: resource_c6257d5f
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2022 Ethiopia Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ethiopia Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2022 (February - 2022 Ethiopia Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=ET&scenario=CS&collection_date=2022-02-01&format=kml
  format: null
  id: resource_a57a4aa7
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2022 Ethiopia Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-eth_fewsnet_currentsituationacutefood_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-12-31'
  start: '2022-01-01'
temporal_resolution: null
title: Ethiopia Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2022
version: null
vulnerability: null
---
