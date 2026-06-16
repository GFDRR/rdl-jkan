---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-around-the-chemical-factory-samut-prakan-province-thailand
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-around-the-chemical-factory-samut-prakan-province-thailand
dataset_id: rdls_el-tha_unosat_damageassessmentaroundche_20210716
description: 'UNOSAT code: AC20210705THA This map illustrates the damage assessment
  after the blast of the 5th July 2021 in Bang Phli Yai sub-district, Bang Phli district,
  Samut Prakan province, Thailand. UNITAR - UNOSAT identified 328 potentially damaged
  structures of which 13 are destroyed and 315 are severely or moderately damaged.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-around-the-chemical-factory-samut-prakan-province-thailand]'
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
    description: Building stock in Bang Phli Yai sub-district assessed for damage
      from the chemical factory blast
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
  description: UNOSAT analysts reviewed and compared satellite imagery before and
    after the 5 July 2021 chemical factory blast in Samut Prakan Province, Thailand,
    to identify and classify structural damage. Building footprints were extracted
    and damage severity was assessed through visual interpretation of satellite imagery,
    resulting in a preliminary damage inventory of 328 structures classified by damage
    level.
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
- href: https://data.humdata.org/dataset/damage-assessment-around-the-chemical-factory-samut-prakan-province-thailand
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the 5 July 2021 chemical factory
      blast in Samut Prakan Province
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
  description: Damage assessment around the chemical factory, Samut Prakan Province,
    Thailand (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/TH/AC20210705THA/AC20210705THA_GDB.zip
  format: Geodatabase
  id: resource_691363ee
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AC20210705THA_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment around the chemical factory, Samut Prakan Province,
    Thailand (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/TH/AC20210705THA/AC20210705THA_SHP.zip
  format: null
  id: resource_27a6d029
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: AC20210705THA_SHP.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-tha_unosat_damageassessmentaroundche_20210716
spatial:
  bbox: null
  centroid: null
  countries:
  - THA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-07-16'
temporal_resolution: null
title: Damage assessment around the chemical factory, Samut Prakan Province, Thailand
version: null
vulnerability: null
---
