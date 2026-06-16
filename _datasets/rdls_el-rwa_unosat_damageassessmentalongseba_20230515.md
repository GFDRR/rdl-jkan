---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-along-the-sebaya-river-rubavu-and-karongi-districts-western-province-rwa
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-along-the-sebaya-river-rubavu-and-karongi-districts-western-province-rwa
dataset_id: rdls_el-rwa_unosat_damageassessmentalongseba_20230515
description: 'UNOSAT code FL20230504RWA, GDACS Id: 1101977 This map illustrates satellite-based
  damage assessment along the Sebaya River, Rubavu and Karongi Districts, Western
  Province, Rwanda detected by using a Pleiades very high resolution satellite image
  acquired on 6 May 2023. Within the analyzed area, UNOSAT identified 355 affected
  and potentially affected structures. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to United Nations Satellite
  Centre (UNOSAT).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-along-the-sebaya-river-rubavu-and-karongi-districts-western-province-rwa]'
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
    description: Building structures affected and potentially affected by flooding
      along the Sebaya River
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
  description: UNOSAT analysts reviewed Pleiades very high resolution satellite imagery
    acquired on 6 May 2023 and compared it with reference imagery to detect notable
    changes in building structures along the Sebaya River. Change detection analysis
    identified 355 affected and potentially affected structures in Rubavu and Karongi
    Districts. This is a preliminary post-event damage assessment not yet validated
    in the field.
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
- href: https://data.humdata.org/dataset/damage-assessment-along-the-sebaya-river-rubavu-and-karongi-districts-western-province-rwa
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding detected via satellite
      imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Damage assessment along the Sebaya River, Rubavu and Karongi Districts,
    Western Province, Rwanda. - 6 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3590/FL20230504RWA_gdb.zip
  format: Geodatabase
  id: resource_cc460fc8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230504RWA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment along the Sebaya River, Rubavu and Karongi Districts,
    Western Province, Rwanda. - 6 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3590/FL20230504RWA_SHP.zip
  format: null
  id: resource_c3693634
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230504RWA_SHP.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-rwa_unosat_damageassessmentalongseba_20230515
spatial:
  bbox: null
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-15'
temporal_resolution: null
title: Damage assessment along the Sebaya River, Rubavu and Karongi Districts, Western
  Province, Rwanda. - 6 May 2023
version: null
vulnerability: null
---
