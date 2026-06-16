---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-idlib-idlib-governorate-syria-november-07-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-idlib-idlib-governorate-syria-november-07-2014
dataset_id: rdls_el-syr_unosat_geodatadamageassessmentid_20141107
description: 'This map illustrates satellite-detected damage and destruction in the
  city of Idlib, Idlib Governorate, Syria. Using satellite imagery acquired 02 May
  2014, 15 September 2013, and 22 March 2010, UNITAR / UNOSAT identified a total of
  307 affected structures. Approximately 102 of these were destroyed, 101 severely
  damaged, and 104 moderately damaged. While much of the city was damaged by 15 September
  2013, 115 structures were newly damaged and one structure experienced an increase
  in damage between that date and 02 May 2014. Due to cloud obstruction in 02 May
  2014 imagery, the total number of affected structures may be underestimated. This
  analysis was done of the REACH initiative for the U.S. Office of Foreign Disaster
  Assistance. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-idlib-idlib-governorate-syria-november-07-2014]'
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
    description: Building stock in Idlib city classified by damage state (destroyed,
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
  description: UNOSAT analysts compared satellite imagery from 22 March 2010, 15 September
    2013, and 02 May 2014 to detect and classify structural damage in Idlib city,
    identifying 307 affected buildings categorized as destroyed (102), severely damaged
    (101), or moderately damaged (104) through visual interpretation of multi-temporal
    satellite imagery.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-idlib-idlib-governorate-syria-november-07-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed from satellite imagery comparison
      between 2010-2014
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
  description: Geodata of Damage Assessment of Idlib, Idlib Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR_shp.zip
  format: null
  id: resource_716eccde
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
  description: Geodata of Damage Assessment of Idlib, Idlib Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR.gdb.zip
  format: null
  id: resource_302e015b
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
slug: rdls_el-syr_unosat_geodatadamageassessmentid_20141107
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
  start: '2014-11-07'
temporal_resolution: null
title: Geodata of Damage Assessment of Idlib, Idlib Governorate, Syria
version: null
vulnerability: null
---
