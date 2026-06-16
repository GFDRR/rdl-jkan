---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-along-the-debed-river-in-tashir-stepanavan-tumanian-municipalites-lori-p
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/damage-assessment-along-the-debed-river-in-tashir-stepanavan-tumanian-municipalites-lori-p
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-along-the-debed-river-in-tashir-stepanavan-tumanian-municipalites-lori-p
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-along-the-debed-river-in-tashir-stepanavan-tumanian-municipalites-lori-p
dataset_id: rdls_el-arm_unosat_damageassessmentalongdebe_20240605
description: "UNOSAT code: FL20240528ARM, GDACS ID: 1102647 This map illustrates satellite\
  \ based structure damage assessment along the Debed river in Tashir, Stepanavan\
  \ and Tumanian Municipalities, Lori Province as observed from a SPOT 6 imagery acquired\
  \ on the 03 June 2024 at 14:35 local time & a Pl\xE9iades imagery acquired on the\
  \ 29 May 2024 at 11:39 local time. UNOSAT observed 124 potentially affected buildings,\
  \ 18 potentially affected bridges, 29 potentially affected road segments and 9 potentially\
  \ affected railway segments. Based on Worldpop population data and within the analysed\
  \ area, about 7,500 people live within 200m from the Debed river. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/damage-assessment-along-the-debed-river-in-tashir-stepanavan-tumanian-municipalites-lori-p]"
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
    description: Building stock affected by flooding along the Debed river, classified
      by damage status
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
- asset_type:
    description: Road and railway segments affected by flooding
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population exposed to flooding based on WorldPop data within the
      analysed area
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_3
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts compared multi-temporal satellite imagery (SPOT 6\
    \ from 03 June 2024 and Pl\xE9iades from 29 May 2024) to detect structural damage\
    \ along the Debed river. Damage assessments were classified by confidence level\
    \ and cross-referenced with WorldPop population data to estimate affected populations.\
    \ The resulting geodatabase contains 124 damaged buildings, 18 affected bridges,\
    \ 29 road segments, and 9 railway segments with spatial geometry and damage classification\
    \ attributes."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-along-the-debed-river-in-tashir-stepanavan-tumanian-municipalites-lori-p
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding observed via satellite
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to bridges and road/railway segments from fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by flooding based on spatial overlap with damaged
      structures
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Damage assessment along the Debed river in Tashir, Stepanavan & Tumanian
    Municipalites, Lori Province, Armenia as of 03 June 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3869/FL20240528ARM_gdb.zip
  format: Geodatabase
  id: resource_27d4adce
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240528ARM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment along the Debed river in Tashir, Stepanavan & Tumanian
    Municipalites, Lori Province, Armenia as of 03 June 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3869/FL20240528ARM_SHP.zip
  format: null
  id: resource_267c8676
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240528ARM_SHP.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-arm_unosat_damageassessmentalongdebe_20240605
spatial:
  bbox: null
  centroid: null
  countries:
  - ARM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-06-05'
temporal_resolution: null
title: Damage assessment along the Debed river in Tashir, Stepanavan & Tumanian Municipalites,
  Lori Province, Armenia as of 03 June 2024
version: null
vulnerability: null
---
