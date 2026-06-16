---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kobane-aleppo-governorate-syria-march-06-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kobane-aleppo-governorate-syria-march-06-2015
dataset_id: rdls_el-syr_unosat_geodatadamageassessmentko_20150306
description: 'This map illustrates satellite-detected damage and destruction in a
  portion of the city of Kobane, Aleppo Governorate, Syria. Using satellite imagery
  acquired 22 January 2015, 6 December 2014, and 6 September 2014, UNITAR / UNOSAT
  identified a total of 3,247 affected structures by 22 January 2015 within the area
  analyzed. Approximately 1,206 of these were destroyed, 1,169 severely damaged, and
  872 moderately damaged. A total of 979 impact craters were also identified within
  Kobane and its immediate surroundings. The inset images show craters likely caused
  by air strikes. By 6 December 2014 UNOSAT identified a total of eight craters possible
  caused by air strikes in the neighborhoods of Sanayi and Kaniya Kurdan and by 22
  January 2015 an additional twelve were identified in the neighborhoods of Kaniya
  Kurdan and Saredari, a possible indicator of ongoing bombardment in the area. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kobane-aleppo-governorate-syria-march-06-2015]'
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
    description: Building stock in Kobane classified by damage severity (destroyed,
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
  description: UNOSAT analysts compared multi-temporal satellite imagery acquired
    over 4 months to identify structural damage through visual interpretation of satellite
    scenes. Building damage was classified into three categories (destroyed, severely
    damaged, moderately damaged) and impact craters were mapped. The resulting geodataset
    contains 3,247 affected structures and 979 impact craters with confidence levels
    and validation flags.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kobane-aleppo-governorate-syria-march-06-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from airstrikes and conflict-related destruction
      in Kobane
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Geodata of Damage Assessment of Kobane, Aleppo Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Kobane_20150122_shp.zip
  format: null
  id: resource_9ff6bfaa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kobane_20150122_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Kobane, Aleppo Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Kobane_20150122_gdb.zip
  format: null
  id: resource_cae1ab9b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Kobane_20150122_gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_geodatadamageassessmentko_20150306
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
  start: '2015-03-06'
temporal_resolution: null
title: Geodata of Damage Assessment of Kobane, Aleppo Governorate, Syria
version: null
vulnerability: null
---
