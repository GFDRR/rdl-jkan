---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-chein-khar-li-ku-lar-village-rakhine-state-myanmar
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-chein-khar-li-ku-lar-village-rakhine-state-myanmar
dataset_id: rdls_el-mmr_unosat_damageassessmentcheinkhar_20170919
description: 'This map illustrates satellite-detected damage in the village of Chein
  Khar Li (Ku Lar), Koe Tan Kauk tract, Rathedaung township, Rakhine state, Myanmar.
  Using imagery collected on 31 August 2017, and comparing with imagery collected
  on 16 May 2017, UNOSAT identified 671 destroyed structures whitin the village. Analysis
  showed visible signs of scorching with darkened soils and burned vegetation. Almost
  the entire village appears destroyed. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-the-chein-khar-li-ku-lar-village-rakhine-state-myanmar]'
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
    description: Building structures in Chein Khar Li village identified through satellite
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
  description: UNOSAT analysts compared satellite imagery from 16 May 2017 (pre-event)
    and 31 August 2017 (post-event) over Chein Khar Li village to detect structural
    damage through visual interpretation of darkened soils, scorching, and burned
    vegetation patterns, identifying 671 destroyed structures as direct impacts from
    the conflict event.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-the-chein-khar-li-ku-lar-village-rakhine-state-myanmar
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building destruction from wildfire with 671 destroyed structures
      identified via satellite damage assessment
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
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
  description: Damage assessment in the Chein Khar Li (Ku Lar) village, Rakhine state,
    Myanmar (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/MM/CE20130326MMR/CE20130326MMR_ToeKan_20170831.gdb.zip
  format: Geodatabase
  id: resource_f937bad2
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130326MMR_ToeKan_20170831.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment in the Chein Khar Li (Ku Lar) village, Rakhine state,
    Myanmar (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/MM/CE20130326MMR/CE20130326MMR_ToeKan_20170831_shp.zip
  format: null
  id: resource_0a5e45b5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20130326MMR_ToeKan_20170831_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mmr_unosat_damageassessmentcheinkhar_20170919
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-09-19'
temporal_resolution: null
title: Damage assessment in the Chein Khar Li (Ku Lar) village, Rakhine state, Myanmar
version: null
vulnerability: null
---
