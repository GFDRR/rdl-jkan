---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20241114
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20241114
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20241114
dataset_id: rdls_hl-phl_philsa_floodingnovember142024_20241114
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of November 14, 2024, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20241114]'
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
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Satellite imagery from ALOS-2 was processed to delineate actual flood
    extent across the Philippines following typhoon-induced rainfall on November 14,
    2024. The Philippine Space Agency applied image classification techniques to identify
    inundated areas, producing both raster and vector outputs for flood mapping and
    impact assessment.
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
- href: https://data.humdata.org/dataset/philippines-flood-20241114
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Areas affected by typhoon-induced flooding as observed through satellite
      imagery
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
  description: Flooding in the Philippines on November 14, 2024 (Flooding extents
    on November 14, 2024 at 11:56 PM using ALOS-2 satellite image)
  download_url: https://data.humdata.org/dataset/ca8d3292-a23f-424a-8d02-182dc9ceafe9/resource/7ca0eece-9564-4bb3-b3e4-f0ef2ba19ec0/download/20241114_2356_fld_alos2_maps.zip
  format: PNG
  id: resource_7ca0eece
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20241114_2356_fld_alos2_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on November 14, 2024 (Flooding extents
    on November 14, 2024 at 11:56 PM using ALOS-2 satellite image)
  download_url: https://data.humdata.org/dataset/ca8d3292-a23f-424a-8d02-182dc9ceafe9/resource/2ee2f1b2-8e73-4707-a278-e6d05727037b/download/20241114_2356_fld_alos2_shp.zip
  format: null
  id: resource_2ee2f1b2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20241114_2356_fld_alos2_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_philsa_floodingnovember142024_20241114
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
  start: '2024-11-14'
temporal_resolution: null
title: Flooding in the Philippines on November 14, 2024
version: null
vulnerability: null
---
