---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-central-west-cuernavaca-city-municipality-of-cuernavaca-state-of-morelos
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-central-west-cuernavaca-city-municipality-of-cuernavaca-state-of-morelos
dataset_id: rdls_hl-mex_unosat_damageassessmentcentralwe_20170927
description: 'This map illustrates satellite-detected, potentially damaged structures
  in the central western part of the city of Cuernavaca and more specifically in the
  neighborhoods of Downtown, La Mina 2 and Altavista, Cuernavaca Municipality, Morelos
  State, Mexico. UNITAR-UNOSAT detected a general moderate damage with a few collapsed
  structures and identified 1,494 potentially affected structures. The analysis was
  performed using a post-event WorldView-3 satellite image acquired on 22 September
  2017 and a pre-event WorldView-2 satellite image acquired on 13 February 2017. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-central-west-cuernavaca-city-municipality-of-cuernavaca-state-of-morelos]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts performed change detection analysis by comparing pre-event
    (13 February 2017) and post-event (22 September 2017) WorldView satellite imagery
    of central Cuernavaca to identify potentially damaged structures. The analysis
    identified 1,494 affected structures with moderate damage and some collapsed buildings
    in three neighborhoods, producing vector geodatabase and shapefile outputs with
    damage classifications and building footprint areas.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-central-west-cuernavaca-city-municipality-of-cuernavaca-state-of-morelos
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake detected via satellite imagery
      comparison; 1,494 potentially affected structures identified
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
  description: Mexico - Damage Assessment in Central West Cuernavaca City, Municipality
    of Cuernavaca, State of Morelos (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_12f70c3b
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
  description: Mexico - Damage Assessment in Central West Cuernavaca City, Municipality
    of Cuernavaca, State of Morelos (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_56d505bd
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
slug: rdls_hl-mex_unosat_damageassessmentcentralwe_20170927
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
  start: '2017-09-27'
temporal_resolution: null
title: Mexico - Damage Assessment in Central West Cuernavaca City, Municipality of
  Cuernavaca, State of Morelos
version: null
vulnerability: null
---
