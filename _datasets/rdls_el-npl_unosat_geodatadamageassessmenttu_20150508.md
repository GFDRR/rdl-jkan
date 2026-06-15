---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tuhure-pasal-area-western-region-nepal-may-08-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tuhure-pasal-area-western-region-nepal-may-08-2015
dataset_id: rdls_el-npl_unosat_geodatadamageassessmenttu_20150508
description: 'This map illustrates satellite-detected damage and destruction in the
  Tuhure Pasal area of Nepal. Located roughly 27 to 31 kilometers southwest of the
  25 April 2015 earthquake epicenter, the Tuhure Pasal area was impacted by this event.
  Using satellite imagery acquired 03 May 2015 UNITAR / UNOSAT identified a total
  of 86 affected structures in the Tuhure Pasal area. Approximately 32 of these were
  destroyed, 21 severely damaged, and 33 moderately damaged. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR / UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tuhure-pasal-area-western-region-nepal-may-08-2015]'
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
    description: Building stock in Tuhure Pasal area classified by damage severity
      from earthquake
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery acquired before and after
    the 25 April 2015 earthquake, with post-event imagery from 03 May 2015, to identify
    and classify structural damage in the Tuhure Pasal area located 27-31 km southwest
    of the epicenter. Building damage was categorized into three severity classes
    (destroyed, severely damaged, moderately damaged) based on visual interpretation
    of satellite-detected changes.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-tuhure-pasal-area-western-region-nepal-may-08-2015
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
  description: Geodata of Damage Assessment of Tuhure Pasal Area, Western Region,
    Nepal (Shapefile)
  download_url: https://cern.ch/unosat-maps/NP/EQ20150425NPL/EQ20150425NPL_shp.zip
  format: null
  id: resource_6f5caca0
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
  description: Geodata of Damage Assessment of Tuhure Pasal Area, Western Region,
    Nepal (Shapefile)
  download_url: https://cern.ch/unosat-maps/NP/EQ20150425NPL/EQ20150425NPL_gdb.zip
  format: null
  id: resource_4b9ece62
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
slug: rdls_el-npl_unosat_geodatadamageassessmenttu_20150508
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
  start: '2015-05-08'
temporal_resolution: null
title: Geodata of Damage Assessment of Tuhure Pasal Area, Western Region, Nepal
version: null
vulnerability: null
---
