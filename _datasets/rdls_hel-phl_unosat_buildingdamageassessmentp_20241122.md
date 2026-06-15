---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/building-damage-assessment-in-panganiban-city-catanduanes-province-bicol-region-the-philip
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-panganiban-city-catanduanes-province-bicol-region-the-philip
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-panganiban-city-catanduanes-province-bicol-region-the-philip
dataset_id: rdls_hel-phl_unosat_buildingdamageassessmentp_20241122
description: 'UNOSAT code: TC20241117PHL, GDACS ID: 1001124 This map provides an analysis
  of structures potentially impacted by Typhoon Man-Yi, utilizing imagery from the
  Pleiades satellite acquired on 18 and 20 November 2024. Within the defined analysis
  area, UNOSAT has identified 23 structures as damaged and 82 as potentially damaged.
  Out of a total of 1,174 buildings identified within the analysis extent, this represents
  approximately 9% of buildings as damaged. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to the United Nations
  Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/building-damage-assessment-in-panganiban-city-catanduanes-province-bicol-region-the-philip]'
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
    description: Building stock inventory of 1,174 structures identified within the
      analysis extent of Panganiban City
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
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 18
    and 20 November 2024, comparing pre- and post-event images to identify structural
    damage from Typhoon Man-Yi. Buildings were classified as damaged, potentially
    damaged, or undamaged based on observable changes in satellite imagery. The analysis
    identified 23 confirmed damaged and 82 potentially damaged structures out of 1,174
    total buildings in the study area.
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
- href: https://data.humdata.org/dataset/building-damage-assessment-in-panganiban-city-catanduanes-province-bicol-region-the-philip
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from Typhoon Man-Yi: 23 confirmed damaged
      and 82 potentially damaged structures'
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
  description: Building Damage Assessment in Panganiban City, Catanduanes Province,
    Bicol Region, The Philippines as of 18 November 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4035/TC20241117PHL_gdb.zip
  format: Geodatabase
  id: resource_0a154e7b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20241117PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Building Damage Assessment in Panganiban City, Catanduanes Province,
    Bicol Region, The Philippines as of 18 November 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4035/TC20241117PHL_SHP.zip
  format: null
  id: resource_749ee7f2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20241117PHL_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-phl_unosat_buildingdamageassessmentp_20241122
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-11-22'
temporal_resolution: null
title: Building Damage Assessment in Panganiban City, Catanduanes Province, Bicol
  Region, The Philippines as of 18 November 2024
version: null
vulnerability: null
---
