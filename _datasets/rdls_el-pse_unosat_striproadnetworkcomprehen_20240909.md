---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-august-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-august-2024
dataset_id: rdls_el-pse_unosat_striproadnetworkcomprehen_20240909
description: 'UNOSAT code: CE20231007PSE This map illustrates a satellite imagery-based
  comprehensive damage assessment to detect damage and affected roads across the Gaza
  Strip, Occupied Palestinian Territory, based on an image collected on 18 August
  2024. According to satellite imagery analysis, UNOSAT identified approximately 1,190km
  of destroyed roads, 415km of severely affected roads and 1,440km of moderately affected
  roads. From these statistics, it has been calculated that approximately 68% of the
  total road network has been damaged (including destroyed and affected roads), across
  the Gaza Strip. This is a preliminary analysis and has not yet been validated in
  the field.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-august-2024]'
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
  description: UNOSAT analysts performed multi-temporal satellite imagery analysis
    comparing images collected on 18 August 2024 against baseline imagery to identify
    and classify road damage into three categories (destroyed, severely affected,
    moderately affected). Damage extents were quantified in kilometers and aggregated
    to calculate total road network damage percentage across the Gaza Strip.
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
- href: https://data.humdata.org/dataset/unosat-gaza-strip-road-network-comprehensive-damage-assessment-august-2024
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
    - August 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3957/UNOSAT_UNHABITAT_RoadDamageAssessment_GDB_18082024.zip
  format: Geodatabase
  id: resource_691fee7a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_UNHABITAT_RoadDamageAssessment_GDB_18082024.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_striproadnetworkcomprehen_20240909
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
  start: '2024-09-09'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Strip Road Network Comprehensive Damage Assessment
  - August 2024
version: null
vulnerability: null
---
