---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-town-of-coatetelco-municipality-of-miacatlan-state-of-morelos-mexico
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-town-of-coatetelco-municipality-of-miacatlan-state-of-morelos-mexico
dataset_id: rdls_lss-mex_unosat_damageassessmenttowncoate_20170928
description: 'This map illustrates satellite-detected, potentially damaged structures
  in the town of Coatetelco, Miacatlan Municipality, Morelos State, Mexico. The analyzed
  area is located approximately 90 km northwest of the main shock epicenter of the
  19 September 2017 M7.1 earthquake. UNITAR-UNOSAT identified 500 potentially damaged
  structures. The analysis was performed using a post-event WorldView-3 satellite
  image acquired on 22 September 2017 and a pre-event WorldView-2 satellite image
  acquired on 17 January 2017. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-the-town-of-coatetelco-municipality-of-miacatlan-state-of-morelos-mexico]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre-event WorldView-2 satellite imagery (17
    January 2017) with post-event WorldView-3 imagery (22 September 2017) to detect
    structural changes and identify 500 potentially damaged buildings in Coatetelco.
    The analysis is preliminary and unvalidated field assessment based on satellite-detected
    damage signatures.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-the-town-of-coatetelco-municipality-of-miacatlan-state-of-morelos-mexico
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected potentially damaged structures from the 19 September
      2017 M7.1 earthquake
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
  description: Damage Assessment in the town of Coatetelco, Municipality of Miacatlan,
    State of Morelos, Mexico (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_30889b40
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
  description: Damage Assessment in the town of Coatetelco, Municipality of Miacatlan,
    State of Morelos, Mexico (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_561d9364
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
slug: rdls_lss-mex_unosat_damageassessmenttowncoate_20170928
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
  start: '2017-09-28'
temporal_resolution: null
title: Damage Assessment in the town of Coatetelco, Municipality of Miacatlan, State
  of Morelos, Mexico
version: null
vulnerability: null
---
