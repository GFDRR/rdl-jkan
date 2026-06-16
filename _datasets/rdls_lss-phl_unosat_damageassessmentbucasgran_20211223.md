---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-bucas-grande-island-socorro-surigao-del-norte-of-philippines-as-of-17
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-bucas-grande-island-socorro-surigao-del-norte-of-philippines-as-of-17
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-bucas-grande-island-socorro-surigao-del-norte-of-philippines-as-of-17
dataset_id: rdls_lss-phl_unosat_damageassessmentbucasgran_20211223
description: 'UNOSAT code: TC20211216PHL This map illustrates potentially damaged
  structures/buildings in Bucas Grande Island, Socorro, Surigao del Norte of Philippines
  as detected by WorldView-3 image acquired on 17 December 2021. Within the analyzed
  area, UNOSAT has identified 351 damaged structures, 129 potentially damaged structures,
  5 road obstacles and 1 destroyed bridge. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to the United Nations
  Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-bucas-grande-island-socorro-surigao-del-norte-of-philippines-as-of-17]'
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts performed post-event damage assessment by comparing
    WorldView-3 satellite imagery acquired on 17 December 2021 with pre-event baseline
    imagery, identifying structural damage through visual interpretation and change
    detection. The resulting geodatabase contains point and polygon geometries of
    351 damaged structures, 129 potentially damaged structures, 5 road obstacles,
    and 1 destroyed bridge in Bucas Grande Island following Typhoon Odette.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-bucas-grande-island-socorro-surigao-del-norte-of-philippines-as-of-17
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone (Typhoon Odette)
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
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage including destroyed bridge and road
      obstacles from tropical cyclone
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  description: Damage assessment in Bucas Grande Island, Socorro, Surigao del Norte
    of Philippines as of 17 December 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_gdb.zip
  format: Geodatabase
  id: resource_b1a287d4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20211216PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment in Bucas Grande Island, Socorro, Surigao del Norte
    of Philippines as of 17 December 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_SHP.zip
  format: null
  id: resource_64d5bb14
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20211216PHL_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_unosat_damageassessmentbucasgran_20211223
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
  start: '2021-12-23'
temporal_resolution: null
title: Damage assessment in Bucas Grande Island, Socorro, Surigao del Norte of Philippines
  as of 17 December 2021
version: null
vulnerability: null
---
