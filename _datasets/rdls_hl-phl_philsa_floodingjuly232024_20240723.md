---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20240723
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20240723
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20240723
dataset_id: rdls_hl-phl_philsa_floodingjuly232024_20240723
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of July 23, 2024, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20240723]'
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
  description: Sentinel-1 satellite imagery was processed by the Philippine Space
    Agency using image classification techniques to identify and map the actual extent
    of flooding caused by typhoon-induced rainfall and storm surge. The resulting
    flood extent polygons and raster maps represent observed inundation areas as of
    the acquisition date, enabling post-event impact assessment and hazard tracking.
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
- href: https://data.humdata.org/dataset/philippines-flood-20240723
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct impact on infrastructure and agriculture from observed flood
      extent
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: Flooding in the Philippines on July 23, 2024 (Flooding extents on July
    23, 2024 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/3dc452ab-54cf-400f-92f5-70487589a865/resource/04190cd1-e710-41c7-98fd-32a14e048f32/download/20240723_0600_fld_s1_maps.zip
  format: PNG
  id: resource_04190cd1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20240723_0600_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 23, 2024 (Flooding extents on July
    23, 2024 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/3dc452ab-54cf-400f-92f5-70487589a865/resource/3dfd57a6-c1fe-4e4f-91dd-9af84f2548d0/download/20240723_0600_fld_s1_shp.zip
  format: null
  id: resource_3dfd57a6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20240723_0600_fld_s1_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_philsa_floodingjuly232024_20240723
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
  start: '2024-07-23'
temporal_resolution: null
title: Flooding in the Philippines on July 23, 2024
version: null
vulnerability: null
---
