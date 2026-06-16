---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20241119
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20241119
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20241119
dataset_id: rdls_hzd-phl_philsa_floodingnovember192024_20241119
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of November 19, 2024, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20241119]'
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Satellite imagery was processed by the Philippine Space Agency to detect
    and delineate actual flood extent across the Philippines resulting from typhoon-induced
    precipitation and storm surge on November 19, 2024. The processed imagery was
    converted to vector (shapefile) and raster (PNG) formats to enable spatial analysis
    and temporal tracking of flood progression.
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
- href: https://data.humdata.org/dataset/philippines-flood-20241119
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
  description: Flooding in the Philippines on November 19, 2024 (Flooding extents
    on November 19, 2024 at 06:15 PM using Gaofen-3 satellite image)
  download_url: https://data.humdata.org/dataset/22005fa8-da88-4167-bb1a-978479b3cb41/resource/749f1b39-b4a9-43c9-93e4-36d3302bdb4a/download/20241119_1815_fld_gf3_maps.zip
  format: PNG
  id: resource_749f1b39
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20241119_1815_fld_gf3_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on November 19, 2024 (Flooding extents
    on November 19, 2024 at 06:15 PM using Gaofen-3 satellite image)
  download_url: https://data.humdata.org/dataset/22005fa8-da88-4167-bb1a-978479b3cb41/resource/a39a151d-ee8b-4212-9712-a79880a5d8f7/download/20241119_1815_fld_gf3_shp.zip
  format: null
  id: resource_a39a151d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20241119_1815_fld_gf3_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingnovember192024_20241119
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
  start: '2024-11-19'
temporal_resolution: null
title: Flooding in the Philippines on November 19, 2024
version: null
vulnerability: null
---
