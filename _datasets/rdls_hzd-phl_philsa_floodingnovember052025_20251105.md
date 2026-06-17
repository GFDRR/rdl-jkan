---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20251105
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20251105
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20251105
dataset_id: rdls_hzd-phl_philsa_floodingnovember052025_20251105
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of November 05, 2025, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20251105]'
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Satellite imagery acquired on November 5, 2025 was processed by the
    Philippine Space Agency to detect and delineate actual flood extent caused by
    typhoon-induced rainfall. The processed results were delivered as raster maps
    (PNG) and vector shapefiles (SHP) representing observed inundation areas.
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
- href: https://data.humdata.org/dataset/philippines-flood-20251105
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
  description: Flooding extents on November 05, 2025 at 05:32 AM using Sentinel-1
    satellite image
  download_url: https://data.humdata.org/dataset/eab2d281-3816-413f-8ad4-24bb18877a8f/resource/8ffca5a3-0a05-492a-84f8-13b4f2263f81/download/20251105_0532_fld_s1_maps.zip
  format: PNG
  id: resource_8ffca5a3
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20251105_0532_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding extents on November 05, 2025 at 05:32 AM using Sentinel-1
    satellite image
  download_url: https://data.humdata.org/dataset/eab2d281-3816-413f-8ad4-24bb18877a8f/resource/05395ef1-3ee5-452c-b009-eb99aee80900/download/20251105_0532_fld_s1_shp.zip
  format: null
  id: resource_05395ef1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20251105_0532_fld_s1_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingnovember052025_20251105
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
  start: '2025-11-05'
temporal_resolution: null
title: Flooding in the Philippines on November 05, 2025
version: null
vulnerability: null
---
