---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-maisi-town-and-surroundings
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-maisi-town-and-surroundings
dataset_id: rdls_hl-cub_unosat_damageassessmentmaisitown_20161013
description: 'This map illustrates potential satellite-detected damaged structures
  in Maisi town and the surrounding area in Guantanamo Province, Cuba. The UNITAR-UNOSAT
  analysis used a Pleiades satellite image, acquired on the 7 October 2016, and identified
  417 damaged structures within the map extent; 230 were identified inside the town
  of Maisi .This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/damage-assessment-in-maisi-town-and-surroundings]'
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre- and post-event Pleiades satellite imagery
    acquired on 7 October 2016 to detect structural damage in Maisi town and surroundings
    following a tropical cyclone event. Damaged structures were manually identified
    and mapped as point or polygon features with confidence ratings and validation
    flags. This is a preliminary satellite-based assessment not yet validated through
    field surveys.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-maisi-town-and-surroundings
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone detected via satellite
      imagery; 417 damaged structures identified in Maisi area
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
  description: Cuba - Damage Assessment in Maisi town and surroundings (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CU/TC20161005CUB/TC20161005CUB.gdb.zip
  format: Geodatabase
  id: resource_dd0edd28
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161005CUB.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cuba - Damage Assessment in Maisi town and surroundings (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CU/TC20161005CUB/TC20161005CUB_shp.zip
  format: null
  id: resource_b253de68
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161005CUB_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-cub_unosat_damageassessmentmaisitown_20161013
spatial:
  bbox: null
  centroid: null
  countries:
  - CUB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-13'
temporal_resolution: null
title: Cuba - Damage Assessment in Maisi town and surroundings
version: null
vulnerability: null
---
