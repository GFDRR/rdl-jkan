---
attributions:
- entity:
    affiliation: null
    email: null
    name: Philippine Space Agency
    url: https://data.humdata.org/dataset/philippines-flood-20221103
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20221103
creator:
  affiliation: null
  email: null
  name: The Philippine Space Agency
  url: https://data.humdata.org/dataset/philippines-flood-20221103
dataset_id: rdls_hl-phl_philsa_floodingnovember032022_20221103
description: 'This dataset shows the actual extent of flooding in the Philippines
  caused by typhoons or tropical cyclones as of November 03, 2022, as observed through
  available satellite imagery. The dataset can be used to track the progression of
  floods over time, identify areas at risk, and assess the impact of these natural
  disasters on infrastructure, agriculture, and local populations.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/philippines-flood-20221103]'
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
  description: Satellite imagery (ICEYE SAR) was processed by the Philippine Space
    Agency to detect and map actual flood extent on November 3, 2022 following typhoon-induced
    rainfall and storm surge. The resulting flood polygons with area measurements
    represent observed inundation footprints derived from radar backscatter analysis,
    enabling post-event impact assessment of affected agricultural and infrastructure
    areas.
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
- href: https://data.humdata.org/dataset/philippines-flood-20221103
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
    description: Infrastructure areas affected by typhoon-induced flooding
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
  description: Flooding in the Philippines on November 03, 2022 (Flooding extents
    on November 03, 2022 at 01:42 AM using ICEYE satellite image)
  download_url: https://data.humdata.org/dataset/ee9b51c7-741c-4f19-8a2d-75c0ce15817f/resource/62350fb2-c824-439a-aec5-2f5e9cfbf69f/download/20221103_0142_fld_iceye_maps.zip
  format: PNG
  id: resource_62350fb2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20221103_0142_fld_iceye_maps.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flooding in the Philippines on November 03, 2022 (Flooding extents
    on November 03, 2022 at 01:42 AM using ICEYE satellite image)
  download_url: https://data.humdata.org/dataset/ee9b51c7-741c-4f19-8a2d-75c0ce15817f/resource/4e2dfeaf-a8fb-41cb-9fa4-f9ed37e2c35b/download/20221103_0142_fld_iceye_shp.zip
  format: null
  id: resource_4e2dfeaf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 20221103_0142_fld_iceye_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_philsa_floodingnovember032022_20221103
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
  start: '2022-11-03'
temporal_resolution: null
title: Flooding in the Philippines on November 03, 2022
version: null
vulnerability: null
---
