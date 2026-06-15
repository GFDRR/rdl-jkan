---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-jojutla-town-jojutla-municipality-state-of-morelos-mexico-2698
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-jojutla-town-jojutla-municipality-state-of-morelos-mexico-2698
dataset_id: rdls_lss-mex_unosat_damageassessmentjojutlato_20171005
description: 'This map illustrates satellite-detected, potentially damaged structures
  in the town of Jojutla, Jojutla Municipality, Morelos State, Mexico. The analyzed
  area is located approximately 82 km west of the main shock epicenter of the 19 September
  2017 M7.1 earthquake. UNITAR-UNOSAT identified 1,102 potentially damaged structures.
  The analysis was performed using a post-event Pleiades satellite image acquired
  on 03 October 2017 and Bing as pre-event image. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR -
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-jojutla-town-jojutla-municipality-state-of-morelos-mexico-2698]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared post-event Pleiades satellite imagery (03
    October 2017) with pre-event Bing imagery to detect structural changes and identify
    potentially damaged buildings in Jojutla town following the 19 September 2017
    M7.1 earthquake. The analysis identified 1,102 potentially damaged structures
    through visual interpretation of satellite imagery, representing a preliminary
    assessment not yet validated in the field.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-jojutla-town-jojutla-municipality-state-of-morelos-mexico-2698
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 19 September 2017 M7.1 earthquake
      detected via satellite imagery
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
  description: Damage Assessment in Jojutla town, Jojutla Municipality, State of Morelos,
    Mexico (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_74e2f32c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Jojutla town, Jojutla Municipality, State of Morelos,
    Mexico (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_e37d5b47
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mex_unosat_damageassessmentjojutlato_20171005
spatial:
  bbox: null
  centroid: null
  countries:
  - MEX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-10-05'
temporal_resolution: null
title: Damage Assessment in Jojutla town, Jojutla Municipality, State of Morelos,
  Mexico
version: null
vulnerability: null
---
