---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-daraa-daraa-governorate-syria
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-daraa-daraa-governorate-syria
dataset_id: rdls_el-syr_unosat_damageassessmentdaraadara_20170612
description: 'This map illustrates satellite-detected damage in the city of Daraa,
  Syrian Arab Republic. Using satellite imagery acquired 07 February and 06 January
  2017, 19 April 2016, 04 June 2015, 01 January 2014, and 07 September 2013, UNITAR
  - UNOSAT identified a total of 1,503 affected structures within the city. Approximately
  224 of these were destroyed, 498 severely damaged, and 781 moderately damaged. While
  some of the city was damaged by 19 April 2016, 419 structures were newly damaged
  and 7 structures experienced an increase in damage between that date and 07 February
  2017. This analysis does not include pre-war military bases and facilities. This
  analysis was done as part of the REACH initiative for the U.S. Office of Foreign
  Disaster Assistance. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-of-daraa-daraa-governorate-syria]'
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
    description: Building stock in Daraa city classified by damage state from satellite
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
  description: UNOSAT analysts compared satellite imagery acquired across six dates
    (2013-2017) to identify structural damage in Daraa city through visual interpretation
    of satellite data. Buildings were classified into damage states (destroyed, severely
    damaged, moderately damaged) based on observable changes in building footprints
    and structural integrity between image pairs. The resulting point dataset contains
    1,503 affected structures with confidence levels and damage classifications.
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
- href: https://data.humdata.org/dataset/damage-assessment-of-daraa-daraa-governorate-syria
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Daraa
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
  description: Damage assessment of Daraa, Daraa Governorate, Syria (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_A3_Daraa_Damage_Points_20170207.gdb.zip
  format: Geodatabase
  id: resource_bc625255
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_A3_Daraa_Damage_Points_20170207.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment of Daraa, Daraa Governorate, Syria (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_A3_Daraa_Damage_Points_20170207.zip
  format: null
  id: resource_f23777ac
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_A3_Daraa_Damage_Points_20170207.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_damageassessmentdaraadara_20170612
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
  start: '2017-06-12'
temporal_resolution: null
title: Damage assessment of Daraa, Daraa Governorate, Syria
version: null
vulnerability: null
---
