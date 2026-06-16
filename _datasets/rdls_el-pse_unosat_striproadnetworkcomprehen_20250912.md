---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-july-2025
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-july-2025
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-july-2025
dataset_id: rdls_el-pse_unosat_striproadnetworkcomprehen_20250912
description: 'UNOSAT code: CE20231007PSE This map illustrates a satellite-imagery
  based comprehensive damage assessment to detect damage and affected roads across
  the Gaza Strip, Occupied Palestinian Territory, based on an image collected on the
  08 July 2025. According to satellite imagery analysis, UNOSAT identified approximately
  1511km of destroyed roads, 484km of severely affected roads and 1484km of moderately
  affected main roads. From these statistics it has been calculated that approximately
  77% of the total road network has been damaged (including destroyed, affected roads
  and roads restricted by obstacles), across the Gaza Strip. This is a preliminary
  analysis and has not yet been validated in the field.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-july-2025]'
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
    description: Road network infrastructure classified by damage severity (destroyed,
      severely affected, moderately affected)
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts conducted satellite imagery analysis by comparing multi-temporal
    images collected on 8 July 2025 to detect notable changes in road infrastructure.
    Roads were classified into three damage categories (destroyed, severely affected,
    moderately affected) based on visual interpretation of satellite imagery, resulting
    in quantified damage statistics (1511 km destroyed, 484 km severely affected,
    1484 km moderately affected) representing 77% of the total road network.
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
- href: https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-july-2025
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to road infrastructure from conflict-related destruction
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
  description: Palestine - UNOSAT Gaza Strip Road Network Comprehensive Damage Assessment
    - July 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4201/CE20231007PSE_UNOSAT_GazaStrip_RoadCDA_20250708_GDB_v1.gdb.zip
  format: Geodatabase
  id: resource_f6a53c5f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20231007PSE_UNOSAT_GazaStrip_RoadCDA_20250708_GDB_v1.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_striproadnetworkcomprehen_20250912
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
  start: '2025-09-12'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Strip Road Network Comprehensive Damage Assessment
  - July 2025
version: null
vulnerability: null
---
