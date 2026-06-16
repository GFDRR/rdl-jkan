---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/percentage-damage-in-residential-area-of-aleppo-city
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/percentage-damage-in-residential-area-of-aleppo-city
dataset_id: rdls_el-syr_unosat_percentagedamageresidenti_20161220
description: 'This map illustrates the percentage of buildings damaged in the city
  of Aleppo, Syrian Arabic Republic, as determined by satellite imagery analysis.
  Using satellite imagery acquired 18 September 2016, 01 May 2015, 26 April 2015,
  23 May 2014, 23 September 2013, and 21 November 2010, UNOSAT identified a total
  of 33,521 damaged structures within the extent of this map. These damaged structures
  are compared with total numbers of buildings found in a pre-conflict satellite image
  collected in 2009 to determine the percentage of damaged buildings across the city.
  Note that this analysis considers only damage in residential areas and excludes
  industrial areas. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/percentage-damage-in-residential-area-of-aleppo-city]'
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
    description: Residential building stock in Aleppo City identified from satellite
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery acquired
    between 2010 and 2016 against a pre-conflict baseline image from 2009 to identify
    structural damage in residential areas. Damaged structures (33,521 total) were
    counted and expressed as a percentage of total buildings in the pre-conflict inventory
    to produce a damage assessment map of Aleppo City.
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
- href: https://data.humdata.org/dataset/percentage-damage-in-residential-area-of-aleppo-city
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed through satellite imagery comparison
      across multiple time periods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
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
  description: Syrian Arab Republic - Percentage damage in residential area of Aleppo
    City (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_DamageAssessment_OFDA_REACH_UPDATE4/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
  format: Geodatabase
  id: resource_cf9d06e1
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
  description: Syrian Arab Republic - Percentage damage in residential area of Aleppo
    City (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_DamageAssessment_OFDA_REACH_UPDATE4/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_shp.zip
  format: null
  id: resource_197ee6df
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
slug: rdls_el-syr_unosat_percentagedamageresidenti_20161220
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
  start: '2016-12-20'
temporal_resolution: null
title: Syrian Arab Republic - Percentage damage in residential area of Aleppo City
version: null
vulnerability: null
---
