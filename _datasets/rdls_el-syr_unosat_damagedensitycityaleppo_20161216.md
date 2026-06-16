---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-in-the-city-of-aleppo-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-in-the-city-of-aleppo-syria
dataset_id: rdls_el-syr_unosat_damagedensitycityaleppo_20161216
description: 'This map illustrates satellite-detected damage density in the city of
  Aleppo, Syrian Arab Republic. Satellite imagery acquired 18 September 2016, 01 May
  2015, 26 April 2015, 23 May 2014, 23 September 2013, and 21 November 2010 was analyzed.
  UNITAR - UNOSAT identified a total of 35,722 affected structures, of which 4,773
  were destroyed, 14,680 severely damaged, and 16,269 moderately damaged, as of 18
  September 2016. This represents an increase of approximately 154.5% in total damage
  since the previous UNITAR-UNOSAT analysis done using images from 1 May 2015 and
  26 April 2015. This analysis was done as part of the REACH initiative for the U.S.
  Office of Foreign Disaster Assistance. It is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-density-in-the-city-of-aleppo-syria]'
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
    description: Building stock in Aleppo classified by damage severity (destroyed,
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery acquired
    between November 2010 and September 2016 to detect structural damage in Aleppo.
    Buildings were classified into damage categories (destroyed, severely damaged,
    moderately damaged) through visual interpretation of satellite imagery changes,
    producing a spatially-explicit damage inventory with 35,722 affected structures.
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
- href: https://data.humdata.org/dataset/damage-density-in-the-city-of-aleppo-syria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Aleppo
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
  description: Damage Density in the City of Aleppo, Syria (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
  format: Geodatabase
  id: resource_dfcbdb50
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
  description: Damage Density in the City of Aleppo, Syria (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_shp.zip
  format: null
  id: resource_55d40087
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
slug: rdls_el-syr_unosat_damagedensitycityaleppo_20161216
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
  start: '2016-12-16'
temporal_resolution: null
title: Damage Density in the City of Aleppo, Syria
version: null
vulnerability: null
---
