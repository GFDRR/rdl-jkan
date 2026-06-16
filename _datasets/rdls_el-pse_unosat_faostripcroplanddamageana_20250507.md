---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-analysis-september-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Food and Agriculture Organization (FAO)
    url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-analysis-september-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-analysis-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-analysis-september-2024
dataset_id: rdls_el-pse_unosat_faostripcroplanddamageana_20250507
description: 'UNOSAT code: CE20231007PSE This map illustrates a satellite imagerybased
  comprehensive assessment of damage and destruction to structures within the area
  of interest in the Gaza Strip, Occupied Palestinian Territory, based on images collected
  on 4 April 2025 when compared to images collected on 1 May 2023, 10 May 2023, 18
  September 2023, 15 October 2023, 7 November 2023, 26 November 2023, 6-7 January
  2024, 29 February 2024, 31 March - 1 April 2024, 3 May 2024, 6 July 2024, 3-6 September
  2024, 1 December 2024, and 25 February 2025. According to satellite imagery analysis,
  UNOSAT identified 70,436 destroyed structures, 18,588 severely damaged structures,
  51,962 moderately damaged structures, and 33,500 possibly damaged structures for
  a total of 174,468 structures. These correspond to around 70% of the total structures
  in the Gaza Strip and a total of 258,201 estimated damaged housing units. The governorates
  of Rafah and North Gaza have experienced the highest rise in damage compared to
  the 25 February 2025 analysis, with around 636 new structures damaged in Rafah and
  around 218 in North Gaza. Within Rafah, Rafah City municipality had the highest
  number of newly damaged structures, totalling 609. This is a preliminary analysis
  and has not yet been validated in the field.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-analysis-september-2024]'
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
    description: Cropland extent and distribution in Gaza Strip mapped from satellite
      imagery
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: Multi-temporal satellite imagery collected between May 2023 and February
    2025 was analyzed through visual interpretation and change detection to identify
    damage to cropland and structures. Analysts compared sequential image pairs to
    determine notable changes in agricultural land cover and structural integrity,
    producing a geodatabase of damage extents and classifications for the Gaza Strip.
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
    name: Food and Agriculture Organization (FAO)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-analysis-september-2024
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct damage to cropland assessed through satellite imagery change
      detection
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
          quantity_kind: area
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
  description: Palestine - UNOSAT FAO Gaza Strip Cropland Damage Analysis - September
    2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4130/UNOSAT_CE20231007PSE_Gaza_Governorate_DA_20231015_GDB_v2.zip
  format: Geodatabase
  id: resource_6e881aac
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20231007PSE_Gaza_Governorate_DA_20231015_GDB_v2.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_faostripcroplanddamageana_20250507
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-05-07'
temporal_resolution: null
title: Palestine - UNOSAT FAO Gaza Strip Cropland Damage Analysis - September 2024
version: null
vulnerability: null
---
