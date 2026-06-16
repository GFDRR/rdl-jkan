---
attributions:
- entity:
    affiliation: null
    email: null
    name: TerraSAR-X satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-the-northwestern-part-of-bangladesh
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-the-northwestern-part-of-bangladesh
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-the-northwestern-part-of-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-the-northwestern-part-of-bangladesh
dataset_id: rdls_hel-bgd_unosat_detectedwatersnorthwester_20170817
description: 'This map illustrates satellite-detected surface water extent in the
  northern part of Bangladesh using a TerraSAR-X satellite image acquired on the 16
  August 2017. In the analysed area; 221,915 ha of lands are likely affected. The
  population exposure analysis using WorldPop data shows that 2,143,586 people are
  potentially affected by floods in this analysed zone: ~1,800,000 are located in
  Rangpur Division and ~280,000 in Dhaka Division. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-the-northwestern-part-of-bangladesh]'
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
    description: Population potentially affected by detected flood waters, derived
      from WorldPop data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Land area affected by satellite-detected surface water extent
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: TerraSAR-X satellite imagery from 16 August 2017 was analyzed by UNOSAT
    to detect surface water extent in northwestern Bangladesh. The delineated water
    bodies (221,915 ha) were intersected with WorldPop gridded population data to
    estimate population exposure (2,143,586 people potentially affected). This is
    a preliminary post-event analysis not yet validated in the field.
  sources:
  - id: source_1
    license: null
    name: TerraSAR-X satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-the-northwestern-part-of-bangladesh
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially affected by detected flood waters in northwestern
      Bangladesh
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: Satellite Detected Waters in the Northwestern Part of Bangladesh (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20170815BGD/FL20170815BGD_gdb.zip
  format: Geodatabase
  id: resource_dd3b2eda
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170815BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Waters in the Northwestern Part of Bangladesh (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/FL20170815BGD/FL20170815BGD_shp.zip
  format: null
  id: resource_96fecfce
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170815BGD_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bgd_unosat_detectedwatersnorthwester_20170817
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-08-17'
temporal_resolution: null
title: Satellite Detected Waters in the Northwestern Part of Bangladesh
version: null
vulnerability: null
---
