---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20250923
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250923
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250923
dataset_id: rdls_hzd-phl_philsa_floodingseptember232025_20250923
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of September 23, 2025, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20250923]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Satellite imagery was processed by the Philippine Space Agency to delineate
    actual flood extent polygons resulting from typhoon-induced precipitation and
    storm surge. The dataset represents post-event observed flood boundaries mapped
    through remote sensing analysis, providing spatial coverage of inundated areas
    across the Philippines on September 23, 2025.
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
- href: https://data.humdata.org/dataset/philippines-flood-20250923
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
  description: Flooding extents on September 23, 2025 at 05:39 AM using Sentinel-1
    satellite image
  download_url: https://data.humdata.org/dataset/c2ad986c-ab61-4a3f-a5bc-83aada35aa63/resource/ea2c369d-0df7-4885-9e15-d3f07914f324/download/20250923_0539_fld_s1_maps.zip
  format: PNG
  id: resource_ea2c369d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250923_0539_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding extents on September 23, 2025 at 05:39 AM using Sentinel-1
    satellite image
  download_url: https://data.humdata.org/dataset/c2ad986c-ab61-4a3f-a5bc-83aada35aa63/resource/57a303e0-e764-49a3-9b1b-edb9f2eec8c1/download/20250923_0539_fld_s1_shp.zip
  format: null
  id: resource_57a303e0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250923_0539_fld_s1_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingseptember232025_20250923
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
  start: '2025-09-23'
temporal_resolution: null
title: Flooding in the Philippines on September 23, 2025
version: null
vulnerability: null
---
