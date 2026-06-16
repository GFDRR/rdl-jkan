---
attributions:
- entity:
    affiliation: null
    email: null
    name: OFDA-REACH
    url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-hama-hama-governorate-syria-november-06-2014
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-hama-hama-governorate-syria-november-06-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-hama-hama-governorate-syria-november-06-2014
dataset_id: rdls_el-syr_unosat_geodatadamageassessmentha_20141106
description: 'This map illustrates satellite-detected damage and destruction in a
  portion of the city of Hama, Hama Governorate, Syria. Using satellite imagery acquired
  05 March 2014, 26 September 2013, and 06 August 2010, UNITAR / UNOSAT identified
  a total of 4,976 affected structures within the area of this map. Approximately
  4,492 of these were destroyed, 174 severely damaged, and 310 moderately damaged.
  The city-wide analysis of Hama revealed a total of 5,233 affected structures, of
  which 4,671 were destroyed, 216 severely damaged, and 346 moderately damaged. While
  most of the city was damaged by 26 September 2013, 308 structures were newly damaged
  and 6 structures experienced an increase in damage between that date and 05 March
  2014. This analysis was done of the REACH initiative for the U.S. Office of Foreign
  Disaster Assistance. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-hama-hama-governorate-syria-november-06-2014]'
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
    description: Building stock in Hama city classified by damage state (destroyed,
      severely damaged, moderately damaged)
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
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (06 August
    2010, 26 September 2013, 05 March 2014) of Hama city to identify structural changes
    and classify affected buildings into damage categories (destroyed, severely damaged,
    moderately damaged) through visual interpretation. Building footprints and damage
    states were vectorized into shapefiles with damage classification attributes,
    producing a post-event damage inventory for humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OFDA-REACH
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-hama-hama-governorate-syria-november-06-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Hama
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
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
  description: Geodata of Damage Assessment of Hama, Hama Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR_shp.zip
  format: null
  id: resource_ce76107b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Hama, Hama Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR.gdb.zip
  format: null
  id: resource_a9c490f8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_geodatadamageassessmentha_20141106
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-11-06'
temporal_resolution: null
title: Geodata of Damage Assessment of Hama, Hama Governorate, Syria
version: null
vulnerability: null
---
