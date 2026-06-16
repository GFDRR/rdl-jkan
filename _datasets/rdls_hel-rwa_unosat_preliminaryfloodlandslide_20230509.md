---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-flood-and-landslide-assessment-report-along-sebaya-river-rubavu-dist
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-flood-and-landslide-assessment-report-along-sebaya-river-rubavu-dist
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-flood-and-landslide-assessment-report-along-sebaya-river-rubavu-dist
dataset_id: rdls_hel-rwa_unosat_preliminaryfloodlandslide_20230509
description: 'UNOSAT code FL20230504RWA, GDACS Id: 1101977 Status: Washed away structures
  and damaged transportation network observed along the Sebaya River Further action(s):
  Continue monitoring Landslides /mudslides observed in Rubavu District, Western Province
  as of 6 May 2023; Washed away structures observed along the Sebaya River in Rubavu
  District, Western Province as of 6 May 2023; Damaged roads and damaged bridge by
  landslide/mudslide observed along the Sebaya River in Rubavu District, Western Province
  as of 6 May 2023;. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-flood-and-landslide-assessment-report-along-sebaya-river-rubavu-dist]'
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
    description: Structures affected by flooding along Sebaya River
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
- asset_type:
    description: Transportation network including roads and bridges in the study area
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_flood_hzd
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: es_flood
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_landslide_hzd
      intensity_measure: pgd:m
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: es_landslide
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery acquired on
    or after 4 May 2023 to identify notable changes in the Sebaya River corridor and
    Rubavu District. Damage features (washed away structures, damaged roads/bridges,
    landslide scars) were manually delineated and attributed with event codes, sensor
    information, and impact notes to produce a post-event damage assessment geodatabase.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/preliminary-satellite-flood-and-landslide-assessment-report-along-sebaya-river-rubavu-dist
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Washed away structures observed along Sebaya River from fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Damaged roads and bridge from landslide/mudslide impacts
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
  description: Preliminary satellite flood and landslide assessment report, Along
    Sebaya River, Rubavu District, Karongi Districtn Western Province, Rwanda (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3579/FL20230504RWA_gdb.zip
  format: Geodatabase
  id: resource_41140ff5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230504RWA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary satellite flood and landslide assessment report, Along
    Sebaya River, Rubavu District, Karongi Districtn Western Province, Rwanda (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3579/FL20230504RWA_SHP.zip
  format: null
  id: resource_2bfb894d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230504RWA_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-rwa_unosat_preliminaryfloodlandslide_20230509
spatial:
  bbox: null
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-09'
temporal_resolution: null
title: Preliminary satellite flood and landslide assessment report, Along Sebaya River,
  Rubavu District, Karongi Districtn Western Province, Rwanda
version: null
vulnerability: null
---
