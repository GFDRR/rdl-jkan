---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-and-flash-floods-impact-analysis-west-of-durban-ethekwini-metropolitan-municipal
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-and-flash-floods-impact-analysis-west-of-durban-ethekwini-metropolitan-municipal
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-and-flash-floods-impact-analysis-west-of-durban-ethekwini-metropolitan-municipal
dataset_id: rdls_hel-zaf_unosat_landslideflashfloodsimpac_20220425
description: 'UNOSAT code: FL20220418ZAF This map illustrates satellite-detected landslides/mudflow
  West of Durban City, eThekwini Metropolitan Municipality, KwaZulu-Natal Province,
  South Africa as observed from a WorldView-3 imagery acquired on 14 April 2022. Within
  the analyzed area, at least 62 structures and 2 bridges appear to be affected by
  floods and/or landslides. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to the United Nations Satellite Centre
  (UNOSAT).. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-and-flash-floods-impact-analysis-west-of-durban-ethekwini-metropolitan-municipal]'
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
    description: Building structures affected by floods and/or landslides in the study
      area
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
    description: Bridge infrastructure affected by floods and/or landslides
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
      id: es_landslide_hzd
      intensity_measure: pgd:m
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: es_landslide
    occurrence_range: null
    seasonality: null
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
  type: landslide, flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared WorldView-3 satellite imagery
    acquired on 14 April 2022 with reference imagery to detect notable changes indicative
    of landslides, mudflows, and flood impacts. Affected structures and bridges were
    identified and mapped through visual interpretation of satellite-detected damage
    signatures. The resulting geodatabase and shapefile contain spatial features of
    observed impacts in the eThekwini Metropolitan Municipality.
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
- href: https://data.humdata.org/dataset/landslide-and-flash-floods-impact-analysis-west-of-durban-ethekwini-metropolitan-municipal
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslides and mudflows
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flash floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage to bridges from landslides
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
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
    description: Direct infrastructure damage to bridges from flash floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_4
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
  description: South Africa - Landslide and flash floods impact analysis West of Durban,
    eThekwini Metropolitan Municipality, KwaZulu-Natal Provincce, (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_gdb.zip
  format: Geodatabase
  id: resource_9c7f62c1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220418ZAF_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Africa - Landslide and flash floods impact analysis West of Durban,
    eThekwini Metropolitan Municipality, KwaZulu-Natal Provincce, (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/ZA/FL20220418ZAF/FL20220418ZAF_SHP.zip
  format: null
  id: resource_1f1ae90e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220418ZAF_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-zaf_unosat_landslideflashfloodsimpac_20220425
spatial:
  bbox: null
  centroid: null
  countries:
  - ZAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-04-25'
temporal_resolution: null
title: South Africa - Landslide and flash floods impact analysis West of Durban, eThekwini
  Metropolitan Municipality, KwaZulu-Natal Provincce,
version: null
vulnerability: null
---
