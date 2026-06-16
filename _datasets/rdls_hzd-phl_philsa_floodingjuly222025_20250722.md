---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20250722
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250722
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250722
dataset_id: rdls_hzd-phl_philsa_floodingjuly222025_20250722
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of July 22, 2025, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20250722]'
details: This dataset has not been validated using ground-truth data.
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Satellite imagery acquired on July 22, 2025 was processed by the Philippine
    Space Agency to detect and delineate actual flood extent caused by typhoon-induced
    precipitation and storm surge. The resulting flood maps were vectorized into shapefile
    format with raster classification codes to enable spatial analysis and temporal
    tracking of inundation progression.
  sources:
  - id: source_1
    license: null
    name: Philippine Space Agency
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/philippines-flood-20250722
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
  description: Flooding extents on July 22, 2025 at 05:45 AM using RADARSAT Constellation
    Mission satellite image
  download_url: https://data.humdata.org/dataset/94a300ca-2516-40d0-b428-8ce8af4d9ba0/resource/201cd2f2-c0b9-4d6d-9e4d-941c2bc09224/download/20250722_0545_fld_rcm_maps.zip
  format: PNG
  id: resource_201cd2f2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250722_0545_fld_rcm_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding extents on July 22, 2025 at 05:45 AM using RADARSAT Constellation
    Mission satellite image
  download_url: https://data.humdata.org/dataset/94a300ca-2516-40d0-b428-8ce8af4d9ba0/resource/4b54e014-f498-4c8b-a9c8-e56e84116dda/download/20250722_0545_fld_rcm_shp.zip
  format: null
  id: resource_4b54e014
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250722_0545_fld_rcm_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingjuly222025_20250722
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-07-22'
temporal_resolution: null
title: Flooding in the Philippines on July 22, 2025
version: null
vulnerability: null
---
