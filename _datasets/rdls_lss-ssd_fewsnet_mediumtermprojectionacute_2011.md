---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/south_sudan_medium_term_projection__fewsnet_ipc_shapefile_for_2011
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/south_sudan_medium_term_projection__fewsnet_ipc_shapefile_for_2011
dataset_id: rdls_lss-ssd_fewsnet_mediumtermprojectionacute_2011
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. South Sudan Medium Term Projection
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2011. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/south_sudan_medium_term_projection__fewsnet_ipc_shapefile_for_2011]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: FEWS NET enumerators collected IPC classification data on a monthly
    schedule across South Sudan in 2011. Geographic boundaries were classified into
    IPC phases representing acute food insecurity severity levels, with multiple scenarios
    projected for medium-term periods. Data was compiled into spatial datasets (GeoJSON/KML)
    with classification metadata including collection dates and scenario parameters.
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
- href: https://data.humdata.org/dataset/south_sudan_medium_term_projection__fewsnet_ipc_shapefile_for_2011
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
  description: South Sudan Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2011 (January - 2011 South Sudan Medium Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=ML2&collection_date=2011-01-01&format=geojson
  format: null
  id: resource_39702628
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2011 South Sudan Medium Term Projection FEWS NET IPC Geographic
    Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2011 (January - 2011 South Sudan Medium Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=ML2&collection_date=2011-01-01&format=kml
  format: null
  id: resource_b49dbae0
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: January - 2011 South Sudan Medium Term Projection FEWS NET IPC Geographic
    Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2011 (April - 2011 South Sudan Medium Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=ML2&collection_date=2011-04-01&format=kml
  format: null
  id: resource_a20834da
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: April - 2011 South Sudan Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2011 (July - 2011 South Sudan Medium Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=ML2&collection_date=2011-07-01&format=geojson
  format: null
  id: resource_6e49b9f0
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: July - 2011 South Sudan Medium Term Projection FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan Medium Term Projection FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2011 (October - 2011 South Sudan Medium Term Projection FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=SS&scenario=ML2&collection_date=2011-10-01&format=geojson
  format: null
  id: resource_9e0f2a49
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2011 South Sudan Medium Term Projection FEWS NET IPC Geographic
    Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_fewsnet_mediumtermprojectionacute_2011
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2011-12-31'
  start: '2011-01-01'
temporal_resolution: null
title: South Sudan Medium Term Projection FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2011
version: null
vulnerability: null
---
