---
attributions:
- entity:
    affiliation: null
    email: null
    name: CHIRPS (Climate Hazards Group InfraRed Precipitation with Station Data)
    url: https://data.humdata.org/dataset/ethiopia-rainfall-anomaly
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-rainfall-anomaly
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-rainfall-anomaly
dataset_id: rdls_hzd-eth_3is_rainfallanomaly_202507
description: 'Rainfall anomaly represents the difference between observed rainfall
  and the long-term average for a specific location and period, indicating whether
  rainfall is above or below normal. Positive anomalies show higher-than-average rainfall,
  while negative anomalies indicate lower amounts. These anomalies help monitor climate
  patterns, droughts, floods, and their effects on agriculture and other sectors.
  For this analysis, we used CHIRPS daily rainfall data for Ethiopia and calculated
  anomalies for May to July 2025 by subtracting the 2000-2020 long-term average from
  the current values.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-rainfall-anomaly]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: RA:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Daily rainfall observations from CHIRPS satellite data were processed
    using Google Earth Engine remote sensing analysis. Rainfall anomalies for May-July
    2025 were calculated by subtracting the 2000-2020 long-term average from current
    observed values, producing gridded anomaly rasters indicating drought/excess precipitation
    conditions across Ethiopia.
  sources:
  - id: source_1
    license: null
    name: CHIRPS (Climate Hazards Group InfraRed Precipitation with Station Data)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-rainfall-anomaly
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Rainfall Anomaly (Rainfall Anomaly Ethiopia Month of July.pdf)'
  download_url: https://data.humdata.org/dataset/81b649eb-3a9e-400c-a172-d7047b60f03b/resource/5a8a2821-a213-4003-948d-3716498e62eb/download/rainfall-anomaly-ethiopia-month-of-july.pdf
  format: null
  id: resource_5a8a2821
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rainfall Anomaly Ethiopia Month of July.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Rainfall Anomaly'
  download_url: https://data.humdata.org/dataset/81b649eb-3a9e-400c-a172-d7047b60f03b/resource/2319ca5e-febd-4191-9ccd-fd8555195718/download/rainfall_anomaly_2025_7.tif
  format: null
  id: resource_2319ca5e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rainfall_Anomaly_2025_7.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Rainfall Anomaly'
  download_url: https://data.humdata.org/dataset/81b649eb-3a9e-400c-a172-d7047b60f03b/resource/33966d12-3e28-4fda-8d44-3d4453f3f87a/download/rainfall_anomaly_2024_7.tif
  format: null
  id: resource_33966d12
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rainfall_Anomaly_2024_7.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: Rainfall Anomaly'
  download_url: https://data.humdata.org/dataset/81b649eb-3a9e-400c-a172-d7047b60f03b/resource/e0aaf6be-c54c-4d5e-9765-b1bdd21e1420/download/rainfall_anomaly_2023_7.tif
  format: null
  id: resource_e0aaf6be
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rainfall_Anomaly_2023_7.tif
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-eth_3is_rainfallanomaly_202507
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
  end: '2025-07-31'
  start: '2025-07-01'
temporal_resolution: null
title: 'Ethiopia: Rainfall Anomaly'
version: null
vulnerability: null
---
