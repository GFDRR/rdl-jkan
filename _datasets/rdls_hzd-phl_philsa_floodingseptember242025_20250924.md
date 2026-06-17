---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20250924
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250924
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250924
dataset_id: rdls_hzd-phl_philsa_floodingseptember242025_20250924
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of September 24, 2025, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20250924]'
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
  type: flood
license: CC-BY-4.0
lineage:
  description: Satellite imagery was processed by the Philippine Space Agency to delineate
    actual flood extent caused by typhoons as of September 24, 2025. The resulting
    flood boundary polygons and raster maps represent observed inundation areas derived
    from synthetic aperture radar (SAR) and optical satellite data, enabling temporal
    tracking of flood progression across the Philippines.
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
- href: https://data.humdata.org/dataset/philippines-flood-20250924
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
  description: Flooding extents on September 24, 2025 at 05:30 AM using Sentinel-1
    satellite image
  download_url: https://data.humdata.org/dataset/a606ca25-94b0-4a83-aef1-ff3eeb52a21b/resource/d169b5c6-b186-4266-9bda-aede9754cc63/download/20250924_0530_fld_s1_maps.zip
  format: PNG
  id: resource_d169b5c6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250924_0530_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding extents on September 24, 2025 at 05:30 AM using Sentinel-1
    satellite image
  download_url: https://data.humdata.org/dataset/a606ca25-94b0-4a83-aef1-ff3eeb52a21b/resource/2c10652c-2031-4d09-8e81-37a1615ca4cb/download/20250924_0530_fld_s1_shp.zip
  format: null
  id: resource_2c10652c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250924_0530_fld_s1_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingseptember242025_20250924
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
  start: '2025-09-24'
temporal_resolution: null
title: Flooding in the Philippines on September 24, 2025
version: null
vulnerability: null
---
