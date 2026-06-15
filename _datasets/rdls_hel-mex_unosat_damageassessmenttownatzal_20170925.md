---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-town-of-atzala-municipality-of-atzala-state-of-puebla-mexico
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-town-of-atzala-municipality-of-atzala-state-of-puebla-mexico
dataset_id: rdls_hel-mex_unosat_damageassessmenttownatzal_20170925
description: 'This map illustrates satellite-detected, potentially damaged structures
  in the town of Atzala, Atzala Municipality, Puebla State, Mexico. The analysed area
  is located approximately 7 km west of the mainshock epicentre of the 19 September
  M 7.1 earthquake. UNITAR-UNOSAT identified 91 potentially damaged structures of
  which 78 are within the town extent. Taking in account the total 559 pre-event structures
  in Atzala town, 14% of the structures are likely to be damaged. These analyses was
  performed using a post-event Pleiades satellite image acquired on 22 September 2017
  and a pre-event WorldView-2 satellite image acquired on 11 April 2017. This is a
  preliminary analysis and has not yet been validated in the field. Please send ground
  feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-the-town-of-atzala-municipality-of-atzala-state-of-puebla-mexico]'
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
    description: Building stock in Atzala town identified from pre-event satellite
      imagery (559 structures)
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
hazard:
  event_sets_by_hazard_type:
    earthquake:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre-event and post-event satellite imagery
    (Pleiades and WorldView) acquired before and after the 19 September 2017 M7.1
    earthquake to identify structural changes and damage. Visual interpretation of
    satellite-detected damage was performed on the town of Atzala located 7 km west
    of the mainshock epicentre, resulting in a damage assessment dataset with 91 potentially
    damaged structures mapped as vector geometries.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-the-town-of-atzala-municipality-of-atzala-state-of-puebla-mexico
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected potentially damaged structures from the 19 September
      2017 earthquake (91 structures identified, 78 within town extent)
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
  description: Damage Assessment in the town of Atzala, Municipality of Atzala, State
    of Puebla, Mexico (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_80dcaece
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
  description: Damage Assessment in the town of Atzala, Municipality of Atzala, State
    of Puebla, Mexico (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_f20962b5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20170919MEX_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mex_unosat_damageassessmenttownatzal_20170925
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
  start: '2017-09-25'
temporal_resolution: null
title: Damage Assessment in the town of Atzala, Municipality of Atzala, State of Puebla,
  Mexico
version: null
vulnerability: null
---
