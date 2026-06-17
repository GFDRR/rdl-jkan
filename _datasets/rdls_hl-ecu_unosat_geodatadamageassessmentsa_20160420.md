---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-salinas-and-la-libertad-areas-santa-elena-pro-april-20-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-salinas-and-la-libertad-areas-santa-elena-pro-april-20-2016
dataset_id: rdls_hl-ecu_unosat_geodatadamageassessmentsa_20160420
description: "This map illustrates satellite-detected potential damaged structures\
  \ in Salinas/La Libertad areas in Santa Elena Province, Ecuador, located at approximately\
  \ 300 km south of the 16 April 2016 Muisne earthquake mainshock epicenter. Using\
  \ a Pl\xE9iades satellite image acquired the 18 April 2016 and a WorldView-2 image\
  \ acquired the 26 December 2015, UNITAR - UNOSAT identified 33 potentially damaged\
  \ structures of which 1 is destroyed, 5 severely damaged, and 27 moderately damaged.\
  \ This is a preliminary analysis and not yet been validated in the field. Please\
  \ send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-salinas-and-la-libertad-areas-santa-elena-pro-april-20-2016]"
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
license: CC-BY-4.0
lineage:
  description: "UNOSAT analysts compared pre- and post-earthquake satellite imagery\
    \ (WorldView-2 baseline from 26 December 2015 and Pl\xE9iades post-event from\
    \ 18 April 2016) to identify structural changes and classify building damage severity\
    \ in the Salinas and La Libertad areas, 300 km from the Muisne earthquake epicenter.\
    \ The resulting damage assessment provides observed post-event impact data for\
    \ earthquake risk characterization in Santa Elena Province."
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-salinas-and-la-libertad-areas-santa-elena-pro-april-20-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Satellite-detected building damage assessment: 33 structures identified
      (1 destroyed, 5 severely damaged, 27 moderately damaged) from the 16 April 2016
      earthquake'
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
  description: Geodata of Damage Assessment of Salinas and La Libertad Areas, Santa
    Elena Province, Ecuador (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU_shp.zip
  format: null
  id: resource_92d99b5e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20160417ECU_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Salinas and La Libertad Areas, Santa
    Elena Province, Ecuador (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU.gdb.zip
  format: null
  id: resource_1f0e8d28
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20160417ECU.gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-ecu_unosat_geodatadamageassessmentsa_20160420
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-04-20'
temporal_resolution: null
title: Geodata of Damage Assessment of Salinas and La Libertad Areas, Santa Elena
  Province, Ecuador
version: null
vulnerability: null
---
