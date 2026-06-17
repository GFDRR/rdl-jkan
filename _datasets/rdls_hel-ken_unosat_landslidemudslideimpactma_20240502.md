---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-mudslide-impact-in-mai-mahiu-and-kijabe-towns-kenya-as-of-1-may-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-mudslide-impact-in-mai-mahiu-and-kijabe-towns-kenya-as-of-1-may-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-mudslide-impact-in-mai-mahiu-and-kijabe-towns-kenya-as-of-1-may-2024
dataset_id: rdls_hel-ken_unosat_landslidemudslideimpactma_20240502
description: "UNOSAT code: FL20240426KEN, GDACS ID: 1102561 This map illustrates satellite-detected\
  \ landslides in Mai Mahiu and Kijabe Towns, Kenya, as observed from a Pl\xE9iades\
  \ image acquired on 1 May 2024 at 11:06 local time (08:06 UTC). Within the analyzed\
  \ area, about 2 km\xB2 of landslide scars with a total length of 10 km were observed.\
  \ UNITAR-UNOSAT identified 1,338 affected structures, about 10 km of affected roads,\
  \ 2 damaged bridges, and 1 damaged railway. This is a preliminary analysis and has\
  \ not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-mudslide-impact-in-mai-mahiu-and-kijabe-towns-kenya-as-of-1-may-2024]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building structures affected by landslide/mudslide events in Mai
      Mahiu and Kijabe Towns
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Road network and railway infrastructure affected by landslide/mudslide
      events
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
      intensity_measure: AA:km2
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Pl\xE9iades satellite imagery acquired on\
    \ 1 May 2024 over Mai Mahiu and Kijabe Towns, Kenya, identifying landslide/mudslide\
    \ scars through visual interpretation and comparing with reference imagery. Affected\
    \ structures and infrastructure were mapped and counted from the satellite-detected\
    \ features. This is a preliminary post-event damage assessment based on remote\
    \ sensing observation without field validation."
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/landslide-mudslide-impact-in-mai-mahiu-and-kijabe-towns-kenya-as-of-1-may-2024
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct damage to 1,338 structures from satellite-detected landslide/mudslide
      events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: landslide
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to approximately 10 km of roads, 2 bridges, and 1 railway
      from landslide/mudslide events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
  description: Landslide/mudslide Impact in Mai Mahiu and Kijabe Towns, Kenya as of
    1 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3832/FL20240426KEN_gdb.zip
  format: Geodatabase
  id: resource_ec499358
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide/mudslide Impact in Mai Mahiu and Kijabe Towns, Kenya as of
    1 May 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3832/FL20240426KEN_SHP.zip
  format: null
  id: resource_aa177a4d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_unosat_landslidemudslideimpactma_20240502
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-02'
temporal_resolution: null
title: Landslide/mudslide Impact in Mai Mahiu and Kijabe Towns, Kenya as of 1 May
  2024
version: null
vulnerability: null
---
