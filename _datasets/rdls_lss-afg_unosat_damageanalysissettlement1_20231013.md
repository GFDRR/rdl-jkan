---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-analysis-by-settlement-of-the-11th-october-2023-hirat-earthquake
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-analysis-by-settlement-of-the-11th-october-2023-hirat-earthquake
dataset_id: rdls_lss-afg_unosat_damageanalysissettlement1_20231013
description: "UNOSAT code EQ20231008AFG, GDACS Id: 1394952 This map illustrates the\
  \ level of damage induced by the 11 October earthquake (M6.3) in settlements North\
  \ and North-West Herat as observed from very high-resolution images WorldView-3\
  \ and WorldView-1 acquired on 11 October 2023. UNOSAT has analysed an area of a\
  \ total of 3,150km\xB2 and detected 123 affected settlements, amongst which 92 are\
  \ moderately affected, 10 severely affected and 21 are almost destroyed. In addition,\
  \ 25 settlements have no visible damages. This is a preliminary analysis and has\
  \ not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-analysis-by-settlement-of-the-11th-october-2023-hirat-earthquake]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts compared very high-resolution satellite imagery acquired\
    \ on 11 October 2023 with pre-event baseline imagery to detect and classify building\
    \ damage across 3,150 km\xB2 in Herat Province. Settlements were categorized into\
    \ damage classes (no visible damage, moderately affected, severely affected, almost\
    \ destroyed) through visual interpretation of structural changes observed in the\
    \ imagery."
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
- href: https://data.humdata.org/dataset/damage-analysis-by-settlement-of-the-11th-october-2023-hirat-earthquake
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from M6.3 earthquake assessed by satellite
      imagery in Herat settlements
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
  description: Afghanistan - Damage analysis by settlement of the 11th October 2023
    Hirat earthquake (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3688/EQ20231008AFG_gdb.zip
  format: Geodatabase
  id: resource_23b2518f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Afghanistan - Damage analysis by settlement of the 11th October 2023
    Hirat earthquake (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3688/EQ20231008AFG_SHP.zip
  format: null
  id: resource_11eac265
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_unosat_damageanalysissettlement1_20231013
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-13'
temporal_resolution: null
title: Afghanistan - Damage analysis by settlement of the 11th October 2023 Hirat
  earthquake
version: null
vulnerability: null
---
