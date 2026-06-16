---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20250719
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250719
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20250719
dataset_id: rdls_hzd-phl_philsa_floodingjuly192025_20250719
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of July 19, 2025, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20250719]'
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
  description: Satellite synthetic aperture radar (SAR) imagery from Sentinel-1 was
    processed and analyzed to detect and map the actual spatial extent of flooding
    caused by tropical cyclone activity in the Philippines. The resulting flood extent
    polygons and raster maps represent observed inundation areas as of the acquisition
    date, enabling temporal tracking of flood progression.
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
- href: https://data.humdata.org/dataset/philippines-flood-20250719
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
  description: Flooding in the Philippines on July 19, 2025 (Flooding extents on July
    19, 2025 at 06:06 PM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/5f93e6b2-b189-4f74-88bd-4c7cf34aeea2/resource/008661a0-13d0-495d-bc79-b4f07a8be06a/download/20250719_1806_fld_s1_maps.zip
  format: PNG
  id: resource_008661a0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250719_1806_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 19, 2025 (Flooding extents on July
    19, 2025 at 06:06 PM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/5f93e6b2-b189-4f74-88bd-4c7cf34aeea2/resource/3793f7ff-d4bd-4613-99f3-f05deeee2123/download/20250719_1806_fld_s1_shp.zip
  format: null
  id: resource_3793f7ff
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20250719_1806_fld_s1_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingjuly192025_20250719
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
  start: '2025-07-19'
temporal_resolution: null
title: Flooding in the Philippines on July 19, 2025
version: null
vulnerability: null
---
