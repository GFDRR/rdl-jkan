---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ancient-city-of-palmyra-syria-april-06-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ancient-city-of-palmyra-syria-april-06-2016
dataset_id: rdls_el-syr_unosat_geodatadamageassessmentan_20160406
description: 'This map illustrates the location of damaged buildings and cultural
  heritage locations in the Ancient City of Palmyra, Syrian Arab Republic as determined
  by satellite imagery analysis. Using satellite imagery acquired 30 March 2016, 18
  October 2015, and 26 June 2015 UNITAR-UNOSAT identified a total of 37 damaged structures
  within the Ancient City of Palmyra, of which 14 are destroyed, 8 are severely damaged,
  and 15 are moderately damaged. The majority of these damaged structures are in the
  vicinity of the Valley of the Tombs and the Necropolis, west and southwest of Palmyra.
  Additionally, satellite imagery analysis identified a total of 59 craters in the
  same area, an indicator of the level of fighting in the area. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ancient-city-of-palmyra-syria-april-06-2016]'
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
    description: Cultural heritage and residential building stock in the Ancient City
      of Palmyra identified through satellite imagery
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
  description: UNOSAT analysts compared multi-temporal satellite imagery acquired
    on 26 June 2015, 18 October 2015, and 30 March 2016 to detect structural changes
    and classify damage severity in the Ancient City of Palmyra. Building damage was
    categorized into three classes (destroyed, severely damaged, moderately damaged)
    based on visual interpretation of satellite-derived changes, resulting in a spatial
    inventory of 37 damaged structures with damage classification.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-for-ancient-city-of-palmyra-syria-april-06-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Palmyra
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
  description: Geodata of Damage Assessment for Ancient City of Palmyra, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Palmyra_Tadmur_20160330_shp.zip
  format: null
  id: resource_24750c65
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Palmyra_Tadmur_20160330_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment for Ancient City of Palmyra, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Palmyra_Tadmur_20160330.gdb.zip
  format: null
  id: resource_2bc91113
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Palmyra_Tadmur_20160330.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_geodatadamageassessmentan_20160406
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-04-06'
temporal_resolution: null
title: Geodata of Damage Assessment for Ancient City of Palmyra, Syria
version: null
vulnerability: null
---
