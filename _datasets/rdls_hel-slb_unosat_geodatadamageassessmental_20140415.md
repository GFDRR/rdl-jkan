---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-along-matanikau-river-honiara-guadalcanal-solomo-april-15-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-along-matanikau-river-honiara-guadalcanal-solomo-april-15-2014
dataset_id: rdls_hel-slb_unosat_geodatadamageassessmental_20140415
description: 'This map illustrates satellite-detected urban areas that were affected
  by flash flooding along the Matanikau River in Honiara, capital city of the Solomon
  Islands. Analysis was conducted using a Resurs-P panchromatic image acquired the
  08th and the 13th of April 2014. Traces of waters can be seen in urban areas along
  the Matakinau River and ~ 100 houses seem to have been washed out and/or flooded
  by the flash flooding event in the identified areas. A bridge in the Chinatown neighbourhood
  appears to be totally destroyed, however the main bridge further north seems intact.
  The exact limit of flood affected zones is uncertain because of the sensor characteristics
  of the satellite data and the nature of the vent (flash flood). This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR / UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-along-matanikau-river-honiara-guadalcanal-solomo-april-15-2014]'
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
    description: Urban building stock in Honiara affected by flash flooding along
      Matanikau River
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
  event_sets:
  - analysis_type: probabilistic
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (Resurs-P
    panchromatic images acquired 8-13 April 2014) to detect changes in urban areas
    affected by flash flooding along Matanikau River. Visual interpretation identified
    water traces, damaged/destroyed buildings, and infrastructure damage in Honiara,
    Solomon Islands, resulting in a post-event damage assessment map.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-along-matanikau-river-honiara-guadalcanal-solomo-april-15-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flash flooding; approximately
      100 houses washed out or flooded
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
    description: Direct infrastructure damage from fluvial flooding; bridge in Chinatown
      neighbourhood totally destroyed
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
  description: Geodata of Damage Assessment Along Matanikau River, Honiara, Guadalcanal,
    Solomon Islands (KML)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SB/FL20140405SLB/UNOSAT_Honiara_Damage_20140413.KMZ
  format: null
  id: resource_17639fe4
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Honiara_Damage_20140413.KMZ
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-slb_unosat_geodatadamageassessmental_20140415
spatial:
  bbox: null
  centroid: null
  countries:
  - SLB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-04-15'
temporal_resolution: null
title: Geodata of Damage Assessment Along Matanikau River, Honiara, Guadalcanal, Solomon
  Islands
version: null
vulnerability: null
---
