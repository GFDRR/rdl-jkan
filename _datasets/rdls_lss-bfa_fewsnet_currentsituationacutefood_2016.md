---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/burkina_faso_current_situation_fewsnet_ipc_shapefile_for_2016
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/burkina_faso_current_situation_fewsnet_ipc_shapefile_for_2016
dataset_id: rdls_lss-bfa_fewsnet_currentsituationacutefood_2016
description: 'The FEWS NET Data Warehouse is currently unavailable . Datasets on HDX
  that refer to the Data Warehouse have been archived. Burkina Faso Current Situation
  FEWS NET Acute Food Insecurity Classifications Geographic data for 2016. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/burkina_faso_current_situation_fewsnet_ipc_shapefile_for_2016]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IPC acute food insecurity phase classifications were collected by FEWS
    NET field enumerators on a regular (typically monthly) schedule across Burkina
    Faso sub-national units. Data were compiled into geographic formats (GeoJSON/KML)
    capturing scenario type, classification scale, and IPC value per administrative
    unit for current situation snapshots in February, June, and October 2016.
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
- href: https://data.humdata.org/dataset/burkina_faso_current_situation_fewsnet_ipc_shapefile_for_2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: IPC acute food insecurity phase classifications for Burkina Faso
      sub-national administrative units, collected by FEWS NET enumerators for current
      situation scenarios in 2016
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
  description: Burkina Faso Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (February - 2016 Burkina Faso Current Situation FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=BF&scenario=CS&collection_date=2016-02-01&format=geojson
  format: null
  id: resource_4af8d011
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2016 Burkina Faso Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burkina Faso Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (February - 2016 Burkina Faso Current Situation FEWS
    NET IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=BF&scenario=CS&collection_date=2016-02-01&format=kml
  format: null
  id: resource_bc0ccc88
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: February - 2016 Burkina Faso Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burkina Faso Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (June - 2016 Burkina Faso Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=BF&scenario=CS&collection_date=2016-06-01&format=geojson
  format: null
  id: resource_a730250c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2016 Burkina Faso Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burkina Faso Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (June - 2016 Burkina Faso Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=BF&scenario=CS&collection_date=2016-06-01&format=kml
  format: null
  id: resource_54ea8b42
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: June - 2016 Burkina Faso Current Situation FEWS NET IPC Geographic Data
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Burkina Faso Current Situation FEWS NET Acute Food Insecurity Classifications
    Geographic Data for 2016 (October - 2016 Burkina Faso Current Situation FEWS NET
    IPC Geographic Data)
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=BF&scenario=CS&collection_date=2016-10-01&format=geojson
  format: null
  id: resource_77d7135d
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: October - 2016 Burkina Faso Current Situation FEWS NET IPC Geographic Data
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bfa_fewsnet_currentsituationacutefood_2016
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2016-12-31'
  start: '2016-01-01'
temporal_resolution: null
title: Burkina Faso Current Situation FEWS NET Acute Food Insecurity Classifications
  Geographic Data for 2016
version: null
vulnerability: null
---
