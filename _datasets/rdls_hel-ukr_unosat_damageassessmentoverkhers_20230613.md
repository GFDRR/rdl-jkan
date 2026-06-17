---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-over-kherson-city-khersonskyi-region-kehersonska-oblast-ukraine-as-of-07
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-over-kherson-city-khersonskyi-region-kehersonska-oblast-ukraine-as-of-07
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-over-kherson-city-khersonskyi-region-kehersonska-oblast-ukraine-as-of-07
dataset_id: rdls_hel-ukr_unosat_damageassessmentoverkhers_20230613
description: "UNOSAT code FL20230606UKR This map illustrates satellite-detected flood\
  \ waters and affected structures over Kherson City, Khersonskyi Region, Kehersonska\
  \ Oblast (Ukraine) as observed from WorldView-3 image acquired on 7 June 2023 at\
  \ 08:19 UTC; and ICEYE image acquired on 7 June 2023. Within the analysed area of\
  \ 64 km\xB2, about 19% (12 km\xB2) of Kherson City area appear to be flooded. 4,302\
  \ structures and 76 harbours are affected. This is a preliminary analysis and has\
  \ not yet been validated in the field. Please send ground feedback to United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-over-kherson-city-khersonskyi-region-kehersonska-oblast-ukraine-as-of-07]"
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
    description: Building structures affected by flood waters in Kherson City, classified
      by damage status
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
    description: Harbor infrastructure affected by flood waters in Kherson City
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
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "Satellite imagery from WorldView-3 (optical) and ICEYE (SAR) acquired\
    \ on 7 June 2023 were analyzed by UNOSAT analysts through visual interpretation\
    \ and multi-temporal comparison to detect flood water extent and identify affected\
    \ structures. Damage assessment was conducted by identifying notable changes in\
    \ building and infrastructure features between pre- and post-flood imagery within\
    \ a 64 km\xB2 study area of Kherson City."
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
- href: https://data.humdata.org/dataset/damage-assessment-over-kherson-city-khersonskyi-region-kehersonska-oblast-ukraine-as-of-07
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct damage to 4,302 structures from fluvial flooding in Kherson
      City
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
    description: Direct damage to 76 harbors from fluvial flooding in Kherson City
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
  description: Damage assessment over Kherson City, Khersonskyi Region, Kehersonska
    Oblast, Ukraine as of 07 June 2023; 08:19 UTC (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3621/FL20230606UKR_gdb.zip
  format: Geodatabase
  id: resource_32e023e0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment over Kherson City, Khersonskyi Region, Kehersonska
    Oblast, Ukraine as of 07 June 2023; 08:19 UTC (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3621/FL20230606UKR_SHP.zip
  format: null
  id: resource_837a1a6e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230606UKR_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ukr_unosat_damageassessmentoverkhers_20230613
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-06-13'
temporal_resolution: null
title: Damage assessment over Kherson City, Khersonskyi Region, Kehersonska Oblast,
  Ukraine as of 07 June 2023; 08:19 UTC
version: null
vulnerability: null
---
