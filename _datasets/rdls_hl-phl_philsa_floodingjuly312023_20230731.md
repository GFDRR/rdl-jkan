---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20230731
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230731
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20230731
dataset_id: rdls_hl-phl_philsa_floodingjuly312023_20230731
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of July 31, 2023, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20230731]'
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
    and delineate actual flood extent caused by typhoon-induced rainfall and storm
    surge. The resulting flood maps were generated as raster (PNG) and vector (shapefile)
    products to track flood progression and spatial distribution across affected areas
    in the Philippines.
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
- href: https://data.humdata.org/dataset/philippines-flood-20230731
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct impact on infrastructure and agriculture from typhoon-induced
      flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: wd:m
      process: null
      trigger: null
      type: strong_wind
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
  description: Flooding in the Philippines on July 31, 2023 (Flooding extents on July
    31, 2023 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/65893827-0c5f-49a6-9a09-7af4b66ddc84/resource/9b529757-02b3-4515-8919-cfd2a5f21e9b/download/20230731_0600_fld_s1_maps-agri.zip
  format: PNG
  id: resource_9b529757
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230731_0600_fld_s1_maps-agri.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 31, 2023 (Flooding extents on July
    31, 2023 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/65893827-0c5f-49a6-9a09-7af4b66ddc84/resource/b4abcfe5-3b5f-4a66-870f-6815bbcc232e/download/20230731_0600_fld_s1_maps.zip
  format: PNG
  id: resource_b4abcfe5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230731_0600_fld_s1_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on July 31, 2023 (Flooding extents on July
    31, 2023 at 06:00 AM using Sentinel-1 satellite image)
  download_url: https://data.humdata.org/dataset/65893827-0c5f-49a6-9a09-7af4b66ddc84/resource/d629b4dc-8997-4205-b0f6-4ea20b6801a7/download/20230731_0600_fld_s1_shp.zip
  format: null
  id: resource_d629b4dc
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20230731_0600_fld_s1_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_philsa_floodingjuly312023_20230731
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
  start: '2023-07-31'
temporal_resolution: null
title: Flooding in the Philippines on July 31, 2023
version: null
vulnerability: null
---
