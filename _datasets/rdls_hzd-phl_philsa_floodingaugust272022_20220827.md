---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20220827
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20220827
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20220827
dataset_id: rdls_hzd-phl_philsa_floodingaugust272022_20220827
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of August 27, 2022, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20220827]'
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
  description: Satellite imagery (Sentinel-1 SAR) was processed by the Philippine
    Space Agency to detect and delineate actual flood extent across the Philippines
    following typhoon-induced rainfall on August 27, 2022. The processed results were
    delivered as raster maps (PNG) and vector shapefiles (SHP) with flood boundary
    geometries and metadata attributes.
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
- href: https://data.humdata.org/dataset/philippines-flood-20220827
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
  description: Flooding in the Philippines on August 27, 2022 (Flooding extents on
    August 27, 2022 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/a4d90519-6dc5-452d-a95d-7e77cffaa4f0/resource/66354665-f9bb-4709-a4c4-97aaf5e4d4b9/download/20220827_0600_fld_s1_maps.zip
  format: PNG
  id: resource_66354665
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20220827_0600_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on August 27, 2022 (Flooding extents on
    August 27, 2022 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/a4d90519-6dc5-452d-a95d-7e77cffaa4f0/resource/fceb2d79-751a-44b7-a61a-a8afdd7d9c8a/download/20220827_0600_fld_s1_shp.zip
  format: null
  id: resource_fceb2d79
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20220827_0600_fld_s1_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingaugust272022_20220827
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
  start: '2022-08-27'
temporal_resolution: null
title: Flooding in the Philippines on August 27, 2022
version: null
vulnerability: null
---
