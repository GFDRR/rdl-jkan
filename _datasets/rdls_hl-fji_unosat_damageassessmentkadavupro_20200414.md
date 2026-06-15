---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-in-kadavu-province-eastern-division-republic-of-fiji
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Pleiades satellite imagery
    url: https://data.humdata.org/dataset/damage-assessment-in-kadavu-province-eastern-division-republic-of-fiji
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-kadavu-province-eastern-division-republic-of-fiji
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-kadavu-province-eastern-division-republic-of-fiji
dataset_id: rdls_hl-fji_unosat_damageassessmentkadavupro_20200414
description: 'UNOSAT code: TC20200408FJI This map illustrates potentially damaged
  structures and buildings in Kadavu Province, Eastern Division, Republic of Fiji
  as detected by satellite image acquired after landfall of the Tropical Cyclone Harold-20
  on 08 April 2020. UNITAR-UNOSAT analysis used a Pleiades image acquired on 12 April
  2020. Within the Kadavu Province boundary, UNITAR-UNOSAT identified in the cloud
  free zones 1,003 potentially damaged structures. Taking into account the pre-building
  footprints provided by OpenStreetMap, this represents about 22% of the total number
  of structures within the analyzed cloud free areas. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-kadavu-province-eastern-division-republic-of-fiji]'
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
    strong_wind:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre-event OpenStreetMap building footprints
    with post-event Pleiades satellite imagery (12 April 2020) acquired after Tropical
    Cyclone Harold landfall on 8 April 2020. Visual interpretation of cloud-free zones
    identified 1,003 potentially damaged structures within Kadavu Province boundary,
    representing approximately 22% of total building stock.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Pleiades satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-kadavu-province-eastern-division-republic-of-fiji
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Post-event satellite-detected damage assessment identifying 1,003
      potentially damaged structures in Kadavu Province from Tropical Cyclone Harold
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
  description: Damage Assessment in Kadavu Province, Eastern Division, Republic of
    Fiji (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20200408FJI/TC20200408FJI_gdb.zip
  format: Geodatabase
  id: resource_904db388
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20200408FJI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Kadavu Province, Eastern Division, Republic of
    Fiji (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20200408FJI/TC20200408FJI_SHP.zip
  format: null
  id: resource_f5e3d7d8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20200408FJI_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-fji_unosat_damageassessmentkadavupro_20200414
spatial:
  bbox: null
  centroid: null
  countries:
  - FJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-04-14'
temporal_resolution: null
title: Damage Assessment in Kadavu Province, Eastern Division, Republic of Fiji
version: null
vulnerability: null
---
