---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-bang-phli-district-samut-prakan-province-t
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-bang-phli-district-samut-prakan-province-t
dataset_id: rdls_el-tha_unosat_preliminaryderiveddamagea_20210709
description: 'UNOSAT code: AC20210705THA Status: Damaged structures observed Action:
  Completed Analysis: United Nations Satellite Centre (UNOSAT) Destroyed structures
  observed nearby the blast epicenter as of 7 July 2021; Widespread damage and damaged
  roofs observed within 1 km radius zone from the blast epicenter as of 7 & 9 July
  2021; No damaged roofs observed beyond 2 km radius from the blast epicenter as of
  7 & 9 July 2021.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-bang-phli-district-samut-prakan-province-t]'
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
    description: Building structures assessed for damage from blast event in Bang
      Phli District
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
  description: UNOSAT analysts conducted post-event satellite image analysis comparing
    multiple satellite images acquired on 7 and 9 July 2021 to identify and map damaged
    building structures within defined radius zones (0-1 km, 1-2 km) from the blast
    epicenter in Bang Phli District. Damage observations were classified by confidence
    level and validated through visual interpretation of structural changes.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-damage-assessment-bang-phli-district-samut-prakan-province-t
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from blast event observed via satellite imagery
      within 2 km radius
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
  description: Preliminary satellite-derived damage assessment, Bang Phli District,
    Samut Prakan Province, Thailand (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/TH/AC20210705THA/AC20210705THA_GDB.zip
  format: Geodatabase
  id: resource_3a389e1a
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
  description: Preliminary satellite-derived damage assessment, Bang Phli District,
    Samut Prakan Province, Thailand (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/TH/AC20210705THA/AC20210705THA_SHP.zip
  format: null
  id: resource_bc691d7a
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
slug: rdls_el-tha_unosat_preliminaryderiveddamagea_20210709
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
  start: '2021-07-09'
temporal_resolution: null
title: Preliminary satellite-derived damage assessment, Bang Phli District, Samut
  Prakan Province, Thailand
version: null
vulnerability: null
---
