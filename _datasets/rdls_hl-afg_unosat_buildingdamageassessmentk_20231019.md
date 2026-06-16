---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/building-damage-assessment-in-koshkak-village-zindajan-district-hirat-province-afghanistan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-koshkak-village-zindajan-district-hirat-province-afghanistan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/building-damage-assessment-in-koshkak-village-zindajan-district-hirat-province-afghanistan
dataset_id: rdls_hl-afg_unosat_buildingdamageassessmentk_20231019
description: "UNOSAT code EQ20231008AFG, GDACS Id: 1394952 This map illustrates destroyed\
  \ and potentially damaged structures by the M6.3 Hirat earthquake of 15 October\
  \ 2023 (03:36 UTC) as observed by using a Pl\xE9iades NEO very high-resolution satellite\
  \ image acquired on 16 October 2023 at 06:44 UTC. Within the map extent, UNOSAT\
  \ identified 491 destroyed structures, 1 potentially damaged structure and 179 temporary\
  \ shelters. This is a preliminary analysis and has not yet been validated in the\
  \ field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/building-damage-assessment-in-koshkak-village-zindajan-district-hirat-province-afghanistan]"
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
  description: "UNOSAT analysts compared Pl\xE9iades NEO satellite imagery acquired\
    \ on 16 October 2023 (one day post-earthquake) with reference imagery to identify\
    \ structural damage from the M6.3 Hirat earthquake of 15 October 2023. Destroyed\
    \ and potentially damaged structures were manually delineated and classified within\
    \ the study area of Koshkak village, Zindajan District."
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
- href: https://data.humdata.org/dataset/building-damage-assessment-in-koshkak-village-zindajan-district-hirat-province-afghanistan
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment identifying 491 destroyed structures
      and 1 potentially damaged structure in Koshkak village from the M6.3 earthquake
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
  description: Building Damage Assessment in Koshkak village, Zindajan District, Hirat
    Province, Afghanistan as of 16 October 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3694/EQ20231008AFG_gdb.zip
  format: Geodatabase
  id: resource_407f43aa
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Building Damage Assessment in Koshkak village, Zindajan District, Hirat
    Province, Afghanistan as of 16 October 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3694/EQ20231008AFG_SHP.zip
  format: null
  id: resource_8bc80f54
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20231008AFG_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_unosat_buildingdamageassessmentk_20231019
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-10-19'
temporal_resolution: null
title: Building Damage Assessment in Koshkak village, Zindajan District, Hirat Province,
  Afghanistan as of 16 October 2023
version: null
vulnerability: null
---
