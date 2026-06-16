---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-baiji-salah-ad-din-governorate-iraq-february-20-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-baiji-salah-ad-din-governorate-iraq-february-20-2015
dataset_id: rdls_el-irq_unosat_geodatadamageassessmentba_20150220
description: 'This map illustrates satellite-detected damage and destruction in a
  portion of the city of Baiji, Salah ad Din governorate, Iraq. Using satellite imagery
  acquired 28 December 2014 and 06 April 2014, UNITAR / UNOSAT identified a total
  of 174 affected structures within the area of this map. Approximately 72 of these
  were destroyed, 57 severely damaged, and 45 moderately damaged. The city-wide analysis
  of Baiji revealed a total of 206 affected structures, of which 81 were destroyed,
  68 severely damaged, and 57 moderately damaged. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR /
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-baiji-salah-ad-din-governorate-iraq-february-20-2015]'
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
    description: Building stock in Baiji classified by damage severity (destroyed,
      severely damaged, moderately damaged)
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 28 December
    2014 and 6 April 2014 over Baiji, Iraq to detect structural damage through visual
    interpretation of notable changes between images. Building damage was classified
    into three severity categories (destroyed, severely damaged, moderately damaged)
    and georeferenced as point or polygon features.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-baiji-salah-ad-din-governorate-iraq-february-20-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Baiji
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
  description: Geodata of Damage Assessment of Baiji, Salah ad Din Governorate, Iraq
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Baiji_Shp.zip
  format: null
  id: resource_b83f60e2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Baiji_Shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Baiji, Salah ad Din Governorate, Iraq
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Baiji.gdb.zip
  format: null
  id: resource_3ccfcbe3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Baiji.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-irq_unosat_geodatadamageassessmentba_20150220
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-02-20'
temporal_resolution: null
title: Geodata of Damage Assessment of Baiji, Salah ad Din Governorate, Iraq
version: null
vulnerability: null
---
