---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/damaged-structures-and-related-density-map-in-sarpol-e-zahab-kermanshah-iran-2732
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damaged-structures-and-related-density-map-in-sarpol-e-zahab-kermanshah-iran-2732
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damaged-structures-and-related-density-map-in-sarpol-e-zahab-kermanshah-iran-2732
dataset_id: rdls_hl-irnirq_unosat_damagedstructuresrelatedd_20171120
description: 'This map illustrates potentially damaged structures/buildings and related
  density in Sarpol-e-Zahab, Kermanshah, Iran as detected by a Pleiades satellite
  image acquired on 16 November 2017. The UNITAR-UNOSAT analysis identified 683 damaged
  structures. Taking into account the pre-building footprints provided by Humanitarian
  OpenStreetMap (~9700 structures), this represents about 7 % of the total number
  of structures within Sarpol-e-Zahab. The damage density highlights that the neighbourhood
  of Maskane Mahar and the area around the Post Office are amongst the most affected
  zones. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/damaged-structures-and-related-density-map-in-sarpol-e-zahab-kermanshah-iran-2732]'
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
  description: UNOSAT analysts compared pre- and post-event Pleiades satellite imagery
    acquired on 16 November 2017 to detect structural damage in Sarpol-e-Zahab following
    the 12 November 2017 earthquake. Detected damage (683 structures) was mapped and
    density-analyzed relative to pre-event building footprints from Humanitarian OpenStreetMap
    to quantify impact extent and spatial distribution.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
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
- href: https://data.humdata.org/dataset/damaged-structures-and-related-density-map-in-sarpol-e-zahab-kermanshah-iran-2732
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake detected via satellite imagery
      analysis (683 damaged structures identified)
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
  description: Damaged structures and related density map in Sarpol-e-Zahab, Kermanshah,
    Iran (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/EQ20171112IRQ/EQ20171112IRQ_gdb.zip
  format: Geodatabase
  id: resource_4042adaf
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
  description: Damaged structures and related density map in Sarpol-e-Zahab, Kermanshah,
    Iran (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/EQ20171112IRQ/EQ20171112IRQ_shp.zip
  format: null
  id: resource_e3b7c421
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20171112IRQ_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-irnirq_unosat_damagedstructuresrelatedd_20171120
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
  start: '2017-11-20'
temporal_resolution: null
title: Damaged structures and related density map in Sarpol-e-Zahab, Kermanshah, Iran
version: null
vulnerability: null
---
