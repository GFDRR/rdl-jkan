---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20230103
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230103
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230103
dataset_id: rdls_hl-phl_philsa_floodingjanuary032023_20230103
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of January 03, 2023, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20230103]'
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
  description: Satellite imagery (SAR) was processed by the Philippine Space Agency
    to detect and map actual flood inundation extent caused by tropical cyclone impacts.
    The resulting flood boundary polygons and raster maps represent observed post-event
    hazard extent, enabling impact assessment and disaster tracking.
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
- href: https://data.humdata.org/dataset/philippines-flood-20230103
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct impact on infrastructure and agriculture from observed flooding
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
  description: Flooding extents on January 03, 2023 at 06:00 AM using Sentinel-1 satellite
    image
  download_url: https://data.humdata.org/dataset/956fb01e-ef38-42ef-9659-c772f9b8f3ff/resource/ad2668e4-548e-4ae4-9775-731b460c88d9/download/20230103_0600_fld_s1_maps.zip
  format: PNG
  id: resource_ad2668e4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230103_0600_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding extents on January 03, 2023 at 06:00 AM using Sentinel-1 satellite
    image
  download_url: https://data.humdata.org/dataset/956fb01e-ef38-42ef-9659-c772f9b8f3ff/resource/b2328c01-17e8-494b-8577-b299496e70fb/download/20230103_0600_fld_s1_shp.zip
  format: null
  id: resource_b2328c01
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230103_0600_fld_s1_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_philsa_floodingjanuary032023_20230103
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
  start: '2023-01-03'
temporal_resolution: null
title: Flooding in the Philippines on January 03, 2023
version: null
vulnerability: null
---
