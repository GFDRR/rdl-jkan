---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/liberia_medium_term_projection__fewsnet_ipc_shapefile_for_2016
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/liberia_medium_term_projection__fewsnet_ipc_shapefile_for_2016
dataset_id: rdls_lss-lbr_fewsnet_mediumtermprojectionacute_2016
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Liberia Medium Term Projection
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2016. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/liberia_medium_term_projection__fewsnet_ipc_shapefile_for_2016]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IPC acute food insecurity phase classifications were collected by FEWS
    NET field enumerators on a regular schedule and assigned to sub-national geographic
    units in Liberia. The data represents medium-term projection scenarios for February,
    June, and October 2016, encoded as GeoJSON and KML spatial files with scenario,
    period, and classification value attributes. The dataset supports food security
    early warning and humanitarian response planning.
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
- href: https://data.humdata.org/dataset/liberia_medium_term_projection__fewsnet_ipc_shapefile_for_2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: FEWS NET IPC acute food insecurity phase classifications for Liberia
      sub-national areas under medium-term projection scenarios for 2016
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
  description: Liberia Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (February - 2016 Liberia Medium Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=LR&scenario=ML2&collection_date=2016-02-01&format=geojson
  format: null
  id: resource_4bde6a14
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2016 Liberia Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liberia Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (June - 2016 Liberia Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=LR&scenario=ML2&collection_date=2016-06-01&format=geojson
  format: null
  id: resource_99098f1d
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2016 Liberia Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liberia Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (June - 2016 Liberia Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=LR&scenario=ML2&collection_date=2016-06-01&format=kml
  format: null
  id: resource_19e06834
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2016 Liberia Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liberia Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (October - 2016 Liberia Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=LR&scenario=ML2&collection_date=2016-10-01&format=geojson
  format: null
  id: resource_6394329d
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2016 Liberia Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Liberia Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (October - 2016 Liberia Medium Term Projection FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=LR&scenario=ML2&collection_date=2016-10-01&format=kml
  format: null
  id: resource_c936947e
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2016 Liberia Medium Term Projection FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lbr_fewsnet_mediumtermprojectionacute_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - LBR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Liberia Medium Term Projection FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2016
version: null
vulnerability: null
---
