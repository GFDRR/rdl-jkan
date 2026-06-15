---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/neighborhood-shelter-damage-percentages-in-aleppo-city
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/neighborhood-shelter-damage-percentages-in-aleppo-city
dataset_id: rdls_el-syr_unosat_percentagebuildingsdamage_20161219
description: 'This map illustrates the percentage of buildings damaged in the city
  of Aleppo, Syrian Arabic Republic, as determined by satellite imagery analysis.
  Using satellite imagery acquired 18 September 2016, 01 May 2015, 26 April 2015,
  23 May 2014, 23 September 2013, and 21 November 2010, UNOSAT identified a total
  of 33,521 damaged structures within the extent of this map. These damaged structures
  are compared with total numbers of buildings found in a pre-conflict satellite image
  collected in 2009 to determine the percentage of damaged buildings across the city.
  Based on this analysis and in the map extent, in 19 neighborhoods the number of
  damaged buildings is more than 40%. The most damaged is Al Aqabeh with 65.61% of
  buildings damaged and the most significant change since UNOSAT''s 2015 analysis
  is Khalidiyeh, which increased in percentage damage from 4.20% to 55.80%. Note that
  this analysis considers only damage in residential areas and excludes industrial
  areas. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/neighborhood-shelter-damage-percentages-in-aleppo-city]'
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
    description: Building stock in Aleppo city identified from pre-conflict 2009 satellite
      imagery
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (baseline
    2009, observations 2010-2016) of Aleppo city to identify structural damage through
    visual interpretation. Damaged structures (33,521 total) were counted and compared
    against the total building inventory from the 2009 pre-conflict baseline to calculate
    damage percentages by neighborhood, producing a damage assessment map.
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
- href: https://data.humdata.org/dataset/neighborhood-shelter-damage-percentages-in-aleppo-city
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed through satellite imagery comparison
      between 2009 baseline and 2016 post-conflict conditions
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
  - asset_category: buildings
    asset_dimension: structure
    description: Percentage of buildings damaged relative to total building stock
      in Aleppo city
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: damage
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
  description: Syrian Arab Republic - Percentage of buildings damaged in the city
    of Aleppo (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_DamageAssessment_OFDA_REACH_UPDATE4/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
  format: Geodatabase
  id: resource_2c37bd97
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Syrian Arab Republic - Percentage of buildings damaged in the city
    of Aleppo (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_DamageAssessment_OFDA_REACH_UPDATE4/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_shp.zip
  format: null
  id: resource_b6101006
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_percentagebuildingsdamage_20161219
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
  start: '2016-12-19'
temporal_resolution: null
title: Syrian Arab Republic - Percentage of buildings damaged in the city of Aleppo
version: null
vulnerability: null
---
