---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-jilah-village-shabwah-governorate-yemen-november-06-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-jilah-village-shabwah-governorate-yemen-november-06-2015
dataset_id: rdls_hel-yem_unosat_geodatadamageassessmentji_20151106
description: 'This map illustrates satellite-detected damage and destruction in Jilah
  village, Shabwah Governorate, Yemen. Using satellite imagery acquired 5 November
  2015 and comparing with imagery collected on 22 August 2015, UNITAR - UNOSAT identified
  an area severely affected by flash flood resulting from rains during Cyclone Chapala.
  Imagery shows that the town of Jilah is partially covered by mud and a total of
  150 structures appear damaged. Approximately 58 of these were destroyed, 57 severely
  damaged, and 35 moderately damaged. Primary road N4 is also highly affected by mud
  as a consequence of the flash floods and it is impassable across several sections.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-jilah-village-shabwah-governorate-yemen-november-06-2015]'
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
    description: Building stock in Jilah village identified through satellite imagery
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
    description: Primary road N4 network affected by mud and flooding
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery acquired before (22 August
    2015) and after (5 November 2015) Cyclone Chapala to detect damage in Jilah village.
    Visual interpretation of satellite imagery identified mud coverage, building damage
    classifications, and infrastructure impacts. Damage assessments were classified
    by severity level (destroyed, severely damaged, moderately damaged) and mapped
    as vector geometries.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-jilah-village-shabwah-governorate-yemen-november-06-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from Cyclone Chapala: 150 structures damaged
      (58 destroyed, 57 severely damaged, 35 moderately damaged)'
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Direct infrastructure damage from flash flooding: primary road N4
      covered by mud'
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
  description: Geodata of Damage Assessment of Jilah Village, Shabwah Governorate,
    Yemen (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/TC20151103YEM/TC20151103YEM_shp.zip
  format: null
  id: resource_53f267a7
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
  description: Geodata of Damage Assessment of Jilah Village, Shabwah Governorate,
    Yemen (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/TC20151103YEM/TC20151103YEM.gdb.zip
  format: null
  id: resource_8a1230c7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20151103YEM.gdb.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-yem_unosat_geodatadamageassessmentji_20151106
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
  start: '2015-11-06'
temporal_resolution: null
title: Geodata of Damage Assessment of Jilah Village, Shabwah Governorate, Yemen
version: null
vulnerability: null
---
