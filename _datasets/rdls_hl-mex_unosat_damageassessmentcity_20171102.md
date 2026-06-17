---
attributions:
- entity:
    affiliation: null
    email: null
    name: Faculty of Geography, Autonomous University of the State of Mexico (UAEMex)
    url: https://data.humdata.org/dataset/damage-assessment-in-mexico-city-mexico-2711
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-mexico-city-mexico-2711
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-mexico-city-mexico-2711
dataset_id: rdls_hl-mex_unosat_damageassessmentcity_20171102
description: 'This map illustrates satellite-detected, potentially damaged structures
  in some affected colonies located in Venustiano Carranza, Cuauhtemoc, Benito Juarez,
  Coyoacan and Iztapalapa Municipalities, Federal District, Mexico. The analysis was
  performed by Faculty of Geography of the Autonomous University of the State of Mexico
  (UAEMex) using as post-event satellite imagery : WorldView-2 acquired as of 20 and
  26 September 2017 and Pleiades acquired as of 22 September 2017. UAEMex identified
  201 potentially damaged structures within the limit of the analyzed colonies, surrounded
  by a blue line in this map: 24 are located in Magdelena Mixhuca colony, 22 in Aculco,
  21 in Atenor Sala and 20 in El Arenal. Please do not hesitate to send feedback to
  UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-mexico-city-mexico-2711]'
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
  - analysis_type: empirical
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
  description: Post-event satellite imagery (WorldView-2 and Pleiades) acquired 20-26
    September 2017 was analyzed by UAEMex using multi-temporal comparison to detect
    structural damage from the 19 September 2017 earthquake. Analysts identified 201
    potentially damaged structures across five municipalities in Mexico City, with
    results delivered as vector geodatabase and shapefile formats.
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
    name: Faculty of Geography, Autonomous University of the State of Mexico (UAEMex)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-mexico-city-mexico-2711
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 2017 Mexico City earthquake identified
      through satellite imagery analysis
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
  description: Damage Assessment in Mexico City, Mexico (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_gdb.zip
  format: Geodatabase
  id: resource_82d41f28
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
  description: Damage Assessment in Mexico City, Mexico (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MX/EQ20170919MEX/EQ20170919MEX_shp.zip
  format: null
  id: resource_b48fc03c
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
slug: rdls_hl-mex_unosat_damageassessmentcity_20171102
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
  start: '2017-11-02'
temporal_resolution: null
title: Damage Assessment in Mexico City, Mexico
version: null
vulnerability: null
---
