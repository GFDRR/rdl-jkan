---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-1km-stretch-of-land-from-the-armistice-d
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-1km-stretch-of-land-from-the-armistice-d
dataset_id: rdls_el-pse_unosat_stripcomprehensivedamagea_20240411
description: 'UNOSAT code: CE20231007PSE This map illustrates a satellite-imagery
  based comprehensive damage assessment (CDA) to detect damage and destruction within
  a stretch of land 1 km from the Armistice Demarcation Line in the Gaza Strip, Occupied
  Palestinian Territory. This analysis includes a CDA from several dates, including
  15 October 2023, 7 November 2023, 26 November 2023, 7 January 2024 and 29 February
  2024. Statistical analysis shows the rapid increase in damaged and destroyed buildings
  within the zone, from 15% to 90% between October 2023 and February 2024. Satellite-derived
  analysis undertaken on 29 February 2024 on 4042 buildings within the zone, shows
  3033 destroyed, 593 damaged (severe or moderately) and 416 with no visible damage..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-1km-stretch-of-land-from-the-armistice-d]'
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
    description: Building stock in the 1 km zone from the Armistice Demarcation Line
      classified by damage state
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
  description: UNOSAT analysts conducted multi-temporal satellite imagery analysis
    comparing images from October 2023 through February 2024 to detect changes in
    building damage states within a 1 km buffer zone from the Armistice Demarcation
    Line. Damage classification was performed through visual interpretation of satellite
    imagery, with statistical analysis quantifying the progression of damaged and
    destroyed buildings from 15% to 90% over the assessment period.
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
- href: https://data.humdata.org/dataset/unosat-gaza-strip-comprehensive-damage-assessment-1km-stretch-of-land-from-the-armistice-d
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage and destruction from conflict-related impacts
      assessed via satellite imagery
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
  description: Palestine - UNOSAT Gaza Strip Comprehensive Damage Assessment 1km Stretch
    of Land from the Armistice Demarcation Line - April 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3820/CE20231007PSE_UNOSAT_1kmArmisticeDemarcationLine_09042024_GDB.zip
  format: Geodatabase
  id: resource_0c8b0ce1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20231007PSE_UNOSAT_1kmArmisticeDemarcationLine_09042024_GDB.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_stripcomprehensivedamagea_20240411
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
  start: '2024-04-11'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Strip Comprehensive Damage Assessment 1km Stretch of
  Land from the Armistice Demarcation Line - April 2024
version: null
vulnerability: null
---
