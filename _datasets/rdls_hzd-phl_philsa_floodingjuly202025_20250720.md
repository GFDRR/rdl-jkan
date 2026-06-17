---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20250720
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250720
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250720
dataset_id: rdls_hzd-phl_philsa_floodingjuly202025_20250720
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of July 20, 2025, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20250720]'
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
  type: flood
license: CC-BY-4.0
lineage:
  description: Satellite radar imagery (Sentinel-1 and ALOS-2) acquired on July 20,
    2025 was processed by the Philippine Space Agency to delineate flood extent polygons
    through image classification. The resulting flood maps represent observed inundation
    areas caused by typhoon-induced rainfall and are provided as both raster and vector
    (shapefile) formats for temporal tracking and spatial analysis.
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
- href: https://data.humdata.org/dataset/philippines-flood-20250720
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
  description: Flooding in the Philippines on July 20, 2025 (Flooding extents on July
    20, 2025 at 05:30 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/83892eb0-210d-40c0-a0a6-390e60c7f6e6/resource/4564c31e-fc3c-4258-a034-fff362e03a59/download/20250720_0530_fld_s1_maps.zip
  format: PNG
  id: resource_4564c31e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250720_0530_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 20, 2025 (Flooding extents on July
    20, 2025 at 05:30 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/83892eb0-210d-40c0-a0a6-390e60c7f6e6/resource/f06bdb75-149d-4e0d-b618-557798defdd5/download/20250720_0530_fld_s1_shp.zip
  format: null
  id: resource_f06bdb75
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250720_0530_fld_s1_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 20, 2025 (Flooding extents on July
    20, 2025 at 11:50 AM using ALOS-2 satellite image)
  download_url: https://data.humdata.org/dataset/83892eb0-210d-40c0-a0a6-390e60c7f6e6/resource/2ea14913-15d0-4958-811c-af460b072eb1/download/20250720_1150_fld_alos2_maps.zip
  format: PNG
  id: resource_2ea14913
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250720_1150_fld_alos2_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 20, 2025 (Flooding extents on July
    20, 2025 at 11:50 AM using ALOS-2 satellite image)
  download_url: https://data.humdata.org/dataset/83892eb0-210d-40c0-a0a6-390e60c7f6e6/resource/dce1ace4-9acf-4b22-b386-64ec7517f776/download/20250720_1150_fld_alos2_shp.zip
  format: null
  id: resource_dce1ace4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250720_1150_fld_alos2_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingjuly202025_20250720
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
  start: '2025-07-20'
temporal_resolution: null
title: Flooding in the Philippines on July 20, 2025
version: null
vulnerability: null
---
