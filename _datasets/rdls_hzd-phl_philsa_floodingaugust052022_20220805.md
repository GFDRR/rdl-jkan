---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20220805
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20220805
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20220805
dataset_id: rdls_hzd-phl_philsa_floodingaugust052022_20220805
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of August 05, 2022, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20220805]'
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
  description: Satellite synthetic aperture radar (SAR) imagery from Sentinel-1 was
    processed by the Philippine Space Agency to delineate actual flood extent across
    the Philippines during typhoon-induced flooding on August 5, 2022. The processed
    imagery was converted to vector shapefiles and raster maps to document the spatial
    distribution of inundated areas.
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
- href: https://data.humdata.org/dataset/philippines-flood-20220805
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
  description: Flooding in the Philippines on August 05, 2022 (Flooding extents on
    August 05, 2022 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/ccafbd97-f995-40bf-8732-0b52971ca8b1/resource/dfa7de46-2e74-45c2-85ce-36d9581eae6a/download/20220805_0600_fld_s1_maps.zip
  format: PNG
  id: resource_dfa7de46
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20220805_0600_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on August 05, 2022 (Flooding extents on
    August 05, 2022 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/ccafbd97-f995-40bf-8732-0b52971ca8b1/resource/967e5940-bc64-40bf-8de4-29bb7a8e9ed3/download/20220805_0600_fld_s1_shp.zip
  format: null
  id: resource_967e5940
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20220805_0600_fld_s1_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-phl_philsa_floodingaugust052022_20220805
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
  start: '2022-08-05'
temporal_resolution: null
title: Flooding in the Philippines on August 05, 2022
version: null
vulnerability: null
---
