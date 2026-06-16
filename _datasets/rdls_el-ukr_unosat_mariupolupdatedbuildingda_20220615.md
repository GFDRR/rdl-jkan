---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/mariupol-updated-building-damage-assessment-overview-map-livoberezhnyi-and-zhovtnevyi-dist
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mariupol-updated-building-damage-assessment-overview-map-livoberezhnyi-and-zhovtnevyi-dist
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mariupol-updated-building-damage-assessment-overview-map-livoberezhnyi-and-zhovtnevyi-dist
dataset_id: rdls_el-ukr_unosat_mariupolupdatedbuildingda_20220615
description: 'UNOSAT code: CE20220223UKR This map illustrates a satellite imagery
  based damage analysis within an area of interest (AOI) in the residential area of
  Mariupol City, Ukraine. Based on imagery collected on 7, 8, 12 May 2022 and 14 March
  2022, and 21 June 2021, analysts found that 5,647 structures sustained visible damage
  in the AOI. This represents approximately 32% of the structures. Out of these, 315
  are destroyed, 2,132 severely damaged, 3,002 moderately damaged and 194 possibly
  damaged. Compared to the 14 March 2022 analysis, 5% of previously affected buildings
  sustained additional damage, and the total damage has increased by 28%, with 4,910
  new damaged buildings. While no complete count of buildings for Mariupol is available,
  an open source dataset, which is visibly incomplete indicates at least 17,568 structures
  in the area. This analysis is based on structures visibly damaged as of 12, 8, 7
  May 2022 and 14 March 2022 as seen in marginally degraded satellite imagery. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mariupol-updated-building-damage-assessment-overview-map-livoberezhnyi-and-zhovtnevyi-dist]'
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
    description: Building stock in Mariupol residential districts classified by damage
      severity
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
  description: UNOSAT analysts compared satellite imagery acquired on 14 March 2022
    (baseline) with imagery from 7, 8, 12 May 2022 (post-event) to detect visible
    structural damage in residential areas of Mariupol. Buildings were classified
    into four damage categories (destroyed, severely damaged, moderately damaged,
    possibly damaged) based on visual interpretation of satellite imagery changes.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mariupol-updated-building-damage-assessment-overview-map-livoberezhnyi-and-zhovtnevyi-dist
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction in Mariupol
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
  description: Ukraine - Mariupol Updated Building Damage Assessment Overview Map
    - Livoberezhnyi and Zhovtnevyi Districts (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/UA/CE20220223UKR/UNOSAT_LivoberezhnyiDistrict_DamageAssessment_12May2022.gdb.zip
  format: Geodatabase
  id: resource_21f8f5ce
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_LivoberezhnyiDistrict_DamageAssessment_12May2022.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine - Mariupol Updated Building Damage Assessment Overview Map
    - Livoberezhnyi and Zhovtnevyi Districts (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/UA/CE20220223UKR/UNOSAT_LivoberezhnyiDistrict_DamageAssessment_12May2022_shp.zip
  format: null
  id: resource_6fab7ef3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_LivoberezhnyiDistrict_DamageAssessment_12May2022_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ukr_unosat_mariupolupdatedbuildingda_20220615
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-06-15'
temporal_resolution: null
title: Ukraine - Mariupol Updated Building Damage Assessment Overview Map - Livoberezhnyi
  and Zhovtnevyi Districts
version: null
vulnerability: null
---
