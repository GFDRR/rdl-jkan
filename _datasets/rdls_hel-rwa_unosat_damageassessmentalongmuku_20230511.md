---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-
dataset_id: rdls_hel-rwa_unosat_damageassessmentalongmuku_20230511
description: "UNOSAT code FL20230504RWA, GDACS Id: 1101977 This map illustrates satellite-detected\
  \ surface waters and the potentially affected structures/roads along the Mukungwa\
  \ River, Western & Northern Province, Rwanda as detected from a Pl\xE9iades image\
  \ acquired on the 10th May 2023. Within the analysis extent of about 22 km2, 10\
  \ structures and 05 road segments appear to be potentially affected. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to the United Nations Satellite Centre (UNOSAT).. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-]"
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
    description: Structures potentially affected by fluvial flooding along Mukungwa
      River
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
    description: Road segments potentially affected by fluvial flooding
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Pl\xE9iades satellite imagery acquired on 10 May 2023 was analyzed\
    \ by UNOSAT analysts through visual interpretation and comparison with reference\
    \ imagery to detect surface water extent and identify potentially affected structures\
    \ and road segments. The analysis covers approximately 22 km\xB2 along the Mukungwa\
    \ River in Western and Northern Provinces, Rwanda, and represents preliminary\
    \ satellite-based damage assessment requiring field validation."
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
- href: https://data.humdata.org/dataset/damage-assessment-along-the-mukungwa-river-western-northern-provinces-rwanda-as-of-10-may-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Structures potentially affected by fluvial flooding along Mukungwa
      River
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
    description: Road segments potentially affected by fluvial flooding
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
  description: Damage assessment along the Mukungwa river, Western & Northern Provinces,
    Rwanda as of 10 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3585/FL20230504RWA_gdb.zip
  format: Geodatabase
  id: resource_89a8a5b7
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
  description: Damage assessment along the Mukungwa river, Western & Northern Provinces,
    Rwanda as of 10 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3585/FL20230504RWA_SHP.zip
  format: null
  id: resource_f0c42c85
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
slug: rdls_hel-rwa_unosat_damageassessmentalongmuku_20230511
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
  start: '2023-05-11'
temporal_resolution: null
title: Damage assessment along the Mukungwa river, Western & Northern Provinces, Rwanda
  as of 10 May 2023
version: null
vulnerability: null
---
