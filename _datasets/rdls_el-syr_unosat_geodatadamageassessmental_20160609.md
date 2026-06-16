---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-al-quaryatayn-homs-governorate-syria-june-09-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-al-quaryatayn-homs-governorate-syria-june-09-2016
dataset_id: rdls_el-syr_unosat_geodatadamageassessmental_20160609
description: 'This map illustrates satellite-detected areas of damage in the town
  of Al Quaryatayn, Homs Governorate, Syria. Using Pleiades satellite imagery acquired
  07 May 2016 and 20 August 2010 WorldView-2 imagery as a reference, UNITAR-UNOSAT
  identified a total of 616 potentially damaged structures. Approximately 79 of these
  were destroyed, 190 severely damaged, 256 moderately damaged, and 91 possibly damaged.
  Additionally, a total of 11 impact craters were observed. Due to cloud obstruction,
  an underestimation of damage is possible. This is a preliminary analysis & has not
  yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-al-quaryatayn-homs-governorate-syria-june-09-2016]'
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
    description: Building stock classified by damage severity (destroyed, severely
      damaged, moderately damaged, possibly damaged)
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
  description: UNOSAT analysts compared multi-temporal satellite imagery (Pleiades
    2016 and WorldView-2 2010) to detect and classify structural damage in Al Quaryatayn.
    Damage was categorized into four severity levels (destroyed, severely damaged,
    moderately damaged, possibly damaged) and impact craters were manually identified.
    The analysis is preliminary and subject to cloud obstruction limitations.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-al-quaryatayn-homs-governorate-syria-june-09-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related impact in
      Al Quaryatayn
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
  description: 'Geodata of Damage Assessment: Al Quaryatayn, Homs Governorate, Syria
    (Shapefile)'
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Al_Quaryatayn_20160507_shp.zip
  format: null
  id: resource_76a59d12
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Al_Quaryatayn_20160507_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Geodata of Damage Assessment: Al Quaryatayn, Homs Governorate, Syria
    (Shapefile)'
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Al_Quaryatayn_20160507.gdb.zip
  format: null
  id: resource_ea83c0f5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Al_Quaryatayn_20160507.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_geodatadamageassessmental_20160609
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
  start: '2016-06-09'
temporal_resolution: null
title: 'Geodata of Damage Assessment: Al Quaryatayn, Homs Governorate, Syria'
version: null
vulnerability: null
---
