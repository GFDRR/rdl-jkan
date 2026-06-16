---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNITAR
    url: https://data.humdata.org/dataset/damage-density-2015-of-deir-ez-zor-deir-ez-zor-governorate-syria
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-2015-of-deir-ez-zor-deir-ez-zor-governorate-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-2015-of-deir-ez-zor-deir-ez-zor-governorate-syria
dataset_id: rdls_el-syr_unosat_damagedensity2015deirezzo_20170106
description: 'This map illustrates satellite-detected damage density in the city of
  Deir Ez Zor, Syrian Arab Republic. Using satellite imagery acquired 10 May 2015,
  13 May 2014, 24 October 2013, and 05 December 2010 UNITAR - UNOSAT identified a
  total of 3,435 affected structures within the city. Approximately 538 of these were
  destroyed, 1,153 severely damaged, and 1,744 moderately damaged. While much of the
  city was damaged by 13 May 2014, 349 structures were newly damaged and 70 structures
  experienced an increase in damage between that date and 10 May 2015. This analysis
  was done as part of the REACH initiative for the U.S. Office of Foreign Disaster
  Assistance. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-density-2015-of-deir-ez-zor-deir-ez-zor-governorate-syria]'
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
    description: Building stock in Deir Ez Zor city classified by damage severity
      (destroyed, severely damaged, moderately damaged)
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
  description: UNOSAT analysts compared satellite imagery acquired on 05 December
    2010, 24 October 2013, 13 May 2014, and 10 May 2015 to detect and classify building
    damage in Deir Ez Zor city. Damage was categorized into three severity classes
    (destroyed, severely damaged, moderately damaged) based on visual interpretation
    of structural changes between image dates. The dataset contains 3,435 affected
    structures with temporal tracking of damage progression.
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
    name: UNITAR
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-density-2015-of-deir-ez-zor-deir-ez-zor-governorate-syria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed from satellite imagery comparing
      multiple dates (2010-2015)
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
  description: Syria - Damage density 2015 of Deir Ez Zor, Deir Ez Zor Governorate
    (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
  format: Geodatabase
  id: resource_ab7b4337
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
  description: Syria - Damage density 2015 of Deir Ez Zor, Deir Ez Zor Governorate
    (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_shp.zip
  format: null
  id: resource_68bc400e
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
slug: rdls_el-syr_unosat_damagedensity2015deirezzo_20170106
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
  start: '2017-01-06'
temporal_resolution: null
title: Syria - Damage density 2015 of Deir Ez Zor, Deir Ez Zor Governorate
version: null
vulnerability: null
---
