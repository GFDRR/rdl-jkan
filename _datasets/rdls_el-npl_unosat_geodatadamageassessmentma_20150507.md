---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-manbu-area-western-region-nepal-may-07-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-manbu-area-western-region-nepal-may-07-2015
dataset_id: rdls_el-npl_unosat_geodatadamageassessmentma_20150507
description: 'This map illustrates satellite-detected damage and destruction in the
  Manbu area of Nepal. Located roughly 10 to 25 kilometers east of the 25 April 2015
  earthquake epicenter, the Manbu area was significantly impacted by this event. Using
  satellite imagery acquired 03 May 2015 and 29 April 2015 UNITAR / UNOSAT identified
  a total of 1,524 affected structures in the Manbu area. Approximately 786 of these
  were destroyed, 375 severely damaged, and 363 moderately damaged. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR / UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-manbu-area-western-region-nepal-may-07-2015]'
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
    description: Building stock in Manbu area classified by damage state from satellite
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
  description: UNOSAT analysts compared satellite imagery acquired on 29 April 2015
    and 3 May 2015 (4-8 days post-earthquake) to detect structural damage in the Manbu
    area through visual interpretation of notable changes between images. Building
    damage was classified into three categories (destroyed, severely damaged, moderately
    damaged) and georeferenced as point or polygon features.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-manbu-area-western-region-nepal-may-07-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from 25 April 2015 earthquake assessed via
      satellite imagery
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
  description: Geodata of Damage Assessment of Manbu Area, Western Region, Nepal (Shapefile)
  download_url: https://cern.ch/unosat-maps/NP/EQ20150425NPL/EQ20150425NPL_shp.zip
  format: null
  id: resource_fab4d77f
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
  description: Geodata of Damage Assessment of Manbu Area, Western Region, Nepal (Shapefile)
  download_url: https://cern.ch/unosat-maps/NP/EQ20150425NPL/EQ20150425NPL_gdb.zip
  format: null
  id: resource_69ecc4c0
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
slug: rdls_el-npl_unosat_geodatadamageassessmentma_20150507
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
  start: '2015-05-07'
temporal_resolution: null
title: Geodata of Damage Assessment of Manbu Area, Western Region, Nepal
version: null
vulnerability: null
---
