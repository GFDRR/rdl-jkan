---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-western-socotra-island-socotra-governorate-ye-november-13-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-western-socotra-island-socotra-governorate-ye-november-13-2015
dataset_id: rdls_hl-yem_unosat_geodatadamageassessmentwe_20151113
description: 'This map illustrates satellite-detected potential damage following Cyclone
  Chapala in western Socotra Island, Socotra Governorate, Yemen. Using satellite imagery
  acquired 04 November 2015 compared with imagery from 27 October 2015, 10 and 23
  September 2015, UNITAR-UNOSAT analyzed an area of approximately 2,157 square kilometers
  or roughly 59% of the island. A total of 81 potentially damaged structures were
  identified as of 04 November 2015. Many affected structures and boats were observed
  near the settlement of Qulansiyah. Detected damage likely reflects an underestimation
  due to significant cloud obstruction. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-western-socotra-island-socotra-governorate-ye-november-13-2015]'
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "UNOSAT analysts compared satellite imagery acquired on 04 November\
    \ 2015 (post-event) with baseline imagery from 27 October 2015 and September 2015\
    \ to detect structural damage from Cyclone Chapala. Visual change detection identified\
    \ 81 potentially damaged structures across approximately 2,157 km\xC2\xB2 of western\
    \ Socotra Island, with damage records stored as point geometries with confidence\
    \ and validation attributes."
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-western-socotra-island-socotra-governorate-ye-november-13-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Cyclone Chapala detected via satellite
      imagery comparison
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Geodata of Damage Assessment of Western Socotra Island, Socotra Governorate,
    Yemen (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/TC20151103YEM/TC20151103YEM_shp.zip
  format: null
  id: resource_5e47a6dd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20151103YEM_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Western Socotra Island, Socotra Governorate,
    Yemen (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/TC20151103YEM/TC20151103YEM.gdb.zip
  format: null
  id: resource_3a9f64ef
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20151103YEM.gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-yem_unosat_geodatadamageassessmentwe_20151113
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-13'
temporal_resolution: null
title: Geodata of Damage Assessment of Western Socotra Island, Socotra Governorate,
  Yemen
version: null
vulnerability: null
---
