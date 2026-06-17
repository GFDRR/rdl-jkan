---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-koeeke-hasan-town-and-surroundings-kermanshah-iran-2736
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-koeeke-hasan-town-and-surroundings-kermanshah-iran-2736
dataset_id: rdls_hel-irnirq_unosat_damageassessmentkoeekehas_20171124
description: 'This map illustrates satellite-detected damaged and potentially damaged
  buildings in the town of Koeeke Hasan, Iran following the M 7.3 earthquake that
  struck the area on the 12 November 2017. The analysis was carried out comparing
  a post-event Pleiades image acquired on the 16 November 2017 with a pre-event WorldView3
  image of 24 July 2017. The results indicate intense damage across the whole town,
  particularly in Koeeke Hasan, Koeeke Aziz and Koeeke Mahmod. A total of 1174 structures
  have been identified as damaged or collapesed across the area extent represented
  here. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/damage-assessment-of-koeeke-hasan-town-and-surroundings-kermanshah-iran-2736]'
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
    description: Building stock in Koeeke Hasan town and surroundings identified through
      satellite imagery
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
  description: UNOSAT analysts compared pre-event and post-event satellite imagery
    to detect structural changes and identify damaged or collapsed buildings in Koeeke
    Hasan town following the M 7.3 earthquake. Building damage was mapped and counted
    across the study area, producing a spatial inventory of direct earthquake impacts
    on the built environment.
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
- href: https://data.humdata.org/dataset/damage-assessment-of-koeeke-hasan-town-and-surroundings-kermanshah-iran-2736
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from earthquake ground motion: 1174 structures
      identified as damaged or collapsed'
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
  description: Damage Assessment of Koeeke Hasan Town and Surroundings, Kermanshah,
    Iran (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/EQ20171112IRQ/EQ20171112IRQ_gdb.zip
  format: Geodatabase
  id: resource_0ea2c686
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20171112IRQ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment of Koeeke Hasan Town and Surroundings, Kermanshah,
    Iran (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/EQ20171112IRQ/EQ20171112IRQ_shp.zip
  format: null
  id: resource_0bc063c0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20171112IRQ_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-irnirq_unosat_damageassessmentkoeekehas_20171124
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  - IRN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-24'
temporal_resolution: null
title: Damage Assessment of Koeeke Hasan Town and Surroundings, Kermanshah, Iran
version: null
vulnerability: null
---
