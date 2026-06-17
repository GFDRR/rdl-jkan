---
attributions:
- entity:
    affiliation: null
    email: null
    name: MODIS MOD13Q1 V6.1
    url: https://data.humdata.org/dataset/ethiopia-ndvi-anomaly-july-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-ndvi-anomaly-july-2025
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-ndvi-anomaly-july-2025
dataset_id: rdls_hzd-eth_3is_ndvianomaly_202507
description: 'NDVI Anomaly is a geospatial metric used to measure how current vegetation
  conditions deviate from what is considered ''normal'' or average for a specific
  location and time period. It helps identify abnormal vegetation growth, whether
  better or worse than expected, and is especially valuable in agriculture, drought
  monitoring, food security, and environmental management. The dataset used for this
  analysis is the MOD13Q1 V6.1 product, which provides a Vegetation Index (VI) value
  on a per-pixel basis. For this study, we used MODIS data from July for the past
  three years, along with historical data spanning from 2010 to 2020.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/ethiopia-ndvi-anomaly-july-2025]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: NDVI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: CC-BY-4.0
lineage:
  description: MODIS MOD13Q1 V6.1 NDVI data from July across three years (2023-2025)
    was processed using Google Earth Engine remote sensing analysis to calculate anomalies
    by comparing current vegetation conditions against historical baselines, generating
    geospatial rasters of vegetation deviation to support drought monitoring and food
    security assessment in Ethiopia.
  sources:
  - id: source_1
    license: null
    name: MODIS MOD13Q1 V6.1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-ndvi-anomaly-july-2025
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
  description: 'Ethiopia: NDVI Anomaly (NDVI Anomaly Ethiopia Month of July.pdf)'
  download_url: https://data.humdata.org/dataset/a9d1996e-a265-485d-aa9c-c65817c2204c/resource/cdb26f94-73a4-4e15-a176-ceb34ca2fdac/download/ndvi-anomaly-ethiopia-month-of-july.pdf
  format: null
  id: resource_cdb26f94
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NDVI Anomaly Ethiopia Month of July.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: NDVI Anomaly'
  download_url: https://data.humdata.org/dataset/a9d1996e-a265-485d-aa9c-c65817c2204c/resource/d52ec573-bc7f-4204-ab19-4cb456f114fb/download/ndvi_anomaly_ethiopia_202507.tif
  format: null
  id: resource_d52ec573
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NDVI_Anomaly_Ethiopia_202507.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: NDVI Anomaly'
  download_url: https://data.humdata.org/dataset/a9d1996e-a265-485d-aa9c-c65817c2204c/resource/f6d507b9-45eb-467d-af4b-e8fa6ffd127f/download/ndvi_anomaly_ethiopia_202407.tif
  format: null
  id: resource_f6d507b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NDVI_Anomaly_Ethiopia_202407.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ethiopia: NDVI Anomaly'
  download_url: https://data.humdata.org/dataset/a9d1996e-a265-485d-aa9c-c65817c2204c/resource/b3ae3c62-cd31-478e-9340-e6f41cea0e4f/download/ndvi_anomaly_ethiopia_202307.tif
  format: null
  id: resource_b3ae3c62
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NDVI_Anomaly_Ethiopia_202307.tif
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-eth_3is_ndvianomaly_202507
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
title: 'Ethiopia: NDVI Anomaly'
version: null
vulnerability: null
---
