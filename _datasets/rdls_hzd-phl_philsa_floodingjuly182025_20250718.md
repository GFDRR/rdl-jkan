---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20250718
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250718
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250718
dataset_id: rdls_hzd-phl_philsa_floodingjuly182025_20250718
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of July 18, 2025, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20250718]'
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
  description: Satellite imagery (optical and SAR) acquired on July 18, 2025 was processed
    by the Philippine Space Agency to delineate flood extent polygons and raster maps.
    The resulting flood boundary dataset represents observed inundation areas caused
    by tropical cyclone-induced rainfall and represents a post-event hazard observation
    rather than a predictive model.
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
- href: https://data.humdata.org/dataset/philippines-flood-20250718
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
  description: Flooding in the Philippines on July 18, 2025 (Flooding extents on July
    18, 2025 at 05:45 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/aed2559f-9b94-4b6a-b215-2e03683cca84/resource/013c9e04-fa18-41d2-ad81-0912be24dbd0/download/20250718_0545_fld_s1_maps.zip
  format: PNG
  id: resource_013c9e04
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250718_0545_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 18, 2025 (Flooding extents on July
    18, 2025 at 05:45 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/aed2559f-9b94-4b6a-b215-2e03683cca84/resource/a7e4e4f3-0f18-49b0-9ff4-e334f460baba/download/20250718_0545_fld_s1_shp.zip
  format: null
  id: resource_a7e4e4f3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250718_0545_fld_s1_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingjuly182025_20250718
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
  start: '2025-07-18'
temporal_resolution: null
title: Flooding in the Philippines on July 18, 2025
version: null
vulnerability: null
---
