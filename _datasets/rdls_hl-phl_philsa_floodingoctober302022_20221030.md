---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20221030
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20221030
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20221030
dataset_id: rdls_hl-phl_philsa_floodingoctober302022_20221030
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of October 30, 2022, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20221030]'
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Satellite imagery was processed by the Philippine Space Agency to detect
    and map the actual extent of flooding caused by typhoons on October 30, 2022.
    The resulting flood extent polygons with area measurements were delivered as shapefiles
    and map visualizations to document the spatial distribution of inundation across
    affected regions.
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
- href: https://data.humdata.org/dataset/philippines-flood-20221030
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural areas affected by typhoon-induced flooding
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
    description: Infrastructure affected by typhoon-induced flooding
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
  description: Flooding in the Philippines on October 30, 2022 (Flooding extents on
    October 30, 2022 at 10:00 AM using Landsat 9 satellite image)
  download_url: https://data.humdata.org/dataset/0a2e35e3-633a-4504-9804-db745e1dee14/resource/17b534e4-2f4e-4d97-9c8a-2f54a40c33e1/download/20221030_1000_fld_l9_maps.zip
  format: PNG
  id: resource_17b534e4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20221030_1000_fld_l9_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on October 30, 2022 (Flooding extents on
    October 30, 2022 at 10:00 AM using Landsat 9 satellite image)
  download_url: https://data.humdata.org/dataset/0a2e35e3-633a-4504-9804-db745e1dee14/resource/5dcfd145-d210-48e4-afc6-b80faf383ab3/download/20221030_1000_fld_l9_shp.zip
  format: null
  id: resource_5dcfd145
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20221030_1000_fld_l9_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on October 30, 2022 (Flooding extents on
    October 30, 2022 at 10:00 AM using NovaSAR-1 satellite image)
  download_url: https://data.humdata.org/dataset/0a2e35e3-633a-4504-9804-db745e1dee14/resource/5c1a0092-e1ec-406a-b404-3b51211b011d/download/20221030_1000_fld_nv1_maps.zip
  format: PNG
  id: resource_5c1a0092
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20221030_1000_fld_nv1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on October 30, 2022 (Flooding extents on
    October 30, 2022 at 10:00 AM using NovaSAR-1 satellite image)
  download_url: https://data.humdata.org/dataset/0a2e35e3-633a-4504-9804-db745e1dee14/resource/2fc47197-2269-487c-8289-556731f2396a/download/20221030_1000_fld_nv1_shp.zip
  format: null
  id: resource_2fc47197
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20221030_1000_fld_nv1_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_philsa_floodingoctober302022_20221030
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
  start: '2022-10-30'
temporal_resolution: null
title: Flooding in the Philippines on October 30, 2022
version: null
vulnerability: null
---
