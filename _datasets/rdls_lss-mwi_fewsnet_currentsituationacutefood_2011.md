---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/malawi_current_situation_fewsnet_ipc_classification
creator:
  affiliation: null
  email: null
  name: FEWS NET
  url: https://data.humdata.org/dataset/malawi_current_situation_fewsnet_ipc_classification
dataset_id: rdls_lss-mwi_fewsnet_currentsituationacutefood_2011
description: 'Malawi Current Situation FEWS NET Acute Food Insecurity Classifications
  Data from 2011. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi_current_situation_fewsnet_ipc_classification]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FEWS NET enumerators collected acute food insecurity classification
    data on a regular monthly schedule in 2011, assessing food security conditions
    across Malawi's administrative divisions using standardized classification scales
    and scenarios. The data represents post-assessment situational classifications
    reflecting population vulnerability to food insecurity.
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
- href: https://data.humdata.org/dataset/malawi_current_situation_fewsnet_ipc_classification
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute food insecurity classifications reflecting population vulnerability
      to drought and food shortage
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
purpose: Acute Food Insecurity Classifications data in different scenarios collected
  by FEWS NET enumerators on a regular schedule (typically monthly).
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications
    Data from 2011
  download_url: https://fdw.fews.net/api/ipcphase/?preference=best&country=MW&scenario=CS&format=xlsx
  format: null
  id: resource_d36c1eee
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications Data
    from 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications
    Data from 2011
  download_url: https://fdw.fews.net/api/ipcphase/?preference=best&country=MW&scenario=CS&format=csv
  format: null
  id: resource_74a49105
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications Data
    from 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications
    Data from 2011
  download_url: https://fdw.fews.net/api/ipcphase/?preference=best&country=MW&scenario=CS&format=json
  format: null
  id: resource_9aa46dc2
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications Data
    from 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications
    Data from 2011
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MW&scenario=CS&collection_date=2022-06-01&format=geojson
  format: null
  id: resource_303298fd
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications Data
    from 2011
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications
    Data from 2011
  download_url: https://fdw.fews.net/api/ipcphasemap/?country=MW&scenario=CS&collection_date=2022-06-01&format=kml
  format: null
  id: resource_69ec43f8
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications Data
    from 2011
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mwi_fewsnet_currentsituationacutefood_2011
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-10-31'
  start: '2011-01-01'
temporal_resolution: null
title: Malawi Current Situation FEWS NET Acute Food Insecurity Classifications Data
version: null
vulnerability: null
---
