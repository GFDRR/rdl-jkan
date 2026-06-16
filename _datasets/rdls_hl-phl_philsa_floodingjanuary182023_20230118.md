---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20230118
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230118
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230118
dataset_id: rdls_hl-phl_philsa_floodingjanuary182023_20230118
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of January 18, 2023, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20230118]'
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
  description: Satellite imagery from January 18, 2023 was processed by the Philippine
    Space Agency to delineate actual flood extent across the Philippines during a
    typhoon event. Flood boundaries were extracted at two time points (0600 and 1000
    UTC) and delivered as both raster maps and vector shapefiles with area measurements,
    enabling temporal tracking of flood progression.
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
- href: https://data.humdata.org/dataset/philippines-flood-20230118
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct impact on agricultural areas from observed flooding
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
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct impact on infrastructure from observed flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  description: Flooding extents on January 18, 2023 at 06:00 AM using Sentinel-1 satellite
    image
  download_url: https://data.humdata.org/dataset/875347f6-77a1-4a6b-9609-97031e29d168/resource/5afdc0ef-c4c8-45ad-aa6e-cc1df69ee7c9/download/20230118_0600_fld_s1_maps.zip
  format: PNG
  id: resource_5afdc0ef
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230118_0600_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding extents on January 18, 2023 at 06:00 AM using Sentinel-1 satellite
    image
  download_url: https://data.humdata.org/dataset/875347f6-77a1-4a6b-9609-97031e29d168/resource/223e2e91-ee8a-4b50-a8ba-0c04cce23de8/download/20230118_0600_fld_s1_shp.zip
  format: null
  id: resource_223e2e91
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230118_0600_fld_s1_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on January 18, 2023 (Flooding extents on
    January 18, 2023 at 10:00 AM using NovaSAR-1 satellite image)
  download_url: https://data.humdata.org/dataset/875347f6-77a1-4a6b-9609-97031e29d168/resource/4ed797ca-9e87-4277-8d13-77aa0d618432/download/20230118_1000_fld_nv1_maps.zip
  format: PNG
  id: resource_4ed797ca
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230118_1000_fld_nv1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on January 18, 2023 (Flooding extents on
    January 18, 2023 at 10:00 AM using NovaSAR-1 satellite image)
  download_url: https://data.humdata.org/dataset/875347f6-77a1-4a6b-9609-97031e29d168/resource/56ab8984-2c4d-48aa-a527-c621773313ef/download/20230118_1000_fld_nv1_shp.zip
  format: null
  id: resource_56ab8984
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230118_1000_fld_nv1_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_philsa_floodingjanuary182023_20230118
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
  start: '2023-01-18'
temporal_resolution: null
title: Flooding in the Philippines on January 18, 2023
version: null
vulnerability: null
---
