---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sankhu-kathmandu-valley-nepal-april-30-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sankhu-kathmandu-valley-nepal-april-30-2015
dataset_id: rdls_el-npl_unosat_geodatadamageassessmentsa_20150430
description: 'This map illustrates satellite-detected damage and destruction in the
  town of Sankhu, Kathmandu Valley, Nepal. Located northeast of Kathmandu city, Sankhu
  was significantly impacted by the 25 April 2015 earthquake in Nepal. Using satellite
  imagery acquired 27 April 2015 UNITAR / UNOSAT identified a total of 300 affected
  structures. Approximately 166 of these were destroyed, 97 severely damaged, and
  37 moderately damaged. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sankhu-kathmandu-valley-nepal-april-30-2015]'
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
    description: Building stock in Sankhu classified by damage state from satellite
      imagery
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
  description: UNOSAT analysts compared satellite imagery acquired on 27 April 2015
    (two days after the 25 April 2015 earthquake) with pre-event imagery to detect
    structural damage in Sankhu. Buildings were classified into three damage categories
    (destroyed, severely damaged, moderately damaged) based on visual interpretation
    of satellite-detected changes, resulting in a preliminary damage assessment of
    300 affected structures.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sankhu-kathmandu-valley-nepal-april-30-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 25 April 2015 Nepal earthquake assessed
      via satellite imagery
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
  description: Geodata of Damage Assessment of Sankhu, Kathmandu Valley, Nepal (Shapefile)
  download_url: https://cern.ch/unosat-maps/NP/EQ20150425NPL/EQ20150425NPL_shp.zip
  format: null
  id: resource_be1fd10b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20150425NPL_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Sankhu, Kathmandu Valley, Nepal (Shapefile)
  download_url: https://cern.ch/unosat-maps/NP/EQ20150425NPL/EQ20150425NPL_gdb.zip
  format: null
  id: resource_bd3726d4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20150425NPL_gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-npl_unosat_geodatadamageassessmentsa_20150430
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-04-30'
temporal_resolution: null
title: Geodata of Damage Assessment of Sankhu, Kathmandu Valley, Nepal
version: null
vulnerability: null
---
