---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-jobar-neighborhood-and-irbin-city-damascus-governorate-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-jobar-neighborhood-and-irbin-city-damascus-governorate-syria
dataset_id: rdls_el-syr_unosat_damageassessmentjobarneig_20170117
description: 'This map illustrates satellite-detected damage east of the city of Damascus,
  Syrian Arab Republic. Using satellite imagery acquired 02 April 2016, UNITAR - UNOSAT
  identified a total of 17,043 affected structures within and around the Jobar neighborhood
  and the city of Irbin. Approximately 4,492 of these were destroyed, 7,032 severely
  damaged, and 5,525 moderately damaged. This analysis was done as part of a broader
  analysis of areas around Damascus, and the full analysis revealed a total of 24,391
  affected structures, of which 7,346 were destroyed, 9,423 severely damaged, and
  7,622 moderately damaged. This analysis does not include pre-war military bases
  and facilities. This analysis was done as part of the REACH initiative for the U.S.
  Office of Foreign Disaster Assistance. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-of-jobar-neighborhood-and-irbin-city-damascus-governorate-syria]'
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
    description: Building stock in Jobar neighborhood and Irbin city classified by
      damage severity
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
  description: UNOSAT analysts compared satellite imagery acquired on April 2, 2016
    with reference imagery to detect structural damage in Jobar and Irbin. Affected
    structures were classified into three damage categories (destroyed, severely damaged,
    moderately damaged) through visual interpretation of satellite-detected changes,
    producing a spatial inventory of 17,043 affected buildings in the study area.
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
- href: https://data.humdata.org/dataset/damage-assessment-of-jobar-neighborhood-and-irbin-city-damascus-governorate-syria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Damascus governorate
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
  description: Syria - Damage assessment of Jobar neighborhood and Irbin city, Damascus
    governorate. (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_gdb.zip
  format: Geodatabase
  id: resource_6fb167a9
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
  description: Syria - Damage assessment of Jobar neighborhood and Irbin city, Damascus
    governorate. (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_Syria_Damage_Assessment_2016_shp.zip
  format: null
  id: resource_60788885
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
slug: rdls_el-syr_unosat_damageassessmentjobarneig_20170117
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
title: Syria - Damage assessment of Jobar neighborhood and Irbin city, Damascus governorate.
version: null
vulnerability: null
---
