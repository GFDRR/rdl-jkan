---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-of-ar-raqqa-ar-raqqa-governorate-syria-2742
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-of-ar-raqqa-ar-raqqa-governorate-syria-2742
dataset_id: rdls_el-syr_unosat_damagedensityarraqqaarraq_20171128
description: 'This map illustrates satellite-detected damage density in the city of
  Ar Raqqa, Syrian Arab Republic. Using satellite imagery acquired 21 October 2017,
  03 February 2017, 29 May 2015, 12 February 2014, 22 October 2013, UNITAR - UNOSAT
  identified a total of 12,668 affected structures within the city. Approximately
  3,289 of these were destroyed, 3,924 severely damaged, and 5,455 moderately damaged.
  While some damaged was present by 3 February, most of the damaged occured between
  that date and 21 October 2017 when 10,991 structures were newly damaged and 64 structures
  experienced an increase in damage.This analysis does not include pre-war military
  bases and facilities. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-density-of-ar-raqqa-ar-raqqa-governorate-syria-2742]'
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
    description: Building stock in Ar Raqqa city classified by damage state from satellite
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
  description: UNOSAT analysts compared satellite imagery acquired on five dates (22
    October 2013, 12 February 2014, 29 May 2015, 03 February 2017, 21 October 2017)
    to detect structural damage in Ar Raqqa city. Buildings were classified into damage
    categories (destroyed, severely damaged, moderately damaged) based on visual interpretation
    of satellite-detected changes. The resulting geodatabase contains 12,668 affected
    structures with damage state classifications and temporal metadata.
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
- href: https://data.humdata.org/dataset/damage-density-of-ar-raqqa-ar-raqqa-governorate-syria-2742
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Ar Raqqa
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
  description: Damage density of Ar Raqqa, Ar Raqqa Governorate, Syria (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Raqqa_Deir.gdb.zip
  format: Geodatabase
  id: resource_cdd81dc6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130604SYR_Raqqa_Deir.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage density of Ar Raqqa, Ar Raqqa Governorate, Syria (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/CE20130604SYR_Raqqa_Deir_shp.zip
  format: null
  id: resource_07d7200a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130604SYR_Raqqa_Deir_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_damagedensityarraqqaarraq_20171128
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
  start: '2017-11-28'
temporal_resolution: null
title: Damage density of Ar Raqqa, Ar Raqqa Governorate, Syria
version: null
vulnerability: null
---
