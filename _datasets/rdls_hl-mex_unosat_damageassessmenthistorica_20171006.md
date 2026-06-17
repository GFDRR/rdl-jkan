---
attributions:
- entity:
    affiliation: null
    email: null
    name: Institute of Geography of the National Autonomous University of Mexico (IGG-UNAM)
    url: https://data.humdata.org/dataset/damage-assessment-in-the-historical-center-of-puebla-state-of-puebla-2700
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-historical-center-of-puebla-state-of-puebla-2700
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-historical-center-of-puebla-state-of-puebla-2700
dataset_id: rdls_hl-mex_unosat_damageassessmenthistorica_20171006
description: 'This map illustrates satellite-detected, potentially damaged structures
  in the Historical Center of Puebla located in Heroica Puebla de Zaragoza Municipality,
  Puebla State, Mexico. The analyzed area is located approximately 90 km north of
  the epicentral zone of the 19 September 2017 M7.1 earthquake. the Institute of Geography
  of the National Autonomous University of Mexico (IGG-UNAM) identified 336 potentially
  damaged structures from which 256 are within Historical Center. The analysis was
  performed using a post-event WorldView-3 satellite image acquired on 23 September
  2017 and a pre-event WorldView-2 satellite image acquired on 28 July 2017. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-the-historical-center-of-puebla-state-of-puebla-2700]'
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
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: Post-event damage assessment conducted by comparing pre-event and post-event
    (23 September 2017) WorldView-3 satellite imagery of the Historical Center of
    Puebla. UNOSAT analysts identified structural changes indicative of earthquake
    damage, with results validated by IGG-UNAM. The dataset contains 336 potentially
    damaged building structures mapped as vector geometries with area measurements.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Institute of Geography of the National Autonomous University of Mexico (IGG-UNAM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-the-historical-center-of-puebla-state-of-puebla-2700
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected potentially damaged structures (336 total, 256
      in Historical Center) from the 19 September 2017 M7.1 earthquake
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Mexico - Damage Assessment in the Historical Center of Puebla, State
    of Puebla (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_53364f18
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
  description: Mexico - Damage Assessment in the Historical Center of Puebla, State
    of Puebla (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_bc740687
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mex_unosat_damageassessmenthistorica_20171006
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
  start: '2017-10-06'
temporal_resolution: null
title: Mexico - Damage Assessment in the Historical Center of Puebla, State of Puebla
version: null
vulnerability: null
---
