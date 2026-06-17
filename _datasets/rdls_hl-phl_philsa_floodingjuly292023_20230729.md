---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20230729
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230729
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230729
dataset_id: rdls_hl-phl_philsa_floodingjuly292023_20230729
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of July 29, 2023, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20230729]'
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
  description: Satellite imagery was processed by the Philippine Space Agency to detect
    and delineate actual flood extent across the Philippines on July 29, 2023, resulting
    from typhoon-induced fluvial flooding. The processed data includes raster maps
    and vector shapefiles representing the observed inundated areas, enabling post-event
    impact assessment and hazard tracking.
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
- href: https://data.humdata.org/dataset/philippines-flood-20230729
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural areas affected by flooding from tropical cyclone-induced
      fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
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
    description: Infrastructure areas affected by flooding from tropical cyclone-induced
      fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
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
  description: Flooding in the Philippines on July 29, 2023 (Flooding extents on July
    29, 2023 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/882ae351-5f39-46f8-9e86-618be89a9a87/resource/6d82150c-9849-4c6b-90a5-815923071666/download/20230729_0600_fld_s1_maps-agri.zip
  format: PNG
  id: resource_6d82150c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230729_0600_fld_s1_maps-agri.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 29, 2023 (Flooding extents on July
    29, 2023 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/882ae351-5f39-46f8-9e86-618be89a9a87/resource/c6a7e71d-d476-4d0b-bc40-09aefb3d15e5/download/20230729_0600_fld_s1_maps.zip
  format: PNG
  id: resource_c6a7e71d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230729_0600_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 29, 2023 (Flooding extents on July
    29, 2023 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/882ae351-5f39-46f8-9e86-618be89a9a87/resource/1729cc7f-9157-424d-aac1-1d13facc2e34/download/20230729_0600_fld_s1_shp.zip
  format: null
  id: resource_1729cc7f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230729_0600_fld_s1_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_philsa_floodingjuly292023_20230729
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
  start: '2023-07-29'
temporal_resolution: null
title: Flooding in the Philippines on July 29, 2023
version: null
vulnerability: null
---
