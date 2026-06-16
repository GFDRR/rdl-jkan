---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-riosucio-town-riosucio-municipality-choco-department-colombi
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-riosucio-town-riosucio-municipality-choco-department-colombi
dataset_id: rdls_el-col_unosat_buildingdamageassessmentr_20241121
description: "UNOSAT code: FL20241112COL, GDACS ID: 1102988 This map illustrates potentially\
  \ affected structures in Riosucio Municipality, Choc\u8D38 Department, Colombia\
  \ as observed from a Pleiades satellite image acquired on 20 November 2024 at 11:07\
  \ Local Time. Within the analysis extent, UNOSAT identified 60 potentially affected\
  \ structures amongst a total of 2,085 structures observed. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/building-damage-assessment-in-riosucio-town-riosucio-municipality-choco-department-colombi]"
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
    description: Building stock in Riosucio town with total inventory of 2,085 structures
      identified from satellite imagery
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
  description: UNOSAT analysts performed change detection analysis on Pleiades satellite
    imagery acquired on 20 November 2024 to identify structural damage in Riosucio
    Municipality following a flooding event. The analysis compared satellite images
    to detect notable changes in building structures, resulting in identification
    of 60 potentially affected structures out of 2,085 total structures in the analysis
    extent. This preliminary assessment has not been validated in the field.
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
- href: https://data.humdata.org/dataset/building-damage-assessment-in-riosucio-town-riosucio-municipality-choco-department-colombi
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from flooding event, with 60 potentially
      affected structures identified from satellite imagery as of 20 November 2024
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
  description: "Building Damage Assessment in Riosucio Town, Riosucio Municipality,\
    \ Choc\u8D38 Department, Colombia as of 20 November 2024 (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/4033/FL20241112COL_gdb.zip
  format: Geodatabase
  id: resource_fcfd0804
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241112COL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Building Damage Assessment in Riosucio Town, Riosucio Municipality,\
    \ Choc\u8D38 Department, Colombia as of 20 November 2024 (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/4033/FL20241112COL_SHP.zip
  format: null
  id: resource_b7555d4b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241112COL_SHP.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-col_unosat_buildingdamageassessmentr_20241121
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-11-21'
temporal_resolution: null
title: "Building Damage Assessment in Riosucio Town, Riosucio Municipality, Choc\u8D38\
  \ Department, Colombia as of 20 November 2024"
version: null
vulnerability: null
---
