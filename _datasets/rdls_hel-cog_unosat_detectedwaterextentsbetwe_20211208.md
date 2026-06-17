---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS satellite imagery
    url: https://data.humdata.org/dataset/water-extents-between-03-and-07-december-2021-in-cuvette-department-republic-of-congo
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: HRSL population data
    url: https://data.humdata.org/dataset/water-extents-between-03-and-07-december-2021-in-cuvette-department-republic-of-congo
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-03-and-07-december-2021-in-cuvette-department-republic-of-congo
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-between-03-and-07-december-2021-in-cuvette-department-republic-of-congo
dataset_id: rdls_hel-cog_unosat_detectedwaterextentsbetwe_20211208
description: 'UNOSAT code: FL20211208COG This map illustrates cumulative satellite-detected
  water using VIIRS in Republic of Congo between 03 to 07 December 2021 compared with
  the period between 26 to 30 November 2021. Within the cloud free analyzed areas
  of about 335,000 km2, a total of about 3,500 km2 of lands appear to be affected
  with flood waters. Water extent appears to have decreased of about 300 km2 since
  the period between 26 to 30 November 2021. Based on HRSL population data and the
  detected surface waters, the potentially exposed population of ~190,000 people is
  mainly located in department of Likouala with ~ 94,000 people, Brazzaville with
  ~ 70,000 people and Plateaux with ~10,000 people. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to the
  United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-between-03-and-07-december-2021-in-cuvette-department-republic-of-congo]'
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
    description: Potentially exposed population derived from HRSL population data
      intersected with detected water extents
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts compared VIIRS satellite imagery from 03-07 December\
    \ 2021 with baseline imagery from 26-30 November 2021 to detect cumulative water\
    \ extents across cloud-free areas of Cuvette department. Detected water polygons\
    \ (3,500 km\xC2\xB2 total) were intersected with HRSL population data to estimate\
    \ potentially exposed population (~190,000 people), producing post-event flood\
    \ impact assessment maps."
  sources:
  - id: source_1
    license: null
    name: VIIRS satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: HRSL population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-between-03-and-07-december-2021-in-cuvette-department-republic-of-congo
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to detected flood waters based on
      spatial intersection of water extents and population distribution
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
  description: Satellite detected water extents between 03 and 07 December 2021 in
    Cuvette department, Republic of Congo (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/CG/FL20211208COG/FL20211208COG_gdb.zip
  format: Geodatabase
  id: resource_90e0e840
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211208COG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents between 03 and 07 December 2021 in
    Cuvette department, Republic of Congo (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/CG/FL20211208COG/FL20211208COG_SHP.zip
  format: null
  id: resource_530634e0
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20211208COG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cog_unosat_detectedwaterextentsbetwe_20211208
spatial:
  bbox: null
  centroid: null
  countries:
  - COG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-12-08'
temporal_resolution: null
title: Satellite detected water extents between 03 and 07 December 2021 in Cuvette
  department, Republic of Congo
version: null
vulnerability: null
---
