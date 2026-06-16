---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20251106
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20251106
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20251106
dataset_id: rdls_hzd-phl_philsa_floodingnovember062025_20251106
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of November 06, 2025, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20251106]'
details: This dataset has not been validated using ground-truth data.
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Sentinel-2 satellite imagery acquired on November 6, 2025 was processed
    by the Philippine Space Agency to delineate actual flood extent through image
    classification and analysis. The resulting flood maps were delivered as both raster
    (PNG) and vector (shapefile) formats to enable spatial tracking of inundation
    progression and identification of affected areas.
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
- href: https://data.humdata.org/dataset/philippines-flood-20251106
  rel: source
loss:
  losses: []
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
  description: Flooding extents on November 06, 2025 at 10:23 AM using Sentinel-2
    satellite image
  download_url: https://data.humdata.org/dataset/b2379135-420d-4ae2-b0d4-bf5db54dc673/resource/09c5dc8e-7f78-479a-a50b-602b92e03fd4/download/20251106_1023_fld_s2_maps.zip
  format: PNG
  id: resource_09c5dc8e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20251106_1023_fld_s2_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding extents on November 06, 2025 at 10:23 AM using Sentinel-2
    satellite image
  download_url: https://data.humdata.org/dataset/b2379135-420d-4ae2-b0d4-bf5db54dc673/resource/7981c463-c718-43e9-85c5-1c05e484e1e8/download/20251106_1023_fld_s2_shp.zip
  format: null
  id: resource_7981c463
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20251106_1023_fld_s2_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingnovember062025_20251106
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
  start: '2025-11-06'
temporal_resolution: null
title: Flooding in the Philippines on November 06, 2025
version: null
vulnerability: null
---
