---
attributions:
- entity:
    affiliation: null
    email: null
    name: USGS Earthquake Hazards Program
    url: https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-innwa-as-of-30-ma
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-innwa-as-of-30-ma
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-innwa-as-of-30-ma
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-innwa-as-of-30-ma
dataset_id: rdls_hel-mmr_unosat_detecteddamageunescotenta_20250411
description: 'UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 This map shows the locations
  where damage was detected based on a very high resolution satellite image collected
  30 March 2025 when compared to very high resolution satellite imagery from 24 February
  2025 and 23 March 2025. The USGS shake map indicates the intensity of the earthquake
  measured 8.5 in this area. Across the site, 18 damaged buildings within the property
  boundary, and 25 damaged buildings within the buffer zone. An additional 2 buildings
  in the property boundary and 5 buildings in the buffer zone have possible damage.
  Part of a wall to the south of the Innwa area was also damaged. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-innwa-as-of-30-ma]'
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
    description: Building stock within UNESCO Tentative List Site (Innwa) property
      boundary and buffer zone
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
hazard:
  event_sets_by_hazard_type:
    earthquake:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared very high resolution satellite imagery from
    24 February 2025, 23 March 2025, and 30 March 2025 to detect structural damage
    in the Innwa UNESCO site following the 28 March 2025 earthquake (magnitude 8.5).
    Damage was classified as confirmed or possible based on visual interpretation
    of change detection between pre- and post-event imagery, with results georeferenced
    to property boundary and buffer zone polygons.
  sources:
  - id: source_1
    license: null
    name: USGS Earthquake Hazards Program
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
- href: https://data.humdata.org/dataset/damage-in-the-unesco-tentative-list-site-ancient-cities-of-upper-myanmar-innwa-as-of-30-ma
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake ground shaking detected via
      satellite imagery comparison
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
  description: 'Satellite-detected damage in the UNESCO Tentative List Site, Ancient
    Cities of Upper Myanmar: Innwa as of 30 March 2025 (Zipped geodatabase)'
  download_url: https://unosat.org/static/unosat_filesystem/4100/GDB.zip
  format: Geodatabase
  id: resource_7c078bd3
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
  description: 'Satellite-detected damage in the UNESCO Tentative List Site, Ancient
    Cities of Upper Myanmar: Innwa as of 30 March 2025 (Zipped shapefile)'
  download_url: https://unosat.org/static/unosat_filesystem/4100/SHP.zip
  format: null
  id: resource_2f17d1f2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mmr_unosat_detecteddamageunescotenta_20250411
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
title: 'Satellite-detected damage in the UNESCO Tentative List Site, Ancient Cities
  of Upper Myanmar: Innwa as of 30 March 2025'
version: null
vulnerability: null
---
