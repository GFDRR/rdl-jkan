---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/niger_medium_term_projection__fewsnet_ipc_shapefile_for_2019
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/niger_medium_term_projection__fewsnet_ipc_shapefile_for_2019
dataset_id: rdls_lss-ner_fewsnet_mediumtermprojectionacute_2019
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Niger Medium Term Projection
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2019. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/niger_medium_term_projection__fewsnet_ipc_shapefile_for_2019]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators collected IPC classification data on a monthly
    schedule across Niger in 2019. Geographic boundaries were mapped with IPC phase
    classifications (1-5 scale) representing acute food insecurity severity. Data
    were compiled into medium-term projections for February, June, and October 2019
    scenarios.
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
- href: https://data.humdata.org/dataset/niger_medium_term_projection__fewsnet_ipc_shapefile_for_2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications for populations affected by
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
  description: Niger Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2019 (February - 2019 Niger Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=ML2&collection_date=2019-02-01&format=geojson
  format: null
  id: resource_ae521e06
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2019 Niger Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2019 (February - 2019 Niger Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=ML2&collection_date=2019-02-01&format=kml
  format: null
  id: resource_09c91d44
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2019 Niger Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2019 (June - 2019 Niger Medium Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=ML2&collection_date=2019-06-01&format=geojson
  format: null
  id: resource_d4fe1133
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2019 Niger Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2019 (June - 2019 Niger Medium Term Projection FEWS NET IPC
    Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=ML2&collection_date=2019-06-01&format=kml
  format: null
  id: resource_0d311a34
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2019 Niger Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niger Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2019 (October - 2019 Niger Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=NE&scenario=ML2&collection_date=2019-10-01&format=geojson
  format: null
  id: resource_d344f391
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2019 Niger Medium Term Projection FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ner_fewsnet_mediumtermprojectionacute_2019
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
  end: '2019-12-31'
  start: '2019-01-01'
temporal_resolution: null
title: Niger Medium Term Projection FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2019
version: null
vulnerability: null
---
