---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20230804
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230804
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230804
dataset_id: rdls_hzd-phl_philsa_floodingaugust042023_20230804
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of August 04, 2023, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20230804]'
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
  description: Satellite imagery from ICEYE was processed by the Philippine Space
    Agency to delineate actual flood extent polygons and raster grids during the August
    4, 2023 typhoon-induced flooding event. The processed data includes both raster
    (PNG) and vector (shapefile) representations of observed inundation areas with
    gridded area calculations.
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
- href: https://data.humdata.org/dataset/philippines-flood-20230804
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
  description: Flooding in the Philippines on August 04, 2023 (Flooding extents on
    August 04, 2023 at 01:15 PM using ICEYE satellite image)
  download_url: https://data.humdata.org/dataset/fba0e0a6-df2c-4c21-bc7f-a5f9f941a326/resource/889cbabd-1bb6-425a-888d-4f9fb60bf17e/download/20230804_1315_fld_iceye_maps.zip
  format: PNG
  id: resource_889cbabd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230804_1315_fld_iceye_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on August 04, 2023 (Flooding extents on
    August 04, 2023 at 01:15 PM using ICEYE satellite image)
  download_url: https://data.humdata.org/dataset/fba0e0a6-df2c-4c21-bc7f-a5f9f941a326/resource/1ecf3e91-ae52-4891-bd30-ee6c7dbdccec/download/20230804_1315_fld_iceye_shp.zip
  format: null
  id: resource_1ecf3e91
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230804_1315_fld_iceye_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingaugust042023_20230804
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
  start: '2023-08-04'
temporal_resolution: null
title: Flooding in the Philippines on August 04, 2023
version: null
vulnerability: null
---
