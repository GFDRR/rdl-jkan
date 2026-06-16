---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/honduras_medium_term_projection__fewsnet_ipc_shapefile_for_2020
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/honduras_medium_term_projection__fewsnet_ipc_shapefile_for_2020
dataset_id: rdls_lss-hnd_fewsnet_mediumtermprojectionacute_2020
description: 'Honduras Medium Term Projection FEWS NET Acute Food Insecurity Classifications
  Geographic data for 2020. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/honduras_medium_term_projection__fewsnet_ipc_shapefile_for_2020]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators conducted regular (typically monthly) field surveys
    to classify acute food insecurity conditions using the IPC methodology. Survey
    results were spatially mapped and compiled into geographic datasets for October,
    November, and December 2020 medium-term projections, representing modeled food
    insecurity impact classifications.
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
- href: https://data.humdata.org/dataset/honduras_medium_term_projection__fewsnet_ipc_shapefile_for_2020
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications derived from drought and other
      livelihood shocks affecting population food security status
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
  description: Honduras Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2020 (October - 2020 Honduras Medium Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=HN&scenario=ML2&collection_date=2020-10-01&format=geojson
  format: null
  id: resource_4fda4bab
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2020 Honduras Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Honduras Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2020 (November - 2020 Honduras Medium Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=HN&scenario=ML2&collection_date=2020-11-01&format=geojson
  format: null
  id: resource_ec5e2782
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: November - 2020 Honduras Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Honduras Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2020 (December - 2020 Honduras Medium Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=HN&scenario=ML2&collection_date=2020-12-01&format=geojson
  format: null
  id: resource_7bce96f9
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: December - 2020 Honduras Medium Term Projection FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hnd_fewsnet_mediumtermprojectionacute_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - HND
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: Honduras Medium Term Projection FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2020
version: null
vulnerability: null
---
