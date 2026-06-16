---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/mali_current_situation_fewsnet_ipc_shapefile_for_2019
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/mali_current_situation_fewsnet_ipc_shapefile_for_2019
dataset_id: rdls_lss-mli_fewsnet_currentsituationacutefood_2019
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Mali Current Situation FEWS
  NET Acute Food Insecurity Classifications Geographic data for 2019. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mali_current_situation_fewsnet_ipc_shapefile_for_2019]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: FEWS NET enumerators conducted regular (typically monthly) field surveys
    across Mali to classify geographic areas into IPC acute food insecurity phases.
    Survey data were spatially compiled into GeoJSON format representing food insecurity
    classifications at three time points in 2019 (February, June, October), reflecting
    population-level impacts of food security crises.
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
- href: https://data.humdata.org/dataset/mali_current_situation_fewsnet_ipc_shapefile_for_2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population classified by acute food insecurity phase due to drought
      and food security crisis
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
  description: Mali Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2019 (February - 2019 Mali Current Situation FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=ML&scenario=CS&collection_date=2019-02-01&format=geojson
  format: null
  id: resource_1e0e3a4b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2019 Mali Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mali Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2019 (June - 2019 Mali Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=ML&scenario=CS&collection_date=2019-06-01&format=geojson
  format: null
  id: resource_25131c9a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2019 Mali Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mali Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2019 (October - 2019 Mali Current Situation FEWS NET IPC Geographic
    Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=ML&scenario=CS&collection_date=2019-10-01&format=geojson
  format: null
  id: resource_3ce23315
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2019 Mali Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_fewsnet_currentsituationacutefood_2019
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019-12-31'
  start: '2019-01-01'
temporal_resolution: null
title: Mali Current Situation FEWS NET Acute Food Insecurity Classifications Geographic
  Data for 2019
version: null
vulnerability: null
---
