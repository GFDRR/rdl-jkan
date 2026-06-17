---
attributions:
- entity:
    affiliation: null
    email: null
    name: United States Geological Survey (USGS)
    url: https://data.humdata.org/dataset/damage-in-the-unesco-world-heritage-site-bagan-component-7-as-of-03-april-2025
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-in-the-unesco-world-heritage-site-bagan-component-7-as-of-03-april-2025
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-in-the-unesco-world-heritage-site-bagan-component-7-as-of-03-april-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-in-the-unesco-world-heritage-site-bagan-component-7-as-of-03-april-2025
dataset_id: rdls_hl-mmr_unosat_detecteddamageunescoworld_20250411
description: 'UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 The map shows no visible
  damage within the World Heritage Site when analysed using a very high resolution
  image collected 3 April 2025 when compared to imagery from May 2023. The USGS shake
  map indicates the intensity of the earthquake measured 5.5-6.5 in this area. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-in-the-unesco-world-heritage-site-bagan-component-7-as-of-03-april-2025]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: MMI:-
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared very high resolution satellite imagery from
    May 2023 (pre-event baseline) with imagery acquired on 3 April 2025 (post-earthquake)
    to detect visible damage in the Bagan UNESCO World Heritage Site. Ground motion
    intensity data from USGS shake maps (MMI 5.5-6.5) provided hazard context. This
    is a preliminary satellite-based damage assessment pending field validation.
  sources:
  - id: source_1
    license: null
    name: United States Geological Survey (USGS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-in-the-unesco-world-heritage-site-bagan-component-7-as-of-03-april-2025
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected damage assessment in Bagan World Heritage Site
      showing no visible damage as of 3 April 2025
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: MMI:-
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: 'Myanmar - Satellite-detected damage in the UNESCO World Heritage Site,
    Bagan: Component 7 as of 03 April 2025 (Zipped geodatabase)'
  download_url: https://unosat.org/static/unosat_filesystem/4101/GDB.zip
  format: Geodatabase
  id: resource_a90ee2f6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Myanmar - Satellite-detected damage in the UNESCO World Heritage Site,
    Bagan: Component 7 as of 03 April 2025 (Zipped shapefile)'
  download_url: https://unosat.org/static/unosat_filesystem/4101/SHP.zip
  format: null
  id: resource_e22bab9f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mmr_unosat_detecteddamageunescoworld_20250411
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-04-11'
temporal_resolution: null
title: 'Myanmar - Satellite-detected damage in the UNESCO World Heritage Site, Bagan:
  Component 7 as of 03 April 2025'
version: null
vulnerability: null
---
