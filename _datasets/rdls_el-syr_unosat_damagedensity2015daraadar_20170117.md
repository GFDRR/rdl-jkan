---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-2015-of-daraa-daraa-governorate-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-2015-of-daraa-daraa-governorate-syria
dataset_id: rdls_el-syr_unosat_damagedensity2015daraadar_20170117
description: 'This map illustrates satellite-detected damage density in the city of
  Daraa, Syrian Arab Republic. Using satellite imagery acquired 04 June 2015, 01 May
  2014, 07 September 2013, and 14 December 2010, UNITAR - UNOSAT identified a total
  of 990 affected structures, of which 152 were destroyed, 358 severely damaged, and
  480 moderately damaged. This analysis does not include pre-war military bases and
  facilities. Trend analysis shows an increase in the number of damaged structures
  since 1 May 2014 and approximately 618 structures are newly damaged. This analysis
  was done as part of the REACH initiative for the U.S. Office of Foreign Disaster
  Assistance. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-density-2015-of-daraa-daraa-governorate-syria]'
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
    description: Building stock in Daraa city classified by damage severity (destroyed,
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
  description: UNOSAT analysts compared satellite imagery acquired on 14 December
    2010, 07 September 2013, 01 May 2014, and 04 June 2015 to detect structural damage
    in Daraa city. Visual interpretation identified 990 affected structures classified
    into three damage categories (destroyed, severely damaged, moderately damaged),
    with trend analysis quantifying 618 newly damaged structures between May 2014
    and June 2015.
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
- href: https://data.humdata.org/dataset/damage-density-2015-of-daraa-daraa-governorate-syria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction detected
      via satellite imagery
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
  description: Syria - Damage density 2015 of Daraa, Daraa Governorate, (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
  format: Geodatabase
  id: resource_6156c511
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
  description: Syria - Damage density 2015 of Daraa, Daraa Governorate, (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_shp.zip
  format: null
  id: resource_8da80e9c
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
slug: rdls_el-syr_unosat_damagedensity2015daraadar_20170117
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
  start: '2017-01-17'
temporal_resolution: null
title: Syria - Damage density 2015 of Daraa, Daraa Governorate,
version: null
vulnerability: null
---
