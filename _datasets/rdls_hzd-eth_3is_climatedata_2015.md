---
attributions:
- entity:
    affiliation: null
    email: null
    name: CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data)
    url: https://data.humdata.org/dataset/ethiopia-climate-data
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-climate-data
creator:
  affiliation: null
  email: null
  name: 3iS
  url: https://data.humdata.org/dataset/ethiopia-climate-data
dataset_id: rdls_hzd-eth_3is_climatedata_2015
description: 'Climate data estimated using satellite images using Google Earth Engine
  (GEE) and Amazon Sagemaker with Geospatial Capabilities.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/ethiopia-climate-data]'
details: Remote Sensing
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
      intensity_measure: PP:mm
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Precipitation data was estimated from satellite imagery using Google
    Earth Engine and Amazon SageMaker geospatial capabilities, leveraging the CHIRPS
    dataset to derive median pentad precipitation values at 4.8km resolution for the
    Shabelle region from 1981 to 2024. This observational precipitation record serves
    as a meteorological drought indicator for climate and agricultural monitoring.
  sources:
  - id: source_1
    license: null
    name: CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ethiopia-climate-data
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Estimation of precipitations in mm every 5 days from 1981 to 2024.
    CHIRPS Satellite. Spatial Resolution: 4.8km Temporal resolution: 5 days'
  download_url: https://data.humdata.org/dataset/6efd3ed9-7918-4c47-80de-07a9702a3bb1/resource/dcb08179-9a08-4a46-9fb2-ad6114af8ca6/download/shabelle-chirps-4.8km-pentad-median-precipitation-in-mm.xlsx
  format: null
  id: resource_dcb08179
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Shabelle - CHIRPS 4.8km Pentad - Median Precipitation in mm.xlsx
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-eth_3is_climatedata_2015
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
  end: '2025-01-07'
  start: '2015-01-01'
temporal_resolution: null
title: Ethiopia - Climate data
version: null
vulnerability: null
---
